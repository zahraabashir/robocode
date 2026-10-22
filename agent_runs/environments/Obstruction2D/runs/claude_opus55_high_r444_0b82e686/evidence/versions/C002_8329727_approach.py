import numpy as np

W, H = 1.618, 1.0
FLOOR = 0.1
DOWN = -np.pi / 2


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=np.float64)
        self.high = np.asarray(action_space.high, dtype=np.float64)
        self.reset(None, None)

    def reset(self, state, info):
        self.phase = "lift"
        self.obj_name = None
        self.drop_x = None
        self.last_robot = None
        self.stuck = 0

    # ---------------- helpers ----------------
    def _rect(self, s, o):
        g = lambda f: float(s.get(o, f))
        return dict(name=o.name, x=g("x"), y=g("y"), w=g("width"), h=g("height"))

    def _parse(self, s):
        r = s.get_objects(self._rtype(s))[0]
        g = lambda f: float(s.get(r, f))
        robot = dict(x=g("x"), y=g("y"), th=g("theta"), arm=g("arm_joint"),
                     vac=g("vacuum"), gw=g("gripper_width"), gh=g("gripper_height"),
                     rad=g("base_radius"), maxarm=g("arm_length"))
        objs = {}
        surf = block = None
        for n in s.get_object_names():
            o = n if not isinstance(n, str) else s.get_object_from_name(n)
            tn = o.type.name if hasattr(o.type, "name") else str(o.type)
            if tn == "crv_robot":
                continue
            rr = self._rect(s, o)
            rr["type"] = tn
            if tn == "target_surface":
                surf = rr
            else:
                objs[rr["name"]] = rr
                if tn == "target_block":
                    block = rr
        return robot, objs, surf, block

    def _rtype(self, s):
        for n in s.get_object_names():
            o = n if not isinstance(n, str) else s.get_object_from_name(n)
            tn = o.type.name if hasattr(o.type, "name") else str(o.type)
            if tn == "crv_robot":
                return o.type
        raise RuntimeError

    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0, vac=0.0):
        a = np.array([dx, dy, dth, darm, vac], dtype=np.float64)
        a = np.clip(a, self.low, self.high)
        return a.astype(np.float32)

    def _choose_next(self, objs, surf, robot):
        # obstructions that conflict with placing the block on the surface
        sx0, sx1 = surf["x"], surf["x"] + surf["w"]
        cands = []
        for o in objs.values():
            if o["type"] == "target_block":
                continue
            if o["x"] < sx1 + 0.005 and o["x"] + o["w"] > sx0 - 0.005 and o["y"] < FLOOR + 0.3:
                cands.append(o)
        if cands:
            cands.sort(key=lambda o: -(o["y"] + o["h"]))
            return cands[0]["name"]
        return "target_block"

    def _drop_x(self, objs, surf, held, block):
        w = held["w"]
        occ = [(surf["x"] - 0.02, surf["x"] + surf["w"] + 0.02)]
        for o in objs.values():
            if o["name"] == held["name"]:
                continue
            occ.append((o["x"], o["x"] + o["w"]))
        margin = 0.03
        best, bestc = None, 1e9
        cur = held["x"] + w / 2
        for c in np.arange(0.1 + 1e-3, W - 0.1, 0.005):
            l, r = c - w / 2 - margin, c + w / 2 + margin
            if l < 0 or r > W:
                continue
            if any(l < b and r > a for a, b in occ):
                continue
            cost = abs(c - cur)
            if cost < bestc:
                best, bestc = c, cost
        if best is None:
            best = 0.1 + 1e-3 if surf["x"] > W / 2 else W - 0.1 - 1e-3
        return best

    # ---------------- main ----------------
    def get_action(self, state):
        robot, objs, surf, block = self._parse(state)
        arm_t = robot["maxarm"]
        max_top = max([o["y"] + o["h"] for o in objs.values()] + [FLOOR])
        held = objs.get(self.obj_name) if self.obj_name else None

        # posture correction first
        dth = np.clip(DOWN - robot["th"], -0.19, 0.19)
        darm = np.clip(arm_t - robot["arm"], -0.1, 0.1)

        def goto(tx, ty, vac):
            return self._act(tx - robot["x"], ty - robot["y"], dth, darm, vac)

        def near(a, b, tol=1e-4):
            return abs(a - b) < tol

        grip_off = arm_t + robot["gw"]  # robot_y - gripper bottom
        hh = held["h"] if (held and robot["vac"] > 0.5) else 0.0
        travel_y = min(H - robot["rad"] - 1e-3,
                       max(max_top + robot["rad"] + 0.03, max_top + 0.03 + grip_off + hh))

        for _ in range(10):
            ph = self.phase
            if ph == "lift":
                if self.obj_name is None:
                    self.obj_name = self._choose_next(objs, surf, robot)
                    held = objs[self.obj_name]
                if robot["y"] < travel_y - 1e-4 or not near(robot["arm"], arm_t) or not near(robot["th"], DOWN):
                    return goto(robot["x"], max(travel_y, robot["y"]), 0.0)
                self.phase = "goto"
                continue
            if ph == "goto":
                tgt = objs[self.obj_name]
                cx = tgt["x"] + tgt["w"] / 2
                if not near(robot["x"], cx):
                    return goto(cx, robot["y"], 0.0)
                self.phase = "descend"
                continue
            if ph == "descend":
                tgt = objs[self.obj_name]
                ty = tgt["y"] + tgt["h"] + grip_off + 2e-4
                if not near(robot["y"], ty, 5e-5):
                    return goto(robot["x"], ty, 0.0)
                self.phase = "grasp"
                return goto(robot["x"], robot["y"], 1.0)
            if ph == "grasp":
                self.phase = "lift_held"
                self.grasp_y = objs[self.obj_name]["y"]
                continue
            if ph == "lift_held":
                if robot["y"] < travel_y - 1e-4:
                    return goto(robot["x"], travel_y, 1.0)
                tgt = objs[self.obj_name]
                if tgt["y"] < self.grasp_y + 1e-3:
                    # grasp failed; retry
                    self.phase = "lift"
                    self.obj_name = None
                    return goto(robot["x"], robot["y"], 0.0)
                if self.obj_name == "target_block":
                    self.drop_x = surf["x"] + surf["w"] / 2
                else:
                    self.drop_x = self._drop_x(objs, surf, tgt, block)
                self.phase = "carry"
                continue
            if ph == "carry":
                tgt = objs[self.obj_name]
                cx = tgt["x"] + tgt["w"] / 2
                tx = robot["x"] + (self.drop_x - cx)
                if not near(cx, self.drop_x):
                    return goto(tx, robot["y"], 1.0)
                self.phase = "lower"
                continue
            if ph == "lower":
                tgt = objs[self.obj_name]
                ty = robot["y"] - (tgt["y"] - (FLOOR + 2e-3))
                if not near(tgt["y"], FLOOR + 2e-3, 5e-4):
                    return goto(robot["x"], ty, 1.0)
                self.phase = "release"
                continue
            if ph == "release":
                self.phase = "lift"
                self.obj_name = None
                return goto(robot["x"], robot["y"], 0.0)
        return goto(robot["x"], robot["y"], robot["vac"])
