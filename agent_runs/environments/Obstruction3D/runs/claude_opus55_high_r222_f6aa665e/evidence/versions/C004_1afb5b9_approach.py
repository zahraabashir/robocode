"""Obstruction3D approach: clear obstructions off the target region, then place the
target block on it.  Uses an internal FK/IK model of the Kinova Gen3 (arm base at the
world origin, verified empirically) and Cartesian straight-line motions."""
import numpy as np

PI = np.pi

# ----------------------------------------------------------------------------- kinematics
def _rpy(r, p, y):
    cr, sr, cp, sp, cy, sy = np.cos(r), np.sin(r), np.cos(p), np.sin(p), np.cos(y), np.sin(y)
    return np.array([[cy * cp, cy * sp * sr - sy * cr, cy * sp * cr + sy * sr],
                     [sy * cp, sy * sp * sr + cy * cr, sy * sp * cr - cy * sr],
                     [-sp, cp * sr, cp * cr]])


def _tf(xyz, rpy):
    T = np.eye(4)
    T[:3, :3] = _rpy(*rpy)
    T[:3, 3] = xyz
    return T


_JOINTS = [
    _tf([0, 0, 0.15643], [PI, 0, 0]),
    _tf([0, 0.005375, -0.12838], [PI / 2, 0, 0]),
    _tf([0, -0.21038, -0.006375], [-PI / 2, 0, 0]),
    _tf([0, 0.006375, -0.21038], [PI / 2, 0, 0]),
    _tf([0, -0.20843, -0.006375], [-PI / 2, 0, 0]),
    _tf([0, 0.00017505, -0.10593], [PI / 2, 0, 0]),
    _tf([0, -0.10593, -0.00017505], [-PI / 2, 0, 0]),
]
_EE = _tf([0, 0, -0.061525], [PI, 0, 0])
FINGER = 0.155          # EE frame -> fingertip distance (along tool z)
FINGER_OFF = 0.05       # finger centre offset from tool axis along closing direction

# joint limits (Kinova Gen3); None = continuous
_LIM = [None, (-2.38, 2.38), None, (-2.63, 2.63), None, (-2.2, 2.2), None]


def fk(q):
    T = np.eye(4)
    zs, ps = [], []
    for i in range(7):
        T = T @ _JOINTS[i]
        zs.append(T[:3, 2].copy())
        ps.append(T[:3, 3].copy())
        c, s = np.cos(q[i]), np.sin(q[i])
        Rz = np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1.0]])
        T = T @ Rz
    T = T @ _EE
    return T, zs, ps


def down_R(yaw):
    c, s = np.cos(yaw), np.sin(yaw)
    x = np.array([c, s, 0.0])
    z = np.array([0, 0, -1.0])
    y = np.cross(z, x)
    return np.stack([x, y, z], axis=1)


def _rotvec(Rm):
    cos = (np.trace(Rm) - 1) / 2
    cos = min(1.0, max(-1.0, cos))
    ang = np.arccos(cos)
    v = np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]])
    if ang < 1e-6:
        return v * 0.5
    if ang > PI - 1e-4:
        # 180 deg: axis from diagonal
        M = (Rm + np.eye(3)) / 2
        k = np.argmax(np.diag(M))
        ax = M[:, k] / np.sqrt(max(M[k, k], 1e-12))
        return ax * ang
    return v * ang / (2 * np.sin(ang))


def ik(q0, pos, Rt, iters=100, tol=1e-5):
    q = np.array(q0, dtype=float)
    err = 1e9
    for _ in range(iters):
        T, zs, ps = fk(q)
        ep = pos - T[:3, 3]
        er = _rotvec(Rt @ T[:3, :3].T)
        e = np.concatenate([ep, 0.3 * er])
        err = np.linalg.norm(e)
        if err < tol:
            break
        J = np.zeros((6, 7))
        pe = T[:3, 3]
        for i in range(7):
            J[:3, i] = np.cross(zs[i], pe - ps[i])
            J[3:, i] = 0.3 * zs[i]
        lam = 1e-4
        dq = J.T @ np.linalg.solve(J @ J.T + lam * np.eye(6), e)
        n = np.max(np.abs(dq))
        if n > 0.4:
            dq *= 0.4 / n
        q += dq
        for i, lim in enumerate(_LIM):
            if lim is not None:
                q[i] = min(lim[1], max(lim[0], q[i]))
    return q, err


def wrap(a):
    return (a + PI) % (2 * PI) - PI


