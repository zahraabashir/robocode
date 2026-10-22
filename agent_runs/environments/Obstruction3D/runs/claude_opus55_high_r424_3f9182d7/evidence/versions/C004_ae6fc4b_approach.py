import numpy as np
from kin import fk, ik, down_R

JF = ['joint_%d' % i for i in range(1, 8)]
TOOL = 0.12          # TCP offset along EE z (gripper centre)
MAXD = 0.19
SAFE_Z = 0.27        # TCP transit height
TABLE_Z = 0.075
X_RANGE = (0.12, 0.44)
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

    def _grasp_yaw(self, s, obj, q, base):
        h = _he(s, obj)
        R = _quat_R(*[s.get(obj, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')])
        oyaw = np.arctan2(R[1, 0], R[0, 0])
        # fingers close along EE x: span the smaller side
        yaw = oyaw if h[0] <= h[1] else oyaw + np.pi / 2
        # choose yaw or yaw+pi closest to current gripper yaw
        M = fk(base, q, TOOL)
        cy = np.arctan2(M[1, 0], M[0, 0])
        if abs(_wrap(yaw - cy)) > np.pi / 2:
            yaw += np.pi
        return _wrap(yaw)

    def _plan_pick_place(self, s, obj, place_xy, support_top):
        _, q, base = self._robot(s)
        p = _pose(s, obj)
        h = _he(s, obj)
        yaw = self._grasp_yaw(s, obj, q, base)
        gz = p[2] + min(0.03, h[2] + 0.005)  # TCP height for grasp
        gz = max(gz, 0.108)
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
            return self._plan_pick_place(s, o, spot, TABLE_Z)
        rp = _pose(s, reg)
        return self._plan_pick_place(s, tb, rp[:2], rp[2] + _he(s, reg)[2])

    # ------------------------------------------------------------------ execution
    def _tcp_target_for_block(self, s, center, yaw):
        """TCP position so that the held block's centre lands at `center`."""
        r = s.get_object_from_name('robot')
        t = np.array([s.get(r, 'grasp_tf_x'), s.get(r, 'grasp_tf_y'), s.get(r, 'grasp_tf_z')])
        return center - down_R(yaw) @ t

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
                return None
            self.retries += 1
            if self.retries > 3:
                # failed grasp: replan from scratch
                self.retries = 0
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
                pos, yaw = self._tcp_target_for_block(s, cmd[1], cmd[2]), cmd[2]
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
            self.last_q = None
        path = self.qtarget
        # drop waypoints already reached
        while len(path) > 1 and np.max(np.abs(path[0] - q)) < 1e-4:
            path.pop(0)
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
        k = 0
        while k + 1 < len(path) and np.max(np.abs(path[k + 1] - q)) <= MAXD:
            k += 1
        self.last_q = q.copy()
        a[3:10] = np.clip(path[k] - q, -MAXD, MAXD)
        return a
