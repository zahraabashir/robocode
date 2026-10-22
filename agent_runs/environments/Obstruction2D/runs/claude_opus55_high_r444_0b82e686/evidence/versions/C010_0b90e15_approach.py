import numpy as np

W, H = 1.618, 1.0
FLOOR = 0.1
DOWN = -np.pi / 2
MARGIN = 0.012      # vertical clearance margin to obstacles
XMARGIN = 0.006     # horizontal clearance margin to obstacles
GRASP_GAP = 2e-4    # gap between gripper and object top when grasping
PLACE_GAP = 2e-3    # gap between object bottom and floor when placing
MAXD = 0.05


def _tname(o):
    t = o.type
    return t.name if hasattr(t, "name") else str(t)


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=np.float64)
        self.high = np.asarray(action_space.high, dtype=np.float64)
        self.reset(None, None)

    def reset(self, state, info):
        self.mode = "pick"
        self.cur = None           # name of object currently being handled
        self.grasp_off = 0.0      # robot_x - object center x (planned / actual)
        self.drop = None          # (object center x) target for placement/drop
        self.place_c = None       # planned block center on surface
        self.block_g = 0.0
        self.blockers = None
        self.last_pose = None
        self.stuck = 0
        self.escape = 0
        self.done = set()
        self.released = None

    # ------------------------------------------------------------------
    def _parse(self, s):
        robot = None
        objs = {}
        surf = None
        for n in s.get_object_names():
            o = s.get_object_from_name(n) if isinstance(n, str) else n
            tn = _tname(o)
            g = lambda f: float(s.get(o, f))
            if tn == "crv_robot":
                robot = dict(x=g("x"), y=g("y"), th=g("theta"), arm=g("arm_joint"),
                             vac=g("vacuum"), gw=g("gripper_width"), gh=g("gripper_height"),
                             r=g("base_radius"), maxarm=g("arm_length"))
                continue
            rr = dict(name=o.name, type=tn, x=g("x"), y=g("y"), w=g("width"), h=g("height"))
            rr["cx"] = rr["x"] + rr["w"] / 2
            rr["top"] = rr["y"] + rr["h"]
            if tn == "target_surface":
                surf = rr
            else:
                objs[rr["name"]] = rr
        return robot, objs, surf

    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
        a = np.array([dx, dy, dth, darm, vac], dtype=np.float64)
        a = np.clip(a, self.low, self.high)
        return a.astype(np.float32)

    # ---------------- geometry ----------------
    def _parts(self, robot, held=None, held_off=None, held_depth=None):
        """Footprint parts relative to robot x: (lo, hi, depth below robot y)."""
        arm = robot["maxarm"]
        parts = [(-robot["r"], robot["r"], robot["r"]),
                 (-robot["gh"] / 2, robot["gh"] / 2, arm + robot["gw"])]
        if held is not None:
            # held_off: object left edge relative to robot x; held_depth: robot y - object bottom
            parts.append((held_off, held_off + held["w"], held_depth))
        return parts

    def _req(self, x, parts, obst):
        """Min robot y at horizontal position x so no part collides."""
        req = 0.0
        for lo, hi, d in parts:
            a, b = x + lo, x + hi
            req = max(req, FLOOR + d)  # floor
            for (o0, o1, top) in obst:
                if a < o1 + XMARGIN and b > o0 - XMARGIN:
                    req = max(req, top + d + MARGIN)
        return req

    def _req_range(self, x0, x1, parts, obst):
        lo, hi = min(x0, x1), max(x0, x1)
        req = 0.0
        for plo, phi, d in parts:
            a, b = lo + plo, hi + phi
            req = max(req, FLOOR + d)
            for (o0, o1, top) in obst:
                if a < o1 + XMARGIN and b > o0 - XMARGIN:
                    req = max(req, top + d + MARGIN)
        return req

    def _obst(self, objs, exclude=()):
        return [(o["x"], o["x"] + o["w"], o["top"]) for n, o in objs.items() if n not in exclude]

    def _xlim(self, robot):
        return robot["r"] + 1e-3, W - robot["r"] - 1e-3

    # ---------------- motion ----------------
    def _move(self, robot, tx, ty, parts, obst, vac):
        """One step toward (tx, ty) staying above clearance profile. Returns (action, arrived)."""
        x, y = robot["x"], robot["y"]
        ymax = H - robot["r"] - 1e-3
        dth = float(np.clip(DOWN - robot["th"], -0.19, 0.19))
        darm = float(np.clip(robot["maxarm"] - robot["arm"], -0.1, 0.1))
        posture_ok = abs(dth) < 1e-4 and abs(darm) < 1e-4
        if abs(tx - x) < 1e-5 and abs(ty - y) < 3e-5 and posture_ok:
            return None, True
        dx = float(np.clip(tx - x, -MAXD, MAXD))
        x1 = x + dx
        # lookahead requirement from x1 toward tx (slope-1 relaxation)
        R = self._req_range(x, x1, parts, obst)
        if abs(tx - x1) > 1e-6:
            n = int(abs(tx - x1) / 0.01) + 1
            for i in range(1, n + 1):
                xs = x1 + (tx - x1) * i / n
                r_here = self._req(xs, parts, obst)
                if i == n:
                    r_here = min(r_here, ty)
                R = max(R, r_here - abs(xs - x1))
        else:
            R = min(R, ty)
        R = min(R, ymax)
        y_des = y + float(np.clip(ty - y, -MAXD, MAXD))
        y1 = max(y_des, R)
        if y1 - y > MAXD + 1e-9:
            # cannot rise enough while moving horizontally: rise first
            dx = 0.0
            y1 = y + MAXD
        dy = y1 - y
        return self._act(dx, dy, dth, darm, vac), False

    # ---------------- planning ----------------
    def _plan_block(self, robot, objs, surf):
        blk = objs["target_block"]
        bw = blk["w"]
        lo, hi = self._xlim(robot)
        s0, s1 = surf["x"], surf["x"] + surf["w"]
        cmin, cmax = s0 + bw / 2 + 0.002, s1 - bw / 2 - 0.002
        if cmax < cmin:
            cmin = cmax = (s0 + s1) / 2
        obstructions = [o for n, o in objs.items() if n != "target_block"]
        center = (s0 + s1) / 2
        best = None
        cands = list(np.linspace(cmin, cmax, max(2, int((cmax - cmin) / 0.002) + 1)))
        cands.append(center)
        gmax = max(0.0, bw / 2 - 0.004)
        place_depth = None
        for c in cands:
            c = float(np.clip(c, cmin, cmax))
            # grasp offset g so that robot x at placement and at grasp is reachable
            glo = max(-gmax, lo - c, lo - blk["cx"])
            ghi = min(gmax, hi - c, hi - blk["cx"])
            if glo > ghi:
                continue
            g = float(np.clip(0.0, glo, ghi))
            blockers = set()
            for o in obstructions:
                if o["x"] < c + bw / 2 + 0.003 and o["x"] + o["w"] > c - bw / 2 - 0.003:
                    blockers.add(o["name"])
            # also obstacles that would hit the robot when placing
            depth = robot["maxarm"] + robot["gw"] + blk["h"]
            parts = self._parts(robot, blk, -g - bw / 2, depth)
            ty = FLOOR + PLACE_GAP + depth
            for o in obstructions:
                if o["name"] in blockers:
                    continue
                if self._req(c + g, parts, [(o["x"], o["x"] + o["w"], o["top"])]) > ty + 1e-6:
                    blockers.add(o["name"])
            cost = (len(blockers), abs(g) > 1e-6, abs(g), abs(c - center))
            if best is None or cost < best[0]:
                best = (cost, c, g, blockers)
        if best is None:
            c = float(np.clip(center, lo, hi))
            return c, 0.0, set(o["name"] for o in obstructions)
        return best[1], best[2], best[3]

    def _grasp_x(self, robot, obj, objs, prefer_g=0.0):
        """Choose robot x to grasp obj (reachable, collision free)."""
        lo, hi = self._xlim(robot)
        parts = self._parts(robot)
        obst = self._obst(objs, exclude=(obj["name"],))
        ty = obj["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
        gmax = max(0.0, obj["w"] / 2 - 0.004)
        best = None
        for g in np.linspace(-gmax, gmax, 41).tolist() + [prefer_g, 0.0]:
            if abs(g) > gmax + 1e-9:
                continue
            x = obj["cx"] + g
            if x < lo or x > hi:
                continue
            ok = self._req(x, parts, obst) <= ty + 1e-9
            cost = (not ok, abs(g - prefer_g))
            if best is None or cost < best[0]:
                best = (cost, x)
        if best is None:
            return float(np.clip(obj["cx"], lo, hi)), ty
        self._last_grasp_ok = not best[0][0]
        return best[1], ty

    def _grasp_ok(self, robot, obj, objs, prefer_g=0.0):
        self._last_grasp_ok = False
        gx, ty = self._grasp_x(robot, obj, objs, prefer_g)
        return self._last_grasp_ok, gx, ty

    def _violators(self, robot, obj, objs, gx, ty):
        parts = self._parts(robot)
        res = []
        for n, o in objs.items():
            if n == obj["name"]:
                continue
            if self._req(gx, parts, [(o["x"], o["x"] + o["w"], o["top"])]) > ty + 1e-9:
                res.append(n)
        return res

    def _steps(self, x0, y0, x1, y1, parts, obst):
        peak = max(y0, y1, self._req_range(x0, x1, parts, obst))
        peak = min(peak, H - 0.1)
        return max(abs(x1 - x0), (peak - y0) + (peak - y1)) / MAXD

    def _drop_spot(self, robot, objs, held, g, next_name, strict=True):
        """Choose (object center x, object bottom y) drop pose for held obstruction."""
        lo, hi = self._xlim(robot)
        w = held["w"]
        others = {n: o for n, o in objs.items() if n != held["name"]}
        obst = self._obst(others)
        depth = robot["y"] - held["y"]
        parts = self._parts(robot, held, -g - w / 2, depth)
        blk = objs.get("target_block")
        reserved = []
        if self.place_c is not None and blk is not None:
            bw = blk["w"]
            reserved.append((self.place_c - bw / 2 - 0.01, self.place_c + bw / 2 + 0.01))
        future = []
        for n in self.blockers:
            if n in others and n not in self.done:
                gx, gty = self._grasp_x(robot, others[n], others)
                future.append((gx, gty))
        # next pick pose
        nxt = others.get(next_name)
        if nxt is not None:
            pref = self.block_g if next_name == "target_block" else 0.0
            ngx, ngty = self._grasp_x(robot, nxt, others, pref)
        bparts0 = self._parts(robot)
        if blk is not None:
            bgx = blk["cx"] + self.block_g
            bgty = blk["top"] + robot["maxarm"] + robot["gw"] + GRASP_GAP
            bdepth = robot["maxarm"] + robot["gw"] + blk["h"]
            pparts = self._parts(robot, blk, -self.block_g - blk["w"] / 2, bdepth)
            px = self.place_c + self.block_g
            pty = FLOOR + PLACE_GAP + bdepth
        levels = [FLOOR + PLACE_GAP + 0.04 * k for k in range(0, 9)]
        sep = 0.01 if strict else 0.002
        best = None
        for c in np.arange(w / 2 + 0.002, W - w / 2 - 0.002, 0.005):
            c = float(c)
            rx = c + g
            if rx < lo or rx > hi:
                continue
            a, b = c - w / 2, c + w / 2
            if any(a < o1 + sep and b > o0 - sep for (o0, o1, _) in obst):
                continue
            if any(a < r1 and b > r0 for (r0, r1) in reserved):
                continue
            req = self._req(rx, parts, obst)
            for bot in levels:
                ty = bot + depth
                if ty > H - robot["r"] - 1e-3:
                    break
                if req > ty + 1e-9:
                    continue
                newob = [(a, b, bot + held["h"])]
                if any(self._req(gx, bparts0, newob) > gty + 1e-9 for gx, gty in future):
                    continue
                if blk is not None and self.place_c is not None:
                    if self._req(bgx, bparts0, newob) > bgty + 1e-9:
                        continue
                    if self._req(px, pparts, newob) > pty + 1e-9:
                        continue
                cost = self._steps(robot["x"], robot["y"], rx, ty, parts, obst)
                obst2 = obst + newob
                if nxt is not None:
                    obst_n = [o for o in obst2 if not (o[0] == nxt["x"] and o[2] == nxt["top"])]
                    cost += self._steps(rx, ty, ngx, ngty, bparts0, obst_n)
                if blk is not None and self.place_c is not None:
                    obst_b = [o for o in obst2 if not (o[0] == blk["x"] and o[2] == blk["top"])]
                    cost += self._steps(bgx, bgty, px, pty, pparts, obst_b)
                cost += 1e-3 * abs(c - held["cx"])
                if best is None or cost < best[0]:
                    best = (cost, c, bot)
        if best is None:
            return None
        return best[1], best[2]

    def _air_spot(self, robot, objs, held, g):
        lo, hi = self._xlim(robot)
        blk = objs.get("target_block")
        best = None
        for rx in np.linspace(lo, hi, 200):
            c = float(rx) - g
            a, b = c - held["w"] / 2, c + held["w"] / 2
            d = 0.0
            for zc in [self.place_c + self.block_g, (blk["cx"] + self.block_g) if blk else None]:
                if zc is not None:
                    d = min(d, abs(rx - zc) - 0.35) if d < 0 else min(abs(rx - zc) - 0.35, 1e9)
            score = min(abs(float(rx) - (self.place_c + self.block_g)),
                        abs(float(rx) - (blk["cx"] + self.block_g)) if blk else 1e9)
            if best is None or score > best[0]:
                best = (score, c)
        return best[1]

    # ---------------- main ----------------
    def get_action(self, state):
        robot, objs, surf = self._parse(state)
        if self.place_c is None:
            self.place_c, self.block_g, self.blockers = self._plan_block(robot, objs, surf)

        # stuck detection / escape
        pose = (round(robot["x"], 6), round(robot["y"], 6))
        if self.escape > 0:
            self.escape -= 1
            self.last_pose = pose
            return self._act(0.0, MAXD, 0.0, 0.0, robot["vac"])
        if self.last_pose == pose and self.mode in ("pick", "carry"):
            self.stuck += 1
            if self.stuck >= 3:
                self.stuck = 0
                self.escape = 2
        else:
            self.stuck = 0
        self.last_pose = pose

        for _ in range(6):
            if self.mode == "pick":
                if self.cur is None:
                    self.cur = self._next_target(robot, objs)
                obj = objs[self.cur]
                prefer = self.block_g if self.cur == "target_block" else 0.0
                gx, gty = self._grasp_x(robot, obj, objs, prefer)
                parts = self._parts(robot)
                obst = self._obst(objs, exclude=(obj["name"],))
                act, arrived = self._move(robot, gx, gty, parts, obst, 0.0)
                self.released = None
                if not arrived:
                    lands = (abs(robot["x"] + float(act[0]) - gx) < 1e-5
                             and abs(robot["y"] + float(act[1]) - gty) < 3e-5
                             and abs(float(act[2])) < 1e-4 and abs(float(act[3])) < 1e-4)
                    if lands:
                        act[4] = 1.0
                        self.mode = "grasp"
                    return act
                if robot["vac"] < 0.5:
                    self.mode = "grasp"
                    return self._act(0, 0, 0, 0, 1.0)
                self.mode = "grasp"
                continue
            if self.mode == "grasp":
                obj = objs[self.cur]
                if robot["vac"] < 0.5:
                    self.mode = "pick"
                    continue
                self.g_actual = robot["x"] - obj["cx"]
                self.depth = robot["y"] - obj["y"]
                if self.cur == "target_block":
                    self.drop = self.place_c
                else:
                    nxt = self._peek_next(robot, objs, exclude=self.cur)
                    d = self._drop_spot(robot, objs, obj, self.g_actual, nxt)
                    if d is None:
                        d = self._drop_spot(robot, objs, obj, self.g_actual, nxt, strict=False)
                    if d is None:
                        d = (self._air_spot(robot, objs, obj, self.g_actual),
                             H - robot["r"] - 1e-3 - self.depth)
                    self.drop, self.drop_bot = d
                self.mode = "carry"
                continue
            if self.mode == "carry":
                obj = objs[self.cur]
                if robot["vac"] < 0.5:
                    self.mode = "pick"
                    continue
                parts = self._parts(robot, obj, obj["x"] - robot["x"], robot["y"] - obj["y"])
                obst = self._obst(objs, exclude=(obj["name"],))
                tx = self.drop + (robot["x"] - obj["cx"])
                ty = robot["y"] - obj["y"] + FLOOR + PLACE_GAP
                if self.cur != "target_block":
                    ty = robot["y"] - obj["y"] + self.drop_bot
                act, arrived = self._move(robot, tx, ty, parts, obst, 1.0)
                # detect failed grasp: object not following
                if abs(robot["y"] - obj["y"] - self.depth) > 5e-3:
                    self.mode = "pick"
                    return self._act(0, 0, 0, 0, 0.0)
                if not arrived:
                    lands = (abs(robot["x"] + float(act[0]) - tx) < 1e-5
                             and abs(robot["y"] + float(act[1]) - ty) < 3e-5
                             and abs(float(act[2])) < 1e-4 and abs(float(act[3])) < 1e-4)
                    if lands and self.cur != "target_block":
                        act[4] = 0.0
                        self.mode = "pick"
                        self.cur = None
                        self.last_pose = None
                    return act
                self.mode = "pick"
                self.cur = None
                self.last_pose = None
                return self._act(0, 0, 0, 0, 0.0)
        return self._act(0, 0, 0, 0, robot["vac"])

    def _remaining_blockers(self, objs):
        return [n for n in self.blockers if n in objs and self._still_blocks(objs[n], objs)]

    def _still_blocks(self, o, objs):
        blk = objs["target_block"]
        bw = blk["w"]
        c = self.place_c
        if o["x"] < c + bw / 2 + 0.003 and o["x"] + o["w"] > c - bw / 2 - 0.003:
            return True
        return False if o.get("_moved") else True

    def _next_target(self, robot, objs):
        rem = [n for n in self.blockers if n in objs and n not in self.done]
        goals = rem if rem else ["target_block"]
        goals = sorted(goals, key=lambda n: abs(objs[n]["cx"] - robot["x"]))
        infeasible = []
        for n in goals:
            pref = self.block_g if n == "target_block" else 0.0
            ok, gx, ty = self._grasp_ok(robot, objs[n], objs, pref)
            if ok:
                if n != "target_block":
                    self.done.add(n)
                return n
            infeasible.append((n, gx, ty))
        # nothing directly graspable: move an obstacle that blocks a goal's grasp
        for n, gx, ty in infeasible:
            for v in self._violators(robot, objs[n], objs, gx, ty):
                if v == "target_block":
                    continue
                ok, _, _ = self._grasp_ok(robot, objs[v], objs)
                if ok:
                    self.done.add(v)
                    return v
        n = goals[0]
        if n != "target_block":
            self.done.add(n)
        return n

    def _peek_next(self, robot, objs, exclude):
        rem = [n for n in self.blockers if n in objs and n not in self.done and n != exclude]
        if rem:
            rem.sort(key=lambda n: abs(objs[n]["cx"] - robot["x"]))
            return rem[0]
        return "target_block"
