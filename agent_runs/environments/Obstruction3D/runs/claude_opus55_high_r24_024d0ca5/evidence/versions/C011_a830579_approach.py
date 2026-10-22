"""Obstruction3D approach: clear obstructions off the target region, then place
the target block on it.  Uses a calibrated Kinova Gen3 FK/IK model (kin.py).

Empirical facts (black-box probing):
- Arm mount is +0.12m along base x; the grasp/tool frame is 0.12m past the flange.
- Gripper fingers lie along the tool x axis, extending ~0.07m from the centre and
  ~0.035m below the tool frame.  Robot/held object collisions reject a step.
- Grasp (close) succeeds when tool z in [bottom+0.044, top+0.033] over the object.
- Release (open) succeeds only if the held object rests within a few mm of a surface.
"""
import numpy as np
from kin import tool_fk, tool_ik, down_R

JN = [f'joint_{i}' for i in range(1, 8)]
STEP = 0.2             # max joint delta per step
FINGER_DOWN = 0.036    # fingertips below tool frame
F_OFF, F_HL, F_HW = 0.046, 0.024, 0.013   # finger centre offset, half length, half width


def _q2R(x, y, z, w):
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def _T(p, q):
    M = np.eye(4); M[:3, :3] = _q2R(*q); M[:3, 3] = p
    return M


def _yaw_of_quat(q):
    x, y, z, w = q
    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def _aabb_of_rect(c, hx, hy, yaw):
    c_, s_ = abs(np.cos(yaw)), abs(np.sin(yaw))
    return np.array(c), np.array([c_ * hx + s_ * hy, s_ * hx + c_ * hy])


def _gap(c1, h1, c2, h2):
    """Signed separation between two AABBs (positive = apart)."""
    return np.max(np.abs(np.asarray(c1) - np.asarray(c2)) - np.asarray(h1) - np.asarray(h2))


