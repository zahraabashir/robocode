"""Approach for Obstruction2DEnv: clear obstructions off the target surface,
then pick the target block and place it on the surface."""
import math
import numpy as np

FLOOR = 0.1
X_MIN, X_MAX = 0.1005, 1.5175   # robot base x limits
Y_MAX = 0.895                   # robot base y limit
WORLD_X = 1.618
BASE_R = 0.1
GRIP_OFF = 0.205                # base center to gripper tip (arm 0.2 + half gripper width)
GAP = 0.0015


def _objs(state, tname):
    out = []
    for o in state.get_object_names() if False else []:
        pass
    return out


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.low = np.asarray(action_space.low, dtype=np.float32)
        self.high = np.asarray(action_space.high, dtype=np.float32)

    # ------------------------------------------------------------------ utils
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
            elif tn == "rectangle":
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

    # --------------------------------------------------------------- planning
    def reset(self, state, info):
        self.plan = []
        self.cur = None
        self.stall = 0
        self.last_pos = None
        self.held = None
        self.grasp_offset = None
        self.fail_count = {}
        self.moved_away = set()

    def _grip_off(self):
        return self.robot["arm_max"] + self.robot["gw"] / 2.0

    def _max_top(self, exclude=()):
        t = FLOOR
        for n, b in self._all_movable().items():
            if n in exclude:
                continue
            t = max(t, b["y"] + b["h"])
        return t

    def _travel_y(self, carried_h, exclude=()):
        need = self._max_top(exclude) + 0.03 + self._grip_off() + carried_h
        return min(Y_MAX, max(need, 0.0))

    def _grasp_x(self, b, others):
        """Choose base x above object b such that base doesn't hit taller neighbors."""
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
                    break
            if ok:
                return x
        return None

    def _free_spot(self, b, others, forbid):
        """Find x (left edge) on the floor for box b avoiding others and forbid intervals."""
        w = b["w"]
        m = 0.03
        ivs = [(o["x"] - m, o["x"] + o["w"] + m) for o in others] + forbid
        cur_c = b["x"] + w / 2
        best = None
        for c in np.arange(X_MIN, X_MAX, 0.005):
            x0 = c - w / 2
            if x0 < 0.0 or x0 + w > WORLD_X:
                continue
            if any(x0 < i1 and x0 + w > i0 for i0, i1 in ivs):
                continue
            # base clearance check wrt taller neighbours when descending
            cost = abs(c - cur_c)
            if best is None or cost < best[0]:
                best = (cost, x0)
        if best is not None:
            return best[1], FLOOR
        # fallback: stack on top of some other object far from surface
        best = None
        for o in others:
            c = o["x"] + o["w"] / 2
            if any(o["x"] < i1 and o["x"] + o["w"] > i0 for i0, i1 in forbid):
                continue
            top = o["y"] + o["h"]
            cost = top
            if best is None or cost < best[0]:
                best = (cost, c - w / 2, top)
        if best is not None:
            return best[1], best[2]
        return None

    def _make_plan(self):
        """Create a list of waypoints: dict(x, y, vac, kind)."""
        s = self.surface
        s0, s1 = s["x"], s["x"] + s["w"]
        blockers = [b for n, b in self.obst.items()
                    if b["x"] < s1 + 0.005 and b["x"] + b["w"] > s0 - 0.005]
        if blockers:
            # nearest blocker to robot
            rx = self.robot["x"]
            tgt = min(blockers, key=lambda b: abs(b["x"] + b["w"] / 2 - rx))
            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
            forbid = [(s0 - 0.03, s1 + 0.03)]
            spot = self._free_spot(tgt, others, forbid)
            if spot is None:
                spot = (0.0, FLOOR)
            dest_x, dest_y = spot
        else:
            tgt = self.block
            others = [b for n, b in self.obst.items()]
            dest_x = s0 + (s["w"] - tgt["w"]) / 2
            dest_y = FLOOR
        for _ in range(10):
            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
            gx = self._grasp_x(tgt, others)
            if gx is not None or self.grasp_conflict is None:
                break
            tgt = self.grasp_conflict
            others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
            forbid = [(s0 - 0.03, s1 + 0.03)]
            spot = self._free_spot(tgt, others, forbid)
            if spot is None:
                spot = (0.0, FLOOR)
            dest_x, dest_y = spot
        if gx is None:
            gx = min(max(tgt["x"] + tgt["w"] / 2, X_MIN), X_MAX)
        self.target_name = tgt["name"]
        others = [b for n, b in self._all_movable().items() if n != tgt["name"]]
        gy = tgt["y"] + tgt["h"] + self._grip_off() + GAP
        ty_empty = max(self._travel_y(0.0), self.robot["y"] if False else 0)
        ty_empty = max(ty_empty, gy)
        plan = []
        plan.append(dict(x=self.robot["x"], y=max(self.robot["y"], ty_empty), vac=0, kind="move"))
        plan.append(dict(x=gx, y=max(self.robot["y"], ty_empty), vac=0, kind="move"))
        plan.append(dict(x=gx, y=gy, vac=0, kind="descend"))
        plan.append(dict(x=gx, y=gy, vac=1, kind="grasp"))
        off = gy - tgt["y"]  # base y minus object bottom
        ty_c = max(self._travel_y(tgt["h"] + 0.005, exclude=(tgt["name"],)), gy)
        # carried object must clear things; object bottom = base_y - off
        ty_c = min(Y_MAX, max(ty_c, self._max_top((tgt["name"],)) + 0.03 + off))
        dx = dest_x + (gx - tgt["x"])
        dx = min(max(dx, X_MIN), X_MAX)
        py = dest_y + off + 0.004
        plan.append(dict(x=gx, y=ty_c, vac=1, kind="lift"))
        plan.append(dict(x=dx, y=ty_c, vac=1, kind="carry"))
        plan.append(dict(x=dx, y=py, vac=1, kind="lower"))
        plan.append(dict(x=dx, y=py, vac=0, kind="release"))
        plan.append(dict(x=dx, y=ty_c, vac=0, kind="retreat"))
        return plan

    # ---------------------------------------------------------------- control
    def get_action(self, state):
        self._parse(state)
        r = self.robot
        if not self.plan:
            self.plan = self._make_plan()
            self.stall = 0
        wp = self.plan[0]
        # check waypoint reached
        for _ in range(12):
            wp = self.plan[0]
            reached = abs(r["x"] - wp["x"]) < 1e-4 and abs(r["y"] - wp["y"]) < 1e-4 \
                and abs(r["arm"] - r["arm_max"]) < 1e-4
            if wp["kind"] in ("grasp", "release"):
                reached = (r["vac"] > 0.5) == (wp["vac"] > 0.5)
            if wp["kind"] == "lift" and reached:
                # verify grasp
                t = self._all_movable()[self.target_name]
                if abs((r["y"] - t["y"]) - (self.plan[0]["y"] - t["y"])) > 1e-3 or \
                        t["y"] < FLOOR + 0.01 and r["y"] > t["y"] + t["h"] + 0.3:
                    pass
            if reached:
                self.plan.pop(0)
                self.stall = 0
                if not self.plan:
                    self.plan = self._make_plan()
                continue
            break
        wp = self.plan[0]
        # stall detection
        pos = (round(r["x"], 5), round(r["y"], 5), round(r["arm"], 5))
        if self.last_pos == pos and wp["kind"] not in ("grasp", "release"):
            self.stall += 1
        else:
            self.stall = 0
        self.last_pos = pos
        if self.stall >= 2:
            if wp["kind"] in ("descend", "lower"):
                # can't go lower: accept current height
                self.plan.pop(0)
                self.stall = 0
                if wp["kind"] == "lower":
                    pass
                return self.get_action(state) if self.plan else self._act(0, 0, 0, wp["vac"])
            else:
                # try going up a bit, then replan
                self.plan = []
                self.stall = 0
                return self._act(0, 0.05, 0, wp["vac"])
        dx = wp["x"] - r["x"]
        dy = wp["y"] - r["y"]
        if wp["kind"] in ("grasp", "release"):
            dx = dy = 0.0
        dth = -math.pi / 2 - r["theta"]
        darm = r["arm_max"] - r["arm"]
        return self._act(dx, dy, darm, wp["vac"], dth)

    def _act(self, dx, dy, darm, vac, dth=0.0):
        a = np.array([dx, dy, dth, darm, float(vac)], dtype=np.float32)
        return np.clip(a, self.low, self.high).astype(np.float32)