# ----------------------------------------------------------------------------- approach
class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space

    # ---------------------------------------------------------------- state helpers
    def _robot(self, state):
        for n in state.get_object_names():
            if n == "robot":
                return state.get_object_from_name(n)
        return None

    def _q(self, state):
        r = self._robot(state)
        return np.array([state.get(r, "joint_%d" % i) for i in range(1, 8)])

    def _boxes(self, state):
        out = {}
        for n in state.get_object_names():
            if n == "robot":
                continue
            o = state.get_object_from_name(n)
            try:
                out[n] = dict(
                    x=state.get(o, "pose_x"), y=state.get(o, "pose_y"), z=state.get(o, "pose_z"),
                    hx=state.get(o, "half_extent_x"), hy=state.get(o, "half_extent_y"),
                    hz=state.get(o, "half_extent_z"), g=state.get(o, "grasp_active"))
            except Exception:
                pass
        return out

    # ---------------------------------------------------------------- episode
    def reset(self, state, info):
        self.segs = []          # queue of segments
        self.cur = None
        self.last_q = None
        self.last_cmd = None
        self.stuck = 0
        self.held = None
        self.moved = set()
        self.fail = {}
        self.placed_spots = []
        self.yaw = 0.0
        self.done_flag = False

    # ---------------------------------------------------------------- geometry
    def _region(self, boxes):
        return boxes.get("target_region")

    def _blocking(self, boxes):
        reg = self._region(boxes)
        res = []
        for n, b in boxes.items():
            if n in ("target_region", "target_block"):
                continue
            if abs(b["x"] - reg["x"]) < b["hx"] + reg["hx"] + 0.003 and \
               abs(b["y"] - reg["y"]) < b["hy"] + reg["hy"] + 0.003 and \
               b["z"] - b["hz"] < reg["z"] + reg["hz"] + 0.08:
                res.append(n)
        return res

    def _grasp_clear(self, boxes, name, yaw):
        """clearance of finger boxes from other objects for a top-down grasp"""
        b = boxes[name]
        ax = np.array([np.cos(yaw), np.sin(yaw)])
        best = 1e9
        for sgn in (-1, 1):
            f = np.array([b["x"], b["y"]]) + sgn * FINGER_OFF * ax
            for n, o in boxes.items():
                if n == name or n == "target_region":
                    continue
                dx = abs(f[0] - o["x"]) - o["hx"]
                dy = abs(f[1] - o["y"]) - o["hy"]
                d = max(dx, dy)
                best = min(best, d)
        return best

    def _choose_yaw(self, boxes, name, q):
        b = boxes[name]
        cands = []
        for yaw in (0.0, PI / 2):
            width = 2 * (b["hx"] if yaw == 0.0 else b["hy"])
            if width > 0.082:
                continue
            clr = self._grasp_clear(boxes, name, yaw)
            cands.append((min(clr, 0.03) - 0.2 * width, yaw))
        if not cands:
            return None
        cands.sort(reverse=True)
        yaw = cands[0][1]
        k = self.fail.get(name, 0)
        if k % 2 == 1 and len(cands) > 1:
            yaw = cands[1][1]
        return self._best_equiv_yaw(yaw, q)

    def _best_equiv_yaw(self, yaw, q):
        # yaw and yaw+pi are equivalent grasps; pick the one nearer the current tool yaw
        T, _, _ = fk(q)
        cur = np.arctan2(T[1, 0], T[0, 0])
        opts = [yaw, wrap(yaw + PI)]
        return min(opts, key=lambda a: abs(wrap(a - cur)))

    def _safe_z(self, boxes, held_hz=0.0, held_off=0.0):
        top = 0.1
        for n, b in boxes.items():
            if b["g"] > 0.5:
                continue
            top = max(top, b["z"] + b["hz"])
        return max(0.34, top + 0.03 + held_hz + held_off + FINGER)

    def _drop_spot(self, boxes, name):
        reg = self._region(boxes)
        b = boxes[name]
        best, bs = None, -1e9
        for x in np.arange(0.15, 0.46, 0.025):
            for y in np.arange(-0.3, 0.31, 0.025):
                clr = 1e9
                for n, o in boxes.items():
                    if n == name:
                        continue
                    m = 0.05 if n != "target_region" else 0.03
                    dx = abs(x - o["x"]) - o["hx"] - b["hx"] - m
                    dy = abs(y - o["y"]) - o["hy"] - b["hy"] - m
                    clr = min(clr, max(dx, dy))
                for (px, py) in self.placed_spots:
                    clr = min(clr, max(abs(x - px), abs(y - py)) - 0.08)
                dist = np.hypot(x - b["x"], y - b["y"])
                score = min(clr, 0.04) * 10 - dist
                if score > bs:
                    bs, best = score, (x, y)
        return best

    # ---------------------------------------------------------------- planning
    def _plan_pick_place(self, state, name, place_xy, place_bottom, final_yaw=None):
        boxes = self._boxes(state)
        q = self._q(state)
        b = boxes[name]
        yaw = self._choose_yaw(boxes, name, q)
        if yaw is None:
            yaw = self._best_equiv_yaw(0.0, q)
        T, _, _ = fk(q)
        safe0 = self._safe_z(boxes)
        # fingertip at object centre (but not below support+5mm)
        tip = max(b["z"], b["z"] - b["hz"] + 0.012)
        grasp_z = tip + FINGER
        off = grasp_z - b["z"]          # EE z - object centre z while held
        safe1 = max(self._safe_z(boxes, b["hz"], 0.0) , b["hz"] + off + 0.03 + 0.15)
        safe1 = max(safe1, self._safe_z({k: v for k, v in boxes.items() if k != name}) + b["hz"])
        segs = []
        segs.append(("move", np.array([T[0, 3], T[1, 3], max(T[2, 3], safe0)]), None))
        segs.append(("move", np.array([b["x"], b["y"], max(safe0, safe1)]), yaw))
        segs.append(("move", np.array([b["x"], b["y"], grasp_z]), yaw, "grasp_descend", name))
        segs.append(("grip", -1.0, name))
        segs.append(("move", np.array([b["x"], b["y"], safe1]), yaw))
        pyaw = yaw if final_yaw is None else final_yaw
        place_z = place_bottom + b["hz"] + off
        segs.append(("move", np.array([place_xy[0], place_xy[1], safe1]), pyaw))
        segs.append(("move", np.array([place_xy[0], place_xy[1], place_z]), pyaw, "place_descend"))
        segs.append(("grip", 1.0, None))
        segs.append(("move", np.array([place_xy[0], place_xy[1], max(safe1, place_z + 0.05)]), pyaw))
        return segs

    def _replan(self, state):
        boxes = self._boxes(state)
        reg = self._region(boxes)
        blk = self._blocking(boxes)
        blk = [n for n in blk if self.fail.get(n, 0) < 6]
        if blk:
            # most accessible first: highest grasp clearance
            q = self._q(state)
            blk.sort(key=lambda n: -max(self._grasp_clear(boxes, n, 0.0),
                                         self._grasp_clear(boxes, n, PI / 2)))
            name = blk[0]
            spot = self._drop_spot(boxes, name)
            self.placed_spots.append(spot)
            b = boxes[name]
            bottom = 0.075 + 0.002
            return self._plan_pick_place(state, name, spot, bottom)
        # place target block
        tb = boxes["target_block"]
        return self._plan_pick_place(state, "target_block", (reg["x"], reg["y"]),
                                     reg["z"] + reg["hz"] + 0.0005)

    # ---------------------------------------------------------------- control
    def get_action(self, state):
        q = self._q(state)
        act = np.zeros(11, dtype=np.float32)
        # detect rejected motion
        rejected = False
        if self.last_cmd is not None and self.last_q is not None:
            if np.max(np.abs(self.last_cmd)) > 1e-6 and np.max(np.abs(q - self.last_q)) < 1e-7:
                rejected = True
        self.last_q = q.copy()
        self.last_cmd = None

        if rejected and self.cur is not None and self.cur[0] == "move":
            self._handle_reject(state)

        for _ in range(20):
            if self.cur is None:
                if not self.segs:
                    self.segs = self._replan(state)
                self.cur = self.segs.pop(0)
                self.stuck = 0
            seg = self.cur
            if seg[0] == "grip":
                act[10] = seg[1]
                self.cur = None
                self.last_cmd = np.zeros(7)
                return act
            # move segment
            goal, yaw = seg[1], seg[2]
            T, _, _ = fk(q)
            if yaw is None:
                Rt = T[:3, :3]
                Rt = down_R(np.arctan2(T[1, 0], T[0, 0])) if abs(T[2, 2] + 1) < 0.2 else Rt
            else:
                Rt = down_R(yaw)
            p = T[:3, 3]
            d = goal - p
            rerr = np.linalg.norm(_rotvec(Rt @ T[:3, :3].T))
            if np.linalg.norm(d) < 5e-4 and rerr < 2e-3:
                self.cur = None
                continue
            # intermediate cartesian target
            step = 0.08
            nd = np.linalg.norm(d)
            tgt = goal if nd < step else p + d * step / nd
            qt, err = ik(q, tgt, Rt)
            dq = qt - q
            m = np.max(np.abs(dq))
            if m > 0.2:
                dq *= 0.2 / m
            if m < 1e-6:
                self.cur = None
                continue
            act[3:10] = dq.astype(np.float32)
            self.last_cmd = dq
            return act
        return act

    def _handle_reject(self, state):
        seg = self.cur
        tag = seg[3] if len(seg) > 3 else None
        self.stuck += 1
        if tag == "place_descend":
            # contact: just release here
            self.cur = None
            return
        if tag == "grasp_descend":
            # can't reach grasp pose: grasp at current height if fingertips reach object, else retry
            name = seg[4]
            boxes = self._boxes(state)
            b = boxes[name]
            T, _, _ = fk(self._q(state))
            tip = T[2, 3] - FINGER
            if tip < b["z"] + b["hz"] - 0.006:
                self.cur = None
                return
            self.fail[name] = self.fail.get(name, 0) + 1
            T, _, _ = fk(self._q(state))
            self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.08]), None)]
            self.cur = None
            return
        # generic: go up a bit, then replan
        T, _, _ = fk(self._q(state))
        self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.03]), None)]
        self.cur = None
