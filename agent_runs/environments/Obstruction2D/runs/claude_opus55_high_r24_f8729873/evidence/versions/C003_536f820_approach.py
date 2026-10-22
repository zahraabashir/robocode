import math
import numpy as np

WORLD_X = (0.0, 1.618)
ROBOT_Y_MAX = 0.895
FLOOR = 0.1
ARM = 0.2          # extended arm length we use
GW = 0.01          # gripper width (along arm)
GH = 0.07          # gripper height (perpendicular)
BASE_R = 0.1
RX_MIN = 0.1 + 0.002
RX_MAX = 1.618 - 0.1 - 0.002
TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)


def _rect_bbox(state, o):
    x = float(state.get(o, "x")); y = float(state.get(o, "y"))
    w = float(state.get(o, "width")); h = float(state.get(o, "height"))
    th = float(state.get(o, "theta"))
    if abs(th) < 1e-6:
        return (x, y, x + w, y + h)
    c, s = math.cos(th), math.sin(th)
    pts = [(x, y), (x + w * c, y + w * s), (x - h * s, y + h * c),
           (x + w * c - h * s, y + w * s + h * c)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def _circle_rect_dist(cx, cy, b):
    dx = max(b[0] - cx, 0.0, cx - b[2])
    dy = max(b[1] - cy, 0.0, cy - b[3])
    return math.hypot(dx, dy)


def _overlap(a, b, m=0.0):
    return a[0] < b[2] + m and b[0] < a[2] + m and a[1] < b[3] + m and b[1] < a[3] + m


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.array(action_space.low, dtype=np.float32)
        self.high = np.array(action_space.high, dtype=np.float32)

    # ------------------------------------------------------------------
    def reset(self, state, info):
        self.state = state
        self.gen = self._plan()
        self.vac = 0.0

    def get_action(self, state):
        self.state = state
        try:
            a = next(self.gen)
        except StopIteration:
            self.gen = self._plan()
            try:
                a = next(self.gen)
            except StopIteration:
                a = np.zeros(5, dtype=np.float32)
        a = np.clip(np.asarray(a, dtype=np.float32), self.low, self.high)
        return a

    # ------------------------------------------------------------------
    def _objs(self):
        s = self.state
        robot = None; block = None; surf = None; obst = []
        for n in sorted(s.get_object_names()):
            o = s.get_object_from_name(n)
            tn = o.type.name
            if tn == "crv_robot":
                robot = o
            elif tn == "target_block":
                block = o
            elif tn == "target_surface":
                surf = o
            else:
                obst.append(o)
        return robot, block, surf, obst

    def _rpos(self):
        r = self._objs()[0]
        s = self.state
        return (float(s.get(r, "x")), float(s.get(r, "y")),
                float(s.get(r, "theta")), float(s.get(r, "arm_joint")))

    # ------------------------------------------------------------------
    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
        return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)

    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200):
        """Move towards (tx, ty); yields actions. Returns True on success."""
        stuck = 0
        last = None
        for _ in range(max_steps):
            x, y, th, aj = self._rpos()
            gx = x if tx is None else tx
            gy = y if ty is None else ty
            ex, ey = gx - x, gy - y
            if abs(ex) <= tol and abs(ey) <= tol:
                return True
            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7:
                stuck += 1
                if stuck >= 2:
                    return False
            else:
                stuck = 0
            last = (x, y)
            yield self._act(float(np.clip(ex, -0.05, 0.05)), float(np.clip(ey, -0.05, 0.05)))
        return False

    def _setup_pose(self):
        # rise, orient downwards, extend arm
        x, y, th, aj = self._rpos()
        yield from self._goto(None, ROBOT_Y_MAX)
        for _ in range(60):
            x, y, th, aj = self._rpos()
            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
            ea = ARM - aj
            if abs(eth) < 1e-4 and abs(ea) < 1e-4:
                break
            yield np.array([0, 0, np.clip(eth, -0.19, 0.19), np.clip(ea, -0.1, 0.1), self.vac],
                           dtype=np.float32)

    # ------------------------------------------------------------------
    def _others_bboxes(self, exclude):
        robot, block, surf, obst = self._objs()
        out = []
        for o in [block] + obst:
            if o in exclude:
                continue
            out.append(_rect_bbox(self.state, o))
        return out

    def _descent_free(self, rx, ry_final, carried_bbox_final, others, margin=0.01):
        """Check vertical descent from travel height to ry_final at x=rx is collision free."""
        # base circle sweep: check at the final (lowest) position -- sweep is vertical,
        # and anything below is covered by checking the column.
        for b in others:
            # circle swept vertically from ry_final upwards
            cy = min(max(ry_final, b[1]), ROBOT_Y_MAX)
            cy = max(cy, ry_final)
            if _circle_rect_dist(rx, cy, b) < BASE_R + margin:
                return False
            # arm + gripper column
            col = (rx - GH / 2, ry_final - TIP, rx + GH / 2, ROBOT_Y_MAX)
            if _overlap(col, b, margin * 0.3):
                return False
            if carried_bbox_final is not None:
                cb = carried_bbox_final
                colc = (cb[0], cb[1], cb[2], cb[3] + (ROBOT_Y_MAX - ry_final))
                if _overlap(colc, b, margin * 0.5):
                    return False
        return True

    def _grasp_cands(self, b, pref=None):
        lo = b[0] + 0.012
        hi = b[2] - 0.012
        cx = (b[0] + b[2]) / 2 if pref is None else pref
        if hi < lo:
            lo = hi = (b[0] + b[2]) / 2
        full_lo = b[0] + GH / 2
        full_hi = b[2] - GH / 2
        vals = np.linspace(lo, hi, 41).tolist() + [min(max(cx, lo), hi)]

        def key(v):
            # prefer full gripper contact, then closeness to preferred
            pen = 0.0
            if full_lo <= full_hi:
                pen = max(0.0, full_lo - v, v - full_hi)
            return (round(pen, 4) > 0.0, abs(v - cx))
        return sorted(vals, key=key)

    def _choose_grasp_x(self, o, others, pref=None):
        b = _rect_bbox(self.state, o)
        ry = b[3] + TIP + 0.003
        for gx in self._grasp_cands(b, pref):
            if gx < RX_MIN or gx > RX_MAX:
                continue
            if self._descent_free(gx, ry, None, others):
                return gx
        return None

    def _pick(self, o, pref=None):
        others = self._others_bboxes([o])
        gx = self._choose_grasp_x(o, others, pref)
        if gx is None:
            return False
        b = _rect_bbox(self.state, o)
        yield from self._goto(None, ROBOT_Y_MAX)
        yield from self._goto(gx, None)
        ry = b[3] + TIP + 0.003
        yield from self._goto(None, ry, tol=1e-4)
        self.vac = 1.0
        yield self._act()
        yield self._act()
        yield from self._goto(None, ROBOT_Y_MAX)
        nb = _rect_bbox(self.state, o)
        if nb[1] < b[1] + 0.05:
            self.vac = 0.0
            yield self._act()
            return False
        return True

    def _place_at(self, o, target_left, target_bottom):
        x, y, _, _ = self._rpos()
        b = _rect_bbox(self.state, o)
        rx = x + (target_left - b[0])
        yield from self._goto(rx, None)
        x, y, _, _ = self._rpos()
        b = _rect_bbox(self.state, o)
        ry = y - (b[1] - target_bottom)
        yield from self._goto(None, ry, tol=1e-4)

    # ------------------------------------------------------------------
    def _final_placement(self):
        """Returns (left, bottom, surface_bbox, grasp_offset_from_block_left)."""
        robot, block, surf, obst = self._objs()
        s = self.state
        sb = _rect_bbox(s, surf)
        bb = _rect_bbox(s, block)
        bw = bb[2] - bb[0]
        Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
        Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
        Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
        if Lhi < Llo:
            Llo = Lhi = Lc
        best = None
        for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
            for L in sorted(np.linspace(Llo, Lhi, 21).tolist() + [Lc], key=lambda v: abs(v - Lc)):
                if RX_MIN <= L + g <= RX_MAX:
                    best = (L, g)
                    break
            if best is not None:
                break
        if best is None:
            best = (Lc, bw / 2)
        return best[0], sb[3] + 0.008, sb, best[1]

    def _blocking(self):
        """Obstructions that interfere with placing the block on the surface."""
        robot, block, surf, obst = self._objs()
        s = self.state
        left, bottom, sb, g = self._final_placement()
        bb = _rect_bbox(s, block)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        final_bb = (left, bottom, left + bw, bottom + bh)
        rx = left + g
        ry = bottom + bh + TIP + 0.003
        res = []
        for o in obst:
            ob = _rect_bbox(s, o)
            if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
                res.append(o)
            elif ob[0] < sb[2] and ob[2] > sb[0] and ob[1] < sb[3] + 0.05:
                res.append(o)
        return res

    def _find_spot(self, o):
        """Find (left, bottom) to park obstruction o."""
        robot, block, surf, obst = self._objs()
        s = self.state
        ob = _rect_bbox(s, o)
        w, h = ob[2] - ob[0], ob[3] - ob[1]
        # offset of grasp relative to object left
        x, y, _, _ = self._rpos()
        goff = x - ob[0]
        sb = _rect_bbox(s, surf)
        others = self._others_bboxes([o])
        left_f, bottom_f, _, _ = self._final_placement()
        bb = _rect_bbox(s, block)
        bw = bb[2] - bb[0]
        # forbidden zone around the surface / final block placement
        fz = (min(sb[0], left_f) - 0.13, max(sb[2], left_f + bw) + 0.13)
        levels = [FLOOR + 0.005]
        best = None
        xs = np.arange(WORLD_X[0] + 0.01, WORLD_X[1] - w - 0.01, 0.01)
        for bottom in levels:
            for lx in xs:
                if lx < fz[1] and lx + w > fz[0]:
                    continue
                rx = lx + goff
                if rx < RX_MIN or rx > RX_MAX:
                    continue
                cand = (lx, bottom, lx + w, bottom + h)
                bad = False
                for b in others:
                    if _overlap(cand, b, 0.02):
                        bad = True
                        break
                if bad:
                    continue
                ry = bottom + h + (y - ob[3])
                if not self._descent_free(rx, ry, cand, others, margin=0.015):
                    continue
                cost = abs(rx - x)
                if best is None or cost < best[0]:
                    best = (cost, lx, bottom)
            if best is not None:
                break
        if best is None:
            # fallback: park in the air high above in the far region
            far = WORLD_X[1] - w - 0.15 if (sb[0] + sb[2]) / 2 < WORLD_X[1] / 2 else 0.15
            return far, 0.45
        return best[1], best[2]

    def _plan(self):
        self.vac = 0.0
        yield from self._setup_pose()
        failures = 0
        for _ in range(30):
            blockers = self._blocking()
            if not blockers:
                break
            # pick blockers in order of height (tallest first) that are graspable
            robot, block, surf, obst = self._objs()
            blockers.sort(key=lambda o: -_rect_bbox(self.state, o)[3])
            picked = False
            for o in blockers:
                others = self._others_bboxes([o])
                if self._choose_grasp_x(o, others) is None:
                    continue
                ok = yield from self._pick(o)
                if not ok:
                    failures += 1
                    continue
                left, bottom = self._find_spot(o)
                yield from self._place_at(o, left, bottom)
                self.vac = 0.0
                yield self._act()
                yield from self._goto(None, ROBOT_Y_MAX)
                picked = True
                break
            if not picked:
                failures += 1
                if failures > 5:
                    break
        # now the target block
        for _ in range(10):
            robot, block, surf, obst = self._objs()
            left, bottom, sb, g = self._final_placement()
            bb = _rect_bbox(self.state, block)
            ok = yield from self._pick(block, pref=bb[0] + g)
            if ok:
                break
        left, bottom, sb, g = self._final_placement()
        yield from self._place_at(block, left, bottom)
        self.vac = 0.0
        for _ in range(5):
            yield self._act()
