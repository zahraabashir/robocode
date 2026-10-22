import numpy as np

WORLD_MIN_X = 0.0
WORLD_MAX_X = 1.618
FLOOR_Y = 0.1


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.array(action_space.low, dtype=np.float32)
        self.high = np.array(action_space.high, dtype=np.float32)
        self.max_dx = float(self.high[0])
        self.max_dth = float(self.high[2])
        self.max_darm = float(self.high[3])

    # ------------------------------------------------------------------ utils
    def _g(self, s, o, f):
        return float(s.get(o, f))

    def _rect(self, s, o):
        x, y = self._g(s, o, "x"), self._g(s, o, "y")
        w, h = self._g(s, o, "width"), self._g(s, o, "height")
        th = self._g(s, o, "theta")
        c, sn = np.cos(th), np.sin(th)
        pts = np.array([[0, 0], [w, 0], [w, h], [0, h]])
        R = np.array([[c, -sn], [sn, c]])
        v = pts @ R.T + np.array([x, y])
        return v[:, 0].min(), v[:, 0].max(), v[:, 1].min(), v[:, 1].max()

    def _parse(self, s):
        robot = s.get_objects(self.t_robot)[0] if self.t_robot else None
        return robot

    def _objs(self, s):
        d = {}
        for name in s.get_object_names():
            o = s.get_object_from_name(name)
            d[str(name) if isinstance(name, str) else o.name] = o
        return d

    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
        a = np.array([dx, dy, dth, darm, vac], dtype=np.float32)
        return np.clip(a, self.low, self.high)

    # ------------------------------------------------------------------ api
    def reset(self, state, info):
        self.phase = "choose"
        self.target = None  # name of object being manipulated
        self.drop_x = None
        self.last_robot = None
        self.last_cmd = None
        self.blocked_count = 0
        self.grasp_offset = None
        self.steps = 0

    def get_action(self, state):
        self.steps += 1
        objs = self._objs(state)
        robot = None
        for n, o in objs.items():
            if o.type.name == "crv_robot":
                robot = o
        rx, ry = self._g(state, robot, "x"), self._g(state, robot, "y")
        rth = self._g(state, robot, "theta")
        arm = self._g(state, robot, "arm_joint")
        arm_max = self._g(state, robot, "arm_length")
        gw = self._g(state, robot, "gripper_width")
        base_r = self._g(state, robot, "base_radius")
        vac = self._g(state, robot, "vacuum")

        # detect blocked motion
        moved = True
        if self.last_robot is not None and self.last_cmd is not None:
            lx, ly = self.last_robot
            cdx, cdy = self.last_cmd
            if (abs(cdx) > 1e-5 or abs(cdy) > 1e-5) and abs(lx - rx) < 1e-7 and abs(ly - ry) < 1e-7:
                moved = False
        self.last_robot = (rx, ry)

        block = surface = None
        obstructions = []
        for n, o in objs.items():
            tn = o.type.name
            if tn == "target_block":
                block = o
            elif tn == "target_surface":
                surface = o
            elif tn == "rectangle":
                obstructions.append(o)
        sx0, sx1, sy0, sy1 = self._rect(state, surface)

        rects = {}
        for o in obstructions + [block]:
            rects[o.name] = self._rect(state, o)

        # gripper face y (pointing down)
        face = ry - arm - gw

        # travel height: carried object bottom clears all tops
        max_top = max(r[3] for r in rects.values())
        carry_h = 0.0
        if self.target is not None and vac > 0.5 and self.phase in ("lift", "carry", "lower"):
            tr = rects[self.target]
            carry_h = tr[3] - tr[2]
        travel_y = max_top + 0.05 + carry_h + arm_max + gw
        travel_y = min(max(travel_y, 0.6), 0.89)

        dx = dy = dth = darm = 0.0
        vcmd = 1.0 if vac > 0.5 else 0.0

        # keep orientation down and arm extended
        th_err = (-np.pi / 2 - rth + np.pi) % (2 * np.pi) - np.pi
        dth = np.clip(th_err, -self.max_dth, self.max_dth)
        darm = np.clip(arm_max - arm, -self.max_darm, self.max_darm)

        if self.phase == "choose":
            # obstructions overlapping surface
            bw = rects[block.name][1] - rects[block.name][0]
            tgt = None
            best = None
            for o in obstructions:
                x0, x1, y0, y1 = rects[o.name]
                if x1 > sx0 - 0.005 and x0 < sx1 + 0.005 and y0 < sy1 + 0.3:
                    d = abs((x0 + x1) / 2 - (sx0 + sx1) / 2)
                    if best is None or d < best:
                        best, tgt = d, o.name
            if tgt is None:
                tgt = block.name
            self.target = tgt
            self.phase = "rise"
            self.last_cmd = (0, 0)
            return self._act(0, 0, dth, darm, 0.0)

        tr = rects[self.target]
        tcx = self._grasp_x(tr, rects[block.name], (sx0, sx1), self.target == block.name)

        if self.phase == "rise":
            # go up to travel height without vacuum
            if ry < travel_y - 1e-3:
                dy = min(travel_y - ry, self.max_dx)
            else:
                self.phase = "over"
        if self.phase == "over":
            ex = tcx - rx
            if abs(ex) > 1e-4:
                dx = ex
            else:
                self.phase = "descend"
                self.blocked_count = 0
        if self.phase == "descend":
            contact_y = tr[3] + arm + gw
            if not moved:
                self.phase = "grasp"
            else:
                rem = ry - contact_y
                if rem > 0.006:
                    dy = -min(rem - 0.004, self.max_dx)
                else:
                    dy = -0.002
                if rem < -0.02:
                    self.phase = "grasp"
                    dy = 0.0
        if self.phase == "grasp":
            vcmd = 1.0
            dy = 0.0
            self.grasp_ref = (tr[0] - rx, tr[2] - ry)
            self.phase = "lift"
            self.last_cmd = (0, 0)
            return self._act(0, 0, dth, 0.0, vcmd)
        if self.phase == "lift":
            vcmd = 1.0
            if ry < travel_y - 1e-3:
                dy = min(travel_y - ry, self.max_dx)
            else:
                self.phase = "carry"
                self._plan_drop(state, rects, block, (sx0, sx1), rx)
        if self.phase == "carry":
            vcmd = 1.0
            ex = self.drop_x - rx
            if abs(ex) > 1e-4:
                dx = ex
            else:
                self.phase = "lower"
        if self.phase == "lower":
            vcmd = 1.0
            is_block = self.target == block.name
            floor_top = sy1 if is_block else FLOOR_Y
            rem = tr[2] - floor_top
            if not moved:
                self.phase = "release"
            else:
                if rem > 0.006:
                    dy = -min(rem - 0.003, self.max_dx)
                else:
                    dy = -0.002
        if self.phase == "release":
            vcmd = 0.0
            dy = 0.0
            self.phase = "post"
            self.last_cmd = (0, 0)
            return self._act(0, 0, dth, 0.0, vcmd)
        if self.phase == "post":
            vcmd = 0.0
            self.phase = "choose"
            dy = 0.02

        dx = float(np.clip(dx, -self.max_dx, self.max_dx))
        dy = float(np.clip(dy, -self.max_dx, self.max_dx))
        # keep within world
        self.last_cmd = (dx, dy)
        return self._act(dx, dy, dth, darm, vcmd)

    XMIN, XMAX = 0.102, 1.516

    def _grasp_x(self, tr, br, surf, is_block):
        """Robot x at which to grasp object with x-range tr."""
        cx = (tr[0] + tr[1]) / 2
        hw = (tr[1] - tr[0]) / 2
        dmax = max(hw + 0.035 - 0.012, 0.0)  # gripper overlap allowance
        lo, hi = -dmax, dmax
        # pick reachability
        lo = max(lo, self.XMIN - cx)
        hi = min(hi, self.XMAX - cx)
        if is_block:
            scx = (surf[0] + surf[1]) / 2
            lo2 = max(lo, self.XMIN - scx)
            hi2 = min(hi, self.XMAX - scx)
            if lo2 <= hi2:
                lo, hi = lo2, hi2
        if lo > hi:
            return float(np.clip(cx, self.XMIN, self.XMAX))
        d = float(np.clip(0.0, lo, hi))
        return cx + d

    def _plan_drop(self, state, rects, block, surf, rx):
        tr = rects[self.target]
        w = tr[1] - tr[0]
        off = tr[0] - rx  # left edge relative to robot x
        if self.target == block.name:
            sx0, sx1 = surf
            want_left = (sx0 + sx1) / 2 - w / 2
            self.drop_x = float(np.clip(want_left - off, self.XMIN, self.XMAX))
            return
        # choose free floor location maximizing clearance
        sx0, sx1 = surf
        bw = rects[block.name][1] - rects[block.name][0]
        forb = [(sx0 - 0.02, sx1 + 0.02)]
        for n, r in rects.items():
            if n == self.target:
                continue
            forb.append((r[0], r[1]))
        best = None
        for left in np.arange(0.005, WORLD_MAX_X - 0.005 - w, 0.005):
            a, b = left, left + w
            if not (self.XMIN <= left - off <= self.XMAX):
                continue
            clr = min(min(abs(a - f1) if a >= f1 else (abs(f0 - b) if b <= f0 else -1.0)
                          for f0, f1 in forb), 0.3)
            if clr < 0:
                continue
            score = clr - 0.02 * abs(left + w / 2 - rx)
            if best is None or score > best[0]:
                best = (score, left)
        left = best[1] if best else 0.15
        self.drop_x = float(np.clip(left - off, self.XMIN, self.XMAX))
