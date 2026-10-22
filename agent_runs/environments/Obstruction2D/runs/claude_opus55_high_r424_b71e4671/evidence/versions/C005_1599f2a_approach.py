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
        boxes = [(-self.base_r, self.base_r, -self.base_r),
                 (-gh, gh, -(self.arm + self.gw))]
        if held_rel is not None:
            boxes.append(held_rel)
        return boxes

    @staticmethod
    def _safe(X, boxes, obstacles):
        """Minimal robot y at each x in X such that boxes clear obstacles."""
        req = np.full(X.shape, -1.0)
        for bx0, bx1, boff in boxes:
            req = np.maximum(req, FLOOR_Y + MY - boff)
            for ox0, ox1, otop in obstacles:
                ov = (X + bx1 > ox0 - MX) & (X + bx0 < ox1 + MX)
                req = np.where(ov, np.maximum(req, otop + MY - boff), req)
        return req

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
        return req <= py + 1e-6

    def _d_options(self, r):
        lo, hi = self._grasp_d(r)
        if lo > hi:
            return []
        c = float(np.clip(0.0, lo, hi))
        opts = [c] + list(np.linspace(lo, hi, 9))
        return sorted(set(float(v) for v in opts), key=lambda v: abs(v - c))

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
        best = None
        for k in range(len(cand) + 1):
            if best is not None and k > 2:
                break
            for R in itertools.permutations(cand, k):
                res = self._plan_subset(start, R, orects, br, (sr[0], sr[1]), boxes0)
                if res is not None and (best is None or res[0] < best[0]):
                    best = res
        return None if best is None else best[1]

    def _plan_subset(self, start, R, orects, br, surf, boxes0):
        sx0, sx1 = surf
        bw = br[1] - br[0]
        lo, hi = self._grasp_d(br)
        if lo > hi:
            return None
        legs = []
        cost = 0.0
        pos = start
        cur = dict(orects)
        block_obs = (br[0], br[1], br[3])
        bd_opts = self._d_options(br)
        e = 0.004
        lefts = np.arange(sx0 + e, sx1 - bw - e + 1e-9, 0.004)
        if len(lefts) == 0:
            lefts = np.array([(sx0 + sx1) / 2 - bw / 2])
        for n in R:
            r = cur[n]
            others = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [block_obs]
            dl = [v for v in self._d_options(r) if self._pick_ok(r, v, others)]
            if not dl:
                return None
            d = dl[0]
            pick = self._pick_pose(r, d)
            c1 = self._leg_cost(pos, pick, boxes0, others + [(r[0], r[1], r[3])])
            held = self._held_rel(r, d)
            boxes_h = self._assembly(held)
            w, h = r[1] - r[0], r[3] - r[2]
            forb = [(q[0], q[1]) for m, q in cur.items() if m != n]
            forb.append((br[0], br[1]))
            bestd = None
            for left in np.arange(0.003, WORLD_MAX_X - 0.003 - w, 0.01):
                a, b = left, left + w
                if any(b > f0 - 0.012 and a < f1 + 0.012 for f0, f1 in forb):
                    continue
                if b > sx0 - 0.04 and a < sx1 + 0.04:
                    ok = any(b + 0.04 <= L or a - 0.04 >= L + bw for L in lefts)
                    if not ok:
                        continue
                tx = left - held[0]
                if not (XMIN <= tx <= XMAX):
                    continue
                ty = DROP_BOT - held[2]
                if ty > YMAX:
                    continue
                dpose = (tx, ty)
                nob = (left, left + w, DROP_BOT + h)
                obs_after = [(q[0], q[1], q[3]) for m, q in cur.items() if m != n] + [nob]
                if not any(self._pick_ok(br, v, obs_after) for v in bd_opts[:5]):
                    continue
                c2 = self._leg_cost(pick, dpose, boxes_h, others)
                c3 = abs(tx - (br[0] + br[1]) / 2) / STEP
                sc = c2 + c3
                if bestd is None or sc < bestd[0]:
                    bestd = (sc, dpose, left, c2)
            if bestd is None:
                return None
            _, dpose, left, c2 = bestd
            cost += c1 + c2
            legs.append(("pick", n, d, pick))
            legs.append(("drop", n, dpose))
            cur[n] = (left, left + w, DROP_BOT, DROP_BOT + h)
            pos = dpose
        obst_final = [(q[0], q[1], q[3]) for q in cur.values()]
        bestp = None
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
                sc = c1 + c2
                if bestp is None or sc < bestp[0]:
                    bestp = (sc, float(d), pick, (tx, ty))
        if bestp is None:
            return None
        sc, d, pick, ppose = bestp
        cost += sc
        legs.append(("pick", self.block_name, d, pick))
        legs.append(("place", self.block_name, ppose))
        return cost, legs

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
        darm = float(np.clip(self.arm - arm, -self.max_darm, self.max_darm))

        if self.last is not None:
            lx, ly, cdx, cdy = self.last
            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
                self.stuck += 1
            else:
                self.stuck = 0

        if self.leg >= len(self.legs):
            self.last = None
            return self._act(0, 0.0, dth, darm, vac)

        leg = self.legs[self.leg]
        kind, name = leg[0], leg[1]
        allr = {o.name: _rect(state, o) for o in obst + [block]}
        holding = kind in ("drop", "place")
        held_rel = None
        if holding:
            r = allr[name]
            held_rel = (r[0] - rx, r[1] - rx, r[2] - ry)
        obstacles = [(q[0], q[1], q[3]) for n, q in allr.items()
                     if not (holding and n == name)]
        tx, ty = leg[3] if kind == "pick" else leg[2]
        boxes = self._assembly(held_rel)
        vcmd = 1.0 if holding else 0.0

        dx, dy = self._control(rx, ry, tx, ty, boxes, obstacles)
        if self.stuck >= 2:
            dx, dy = 0.0, min(STEP, YMAX - ry)
        arrived = abs(rx + dx - tx) < 1e-5 and abs(ry + dy - ty) < 1e-5
        if arrived:
            if kind == "pick":
                vcmd = 1.0
            elif kind == "drop":
                vcmd = 0.0
            self.leg += 1
        self.last = (rx, ry, dx, dy)
        return self._act(dx, dy, dth, darm, vcmd)

    def _control(self, rx, ry, tx, ty, boxes, obstacles):
        md = self.max_d - 1e-6
        ex, ey = tx - rx, ty - ry
        if abs(ex) <= md and abs(ey) <= md:
            req = float(self._safe(np.array([tx]), boxes, obstacles)[0])
            X = np.linspace(rx, tx, 12)
            if req <= ty + 1e-6 and float(self._safe(X, boxes, obstacles).max()) <= max(ty, ry) + 1e-6:
                return ex, ey
        n = max(2, int(abs(ex) / 0.0025) + 2)
        X = np.linspace(rx, tx, n)
        S = self._safe(X, boxes, obstacles)
        sgn = 1.0 if ex >= 0 else -1.0
        dxf = float(np.clip(ex, -md, md))
        for f in (1.0, 0.8, 0.6, 0.4, 0.25, 0.1, 0.0):
            dx = dxf * f
            nx = rx + dx
            sw = (X - nx) * sgn <= 1e-9
            req_sweep = float(S[sw].max()) if sw.any() else -1.0
            req_sweep = max(req_sweep, float(self._safe(np.array([nx]), boxes, obstacles)[0]))
            ahead = ~sw
            req_ahead = float((S[ahead] - 0.9 * np.abs(X[ahead] - nx)).max()) if ahead.any() else -1.0
            req = max(req_sweep, req_ahead)
            ny = ry + float(np.clip(ey, -md, md))
            ny = max(ny, req + 1e-4)
            if ny - ry > md + 1e-9 or ny > YMAX:
                continue
            return dx, ny - ry
        return 0.0, max(0.0, min(md, YMAX - ry))
