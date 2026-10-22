"""Approach for Obstruction2DEnv: clear obstructions off the target surface,
then pick the target block and place it on the surface.

Robot is kept pointing straight down (theta=-pi/2) with arm fully extended.
Motions between key poses are planned with a small collision-checked
path search (plateau paths with diagonal rise/fall)."""
import math
import numpy as np

FLOOR = 0.1
X_MIN, X_MAX = 0.1005, 1.5175   # robot base x limits
Y_MAX = 0.895                   # robot base y limit
WORLD_X = 1.618
GAP = 0.0015                    # gripper gap above object when grasping
PLACE_GAP = 0.004               # object gap above floor when releasing
SPEED = 0.05


def _cheb(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def _nsteps(path):
    return sum(math.ceil(_cheb(path[i], path[i + 1]) / SPEED - 1e-6) for i in range(len(path) - 1))


class GeneratedApproach:
    FLOOR_BOX = dict(name="__floor__", x=-2.0, y=-2.0, w=6.0, h=2.0 + FLOOR)
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.low = np.asarray(action_space.low, dtype=np.float32)
        self.high = np.asarray(action_space.high, dtype=np.float32)

    # ------------------------------------------------------------------ parse
    def _parse(self, state):
        robot = None
        rects = {}
        block = surface = None
        for name in state.get_object_names():
            o = state.get_object_from_name(name) if isinstance(name, str) else name
            tn = o.type.name
            if tn == "crv_robot":
                robot = o
            elif tn == "target_block":
                block = o
            elif tn == "target_surface":
                surface = o
            elif tn in ("rectangle",):
                rects[o.name] = o
        g = lambda o, f: float(state.get(o, f))
        self.robot = dict(x=g(robot, "x"), y=g(robot, "y"), theta=g(robot, "theta"),
                          arm=g(robot, "arm_joint"), vac=g(robot, "vacuum"),
                          arm_max=g(robot, "arm_length"),
                          gw=g(robot, "gripper_width"), gh=g(robot, "gripper_height"),
                          r=g(robot, "base_radius"))

        def box(o):
            return dict(name=o.name, x=g(o, "x"), y=g(o, "y"), w=g(o, "width"), h=g(o, "height"))
        self.block = box(block)
        self.surface = box(surface)
        self.obst = {n: box(o) for n, o in rects.items()}

    def _all_movable(self):
        d = dict(self.obst)
        d[self.block["name"]] = self.block
        return d

    def _grip_off(self):
        return self.robot["arm_max"] + self.robot["gw"] / 2.0

    # --------------------------------------------------------- collision check
    def _collides(self, pts, obstacles, carried, margin_map, default_margin):
        """pts: (N,2) base positions. carried: (dx0, dx1, dy0, dy1) rel to base or None.
        obstacles: list of boxes. Returns True if any sample collides."""
        X = pts[:, 0]
        Y = pts[:, 1]
        r = self.robot["r"]
        half = self.robot["gh"] / 2.0
        go = self._grip_off()
        if np.any(X < X_MIN - 1e-6) or np.any(X > X_MAX + 1e-6) or np.any(Y > Y_MAX + 1e-6):
            return True
        # boxes attached to robot: gripper/arm, carried
        att = [(X - half, X + half, Y - go, Y)]
        if carried is not None:
            att.append((X + carried[0], X + carried[1], Y + carried[2], Y + carried[3]))
        for o in list(obstacles) + [self.FLOOR_BOX]:
            m = margin_map.get(o["name"], default_margin)
            ox0, ox1 = o["x"] - m, o["x"] + o["w"] + m
            oy0, oy1 = o["y"] - m, o["y"] + o["h"] + m
            # circle vs rect
            cx = np.clip(X, ox0, ox1)
            cy = np.clip(Y, oy0, oy1)
            if np.any((X - cx) ** 2 + (Y - cy) ** 2 < r * r):
                return True
            for (x0, x1, y0, y1) in att:
                if np.any((x0 < ox1) & (x1 > ox0) & (y0 < oy1) & (y1 > oy0)):
                    return True
        return False

    def _path_free(self, path, obstacles, carried, margin_map, m):
        for i in range(len(path) - 1):
            a, b = np.array(path[i]), np.array(path[i + 1])
            L = max(np.linalg.norm(b - a), 1e-9)
            n = int(L / 0.003) + 2
            t = np.linspace(0, 1, n)[:, None]
            pts = a[None] * (1 - t) + b[None] * t
            if self._collides(pts, obstacles, carried, margin_map, m):
                return False
        return True

    def _plan_path(self, A, B, obstacles, carried, special_margin=None):
        """Find short collision-free polyline from A to B."""
        m = 0.004
        margin_map = {}
        # obstacles in contact at endpoints get zero margin
        for o in list(obstacles) + [self.FLOOR_BOX]:
            for P in (A, B):
                if self._collides(np.array([P]), [o], carried, {}, m):
                    margin_map[o["name"]] = 0.0
        if special_margin:
            margin_map.update(special_margin)
        cands = [[A, B]]
        sgn = 1.0 if B[0] >= A[0] else -1.0
        hs = np.arange(max(A[1], B[1]), Y_MAX + 1e-9, 0.01)
        hs = np.append(hs, Y_MAX)
        h_min = Y_MAX
        for h in hs:
            if self._path_free([(A[0], h), (B[0], h)], obstacles, carried, margin_map, m):
                h_min = h
                break
        hs = hs[hs >= h_min - 1e-9]
        for h in hs:
            for k1 in (1.0, 0.5, 0.0):
                for k2 in (1.0, 0.5, 0.0):
                    x1 = A[0] + sgn * k1 * (h - A[1])
                    x2 = B[0] - sgn * k2 * (h - B[1])
                    if sgn * (x2 - x1) <= 0:
                        # triangle: find intersection point
                        continue
                    p = [A, (x1, h), (x2, h), B]
                    cands.append(p)
            # triangle via single apex
            for xv in np.linspace(A[0], B[0], 9)[1:-1]:
                cands.append([A, (xv, h), B])
        scored = sorted(((_nsteps(p), len(p), i) for i, p in enumerate(cands)))
        checked = 0
        for s, _, i in scored:
            p = cands[i]
            checked += 1
            if checked > 3000:
                break
            if self._path_free(p, obstacles, carried, margin_map, m):
                return p
        # fallback: straight up, over, down
        return [A, (A[0], Y_MAX), (B[0], Y_MAX), B]

    # --------------------------------------------------------------- planning
    def reset(self, state, info):
        self.plan = []
        self.stall = 0
        self.last_pos = None
        self.target_name = None
        self.block_dest = None
        self.attempts = {}

    def _grasp_x(self, b, others):
        half = self.robot["gh"] / 2.0
        lo, hi = b["x"] + half + 0.003, b["x"] + b["w"] - half - 0.003
        if hi < lo:
            lo = hi = b["x"] + b["w"] / 2
        by = b["y"] + b["h"] + self._grip_off() + GAP
        c = b["x"] + b["w"] / 2
        cands = sorted(np.linspace(lo, hi, 21), key=lambda x: abs(x - c))
        R = self.robot["r"] + 0.005
        btop = b["y"] + b["h"]
        self.grasp_conflict = None
        for x in cands:
            if x < X_MIN or x > X_MAX:
                continue
            ok = True
            for o in others:
                if o["y"] + o["h"] > btop - 0.005 and o["x"] < x + half + 0.004 \
                        and o["x"] + o["w"] > x - half - 0.004:
                    ok = False
                    if self.grasp_conflict is None:
                        self.grasp_conflict = o
                    break
            if not ok:
                continue
            for o in others:
                x0, x1 = o["x"], o["x"] + o["w"]
                d = 0.0 if x0 <= x <= x1 else min(abs(x - x0), abs(x - x1))
                if d >= R:
                    continue
                if o["y"] + o["h"] > by - math.sqrt(R * R - d * d):
                    ok = False
                    if self.grasp_conflict is None:
                        self.grasp_conflict = o
                    break
            if ok:
                return x
        return None

    def _free_spot(self, b, others, forbid, gx_rel, gpos, next_pos):
        """Find (left x, bottom y) for box b on floor avoiding others and forbid."""
        w = b["w"]
        m = 0.03
        ivs = [(o["x"] - m, o["x"] + o["w"] + m) for o in others] + forbid
        best = None
        off = gpos[1] - b["y"]
        for bx in np.arange(X_MIN, X_MAX, 0.005):
            x0 = bx - gx_rel
            if x0 < 0.0 or x0 + w > WORLD_X:
                continue
            if any(x0 < i1 and x0 + w > i0 for i0, i1 in ivs):
                continue
            if self._column_hit(dict(b, x=x0, y=FLOOR + PLACE_GAP), extra=0.02):
                continue
            P = (bx, FLOOR + PLACE_GAP + off)
            cost = _cheb(gpos, P) + _cheb(P, next_pos)
            if best is None or cost < best[0]:
                best = (cost, x0)
        if best is not None:
            return best[1], FLOOR
        # fallback: stack on top of some other object away from surface
        best = None
        for o in others:
            top = o["y"] + o["h"]
            x0 = o["x"] + o["w"] / 2 - w / 2
            if self._column_hit(dict(b, x=x0, y=top + PLACE_GAP), extra=0.02):
                continue
            if best is None or top < best[0]:
                best = (top, x0)
        if best is not None:
            return best[1], best[0]
        return None

    def _column_info(self, dest_x):
        b = self.block
        gx_rel = b["w"] / 2
        gy_rel = b["h"] + self._grip_off() + GAP
        bx = dest_x + gx_rel
        py = FLOOR + 0.012 + gy_rel
        pts = np.stack([np.full(40, bx), np.linspace(py, Y_MAX, 40)], axis=1)
        carried = (-gx_rel, b["w"] - gx_rel, -gy_rel, b["h"] - gy_rel)
        return pts, carried

    def _column_hit(self, o, extra=0.0, dest_x=None):
        if dest_x is None:
            dest_x = self.block_dest
        pts, carried = self._column_info(dest_x)
        return self._collides(pts, [o], carried, {"__floor__": -1.0}, 0.01 + extra)

    def _choose_block_dest(self):
        s = self.surface
        b = self.block
        lo = s["x"] + 0.003
        hi = s["x"] + s["w"] - b["w"] - 0.003
        center = s["x"] + (s["w"] - b["w"]) / 2
        if hi <= lo:
            return center
        best = None
        for dx in np.linspace(lo, hi, 25):
            nb = 0
            for o in self.obst.values():
                if self._column_hit(o, dest_x=dx):
                    nb += 1
            cost = nb * 100 + abs(dx - center) * 0.1
            if best is None or cost < best[0]:
                best = (cost, dx)
        return best[1]

    def _make_plan(self):
        """Returns list of segments: each (waypoint list, vac, kind)."""
        s = self.surface
        s0, s1 = s["x"], s["x"] + s["w"]
        movable = self._all_movable()
        if self.block_dest is None:
            self.block_dest = self._choose_block_dest()
        blockers = [o for o in self.obst.values() if self._column_hit(o)]
        rx, ry = self.robot["x"], self.robot["y"]
        if blockers:
            tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
        else:
            tgt = self.block
        gx = None
        for _ in range(10):
            others = [b for n, b in movable.items() if n != tgt["name"]]
            gx = self._grasp_x(tgt, others)
            if gx is not None or self.grasp_conflict is None:
                break
            tgt = self.grasp_conflict
        n_att = self.attempts.get(tgt["name"], 0)
        self.attempts[tgt["name"]] = n_att + 1
        if n_att >= 3:
            # repeated failure: move the tallest nearby object instead
            near = [o for o in movable.values() if o["name"] != tgt["name"]
                    and o["name"] != self.block["name"]
                    and abs((o["x"] + o["w"] / 2) - (tgt["x"] + tgt["w"] / 2)) < 0.3
                    and self.attempts.get(o["name"], 0) < 3]
            if near:
                tgt = max(near, key=lambda o: o["y"] + o["h"])
                others = [b for n, b in movable.items() if n != tgt["name"]]
                gx = self._grasp_x(tgt, others)
        if gx is None:
            gx = min(max(tgt["x"] + tgt["w"] / 2, X_MIN), X_MAX)
        others = [b for n, b in movable.items() if n != tgt["name"]]
        self.target_name = tgt["name"]
        is_block = tgt["name"] == self.block["name"]
        gy = tgt["y"] + tgt["h"] + self._grip_off() + GAP
        gpos = (gx, gy)
        off = gy - tgt["y"]
        gx_rel = gx - tgt["x"]
        if is_block:
            dest_x = self.block_dest
            dest_y = FLOOR + 0.012 - PLACE_GAP
        else:
            b = self.block
            bgx = b["x"] + b["w"] / 2
            next_pos = (bgx, b["y"] + b["h"] + self._grip_off() + GAP)
            spot = self._free_spot(tgt, others, [], gx_rel, gpos, next_pos)
            if spot is None:
                spot = (tgt["x"], min(0.6, tgt["y"] + 0.3))
            dest_x, dest_y = spot
        px = min(max(dest_x + gx_rel, X_MIN), X_MAX)
        py = dest_y + off + PLACE_GAP
        # approach path (nothing carried)
        p1 = self._plan_path((rx, ry), gpos, others + [tgt], None,
                             special_margin={tgt["name"]: 0.0})
        carried = (tgt["x"] - gx, tgt["x"] + tgt["w"] - gx, tgt["y"] - gy, tgt["y"] + tgt["h"] - gy)
        p2 = self._plan_path(gpos, (px, py), others, carried)
        segs = []
        for w in p1[1:]:
            segs.append(dict(x=w[0], y=w[1], vac=0, kind="move"))
        segs.append(dict(x=gx, y=gy, vac=1, kind="grasp"))
        for w in p2[1:]:
            segs.append(dict(x=w[0], y=w[1], vac=1, kind="carry"))
        # release on the final step of the carry
        segs[-1]["release_last"] = not is_block
        return segs

    # ---------------------------------------------------------------- control
    def get_action(self, state):
        self._parse(state)
        r = self.robot
        if not self.plan:
            self.plan = self._make_plan()
            self.stall = 0
        for _ in range(20):
            wp = self.plan[0]
            if wp["kind"] == "grasp":
                reached = r["vac"] > 0.5
            else:
                reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4
                if wp.get("release_last"):
                    reached = reached and r["vac"] < 0.5
            if reached:
                self.plan.pop(0)
                self.stall = 0
                if not self.plan:
                    self.plan = self._make_plan()
                continue
            break
        wp = self.plan[0]
        pos = (round(r["x"], 5), round(r["y"], 5), round(r["arm"], 5), round(r["vac"]))
        if self.last_pos == pos:
            self.stall += 1
        else:
            self.stall = 0
        self.last_pos = pos
        dth = -math.pi / 2 - r["theta"]
        darm = r["arm_max"] - r["arm"]
        if wp["kind"] == "grasp":
            return self._act(0, 0, darm, 1, dth)
        if self.stall >= 2:
            # stuck: nudge up and replan
            self.stall = 0
            self.plan = []
            if wp["kind"] == "carry" and wp is not None:
                return self._act(0, 0.02, 0, 1 if r["vac"] > 0.5 else 0, dth)
            return self._act(0, 0.02, 0, 0, dth)
        dx = wp["x"] - r["x"]
        dy = wp["y"] - r["y"]
        mx = max(abs(dx), abs(dy))
        sc = min(1.0, SPEED / mx) if mx > 0 else 1.0
        vac = wp["vac"]
        if wp.get("release_last") and sc >= 1.0:
            vac = 0
        return self._act(dx * sc, dy * sc, darm, vac, dth)

    def _act(self, dx, dy, darm, vac, dth=0.0):
        a = np.array([dx, dy, dth, darm, float(vac)], dtype=np.float32)
        return np.clip(a, self.low, self.high).astype(np.float32)
