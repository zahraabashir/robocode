"""Obstruction2D approach: plan pick/drop/place legs, execute each leg with a
greedy Chebyshev (simultaneous dx/dy) controller that keeps the robot
assembly above all obstacles via a look-ahead clearance cone."""
import itertools
import numpy as np

WORLD_MAX_X = 1.618
FLOOR_Y = 0.1
XMIN, XMAX = 0.1015, 1.5170
YMAX = 0.897
MX = 0.006      # horizontal clearance margin
MY = 0.004      # vertical clearance margin
GAP = 0.006     # gripper gap to object top when grasping (grasp works <= ~0.01)
DROP_BOT = FLOOR_Y + 0.006
PLACE_BOT = FLOOR_Y + 0.012
STEP = 0.05
VAC_CLR = 0.02


def _g(s, o, f):
    return float(s.get(o, f))


def _rect(s, o):
    x, y = _g(s, o, "x"), _g(s, o, "y")
    w, h = _g(s, o, "width"), _g(s, o, "height")
    th = _g(s, o, "theta")
    c, sn = np.cos(th), np.sin(th)
    pts = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=float)
    R = np.array([[c, -sn], [sn, c]])
    v = pts @ R.T + np.array([x, y])
    return (float(v[:, 0].min()), float(v[:, 0].max()),
            float(v[:, 1].min()), float(v[:, 1].max()))


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.array(action_space.low, dtype=np.float32)
        self.high = np.array(action_space.high, dtype=np.float32)
        self.max_d = float(self.high[0])
        self.max_dth = float(self.high[2])
        self.max_darm = float(self.high[3])
        self.n_sim = 60
        self.k_drop = 5
        self.k_place = 5

    # ------------------------------------------------------------ parsing
    def _parse(self, s):
        robot = block = surface = None
        obst = []
        for name in s.get_object_names():
            o = s.get_object_from_name(name)
            tn = o.type.name
            if tn == "crv_robot":
                robot = o
            elif tn == "target_block":
                block = o
            elif tn == "target_surface":
                surface = o
            else:
                try:
                    _g(s, o, "width")
                    _g(s, o, "height")
                    obst.append(o)
                except Exception:
                    pass
        return robot, block, surface, obst

    # ------------------------------------------------------------ geometry
    def _assembly(self, held_rel=None):
        """Boxes (x0, x1, bottom_offset) relative to robot position."""
        gh = self.gh / 2.0
        rb = self.base_r
        boxes = [(-gh, gh, -(self.arm + self.gw))]
        edges = np.linspace(0.0, rb, 6)
        for a, b in zip(edges[:-1], edges[1:]):
            off = -np.sqrt(max(rb * rb - a * a, 0.0))
            boxes.append((a, b, off))
            boxes.append((-b, -a, off))
        if held_rel is not None:
            boxes.append(held_rel)
        return boxes

    @staticmethod
    def _safe(X, boxes, obstacles):
        """Minimal robot y at each x in X such that boxes clear obstacles."""
        B = np.asarray(boxes, dtype=float)
        base = FLOOR_Y + MY - float(B[:, 2].min())
        if len(obstacles) == 0:
            return np.full(np.shape(X), base)
        O = np.asarray(obstacles, dtype=float)
        Xa = np.asarray(X, dtype=float)[:, None, None]
        ov = ((Xa + B[None, :, 1:2] > O[None, None, :, 0] - MX) &
              (Xa + B[None, :, 0:1] < O[None, None, :, 1] + MX))
        val = O[None, None, :, 2] + MY - B[None, :, 2:3]
        req = np.where(ov, val, -1.0).max(axis=(1, 2))
        return np.maximum(req, base)

    def _leg_cost(self, p0, p1, boxes, obstacles):
        x0, y0 = p0
        x1, y1 = p1
        n = max(2, int(abs(x1 - x0) / 0.01) + 2)
        X = np.linspace(x0, x1, n)
        peak = float(self._safe(X, boxes, obstacles).max())
        peak = max(peak, y0, y1)
        vert = (peak - y0) + (peak - y1)
        return max(abs(x1 - x0), vert) / STEP

    # ------------------------------------------------------------ planning
    def reset(self, state, info):
        robot, block, surface, obst = self._parse(state)
        self.base_r = _g(state, robot, "base_radius")
        self.arm = _g(state, robot, "arm_length")
        self.gw = _g(state, robot, "gripper_width")
        self.gh = _g(state, robot, "gripper_height")
        self.block_name = block.name
        self.steps = 0
        self.leg = 0
        self.last = None
        self.stuck = 0
        self.noprog = 0
        self.last_arm = 0.0
        self.replan = False
        self.replans = 0
        try:
            self.legs = self._plan(state)
        except Exception:
            self.legs = None
        if not self.legs:
            self.legs = self._fallback_plan(state)

    def _grasp_d(self, r):
        """Allowed range of grasp offsets d (gripper x - object center)."""
        cx = (r[0] + r[1]) / 2
        hw = (r[1] - r[0]) / 2
        dmax = max(hw + self.gh / 2 - 0.012, 0.0)
        return max(-dmax, XMIN - cx), min(dmax, XMAX - cx)

    def _pick_pose(self, r, d):
        cx = (r[0] + r[1]) / 2
        return (cx + d, r[3] + GAP + self.arm + self.gw)

    def _pick_ok(self, r, d, obstacles):
        """Is the grasp pose over r at offset d clear of other obstacles?"""
        px, py = self._pick_pose(r, d)
        if not (XMIN <= px <= XMAX) or py > YMAX:
            return False
        req = float(self._safe(np.array([px]), self._assembly(), obstacles)[0])
        if req > py + 1e-6:
            return False
        # avoid vacuuming neighbours: no other object near the gripper face
        face = py - self.arm - self.gw
        g0, g1 = px - self.gh / 2 - 0.015, px + self.gh / 2 + 0.015
        for ox0, ox1, otop in obstacles:
            if ox1 > g0 and ox0 < g1 and otop > face - 0.04:
                return False
        return True

    def _d_options(self, r):
        lo, hi = self._grasp_d(r)
        if lo > hi:
            return []
        c = float(np.clip(0.0, lo, hi))
        opts = [c] + list(np.linspace(lo, hi, 9))
        return sorted(set(float(v) for v in opts), key=lambda v: abs(v - c))

    def _place_any(self, br, d, lefts, obstacles):
        """Is there any feasible final placement given obstacles?"""
        bw = br[1] - br[0]
        held = self._held_rel(br, d)
        ok = np.ones(len(lefts), dtype=bool)
        for q in obstacles:
            ok &= ~((lefts + bw > q[0] - 0.003) & (lefts < q[1] + 0.003))
        X = lefts - held[0]
        ty = PLACE_BOT - held[2]
        ok &= (X >= XMIN) & (X <= XMAX)
        if ty > YMAX:
            return False
        req = self._safe(X, self._assembly(held), obstacles)
        ok &= req <= ty + 1e-6
        return bool(ok.any())

    def _held_rel(self, r, d):
        rx, ry = self._pick_pose(r, d)
        return (r[0] - rx, r[1] - rx, r[2] - ry)

    def _plan(self, state):
        robot, block, surface, obst = self._parse(state)
        start = (_g(state, robot, "x"), _g(state, robot, "y"))
        sr = _rect(state, surface)
        br = _rect(state, block)
        orects = {o.name: _rect(state, o) for o in obst}
        boxes0 = self._assembly()
        cand = [n for n, r in orects.items()
                if r[1] > sr[0] - 0.1 and r[0] < sr[1] + 0.1]
        plans = []
        for k in range(len(cand) + 1):
            if plans and k > 2:
                break
            for R in itertools.permutations(cand, k):
                plans += self._plan_subset(start, R, orects, br, (sr[0], sr[1]), boxes0)
        if not plans:
            return None
        plans.sort(key=lambda p: p[0])
        best = None
        a0 = _g(state, robot, "arm_joint")
        for cost, legs, specs in plans[:self.n_sim]:
            steps = self._sim_plan(start, a0, specs)
            key = (steps, cost)
            if best is None or key < best[0]:
                best = (key, legs)
        self._best_key = best[0]
        return best[1]

    def _sim_plan(self, start, a0, specs, cap=120):
        x, y = start
        a = a0
        total = 0
        for p0, p1, held_y, obstacles in specs:
            held_g = None
            if held_y is not None:
                held_g = (held_y[0], held_y[1], held_y[2] + self.arm)
            G, B = self._split_boxes(held_g)
            tx, tg = p1[0], p1[1] - self.arm
            for i in range(cap):
                dx, dy, da, arrived = self._control(x, y, a, tx, tg, G, B, obstacles)
                x += dx
                y += dy
                a += da
                total += 1
                if arrived:
                    break
                if abs(dx) < 1e-9 and abs(dy) < 1e-9 and abs(da) < 1e-9:
                    return total + 10 * cap
            else:
                return total + 10 * cap
        return total

    def _plan_subset(self, start, R, orects, br, surf, boxes0):
        sx0, sx1 = surf
        bw = br[1] - br[0]
        lo, hi = self._grasp_d(br)
        if lo > hi:
            return []
        block_obs = (br[0], br[1], br[3])
        bd_opts = self._d_options(br)
        e = 0.004
        lefts = np.arange(sx0 + e, sx1 - bw - e + 1e-9, 0.004)
        if len(lefts) == 0:
            lefts = np.array([(sx0 + sx1) / 2 - bw / 2])
        out = []

        def rec(i, pos, cur, legs, specs, cost):
            if i == len(R):
                self._finish(pos, cur, legs, specs, cost, br, bd_opts, lefts, boxes0, out)
                return
            n = R[i]
            pending = set(R[i + 1:])
            r = cur[n]
            others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
            dl = [v for v in self._d_options(r) if self._pick_ok(r, v, others)]
            if not dl:
                return
            d = dl[0]
            pick = self._pick_pose(r, d)
            c1 = self._leg_cost(pos, pick, boxes0, others + [(r[0], r[1], r[3])])
            held = self._held_rel(r, d)
            boxes_h = self._assembly(held)
            w, h = r[1] - r[0], r[3] - r[2]
            forb = [(q[0], q[1]) for m, q in cur.items() if m != n]
            forb.append((br[0], br[1]))
            if pending:
                nr = cur[R[i + 1]]
                nxt = (nr[0] + nr[1]) / 2
            else:
                nxt = (br[0] + br[1]) / 2
            opts = []
            for left in np.arange(0.003, WORLD_MAX_X - 0.003 - w, 0.01):
                a, b = left, left + w
                if any(b > f0 - 0.012 and a < f1 + 0.012 for f0, f1 in forb):
                    continue
                if b > sx0 - 0.04 and a < sx1 + 0.04:
                    if not any(b + 0.04 <= L or a - 0.04 >= L + bw for L in lefts):
                        continue
                tx = left - held[0]
                if not (XMIN <= tx <= XMAX):
                    continue
                ty = DROP_BOT - held[2]
                if ty > YMAX:
                    continue
                if float(self._safe(np.array([tx]), boxes_h, others)[0]) > ty + 1e-6:
                    continue
                c2 = self._leg_cost(pick, (tx, ty), boxes_h, others)
                c3 = abs(tx - nxt) / STEP
                opts.append((c2 + c3, left, (tx, ty), c2))
            opts.sort(key=lambda o: o[0])
            taken = []
            for sc, left, dpose, c2 in opts:
                if len(taken) >= self.k_drop:
                    break
                if any(abs(left - tl) < 0.05 for tl in taken):
                    continue
                nob = (left, left + w, DROP_BOT + h)
                obs_after = [(q[0], q[1], q[3]) for m, q in cur.items()
                             if m != n and m not in pending] + [nob]
                if not any(self._pick_ok(br, v, obs_after) and
                           self._place_any(br, v, lefts, obs_after) for v in bd_opts):
                    continue
                taken.append(left)
                ncur = dict(cur)
                ncur[n] = (left, left + w, DROP_BOT, DROP_BOT + h)
                nlegs = legs + [("pick", n, d, pick), ("drop", n, dpose)]
                nspecs = specs + [(pos, pick, None, others + [(r[0], r[1], r[3])]),
                                  (pick, dpose, held, others)]
                rec(i + 1, dpose, ncur, nlegs, nspecs, cost + c1 + c2)

        rec(0, start, dict(orects), [], [], 0.0)
        return out

    def _finish(self, pos, cur, legs, specs, cost, br, bd_opts, lefts, boxes0, out):
        bw = br[1] - br[0]
        block_obs = (br[0], br[1], br[3])
        obst_final = [(q[0], q[1], q[3]) for q in cur.values()]
        cands = []
        for d in bd_opts:
            if not self._pick_ok(br, d, obst_final):
                continue
            pick = self._pick_pose(br, d)
            held = self._held_rel(br, d)
            boxes_h = self._assembly(held)
            c1 = self._leg_cost(pos, pick, boxes0, obst_final + [block_obs])
            for L in lefts:
                if any(L + bw > q[0] - 0.003 and L < q[1] + 0.003 for q in cur.values()):
                    continue
                tx = L - held[0]
                if not (XMIN <= tx <= XMAX):
                    continue
                ty = PLACE_BOT - held[2]
                if ty > YMAX:
                    continue
                req = float(self._safe(np.array([tx]), boxes_h, obst_final)[0])
                if req > ty + 1e-6:
                    continue
                c2 = self._leg_cost(pick, (tx, ty), boxes_h, obst_final)
                cands.append((c1 + c2, float(d), pick, (tx, ty), held))
        cands.sort(key=lambda c: c[0])
        used = []
        for sc, d, pick, ppose, held in cands:
            if len(used) >= self.k_place:
                break
            if any(abs(d - ud) < 1e-9 and abs(ppose[0] - ux) < 0.02 for ud, ux in used):
                continue
            used.append((d, ppose[0]))
            nlegs = legs + [("pick", self.block_name, d, pick),
                            ("place", self.block_name, ppose)]
            nspecs = specs + [(pos, pick, None, obst_final + [block_obs]),
                              (pick, ppose, held, obst_final)]
            out.append((cost + sc, nlegs, nspecs))

    def _fallback_plan(self, state):
        robot, block, surface, obst = self._parse(state)
        br = _rect(state, block)
        sr = _rect(state, surface)
        lo, hi = self._grasp_d(br)
        d = float(np.clip(0.0, lo, hi)) if lo <= hi else 0.0
        pick = self._pick_pose(br, d)
        held = self._held_rel(br, d)
        tx = float(np.clip((sr[0] + sr[1]) / 2 - (br[1] - br[0]) / 2 - held[0], XMIN, XMAX))
        return [("pick", self.block_name, d, pick),
                ("place", self.block_name, (tx, PLACE_BOT - held[2]))]

    # ------------------------------------------------------------ control
    def _act(self, dx, dy, dth, darm, vac):
        a = np.array([dx, dy, dth, darm, vac], dtype=np.float32)
        return np.clip(a, self.low, self.high)

    def get_action(self, state):
        self.steps += 1
        robot, block, surface, obst = self._parse(state)
        rx, ry = _g(state, robot, "x"), _g(state, robot, "y")
        rth = _g(state, robot, "theta")
        arm = _g(state, robot, "arm_joint")
        vac = _g(state, robot, "vacuum")
        th_err = (-np.pi / 2 - rth + np.pi) % (2 * np.pi) - np.pi
        dth = float(np.clip(th_err, -self.max_dth, self.max_dth))
        darm = 0.0

        if self.last is not None:
            lx, ly, cdx, cdy = self.last
            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
                self.stuck += 1
            else:
                self.stuck = 0

        if self.last is not None and abs(self.last[0] - rx) < 1e-6 and abs(self.last[1] - ry) < 1e-6 \
                and abs(self.last_arm - arm) < 1e-6:
            self.noprog += 1
        else:
            self.noprog = 0

        if self.replan and vac < 0.5:
            self.replan = False
            self.replans += 1
            try:
                legs = self._plan(state)
            except Exception:
                legs = None
            self.legs = legs if legs else self._fallback_plan(state)
            self.leg = 0
            self.noprog = 0

        if self.leg >= len(self.legs):
            self.last = None
            return self._act(0, 0.0, dth, darm, vac)

        if self.noprog >= 6 and self.replans < 5:
            kind = self.legs[self.leg][0]
            self.noprog = 0
            self.replan = True
            self.last = (rx, ry, 0.0, 0.0)
            self.last_arm = arm
            if kind == "drop":
                return self._act(0, 0, dth, darm, 0.0)
            if kind == "pick":
                return self._act(0, 0, dth, darm, 0.0)

        leg = self.legs[self.leg]
        kind, name = leg[0], leg[1]
        allr = {o.name: _rect(state, o) for o in obst + [block]}
        holding = kind in ("drop", "place")
        held_g = None
        gref = ry - arm
        if holding:
            r = allr[name]
            held_g = (r[0] - rx, r[1] - rx, r[2] - gref)
        obstacles = [(q[0], q[1], q[3]) for n, q in allr.items()
                     if not (holding and n == name)]
        tx, ty = leg[3] if kind == "pick" else leg[2]
        G, B = self._split_boxes(held_g)
        vcmd = 1.0 if holding else 0.0

        dx, dy, darm, arrived = self._control(rx, ry, arm, tx, ty - self.arm, G, B, obstacles)
        if self.stuck >= 2:
            dx, dy, darm, arrived = 0.0, min(STEP, YMAX - ry), 0.0, False
        if arrived:
            if kind == "pick":
                vcmd = 1.0
            elif kind == "drop":
                vcmd = 0.0
            self.leg += 1
        self.last = (rx, ry, dx, dy)
        self.last_arm = arm
        return self._act(dx, dy, dth, darm, vcmd)

    def _split_boxes(self, held_g=None):
        """Gripper-attached boxes (relative to g = y - arm) and base boxes."""
        gh = self.gh / 2.0
        G = [(-gh, gh, -self.gw)]
        if held_g is not None:
            # keep the vacuum face well above other objects while carrying
            G = [(-gh, gh, -self.gw - VAC_CLR), held_g]
        rb = self.base_r
        Bx = []
        edges = np.linspace(0.0, rb, 6)
        for a0, b0 in zip(edges[:-1], edges[1:]):
            off = -np.sqrt(max(rb * rb - a0 * a0, 0.0))
            Bx.append((a0, b0, off))
            Bx.append((-b0, -a0, off))
        return G, Bx

    def _control(self, x, y, a, tx, tg, G, B, obstacles):
        """Returns (dx, dy, darm, arrived). g = y - a is the gripper ref."""
        md = self.max_d - 1e-6
        mda = self.max_darm - 1e-6
        amin, amax = self.base_r, self.arm
        g = y - a
        ex = tx - x
        n = max(2, int(abs(ex) / 0.0025) + 2)
        X = np.linspace(x, tx, n)
        SG = self._safe(X, G, obstacles)
        SB = self._safe(X, B, obstacles)
        sgn = 1.0 if ex >= 0 else -1.0
        dxf = float(np.clip(ex, -md, md))
        lo_a, hi_a = max(amin, a - mda), min(amax, a + mda)
        for f in (1.0, 0.8, 0.6, 0.4, 0.25, 0.1, 0.0):
            dx = dxf * f
            nx = x + dx
            sw = (X - nx) * sgn <= 1e-9
            px = np.array([nx])
            rg_sw = max(float(SG[sw].max()) if sw.any() else -1.0,
                        float(self._safe(px, G, obstacles)[0]))
            rb_sw = max(float(SB[sw].max()) if sw.any() else -1.0,
                        float(self._safe(px, B, obstacles)[0]))
            ahead = ~sw
            if ahead.any():
                dist = 0.9 * np.abs(X[ahead] - nx)
                rg_ah = float((SG[ahead] - dist).max())
                rb_ah = float((SB[ahead] - dist).max())
            else:
                rg_ah = rb_ah = -1.0
            y_lo = max(y - md, rb_sw, rb_ah, rg_ah + amin, rg_sw + amin)
            y_hi = min(y + md, YMAX)
            if y_lo > y_hi + 1e-9:
                continue
            g_des = float(np.clip(tg, g - md - mda, g + md + mda))
            g_des = max(g_des, rg_sw)
            ny = float(np.clip(g_des + amax, y_lo, y_hi))
            ng = float(np.clip(g_des, ny - hi_a, ny - lo_a))
            if ng < rg_sw - 1e-9:
                continue
            arrived = abs(nx - tx) < 1e-5 and abs(ng - tg) < 1e-5
            return dx, ny - y, (ny - ng) - a, arrived
        dy = max(0.0, min(md, YMAX - y))
        return 0.0, dy, -(a - lo_a), False
