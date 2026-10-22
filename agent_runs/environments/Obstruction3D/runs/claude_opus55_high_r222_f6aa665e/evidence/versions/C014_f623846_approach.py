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


def _expm(v):
    th = np.linalg.norm(v)
    if th < 1e-12:
        return np.eye(3)
    k = v / th
    K = np.array([[0, -k[2], k[1]], [k[2], 0, -k[0]], [-k[1], k[0], 0]])
    return np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * (K @ K)


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
TABLE_TOP = 0.075
STEP_FAST = 0.12
STEP_LOW = 0.05
SAFE_FLOOR = 0.2
BASE_ASSIST = True
STEP_TRAVEL = 0.25
ASSIST_MINX = 0.2
SAFE_CLR = 0.02
MOUNT_OFF = 0.12            # arm mount = base_xy + MOUNT_OFF * (cos rot, sin rot)
TABLE_X = (0.10, 0.50)
TABLE_Y = (-0.40, 0.40)
MAX_OPEN = 0.078            # max object width between the fingers


def _yaw_of(Rm):
    return np.arctan2(Rm[1, 0], Rm[0, 0])


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space

    # ---------------------------------------------------------------- state helpers
    def _robot(self, state):
        return state.get_object_from_name("robot")

    def _q(self, state):
        r = self._robot(state)
        return np.array([state.get(r, "joint_%d" % i) for i in range(1, 8)])

    def _base(self, state):
        r = self._robot(state)
        return np.array([state.get(r, "pos_base_x"), state.get(r, "pos_base_y"),
                         state.get(r, "pos_base_rot")])

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
                    hz=state.get(o, "half_extent_z"), g=state.get(o, "grasp_active"),
                    yaw=2 * np.arctan2(state.get(o, "pose_qz"), state.get(o, "pose_qw")))
            except Exception:
                pass
        return out

    # ---------------------------------------------------------------- frames
    @staticmethod
    def _mount(base):
        c, s = np.cos(base[2]), np.sin(base[2])
        M = np.eye(4)
        M[:3, :3] = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])
        M[0, 3] = base[0] + MOUNT_OFF * c
        M[1, 3] = base[1] + MOUNT_OFF * s
        return M

    def _ee_world(self, q, base):
        T, _, _ = fk(q)
        return self._mount(base) @ T

    def _ik_world(self, q0, pos, Rw, base, iters=100):
        M = self._mount(base)
        pa = M[:3, :3].T @ (np.asarray(pos) - M[:3, 3])
        Ra = M[:3, :3].T @ Rw
        return ik(q0, pa, Ra, iters=iters)

    def _feasible(self, base, pos, yaw, seeds):
        """IK feasibility of a top-down pose from a few seeds; returns q or None."""
        Rw = down_R(yaw)
        for s in seeds:
            q, e = self._ik_world(s, pos, Rw, base, iters=150)
            if e < 1e-4:
                return q
        return None

    # ---------------------------------------------------------------- episode
    def reset(self, state, info):
        self.segs = []
        self.cur = None
        self.last_q = None
        self.last_base = None
        self.last_cmd = False
        self.fail = {}              # candidate key -> failures
        self.obj_fail = {}
        self.placed_spots = []
        self.pending_check = None
        self.best_d = None
        self.stall = 0
        self.q_home = self._q(state)
        self.nsteps = 0
        self.scale = 1.0
        self.max_top = 0.15
        self.esc = 0
        # a nominal top-down configuration used as an extra IK seed
        b = self._base(state)
        qn, e = self._ik_world(self.q_home, [0.30, 0.0, 0.33], down_R(0.0), b, iters=200)
        self.q_nom = qn

    # ---------------------------------------------------------------- geometry
    def _blocking(self, boxes):
        reg = boxes["target_region"]
        res = []
        for n, b in boxes.items():
            if n in ("target_region", "target_block") or b["g"] > 0.5:
                continue
            ex, ey = self._extent_xy(b)
            if abs(b["x"] - reg["x"]) < ex + reg["hx"] + 0.004 and \
               abs(b["y"] - reg["y"]) < ey + reg["hy"] + 0.004 and \
               b["z"] - b["hz"] < reg["z"] + reg["hz"] + 0.08:
                res.append(n)
        return res

    @staticmethod
    def _extent_xy(b):
        c, s = abs(np.cos(b["yaw"])), abs(np.sin(b["yaw"]))
        return b["hx"] * c + b["hy"] * s, b["hx"] * s + b["hy"] * c

    @staticmethod
    def _width_along(b, yaw):
        a = yaw - b["yaw"]
        c, s = abs(np.cos(a)), abs(np.sin(a))
        return 2 * (b["hx"] * c + b["hy"] * s), 2 * (b["hx"] * s + b["hy"] * c)

    def _grasp_clear(self, boxes, name, yaw, tip):
        """Approximate clearance of the finger volumes (open + closing sweep) and the
        palm from other objects for a top-down grasp."""
        b = boxes[name]
        wu, wv = self._width_along(b, yaw)
        u = np.array([np.cos(yaw), np.sin(yaw)])
        v = np.array([-u[1], u[0]])
        c0 = np.array([b["x"], b["y"]])
        best = 1.0
        for n, o in boxes.items():
            if n == name or o["g"] > 0.5:
                continue
            otop = o["z"] + o["hz"]
            if n == "target_region":
                continue
            # z-overlap with finger volume (tip-0.015 .. tip+0.045) and palm (above)
            if otop < tip - 0.016:
                continue
            ex, ey = self._extent_xy(o)
            # sample the object's footprint corners/edges in gripper frame
            pts = []
            for fx in (-1, -0.5, 0, 0.5, 1):
                for fy in (-1, -0.5, 0, 0.5, 1):
                    pts.append([o["x"] + fx * ex, o["y"] + fy * ey])
            pts = np.array(pts) - c0
            pu = np.abs(pts @ u)
            pv = np.abs(pts @ v)
            # finger band: u in [wu/2, 0.068], |v| < 0.014
            du = np.maximum(wu / 2 - pu, pu - 0.068)
            dv = pv - 0.014
            d_f = np.min(np.maximum(du, dv))
            # palm: |u| < 0.07, |v| < 0.035, z > tip + 0.045
            if otop > tip + 0.040:
                d_p = np.min(np.maximum(pu - 0.07, pv - 0.035))
                d_f = min(d_f, d_p)
            best = min(best, d_f)
        return best

    def _grasp_candidates(self, boxes, name):
        b = boxes[name]
        support = b["z"] - b["hz"]
        top = b["z"] + b["hz"]
        tip0 = min(max(b["z"], support + 0.017), top - 0.001)
        tips = [tip0, min(tip0 + 0.004, top - 0.001), top - 0.002]
        cands = []
        for yaw in (b["yaw"], b["yaw"] + PI / 2, b["yaw"] + PI / 4, b["yaw"] - PI / 4):
            yaw = wrap(yaw)
            wu, wv = self._width_along(b, yaw)
            if wu > MAX_OPEN:
                continue
            for ti, tip in enumerate(tips):
                if tip < support + 0.0125:
                    continue
                key = (name, round(yaw, 3), round(tip, 4))
                if self.fail.get(key, 0) > 0:
                    continue
                clr = self._grasp_clear(boxes, name, yaw, tip)
                diag = 0 if abs(wrap(2 * (yaw - b["yaw"]))) < 0.1 else 1
                score = min(clr, 0.02) - 0.004 * diag - 0.003 * ti - 0.1 * wu * (clr > 0.005)
                cands.append((score, yaw, tip, key, clr))
        cands.sort(key=lambda c: -c[0])
        return cands

    def _safe_z(self, boxes, exclude=None, held_below=0.0, path=None, rad=0.08):
        top = TABLE_TOP + 0.03
        for n, b in boxes.items():
            if b["g"] > 0.5 or n == exclude:
                continue
            if path is not None:
                a = np.asarray(path[0][:2], float)
                c = np.asarray(path[1][:2], float)
                o = np.array([b["x"], b["y"]])
                ab = c - a
                t = 0.0 if ab @ ab < 1e-12 else min(1.0, max(0.0, (o - a) @ ab / (ab @ ab)))
                ex, ey = self._extent_xy(b)
                if np.linalg.norm(a + t * ab - o) > rad + np.hypot(ex, ey):
                    continue
            top = max(top, b["z"] + b["hz"])
        return max(SAFE_FLOOR, top + SAFE_CLR + held_below + FINGER)

    def _drop_spot(self, boxes, name, base, seeds, safe):
        reg = boxes["target_region"]
        b = boxes[name]
        bex, bey = self._extent_xy(b)
        cands = []
        for x in np.arange(TABLE_X[0] + 0.06, TABLE_X[1] - 0.03, 0.025):
            for y in np.arange(TABLE_Y[0] + 0.05, TABLE_Y[1] - 0.049, 0.025):
                if x < 0.2 and abs(y) < 0.14:
                    continue
                clr = 1.0
                for n, o in boxes.items():
                    if n == name:
                        continue
                    ex, ey = self._extent_xy(o)
                    m = 0.06 if n != "target_region" else 0.03
                    if n == "target_block":
                        m = 0.075
                    dx = abs(x - o["x"]) - ex - bex - m
                    dy = abs(y - o["y"]) - ey - bey - m
                    clr = min(clr, max(dx, dy))
                for (px, py) in self.placed_spots:
                    clr = min(clr, max(abs(x - px), abs(y - py)) - 0.07)
                dist = np.hypot(x - b["x"], y - b["y"])
                tb = boxes["target_block"]
                if name != "target_block":
                    dist += 0.7 * np.hypot(x - tb["x"], y - tb["y"])
                cands.append((min(clr, 0.03) * 10 - dist, x, y))
        cands.sort(key=lambda c: -c[0])
        for sc, x, y in cands[:25]:
            if self._feasible(base, [x, y, safe], 0.0, seeds) is not None:
                return (x, y)
        return (cands[0][1], cands[0][2])

    # ---------------------------------------------------------------- base selection
    def _choose_base(self, base, poses, seeds):
        """Return a base pose from which all (pos, yaw) poses are IK-feasible, preferring
        the current base.  Returns (base, ok)."""
        def ok(bb):
            ss = list(seeds)
            for pos, yaw in poses:
                q = self._feasible(bb, pos, yaw, ss)
                if q is None:
                    return False
                ss = [q] + ss
            return True
        if ok(base):
            return base, True
        cx = np.mean([p[0][0] for p in poses])
        cy = np.mean([p[0][1] for p in poses])
        cands = []
        for dx in (0.0, -0.05, -0.1, -0.15, -0.2, -0.25, 0.05):
            for dy in (0.0, -0.1, 0.1, -0.2, 0.2):
                bx = min(base[0] + dx, -0.08)
                by = base[1] + dy
                # prefer reach distance ~0.35-0.45 from mount
                mx = bx + MOUNT_OFF
                r = np.hypot(cx - mx, cy - by)
                cost = abs(dx) + abs(dy) + 0.5 * abs(r - 0.4)
                cands.append((cost, np.array([bx, by, 0.0])))
        cands.sort(key=lambda c: c[0])
        for cost, bb in cands:
            if ok(bb):
                return bb, True
        return base, False

    # ---------------------------------------------------------------- planning
    def _plan_pick(self, state, boxes, name, cand):
        """Segments to pick object `name` with candidate (yaw, tip)."""
        q = self._q(state)
        base = self._base(state)
        b = boxes[name]
        yaw, tip = cand
        seeds = [q, self.q_nom, self.q_home]
        Tw0 = self._ee_world(q, base)
        safe = self._safe_z(boxes, path=(Tw0[:3, 3], (b["x"], b["y"])))
        grasp_z = tip + FINGER
        above = np.array([b["x"], b["y"], safe])
        gpos = np.array([b["x"], b["y"], grasp_z])
        # choose equivalent yaw (yaw or yaw+pi) closest to current tool yaw
        Tw = self._ee_world(q, base)
        cur_yaw = _yaw_of(Tw[:3, :3])
        opts = sorted([yaw, wrap(yaw + PI)], key=lambda a: abs(wrap(a - cur_yaw)))
        for y in opts:
            nb, ok = self._choose_base(base, [(above, y), (gpos, y)], seeds)
            if ok:
                yaw = y
                break
        segs = []
        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], max(Tw[2, 3], safe)]), None, "lift"))
        if np.max(np.abs(nb - base)) > 1e-6:
            segs.append(("base", nb))
        segs.append(("move", above, yaw, "travel"))
        segs.append(("move", gpos, yaw, "grasp_descend", name))
        segs.append(("grip", -1.0, name))
        return segs

    def _plan_place(self, state, boxes, name, place_xy, bottom):
        """Segments to place currently-held object `name` with its bottom at `bottom`."""
        q = self._q(state)
        base = self._base(state)
        b = boxes[name]
        Tw = self._ee_world(q, base)
        yaw = _yaw_of(Tw[:3, :3])
        off = Tw[2, 3] - b["z"]                 # EE z - object centre z
        # xy offset of object centre relative to EE (in world, keep yaw constant)
        dxy = np.array([b["x"] - Tw[0, 3], b["y"] - Tw[1, 3]])
        seeds = [q, self.q_nom, self.q_home]
        hb = b["hz"] + off - FINGER
        ex0 = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
        bex, bey = self._extent_xy(b)
        safe = self._safe_z(boxes, exclude=name, held_below=hb,
                            path=(Tw[:3, 3], ex0), rad=max(0.08, np.hypot(bex, bey) + 0.02))
        safe = max(safe, bottom + b["hz"] + off + 0.03)
        ex = np.array([place_xy[0] - dxy[0], place_xy[1] - dxy[1]])
        pz = bottom + b["hz"] + off
        above = np.array([ex[0], ex[1], safe])
        ppos = np.array([ex[0], ex[1], pz])
        nb, ok = self._choose_base(base, [(above, yaw), (ppos, yaw)], seeds)
        segs = []
        segs.append(("move", np.array([Tw[0, 3], Tw[1, 3], max(safe, Tw[2, 3])]), yaw, "lift"))
        if np.max(np.abs(nb - base)) > 1e-6:
            segs.append(("base", nb))
        segs.append(("move", above, yaw, "travel"))
        segs.append(("move", ppos, yaw, "place_descend"))
        segs.append(("grip", 1.0, None))
        return segs

    def _held(self, boxes):
        for n, b in boxes.items():
            if b["g"] > 0.5:
                return n
        return None

    def _replan(self, state):
        boxes = self._boxes(state)
        reg = boxes["target_region"]
        held = self._held(boxes)
        r = self._robot(state)
        if held is None and state.get(r, "grasp_active") > 0.5:
            held = None
        if held is not None:
            if held == "target_block" and not self._blocking(boxes):
                return self._plan_place(state, boxes, held, (reg["x"], reg["y"]),
                                        reg["z"] + reg["hz"] + 0.0005)
            if held == "target_block":
                # should not happen often: park the block somewhere free
                base = self._base(state)
                seeds = [self._q(state), self.q_nom, self.q_home]
                spot = self._drop_spot(boxes, held, base, seeds, self._safe_z(boxes))
                return self._plan_place(state, boxes, held, spot, TABLE_TOP + 0.001)
            base = self._base(state)
            seeds = [self._q(state), self.q_nom, self.q_home]
            spot = self._drop_spot(boxes, held, base, seeds, self._safe_z(boxes))
            self.placed_spots.append(spot)
            return self._plan_place(state, boxes, held, spot, TABLE_TOP + 0.0015)
        blk = self._blocking(boxes)
        targets = blk if blk else ["target_block"]
        best = None
        for n in targets:
            cands = self._grasp_candidates(boxes, n)
            if cands:
                c = cands[0]
                if best is None or c[0] > best[0][0]:
                    best = (c, n)
        if best is None:
            # everything failed once: reset failure memory and retry
            self.fail = {}
            for n in targets:
                cands = self._grasp_candidates(boxes, n)
                if cands:
                    best = (cands[0], n)
                    break
        if best is None:
            T = self._ee_world(self._q(state), self._base(state))
            return [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.02]), None, "lift")]
        c, n = best
        self.cur_key = c[3]
        return self._plan_pick(state, boxes, n, (c[1], c[2]))

    # ---------------------------------------------------------------- control
    def get_action(self, state):
        self.nsteps += 1
        boxes0 = self._boxes(state)
        self.max_top = max([b["z"] + b["hz"] for n, b in boxes0.items() if b["g"] < 0.5] + [0.1])
        q = self._q(state)
        base = self._base(state)
        act = np.zeros(11, dtype=np.float32)
        rejected = False
        if self.last_cmd and self.last_q is not None:
            if np.max(np.abs(q - self.last_q)) < 1e-7 and \
               np.max(np.abs(base - self.last_base)) < 1e-7:
                rejected = True
        self.last_q = q.copy()
        self.last_base = base.copy()
        self.last_cmd = False

        if self.pending_check is not None:
            name = self.pending_check
            self.pending_check = None
            r = self._robot(state)
            if state.get(r, "grasp_active") < 0.5:
                key = getattr(self, "cur_key", None)
                if key is not None:
                    self.fail[key] = self.fail.get(key, 0) + 1
                self.segs = []
                self.cur = None

        if rejected:
            self.scale = max(self.scale * 0.35, 0.01)
        elif self.last_q is not None:
            self.scale = min(1.0, self.scale * 1.5)
        if rejected and self.cur is not None and self.cur[0] in ("move", "base"):
            if self.scale > 0.02 and self.cur[0] == "move" and self.cur[3] != "escape":
                pass            # retry the same segment with a smaller step
            else:
                self._handle_reject(state)

        for _ in range(30):
            if self.cur is None:
                if not self.segs:
                    self.segs = self._replan(state)
                self.cur = self.segs.pop(0)
                self.best_d = None
                self.stall = 0
            seg = self.cur
            if seg[0] == "grip":
                act[10] = seg[1]
                self.cur = None
                self.pending_check = seg[2] if seg[1] < 0 else None
                return act
            if seg[0] == "base":
                d = seg[1] - base
                d[2] = wrap(d[2])
                if np.max(np.abs(d)) < 1e-6:
                    self.cur = None
                    continue
                act[0:3] = np.clip(d, -0.2, 0.2)
                self.last_cmd = True
                return act
            goal, yaw = seg[1], seg[2]
            Tw = self._ee_world(q, base)
            if yaw is None:
                Rt = down_R(_yaw_of(Tw[:3, :3])) if Tw[2, 2] < -0.8 else Tw[:3, :3]
            else:
                Rt = down_R(yaw)
            p = Tw[:3, 3]
            d = goal - p
            nd = np.linalg.norm(d)
            rerr = np.linalg.norm(_rotvec(Rt @ Tw[:3, :3].T))
            if nd < 5e-4 and rerr < 2e-3:
                self.cur = None
                continue
            # stall detection
            prog = nd + 0.1 * rerr
            if self.best_d is None or prog < self.best_d - 2e-4:
                self.best_d = prog
                self.stall = 0
            else:
                self.stall += 1
                if self.stall >= 4:
                    if nd < 3e-3 and rerr < 2e-2:
                        self.cur = None
                        continue
                    self._handle_reject(state)
                    continue
            step = STEP_FAST
            low = p[2] - FINGER < self.max_top + 0.03
            if low and seg[3] in ("lift", "grasp_descend", "place_descend", "retreat"):
                step = STEP_LOW
            step *= self.scale
            rv = _rotvec(Rt @ Tw[:3, :3].T)
            f = 1.0
            if nd > 1e-9:
                f = min(f, step / nd)
            if rerr > 1e-9:
                f = min(f, max(0.5 * self.scale, 0.02) / rerr)
            lim = 0.2 * max(self.scale, 0.05)
            dq = None
            assist = BASE_ASSIST and seg[3] == "travel" and abs(d[1]) > 1e-4 and \
                min(p[0], goal[0]) - self._mount(base)[0, 3] > ASSIST_MINX
            if assist:
                f = min(1.0, STEP_TRAVEL * self.scale / nd, 0.2 * self.scale / abs(d[1]))
                if rerr > 1e-9:
                    f = min(f, max(0.5 * self.scale, 0.02) / rerr)
            db = np.zeros(3)
            for _it in range(5):
                tgt = p + d * f
                Rs = _expm(rv * f) @ Tw[:3, :3]
                bb = base
                if assist:
                    db = np.array([0.0, d[1] * f, 0.0])
                    bb = base + db
                qt, err = self._ik_world(q, tgt, Rs, bb)
                dq = qt - q
                m = np.max(np.abs(dq))
                if m <= lim:
                    break
                f *= lim / m * 0.97
            if assist:
                act[0:3] = db.astype(np.float32)
            m = np.max(np.abs(dq))
            if m > lim:
                dq *= lim / m
            if m < 1e-7:
                self.stall += 1
                continue
            act[3:10] = dq.astype(np.float32)
            self.last_cmd = True
            return act
        return act

    def _handle_reject(self, state):
        seg = self.cur
        tag = seg[3] if (seg[0] == "move" and len(seg) > 3) else None
        q = self._q(state)
        base = self._base(state)
        T = self._ee_world(q, base)
        if tag == "place_descend":
            # contact: release here (object is resting on something)
            self.cur = None
            return
        if tag == "grasp_descend":
            key = getattr(self, "cur_key", None)
            if key is not None:
                self.fail[key] = self.fail.get(key, 0) + 1
            self.segs = [("move", np.array([T[0, 3], T[1, 3], T[2, 3] + 0.06]), None, "lift")]
            self.cur = None
            return
        if seg[0] == "base":
            self.segs = []
            self.cur = None
            return
        # generic: small escape displacement in a cycling direction, then replan
        dirs = [(0, 0, 1), (1, 0, 0.5), (-1, 0, 0.5), (0, 1, 0.5), (0, -1, 0.5),
                (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (1, 1, 1), (-1, -1, 1),
                (1, -1, 1), (-1, 1, 1)]
        d = np.array(dirs[self.esc % len(dirs)], dtype=float)
        self.esc += 1
        d /= np.linalg.norm(d)
        mag = 0.003 if tag != "escape" else 0.003 + 0.002 * (self.esc // len(dirs) % 3)
        self.segs = [("move", T[:3, 3] + d * mag, None, "escape")]
        self.cur = None
        self.scale = 0.3
