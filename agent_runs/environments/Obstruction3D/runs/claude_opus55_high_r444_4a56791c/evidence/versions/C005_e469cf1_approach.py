"""Obstruction3D approach: clear obstructions from target region, then place target block.

Kinematics: Kinova Gen3 URDF chain, calibrated empirically (see kin.py):
  arm mount = base pose + 0.12 m along base x, z=-0.0052; tool point 0.12 m along flange z.
grasp_tf = object pose expressed in tool frame (T_obj = T_tool @ G).
Grasp succeeds if tool z in [obj_bottom+0.042, obj_top+0.03] and object between fingers.
Release only succeeds when the held object's bottom is within ~5mm of a support.
"""
import numpy as np
import kin

JN = [f'joint_{i}' for i in range(1, 8)]
TABLE_TOP = 0.075
Z_SAFE = 0.25          # tool z for transit
JLIM = np.array([np.inf, 2.41, np.inf, 2.66, np.inf, 2.23, np.inf])
TABLE_X = (0.13, 0.47)
TABLE_Y = (-0.36, 0.36)


def quat_mat(x, y, z, w):
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def rotz3(a):
    c, s = np.cos(a), np.sin(a)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


class Obj:
    def __init__(self, state, o):
        g = lambda f: float(state.get(o, f))
        self.name = o.name
        self.p = np.array([g('pose_x'), g('pose_y'), g('pose_z')])
        self.h = np.array([g('half_extent_x'), g('half_extent_y'), g('half_extent_z')])
        self.q = np.array([g('pose_qx'), g('pose_qy'), g('pose_qz'), g('pose_qw')])
        self.R = quat_mat(*self.q)
        self.yaw = np.arctan2(self.R[1, 0], self.R[0, 0])
        try:
            self.grasped = g('grasp_active') > 0.5
        except Exception:
            self.grasped = False

    def footprint(self):
        c, s = abs(np.cos(self.yaw)), abs(np.sin(self.yaw))
        return np.array([c * self.h[0] + s * self.h[1], s * self.h[0] + c * self.h[1]])

    @property
    def top(self):
        return self.p[2] + self.h[2]

    @property
    def bottom(self):
        return self.p[2] - self.h[2]


