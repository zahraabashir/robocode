import numpy as np
from kin import fk, ik, down_R

JF = ['joint_%d' % i for i in range(1, 8)]
TOOL = 0.12          # TCP offset along EE z (gripper centre)
MAXD = 0.19
SAFE_Z = 0.27        # TCP transit height
TABLE_Z = 0.075
X_RANGE = (0.12, 0.44)
FINGER_OFF = 0.052   # finger centre offset along EE x (open)
FINGER_HX = 0.011
FINGER_HY = 0.013
Y_RANGE = (-0.36, 0.36)


def _pose(s, o):
    return np.array([s.get(o, 'pose_x'), s.get(o, 'pose_y'), s.get(o, 'pose_z')])


def _he(s, o):
    return np.array([s.get(o, 'half_extent_x'), s.get(o, 'half_extent_y'), s.get(o, 'half_extent_z')])


def _quat_R(x, y, z, w):
    return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
                     [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
                     [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space

    def reset(self, state, info):
        self.queue = []
        self.qtarget = None
        self.cur = None
        self.last_q = None
        self.retries = 0
        self.grasp_fail = 0
        self.place_yaw = None

    def _robot(self, s):
        r = s.get_object_from_name('robot')
        q = np.array([s.get(r, f) for f in JF])
        base = (s.get(r, 'pos_base_x'), s.get(r, 'pos_base_y'), s.get(r, 'pos_base_rot'))
        return r, q, base

    # ------------------------------------------------------------------ planning
    def _overlaps(self, s, o, reg, margin=0.004):
        p, h = _pose(s, o), _he(s, o)
        rp, rh = _pose(s, reg), _he(s, reg)
        return (abs(p[0] - rp[0]) < h[0] + rh[0] + margin and
                abs(p[1] - rp[1]) < h[1] + rh[1] + margin)

    def _free_spot(self, s, obj, avoid, cur):
        h = _he(s, obj)
        best, bestscore = None, -1e9
        for x in np.linspace(X_RANGE[0], X_RANGE[1], 17):
            for y in np.linspace(Y_RANGE[0], Y_RANGE[1], 37):
                dmin = 1e9
                for o in avoid:
                    p, oh = _pose(s, o), _he(s, o)
                    dx = abs(x - p[0]) - (h[0] + oh[0])
                    dy = abs(y - p[1]) - (h[1] + oh[1])
                    dmin = min(dmin, max(dx, dy))
                score = min(dmin, 0.07) - 0.1 * np.hypot(x - cur[0], y - cur[1])
                if score > bestscore:
                    best, bestscore = (x, y), score
        return np.array(best)

    def _obj_yaw(self, s, o):
        R = _quat_R(*[s.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')])
        return np.arctan2(R[1, 0], R[0, 0])

    def _finger_clearance(self, s, obj, yaw, others):
        """Min clearance between finger boxes (at obj, given yaw) and other objects' footprints."""
        p = _pose(s, obj)
        c, sn = np.cos(yaw), np.sin(yaw)
        ax = np.array([c, sn]); ay = np.array([-sn, c])
        best = 1e9
        for o in others:
            op, oh = _pose(s, o), _he(s, o)
            if op[2] + oh[2] < p[2] - 0.035:   # below fingertips
                continue
            oyaw = self._obj_yaw(s, o)
            oc, os_ = np.cos(oyaw), np.sin(oyaw)
            corners = [op[:2] + sx * oh[0] * np.array([oc, os_]) + sy * oh[1] * np.array([-os_, oc])
                       for sx in (-1, 1) for sy in (-1, 1)]
            for side in (-1, 1):
                fc = p[:2] + side * FINGER_OFF * ax
                # separating-axis distance between finger rect and object rect
                d = -1e9
                for axis in (ax, ay, np.array([oc, os_]), np.array([-os_, oc])):
                    fr = FINGER_HX * abs(axis @ ax) + FINGER_HY * abs(axis @ ay)
                    pr = [axis @ (cc - fc) for cc in corners]
                    gap = max(min(pr) - fr, -fr - max(pr))
                    d = max(d, gap)
                best = min(best, d)
        return best

    def _grasp_yaw(self, s, obj, q, base, others, aligned_only):
        h = _he(s, obj)
        oyaw = self._obj_yaw(s, obj)
        M = fk(base, q, TOOL)
        cy = np.arctan2(M[1, 0], M[0, 0])
        steps = 4 if aligned_only else 24
        cands = []
        for k in range(steps):
            yaw = oyaw + k * (2 * np.pi / steps)
            rel = yaw - oyaw
            span = abs(np.cos(rel)) * h[0] + abs(np.sin(rel)) * h[1]
            if span > 0.041:
                continue
            clr = self._finger_clearance(s, obj, yaw, others)
            score = min(clr, 0.02) - 0.002 * abs(_wrap(yaw - cy)) - 0.01 * span \
                - (0.0 if abs(np.sin(2 * rel)) < 1e-6 else 0.005)
            cands.append((score, _wrap(yaw)))
        if not cands:
            yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
            return _wrap(yaw)
        cands.sort(reverse=True)
        idx = min(self.grasp_fail, len(cands) - 1)
        return cands[idx][1]

    def _plan_pick_place(self, s, obj, place_xy, support_top, others, place_yaw=None):
        _, q, base = self._robot(s)
        p = _pose(s, obj)
        h = _he(s, obj)
        yaw = self._grasp_yaw(s, obj, q, base, others, place_yaw is not None)
        self.place_yaw = place_yaw
        gz = p[2] + 0.035  # TCP height for grasp (object centre 2-5 cm below TCP works)
        place_center = np.array([place_xy[0], place_xy[1], support_top + h[2] + 0.002])
        return [
            ('move', np.array([p[0], p[1], max(SAFE_Z, gz + 0.05)]), yaw, False),
            ('move', np.array([p[0], p[1], gz]), yaw, True),
            ('close', obj.name),
            ('move', np.array([p[0], p[1], SAFE_Z]), yaw, False),
            ('place_move', place_center + np.array([0, 0, SAFE_Z - place_center[2]]), yaw, False),
            ('place_move', place_center + np.array([0, 0, 0.02]), yaw, False),
            ('place_move', place_center, yaw, True),
            ('open', place_center, yaw),
            ('move_rel_up', SAFE_Z, yaw),
        ]

    def _plan(self, s):
        reg = s.get_object_from_name('target_region')
        tb = s.get_object_from_name('target_block')
        _, q, base = self._robot(s)
        cur = fk(base, q, TOOL)[:3, 3]
        cubes = [s.get_object_from_name(n) for n in sorted(s.get_object_names())
                 if n.startswith('obstruction')]
        blocking = [o for o in cubes if self._overlaps(s, o, reg)]
        if blocking:
            # remove the tallest (top-most) first
            o = max(blocking, key=lambda c: _pose(s, c)[2] + _he(s, c)[2])
            others = [c for c in cubes if c.name != o.name] + [reg, tb]
            spot = self._free_spot(s, o, others, cur)
            return self._plan_pick_place(s, o, spot, TABLE_Z, others)
        rp = _pose(s, reg)
        others = cubes
        return self._plan_pick_place(s, tb, rp[:2], rp[2] + _he(s, reg)[2], others,
                                     place_yaw=self._obj_yaw(s, reg))

    # ------------------------------------------------------------------ execution
    def _tcp_target_for_block(self, s, center, yaw):
        """TCP position so that the held block's centre lands at `center`."""
        r = s.get_object_from_name('robot')
        t = np.array([s.get(r, 'grasp_tf_x'), s.get(r, 'grasp_tf_y'), s.get(r, 'grasp_tf_z')])
        return center - down_R(yaw) @ t

    def _resolve_place_yaw(self, s, yaw, cur_yaw):
        if self.place_yaw is None:
            return yaw
        r = s.get_object_from_name('robot')
        Rtf = _quat_R(*[s.get(r, f) for f in ('grasp_tf_qx', 'grasp_tf_qy', 'grasp_tf_qz', 'grasp_tf_qw')])
        Rb = down_R(0.0) @ Rtf
        rel = np.arctan2(Rb[1, 0], Rb[0, 0])
        y = self.place_yaw - rel
        # block symmetric under pi rotation: pick closest to current gripper yaw
        if abs(_wrap(y - cur_yaw)) > np.pi / 2:
            y += np.pi
        return _wrap(y)

    def get_action(self, s):
        for _ in range(20):
            a = self._step(s)
            if a is not None:
                return a
        return np.zeros(11, dtype=np.float32)

    def _step(self, s):
        a = np.zeros(11, dtype=np.float32)
        r, q, base = self._robot(s)
        grasping = s.get(r, 'grasp_active') > 0.5
        if grasping:
            a[10] = -1.0
        if not self.queue:
            self.queue = self._plan(s)
            self.qtarget = None
            self.last_q = None
        cmd = self.queue[0]
        kind = cmd[0]
        if kind == 'close':
            if grasping:
                self.queue.pop(0)
                self.retries = 0
                self.grasp_fail = 0
                return None
            self.retries += 1
            if self.retries > 2:
                # failed grasp: replan from scratch with another yaw
                self.retries = 0
                self.grasp_fail += 1
                self.queue = [('move_rel_up', SAFE_Z, None)]
                return None
            a[10] = -1.0
            return a
        if kind == 'open':
            if not grasping:
                self.queue.pop(0)
                self.retries = 0
                return None
            self.retries += 1
            if self.retries > 1:
                # lower a bit and try again
                self.retries = 0
                c = cmd[1] - np.array([0, 0, 0.002])
                self.queue[0] = ('open', c, cmd[2])
                self.queue.insert(0, ('place_move', c, cmd[2], True))
                return None
            a[10] = 1.0
            return a
        if self.qtarget is None:
            M = fk(base, q, TOOL)
            p0 = M[:3, 3].copy(); y0 = np.arctan2(M[1, 0], M[0, 0])
            if kind == 'move':
                pos, yaw = cmd[1], cmd[2]
            elif kind == 'place_move':
                yaw = self._resolve_place_yaw(s, cmd[2], y0)
                pos = self._tcp_target_for_block(s, cmd[1], yaw)
            elif kind == 'move_rel_up':
                pos = p0.copy(); pos[2] = max(pos[2], cmd[1])
                yaw = y0 if cmd[2] is None else cmd[2]
            dy = _wrap(yaw - y0)
            n = int(np.ceil(max(np.linalg.norm(pos - p0) / 0.01, abs(dy) / 0.1, 1)))
            path = []
            qc = q.copy()
            for i in range(1, n + 1):
                f = i / n
                qc, ok = ik(base, qc, p0 + f * (pos - p0), down_R(y0 + f * dy), tool=TOOL,
                            iters=100 if i < n else 300)
                path.append(qc.copy())
            self.qtarget = path
            self.pidx = 0
            self.last_q = None
        path = self.qtarget
        if np.max(np.abs(path[-1] - q)) < 1e-4:
            self.queue.pop(0)
            self.qtarget = None
            return None
        if self.last_q is not None and np.allclose(self.last_q, q, atol=1e-7):
            # previous action rejected (collision)
            allow = len(cmd) > 3 and cmd[3]
            self.queue.pop(0)
            self.qtarget = None
            if not allow:
                self.queue = [('move_rel_up', SAFE_Z + 0.03, None, True)]  # retreat, then replan
            return None
        # furthest waypoint reachable in one step
        k = self.pidx
        while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
            k += 1
        self.last_q = q.copy()
        self.pidx = k
        a[3:10] = np.clip(path[k] - q, -MAXD, MAXD)
        return a