def _finger_boxes(xy, yaw):
    d = np.array([np.cos(yaw), np.sin(yaw)])
    out = []
    for sgn in (1, -1):
        out.append(_aabb_of_rect(np.asarray(xy) + sgn * F_OFF * d, F_HL, F_HW, yaw))
    return out


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space

    # ------------------------------------------------------------ helpers
    def _obj(self, state, name):
        return state.get_object_from_name(name)

    def _pose(self, state, name):
        o = self._obj(state, name)
        return (np.array([state.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')]),
                np.array([state.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]),
                np.array([state.get(o, f) for f in ('half_extent_x', 'half_extent_y', 'half_extent_z')]))

    def _box(self, state, name):
        """(centre_xy, half_xy AABB, bottom z, top z)"""
        p, q, h = self._pose(state, name)
        c, hh = _aabb_of_rect(p[:2], h[0], h[1], _yaw_of_quat(q))
        return c, hh, p[2] - h[2], p[2] + h[2]

    def _q(self, state):
        return np.array([state.get(self.robot, f) for f in JN])

    def _base(self, state):
        return (state.get(self.robot, 'pos_base_x'), state.get(self.robot, 'pos_base_y'),
                state.get(self.robot, 'pos_base_rot'))

    def _tool(self, state):
        return tool_fk(self._q(state), self._base(state))

    def _grasped_name(self, state):
        for n in self.names:
            if state.get(self._obj(state, n), 'grasp_active') > 0.5:
                return n
        return None

    def _max_top(self, state, exclude=()):
        t = self.table_z
        for n in self.names:
            if n in exclude:
                continue
            t = max(t, self._box(state, n)[3])
        return t

    # ------------------------------------------------------------ planning
    def reset(self, state, info):
        self.robot = state.get_object_from_name('robot')
        self.names = sorted(n for n in state.get_object_names() if n != 'robot')
        self.obstructions = sorted(n for n in self.names if n.startswith('obstruction'))
        rp, _, rh = self._pose(state, 'target_region')
        self.table_z = rp[2] - rh[2]
        self.region = (rp, rh)
        self.tasks = [(n, 'clear') for n in self._blocking_obstructions(state)]
        self.tasks.append(('target_block', 'goal'))
        self.phase = None
        self.qpath = []
        self.last_q = None
        self.last_a = None
        self.blocked = False
        self.stuck = 0
        self.descent_len = 0
        self.release_tries = 0
        self.grasp_attempt = 0
        self.total_fail = 0
        self.final_grip = 0.0
        self.wp_yaw = 0.0
        self._start_task(state)

    def _blocking_obstructions(self, state, margin=0.003):
        rp, rh = self.region
        out = []
        for n in self.obstructions:
            c, hh, _, _ = self._box(state, n)
            if _gap(c, hh, rp[:2], rh[:2]) < margin:
                out.append(n)
        return out

    def _finger_clearance(self, state, xy, yaw, tip_z, exclude):
        """Min xy gap between finger boxes and objects whose top is above tip_z."""
        clear = 1.0
        fbs = _finger_boxes(xy, yaw)
        for n in self.names:
            if n in exclude:
                continue
            c, hh, bot, top = self._box(state, n)
            if top < tip_z - 0.002:
                continue
            for fc, fh in fbs:
                clear = min(clear, _gap(fc, fh, c, hh))
        return clear

    def _choose_yaw(self, state, name, kind, attempt):
        p, q, h = self._pose(state, name)
        oy = _yaw_of_quat(q)
        gz = self._grasp_z(p, h)
        cands = [oy, oy + np.pi / 2, oy + np.pi / 4, oy - np.pi / 4]
        scored = []
        for i, y in enumerate(cands):
            y = _wrap(2 * y) / 2  # modulo pi
            c = self._finger_clearance(state, p[:2], y, gz - FINGER_DOWN, exclude=(name,))
            if kind == 'goal':
                rp, rh = self.region
                surf = rp[2] + rh[2]
                tip = surf + 0.001 + (gz - (p[2] - h[2])) - FINGER_DOWN
                c = min(c, self._finger_clearance(state, rp[:2], y, tip,
                                                  exclude=(name, 'target_region')))
            scored.append((min(c, 0.02) - 0.001 * i, y))
        scored.sort(key=lambda t: -t[0])
        return scored[attempt % len(scored)][1]

    def _grasp_z(self, p, h):
        lo = p[2] - h[2] + 0.045
        hi = p[2] + h[2] + 0.032
        return 0.5 * (lo + hi) if hi > lo else hi - 0.001

    def _free_spot(self, state, name, yaw, hold_off):
        """Pick a table spot clear of region/other objects (object + fingers)."""
        p0, _, _ = self._pose(state, name)
        c0, h, _, _ = self._box(state, name)
        others = []
        for n in self.names:
            if n == name:
                continue
            others.append(self._box(state, n))
        rp, rh = self.region
        tip = self.table_z + 0.001 + hold_off - FINGER_DOWN
        best, best_score = None, 1e9
        fb, fb_score = None, -1e9
        for x in np.linspace(0.2, 0.5, 16):
            for y in np.linspace(-0.34, 0.34, 35):
                c = np.array([x, y])
                clear = _gap(c, h, rp[:2], rh[:2]) - 0.03
                fbs = _finger_boxes(c, yaw)
                for oc, oh, bot, top in others:
                    clear = min(clear, _gap(c, h, oc, oh) - 0.02)
                    if top > tip - 0.002:
                        for fc, fh in fbs:
                            clear = min(clear, _gap(fc, fh, oc, oh) - 0.008)
                if clear > fb_score:
                    fb, fb_score = c, clear
                if clear >= 0:
                    score = np.linalg.norm(c - p0[:2])
                    if score < best_score:
                        best, best_score = c, score
        return best if best is not None else fb

    def _transit_z(self, state, hold_off=0.0, exclude=()):
        top = self._max_top(state, exclude)
        return max(top + 0.03 + max(FINGER_DOWN, hold_off), 0.2)

    def _start_task(self, state):
        if not self.tasks:
            self.phase = 'done'
            return
        name, kind = self.tasks[0]
        p, q, h = self._pose(state, name)
        self.cur_obj = name
        self.grasp_yaw = self._choose_yaw(state, name, kind, self.grasp_attempt)
        gz = self._grasp_z(p, h)
        zt = self._transit_z(state)
        tool = self._tool(state)[:3, 3]
        wps = []
        if tool[2] < zt - 0.01:
            wps.append(np.array([tool[0], tool[1], zt]))
        wps.append(np.array([p[0], p[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]))
        wps.append(np.array([p[0], p[1], gz]))
        self._set_path(state, wps, self.grasp_yaw, final_grip=-1.0, flip=True)
        self.phase = 'to_grasp'

    def _set_path(self, state, wps, yaw, final_grip=0.0, res=0.01, flip=False):
        """Cartesian waypoints -> dense joint path (IK warm-started).
        Yaw is interpolated from the current tool yaw over all but the last segment."""
        q = self._q(state)
        base = self._base(state)
        T0 = tool_fk(q, base)
        cur = T0[:3, 3]
        y0 = np.arctan2(T0[1, 0], T0[0, 0])
        dy = _wrap(yaw - y0)
        if flip and abs(dy) > np.pi / 2:
            dy = dy - np.sign(dy) * np.pi
        yaw = y0 + dy
        pts = [cur]
        for w in wps:
            pts.append(np.asarray(w, dtype=float))
        seg = [np.linalg.norm(pts[i + 1] - pts[i]) for i in range(len(wps))]
        rot_len = sum(seg[:-1]) if len(seg) > 1 and sum(seg[:-1]) > 0.02 else sum(seg)
        rot_len = max(rot_len, 1e-6)
        path = []
        self.corners = set()
        qc = q.copy()
        travelled = 0.0
        for i, w in enumerate(wps):
            w = pts[i + 1]
            d = seg[i]
            n = max(1, int(np.ceil(d / res)), int(np.ceil(abs(dy) * min(d, rot_len) / rot_len / 0.1)))
            for k in range(1, n + 1):
                pt = cur + (w - cur) * k / n
                f = min(1.0, (travelled + d * k / n) / rot_len)
                qn, ok = tool_ik(qc, pt, down_R(y0 + f * dy), base, iters=40)
                qn = qc + _wrap(qn - qc)
                path.append(qn)
                qc = qn
            travelled += d
            self.corners.add(len(path) - 1)
            cur = w
        self.qpath = path
        self.popped = 0
        self.wp_yaw = yaw
        self.final_grip = final_grip
        self.travel_grip = 1.0 if final_grip < 0 else 0.0
        self.stuck = 0

    # ------------------------------------------------------------ control
    def _track(self, state):
        """Step along the precomputed joint path; None if done."""
        q = self._q(state)
        while self.qpath and np.max(np.abs(_wrap(self.qpath[0] - q))) < 1e-4:
            self.qpath.pop(0)
            self.popped += 1
        if not self.qpath:
            return None
        k = -1
        for i, qp in enumerate(self.qpath):
            if np.max(np.abs(_wrap(qp - q))) <= STEP:
                k = i
                if (i + self.popped) in self.corners:
                    break
            else:
                break
        a = np.zeros(11, dtype=np.float32)
        if k >= 0:
            self.qpath = self.qpath[k:]
            self.popped += k
            k = 0
            d = _wrap(self.qpath[0] - q)
            a[3:10] = d
            a[10] = self.travel_grip
        else:
            d = _wrap(self.qpath[0] - q)
            a[3:10] = d * (STEP / np.max(np.abs(d)))
        return a

    def _noop(self, grip=0.0):
        a = np.zeros(11, dtype=np.float32); a[10] = grip
        return a

    def get_action(self, state):
        q = self._q(state)
        moved = self.last_q is None or not np.allclose(q, self.last_q, atol=1e-7)
        attempted = self.last_a is not None and np.any(np.abs(self.last_a[3:10]) > 1e-9)
        self.blocked = attempted and not moved
        self.last_q = q.copy()
        try:
            a = self._policy(state)
        except Exception:
            a = self._noop()
        a = np.asarray(a, dtype=np.float32).copy()
        a[:10] = np.clip(a[:10], -STEP, STEP)
        a[10] = np.clip(a[10], -1, 1)
        self.last_a = a
        return a

    def _policy(self, state):
        ph = self.phase
        if ph == 'done':
            if self._grasped_name(state) is None and self.tasks:
                self._start_task(state)
            return self._noop()

        if ph == 'to_grasp':
            g = self._grasped_name(state)
            if g is not None:
                return self._on_grasped(state, g)
            if self.blocked:
                self.stuck += 1
                if self.stuck >= 2:
                    self.qpath = []
            a = self._track(state)
            if a is not None:
                return a
            self.phase = 'close'
            return self._noop(-1.0)

        if ph == 'close':
            g = self._grasped_name(state)
            if g is None:
                self.grasp_attempt += 1
                self.total_fail += 1
                self._start_task(state)
                return self._track(state) if self.qpath else self._noop()
            return self._on_grasped(state, g)

        if ph == 'to_place':
            if self._grasped_name(state) is None:
                return self._on_released(state)
            if self.blocked:
                self.stuck += 1
                if len(self.qpath) <= self.descent_len:
                    self.qpath = []
                elif self.stuck >= 3:
                    self._plan_place(state, replan=True)
            a = self._track(state)
            if a is not None:
                return a
            self.phase = 'open'
            return self._noop(1.0)

        if ph == 'open':
            if self._grasped_name(state) is None:
                return self._on_released(state)
            self.release_tries += 1
            tool = self._tool(state)[:3, 3]
            self._set_path(state, [tool - np.array([0, 0, 0.002])], self.wp_yaw, final_grip=1.0)
            self.descent_len = 2
            self.phase = 'to_place'
            if self.release_tries > 12:
                self.release_tries = 0
                self._plan_place(state, replan=True)
            a = self._track(state)
            return a if a is not None else self._noop(1.0)

        if ph == 'retreat':
            if self.blocked:
                self.stuck += 1
                if self.stuck >= 2:
                    self.qpath = []
            a = self._track(state)
            if a is not None:
                return a
            self._next_task(state)
            a = self._track(state) if self.phase == 'to_grasp' else None
            return a if a is not None else self._noop()

        return self._noop()

    def _on_grasped(self, state, g):
        self.grasp_attempt = 0
        if g != self.cur_obj:
            self.tasks.insert(0, (g, 'clear'))
            self.cur_obj = g
        self._plan_place(state)
        a = self._track(state)
        return a if a is not None else self._noop()

    def _on_released(self, state):
        self.release_tries = 0
        name, kind = self.tasks.pop(0) if self.tasks else (None, None)
        if kind == 'goal':
            self.phase = 'done'
            return self._noop()
        tool = self._tool(state)[:3, 3]
        self._set_path(state, [tool + np.array([0, 0, 0.03])], self.wp_yaw, flip=True)
        self.phase = 'retreat'
        a = self._track(state)
        return a if a is not None else self._noop()

    def _next_task(self, state):
        if self.tasks and self.tasks[0][1] == 'goal':
            for n in self._blocking_obstructions(state):
                if all(t[0] != n for t in self.tasks):
                    self.tasks.insert(0, (n, 'clear'))
        self._start_task(state)

    def _plan_place(self, state, replan=False):
        name = self.cur_obj
        p, qo, h = self._pose(state, name)
        r = self.robot
        tf = _T([state.get(r, 'grasp_tf_x'), state.get(r, 'grasp_tf_y'), state.get(r, 'grasp_tf_z')],
                [state.get(r, 'grasp_tf_qx'), state.get(r, 'grasp_tf_qy'), state.get(r, 'grasp_tf_qz'),
                 state.get(r, 'grasp_tf_qw')])
        kind = self.tasks[0][1] if self.tasks and self.tasks[0][0] == name else 'clear'
        Ttool_now = self._tool(state)
        hold_off = Ttool_now[2, 3] - (p[2] - h[2])   # tool height above held-object bottom
        yaw = np.arctan2(Ttool_now[1, 0], Ttool_now[0, 0])
        if kind == 'goal':
            rp, rh = self.region
            xy = rp[:2]
            surf = rp[2] + rh[2]
        else:
            xy = self._free_spot(state, name, yaw, hold_off)
            if replan:
                xy = xy + np.random.uniform(-0.03, 0.03, 2)
            surf = self.table_z
        Tobj = _T([xy[0], xy[1], surf + h[2] + 0.001], qo)
        Ttool = Tobj @ np.linalg.inv(tf)
        tgt = Ttool[:3, 3]
        tyaw = np.arctan2(Ttool[1, 0], Ttool[0, 0])
        zt = self._transit_z(state, hold_off, exclude=(name,))
        tool = Ttool_now[:3, 3]
        wps = []
        if tool[2] < zt - 0.005:
            wps.append(np.array([tool[0], tool[1], zt]))
        wps += [np.array([tgt[0], tgt[1], max(zt, tool[2]) if tool[2] < zt + 0.05 else zt]),
                np.array([tgt[0], tgt[1], tgt[2] + 0.015])]
        self._set_path(state, wps, tyaw)
        n_before = len(self.qpath)
        self._append_descent(state, tgt, tyaw)
        self.descent_len = len(self.qpath) - n_before + 2
        self.final_grip = 1.0
        self.phase = 'to_place'

    def _append_descent(self, state, tgt, yaw):
        base = self._base(state)
        qc = self.qpath[-1] if self.qpath else self._q(state)
        R = down_R(yaw)
        for dz in (0.008, 0.003, 0.0):
            qn, ok = tool_ik(qc, tgt + np.array([0, 0, dz]), R, base, iters=40)
            qn = qc + _wrap(qn - qc)
            self.qpath.append(qn)
            qc = qn
