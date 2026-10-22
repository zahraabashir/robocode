import numpy as np
from kin import fk, ik, down_R

JF = ['joint_%d' % i for i in range(1, 8)]
MAXD = 0.19
SAFE_Z = 0.33       # EE transit height
GRASP_DZ = 0.14     # EE height above object center when grasping (calibrate)
TABLE_Z = 0.075


def _pose(s, o):
    return np.array([s.get(o, 'pose_x'), s.get(o, 'pose_y'), s.get(o, 'pose_z')])


def _he(s, o):
    return np.array([s.get(o, 'half_extent_x'), s.get(o, 'half_extent_y'), s.get(o, 'half_extent_z')])


def _yaw(s, o):
    qx, qy, qz, qw = [s.get(o, f) for f in ('pose_qx', 'pose_qy', 'pose_qz', 'pose_qw')]
    return np.arctan2(2 * (qw * qz + qx * qy), 1 - 2 * (qy * qy + qz * qz))


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space

    # ------------------------------------------------------------------
    def reset(self, state, info):
        self.queue = []       # list of ('move', pos, yaw) | ('grip', val, n)
        self.phase = 'plan'
        self.qtarget = None
        self.stuck = 0
        self.last_q = None

    def _robot(self, s):
        r = s.get_object_from_name('robot')
        q = np.array([s.get(r, f) for f in JF])
        base = (s.get(r, 'pos_base_x'), s.get(r, 'pos_base_y'), s.get(r, 'pos_base_rot'))
        return r, q, base

    # ------------------------------------------------------------------
    def _overlaps(self, s, o, reg):
        p, h = _pose(s, o), _he(s, o)
        rp, rh = _pose(s, reg), _he(s, reg)
        return (abs(p[0] - rp[0]) < h[0] + rh[0] + 0.005 and
                abs(p[1] - rp[1]) < h[1] + rh[1] + 0.005)

    def _free_spot(self, s, obj, avoid):
        """Find a free table spot for obj away from the objects in avoid."""
        h = _he(s, obj)
        best, bestd = None, -1
        for x in np.linspace(0.05, 0.35, 13):
            for y in np.linspace(-0.3, 0.3, 25):
                dmin = 1e9
                for o in avoid:
                    p, oh = _pose(s, o), _he(s, o)
                    dx = abs(x - p[0]) - (h[0] + oh[0])
                    dy = abs(y - p[1]) - (h[1] + oh[1])
                    dmin = min(dmin, max(dx, dy))
                if dmin > 0.06:
                    # prefer close to robot centre line
                    score = dmin - 0.2 * abs(y)
                    if best is None or score > bestd:
                        best, bestd = (x, y), score
                elif best is None and dmin > bestd:
                    bestd = dmin
                    best = (x, y)
        return np.array(best)

    def _plan_pick_place(self, s, obj, place_xy, place_z_center):
        p = _pose(s, obj)
        yaw = _yaw(s, obj)
        q = []
        q.append(('grip', 1.0, 1))
        q.append(('move', np.array([p[0], p[1], SAFE_Z]), yaw))
        q.append(('move', np.array([p[0], p[1], p[2] + GRASP_DZ]), yaw))
        q.append(('grip', -1.0, 2))
        q.append(('move', np.array([p[0], p[1], SAFE_Z]), yaw))
        q.append(('move', np.array([place_xy[0], place_xy[1], SAFE_Z]), yaw))
        q.append(('move', np.array([place_xy[0], place_xy[1], place_z_center + GRASP_DZ + 0.003]), yaw))
        q.append(('grip', 1.0, 2))
        q.append(('move', np.array([place_xy[0], place_xy[1], SAFE_Z]), yaw))
        return q

    def _plan(self, s):
        reg = s.get_object_from_name('target_region')
        tb = s.get_object_from_name('target_block')
        cubes = [s.get_object_from_name(n) for n in s.get_object_names()
                 if n.startswith('obstruction')]
        blocking = [o for o in cubes if self._overlaps(s, o, reg)]
        if blocking:
            o = blocking[0]
            others = [c for c in cubes if c.name != o.name] + [reg, tb]
            spot = self._free_spot(s, o, others)
            return self._plan_pick_place(s, o, spot, TABLE_Z + _he(s, o)[2])
        rp = _pose(s, reg)
        z = rp[2] + _he(s, reg)[2] + _he(s, tb)[2]
        return self._plan_pick_place(s, tb, rp[:2], z)

    # ------------------------------------------------------------------
    def get_action(self, s):
        a = np.zeros(11, dtype=np.float32)
        r, q, base = self._robot(s)
        if not self.queue:
            self.queue = self._plan(s)
            self.qtarget = None
        cmd = self.queue[0]
        if cmd[0] == 'grip':
            a[10] = cmd[1]
            n = cmd[2] - 1
            if n <= 0:
                self.queue.pop(0)
            else:
                self.queue[0] = ('grip', cmd[1], n)
            return a
        # move
        if self.qtarget is None:
            qt, ok = ik(base, q, cmd[1], down_R(cmd[2]))
            self.qtarget = qt
        d = self.qtarget - q
        if np.max(np.abs(d)) < 1e-4:
            self.queue.pop(0)
            self.qtarget = None
            return self.get_action(s) if self.queue else a
        a[3:10] = np.clip(d, -MAXD, MAXD)
        return a