def overlap(pa, ha, pb, hb, margin=0.0):
    return (abs(pa[0] - pb[0]) < ha[0] + hb[0] + margin) and (abs(pa[1] - pb[1]) < ha[1] + hb[1] + margin)


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.rng = np.random.default_rng(0)

    # ------------------------------------------------------------------ utils
    def _parse(self, state):
        self.robot = state.get_object_from_name('robot')
        objs = {}
        for n in state.get_object_names():
            if n == 'robot':
                continue
            o = state.get_object_from_name(n)
            try:
                objs[n] = Obj(state, o)
            except Exception:
                pass
        return objs

    def _q(self, state):
        return np.array([float(state.get(self.robot, f)) for f in JN])

    def _base(self, state):
        return np.array([float(state.get(self.robot, f)) for f in ['pos_base_x', 'pos_base_y', 'pos_base_rot']])

    def _G(self, state):
        g = [float(state.get(self.robot, f)) for f in
             ['grasp_tf_x', 'grasp_tf_y', 'grasp_tf_z', 'grasp_tf_qx', 'grasp_tf_qy', 'grasp_tf_qz', 'grasp_tf_qw']]
        G = np.eye(4)
        G[:3, :3] = quat_mat(*g[3:])
        G[:3, 3] = g[:3]
        return G

    def _ik(self, q0, p, R):
        best = None
        for attempt in range(3):
            qs = np.array(q0, dtype=float)
            if attempt > 0:
                qs = qs + self.rng.uniform(-0.4, 0.4, 7)
            q, ok = kin.ik(self.base, qs, np.asarray(p, float), R, iters=100, tol=1e-5)
            if ok and np.all(np.abs(q) <= JLIM):
                return q, True
            if best is None:
                best = np.clip(q, -JLIM, JLIM)
        return best, False

    def _cart_path(self, q0, p_from, p_to, R, step=0.04):
        """IK waypoints along a straight line in tool position with fixed orientation R."""
        p_from = np.asarray(p_from, float)
        p_to = np.asarray(p_to, float)
        d = np.linalg.norm(p_to - p_from)
        n = max(1, int(np.ceil(d / step)))
        qs = []
        q = np.array(q0, float)
        allok = True
        for i in range(1, n + 1):
            p = p_from + (p_to - p_from) * i / n
            q, ok = self._ik(q, p, R)
            allok &= ok
            qs.append(q.copy())
        return qs, q, allok

    def _tool(self, q):
        return kin.fk(self.base, q)

    def _finger_boxes(self, x, y, yaw, inner=0.041, outer=0.068, half_across=0.017):
        d = np.array([-np.sin(yaw), np.cos(yaw)])
        a = np.array([np.cos(yaw), np.sin(yaw)])
        c = 0.5 * (inner + outer)
        hl = 0.5 * (outer - inner)
        return [(np.array([x, y]) + sgn * c * d, d, a, hl, half_across) for sgn in (1, -1)]

    @staticmethod
    def _box_hits_obj(box, b, infl=0.004):
        """SAT test: oriented finger box vs object footprint (yawed rectangle)."""
        cen, d, a, hd, ha = box
        cy, sy = np.cos(b.yaw), np.sin(b.yaw)
        bx = np.array([cy, sy]); by = np.array([-sy, cy])
        bh = (b.h[0] + infl, b.h[1] + infl)
        rel = b.p[:2] - cen
        for ax in (d, a, bx, by):
            r1 = hd * abs(ax @ d) + ha * abs(ax @ a)
            r2 = bh[0] * abs(ax @ bx) + bh[1] * abs(ax @ by)
            if abs(rel @ ax) > r1 + r2:
                return False
        return True

    def _grasp_candidates(self, o, objs):
        """list of (score, yaw, x, y, blockers) grasp candidates for object o."""
        out = []
        for k in range(2):
            yaw = o.yaw + k * np.pi / 2
            d = np.array([-np.sin(yaw), np.cos(yaw)])
            a = np.array([np.cos(yaw), np.sin(yaw)])
            wd = abs(d @ o.R[:2, 0]) * o.h[0] + abs(d @ o.R[:2, 1]) * o.h[1]
            wa = abs(a @ o.R[:2, 0]) * o.h[0] + abs(a @ o.R[:2, 1]) * o.h[1]
            if wd > 0.041:
                continue
            smax = max(0.0, 0.037 - wd)
            amax = max(0.0, wa - 0.004)
            for sd in [0.0, 0.5 * smax, -0.5 * smax, smax, -smax]:
                for sa in [0.0, 0.5 * amax, -0.5 * amax, amax, -amax]:
                    x, y = o.p[:2] + sd * d + sa * a
                    blockers = []
                    for n, b in objs.items():
                        if n == o.name or n == 'target_region':
                            continue
                        for box in self._finger_boxes(x, y, yaw):
                            if self._box_hits_obj(box, b):
                                blockers.append(n)
                                break
                    score = len(blockers) * 10 + abs(sd) + abs(sa) + 0.01 * k * (wd > wa)
                    out.append((score, yaw, x, y, blockers))
        out.sort(key=lambda c: c[0])
        return out

    def _support_top(self, o, objs):
        top = TABLE_TOP
        for n, b in objs.items():
            if n == o.name:
                continue
            if b.top <= o.bottom + 2e-3 and overlap(o.p, o.footprint(), b.p, b.footprint()):
                top = max(top, b.top)
        return top

    # --------------------------------------------------------------- episode
    def reset(self, state, info):
        self.objs = self._parse(state)
        self.base = self._base(state)
        self.plan = []
        self.current = None
        self.blocked = 0
        self.last_q = None
        self.fail_count = {}
        self.steps = 0
        self.plans_made = 0
        self.aborting = False

    def _block_place_candidates(self, objs):
        """candidate (tool-free) placement yaws for target block on region, with blockers."""
        reg = objs['target_region']
        tb = objs['target_block']
        out = []
        for k in range(2):
            yaw = reg.yaw + k * np.pi / 2  # tool yaw (fingers close along (-sin, cos))
            blockers = []
            for n, b in objs.items():
                if n in ('target_region', 'target_block'):
                    continue
                for box in self._finger_boxes(reg.p[0], reg.p[1], yaw):
                    if self._box_hits_obj(box, b):
                        blockers.append(n)
                        break
            out.append((len(blockers), yaw, blockers))
        return out

    def _to_clear(self, objs):
        reg = objs['target_region']
        res = set()
        for n, o in objs.items():
            if not n.startswith('obstruction'):
                continue
            if overlap(o.p, o.footprint(), reg.p, reg.footprint(), 0.004):
                res.add(n)
        return res

    def _pick_target(self, objs):
        """decide which object to pick next and the grasp candidate."""
        clear = self._to_clear(objs)
        tb = objs['target_block']
        if not clear:
            # placement fingers: if the block can be grasped along an axis whose placement is blocked,
            # handled at place time; ensure at least one clean placement yaw.
            pc = self._block_place_candidates(objs)
            if min(c[0] for c in pc) > 0:
                clear |= set(min(pc, key=lambda c: c[0])[2])
        if not clear:
            want = ['target_block']
        else:
            want = list(clear)
        # expand with blockers
        best = None
        seen = set()
        frontier = list(want)
        depth = 0
        while frontier and depth < 3:
            nxt = []
            for n in frontier:
                if n in seen or n not in objs:
                    continue
                seen.add(n)
                cands = self._grasp_candidates(objs[n], objs)
                if n == 'target_block':
                    # prefer tool yaws allowing clean placement
                    pc = {round(wrap(c[1]) % np.pi, 3): c[0] for c in self._block_place_candidates(objs)}
                    cands = sorted(cands, key=lambda c: c[0] + 5 * (pc.get(round(wrap(c[1] - objs['target_region'].yaw + objs['target_region'].yaw) % np.pi, 3), 0) > 0))
                if not cands:
                    continue
                fc = self.fail_count.get(n, 0)
                c = cands[min(fc, len(cands) - 1)] if fc < len(cands) else cands[fc % len(cands)]
                score = len(c[4]) + 0.3 * fc + 0.1 * depth
                if best is None or score < best[0]:
                    best = (score, n, c)
                for bn in c[4]:
                    if bn.startswith('obstruction') or bn == 'target_block':
                        nxt.append(bn)
            frontier = nxt
            depth += 1
        return best

    def _plan_pick(self, state, name, cand):
        objs = self._parse(state)
        o = objs[name]
        _, yaw, gx, gy, _ = cand
        q = self._q(state)
        T = self._tool(q)
        best = None
        for y in [yaw, yaw + np.pi]:
            R = kin.topdown_R(y)
            qa, ok = self._ik(q, np.array([gx, gy, Z_SAFE]), R)
            c = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
            if best is None or c < best[0]:
                best = (c, y, R)
        _, yaw, R = best
        lo = o.bottom + 0.044
        hi = o.top + 0.028
        zg = 0.5 * (lo + hi) if hi >= lo else lo
        zg = min(zg, lo + 0.012)
        p0 = T[:3, 3]
        above = np.array([gx, gy, max(Z_SAFE, p0[2])])
        start = np.array([p0[0], p0[1], max(p0[2], Z_SAFE)])
        plan = []
        if p0[2] < Z_SAFE - 0.005:
            qs, q, _ = self._cart_path(q, p0, start, T[:3, :3], step=0.05)
            plan += [('move', x) for x in qs]
        qs, q, _ = self._cart_path(q, start, above, R, step=0.08)
        plan += [('move', x) for x in qs]
        qs, q, _ = self._cart_path(q, above, np.array([gx, gy, zg]), R, step=0.05)
        plan += [('move', x) for x in qs]
        plan += [('grip', -1.0), ('check', 'grasp')]
        self.plan = plan

    def _free_spot(self, o, objs, tool_yaw):
        fp = o.footprint()
        best = None
        cur = o.p[:2]
        for x in np.arange(TABLE_X[0] + fp[0], TABLE_X[1] - fp[0], 0.02):
            for y in np.arange(TABLE_Y[0] + fp[1], TABLE_Y[1] - fp[1], 0.02):
                p = np.array([x, y])
                cost = np.linalg.norm(p - cur)
                if best is not None and cost >= best[0]:
                    continue
                ok = True
                for n, b in objs.items():
                    if n == o.name:
                        continue
                    m = 0.075 if n in ('target_region', 'target_block') else 0.02
                    if overlap(p, fp, b.p, b.footprint(), m):
                        ok = False
                        break
                if not ok:
                    continue
                for box in self._finger_boxes(x, y, tool_yaw):
                    for n, b in objs.items():
                        if n != o.name and self._box_hits_obj(box, b, 0.01):
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    best = (cost, p)
        return None if best is None else best[1]

    def _plan_place(self, state, name, xy, support_top, yaw_obj):
        objs = self._parse(state)
        o = objs[name]
        q = self._q(state)
        T = self._tool(q)
        G = self._G(state)
        Ginv = np.linalg.inv(G)
        best = None
        for yo in [yaw_obj, yaw_obj + np.pi]:
            To = np.eye(4)
            To[:3, :3] = rotz3(yo)
            To[:3, 3] = [xy[0], xy[1], support_top + o.h[2] + 0.0015]
            Tt = To @ Ginv
            qa, ok = self._ik(q, Tt[:3, 3] + np.array([0, 0, Z_SAFE - Tt[2, 3]]), Tt[:3, :3])
            cst = np.sum(np.abs(wrap(qa - q))) + (0 if ok else 100)
            if best is None or cst < best[0]:
                best = (cst, Tt)
        Tt = best[1]
        R = Tt[:3, :3]
        p0 = T[:3, 3]
        maxtop = max([b.top for n, b in objs.items() if n != name] + [TABLE_TOP])
        obj_bottom = (T @ G)[2, 3] - o.h[2]
        lift_z = max(Z_SAFE, p0[2] + (maxtop + 0.025 - obj_bottom))
        up = np.array([p0[0], p0[1], lift_z])
        above = np.array([Tt[0, 3], Tt[1, 3], lift_z])
        plan = []
        qs, q, _ = self._cart_path(q, p0, up, T[:3, :3], step=0.05)
        plan += [('move', x) for x in qs]
        qs, q, _ = self._cart_path(q, up, above, R, step=0.08)
        plan += [('move', x) for x in qs]
        qs, q, _ = self._cart_path(q, above, Tt[:3, 3], R, step=0.05)
        plan += [('move', x) for x in qs]
        plan += [('grip', 1.0), ('check', 'release')]
        self.plan = plan

    def _held(self, state, objs):
        for n, o in objs.items():
            if o.grasped:
                return n
        return self.current

    def _next_task(self, state):
        self.plans_made += 1
        objs = self._parse(state)
        grasped = float(state.get(self.robot, 'grasp_active')) > 0.5
        if grasped:
            held = self._held(state, objs)
            self.current = held
            o = objs[held]
            clear = self._to_clear(objs)
            reg = objs['target_region']
            if held == 'target_block' and not clear:
                self._plan_place(state, held, reg.p[:2], reg.top, reg.yaw)
                return
            G = self._G(state)
            Rt = rotz3(o.yaw) @ np.linalg.inv(G)[:3, :3]
            tool_yaw = np.arctan2(-Rt[0, 0], Rt[1, 0])
            spot = self._free_spot(o, objs, tool_yaw)
            if spot is None:
                spot = o.p[:2]
            self._plan_place(state, held, spot, TABLE_TOP, o.yaw)
            return
        best = self._pick_target(objs)
        if best is None:
            self.current = 'target_block'
            cands = self._grasp_candidates(objs['target_block'], objs)
            if not cands:
                return
            best = (0, 'target_block', cands[0])
        self.current = best[1]
        self._plan_pick(state, best[1], best[2])

    def _abort(self, state):
        """blocked: retreat straight up and replan."""
        self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
        q = self._q(state)
        T = self._tool(q)
        p0 = T[:3, 3]
        qs, _, _ = self._cart_path(q, p0, np.array([p0[0], p0[1], max(p0[2] + 0.03, Z_SAFE)]), T[:3, :3], step=0.05)
        self.plan = [('move', x) for x in qs]

    # ---------------------------------------------------------------- acting
    def get_action(self, state):
        self.steps += 1
        a = np.zeros(11, dtype=np.float32)
        q = self._q(state)
        for _ in range(20):
            if not self.plan:
                self.aborting = False
                self._next_task(state)
                self.last_q = None
                if not self.plan:
                    return a
            kind, val = self.plan[0]
            if kind == 'move':
                d = wrap(val - q)
                if np.max(np.abs(d)) < 1e-4:
                    self.plan.pop(0)
                    self.last_q = None
                    self.blocked = 0
                    continue
                if self.last_q is not None and np.max(np.abs(q - self.last_q)) < 1e-7:
                    self.blocked += 1
                else:
                    self.blocked = 0
                if self.blocked >= 1:
                    self.blocked = 0
                    self.last_q = None
                    if getattr(self, 'aborting', False):
                        self.plan.pop(0)
                    else:
                        self.aborting = True
                        self._abort(state)
                    continue
                self.last_q = q.copy()
                s = max(1.0, np.max(np.abs(d)) / 0.2)
                a[3:10] = d / s
                return a
            self.aborting = False
            if kind == 'grip':
                self.plan.pop(0)
                a[10] = val
                self.last_q = None
                return a
            if kind == 'check':
                self.plan.pop(0)
                g = float(state.get(self.robot, 'grasp_active')) > 0.5
                if val == 'grasp' and not g:
                    self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
                    self.plan = []
                elif val == 'release' and g:
                    self.fail_count[self.current] = self.fail_count.get(self.current, 0) + 1
                    self.plan = []
                continue
        return a
