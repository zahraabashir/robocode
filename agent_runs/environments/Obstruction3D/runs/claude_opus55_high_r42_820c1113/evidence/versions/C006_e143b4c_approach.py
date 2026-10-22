"""Obstruction3D approach: clear obstructions off the target region, then place
the target block on the region.  Uses a calibrated Kinova Gen3 FK/IK model
(see kin.py) and a Cartesian waypoint controller."""
import numpy as np
from kin import fk, ik, down_R, jac, rot_err

TABLE_Z = 0.075
TABLE_X = (0.10, 0.50)
TABLE_Y = (-0.40, 0.40)
SAFE_MARGIN = 0.03
VSTEP = 0.08
HSTEP = 0.10
GRASP_DZ = 0.028       # tool height above object top when closing
PLACE_EPS = 0.0015     # clearance above support surface when releasing
MAX_DQ = 0.2
JLIM = {1: 2.41, 3: 2.66, 5: 2.23}   # limited joints (0-indexed): 2,4,6 in 1-index


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space

    # ------------------------------------------------------------------ utils
    def _read(self, s):
        self.s = s
        self.R = s.get_object_from_name('robot')
        self.q = np.array([s.get(self.R, f'joint_{i}') for i in range(1, 8)])
        self.base = tuple(s.get(self.R, f) for f in ('pos_base_x', 'pos_base_y', 'pos_base_rot'))
        self.grasped = s.get(self.R, 'grasp_active') > 0.5
        self.objs = {}
        for n in s.get_object_names():
            if n == 'robot':
                continue
            o = s.get_object_from_name(n)
            try:
                p = np.array([s.get(o, f) for f in ('pose_x', 'pose_y', 'pose_z')])
                he = np.array([s.get(o, 'half_extent_' + c) for c in 'xyz'])
            except Exception:
                continue
            self.objs[n] = (p, he)

    def _obstructions(self):
        return sorted(n for n in self.objs if n not in ('target_block', 'target_region'))

    def reset(self, state, info):
        self._read(state)
        self.phase = 'plan'
        self.task = None
        self.path = []
        self.last_q = None
        self.last_cmd = None
        self.blocked = 0
        self.scale = 1.0
        self.fail = {}
        self.t = 0
        self.wait = 0

    # ------------------------------------------------------------ geometry
    def _final_block_xy(self):
        p, _ = self.objs['target_region']
        return p[:2].copy()

    def _needs_clearing(self, n):
        """Obstruction overlaps the target block's final footprint (+margin)."""
        rp, rhe = self.objs['target_region']
        bp, bhe = self.objs['target_block']
        p, he = self.objs[n]
        c = self._final_block_xy()
        m = 0.012
        ox = abs(p[0] - c[0]) < he[0] + bhe[0] + m
        oy = abs(p[1] - c[1]) < he[1] + bhe[1] + m
        # also anything touching the region itself
        rx = abs(p[0] - rp[0]) < he[0] + rhe[0] + 0.005
        ry = abs(p[1] - rp[1]) < he[1] + rhe[1] + 0.005
        return (ox and oy) or (rx and ry and p[2] - he[2] > rp[2])

    def _free_spot(self, name):
        """Pick a table location for obstruction `name` far from other stuff."""
        p0, he0 = self.objs[name]
        rp, rhe = self.objs['target_region']
        c = self._final_block_xy()
        best, bestv = None, -1e9
        r0 = max(he0[0], he0[1])
        for x in np.linspace(TABLE_X[0] + 0.07, TABLE_X[1] - 0.06, 11):
            for y in np.linspace(TABLE_Y[0] + 0.06, TABLE_Y[1] - 0.06, 17):
                clear = 1e9
                for n, (p, he) in self.objs.items():
                    if n == name:
                        continue
                    ext = he[:2].copy()
                    if n == 'target_region':
                        ext = ext + 0.03
                    dx = max(0.0, abs(x - p[0]) - ext[0] - r0)
                    dy = max(0.0, abs(y - p[1]) - ext[1] - r0)
                    clear = min(clear, np.hypot(dx, dy))
                dxy = abs(x - c[0]), abs(y - c[1])
                clear = min(clear, np.hypot(max(0, dxy[0] - 0.08), max(0, dxy[1] - 0.08)) + 0.02)
                for bad in self.fail.get(name, []):
                    if np.hypot(x - bad[0], y - bad[1]) < 0.05:
                        clear = -1
                v = min(clear, 0.08) - 0.05 * np.hypot(x - p0[0], y - p0[1])
                if v > bestv:
                    bestv, best = v, np.array([x, y])
        return best

    # ------------------------------------------------------------- planning
    def _plan_next(self):
        obs = [n for n in self._obstructions() if self._needs_clearing(n)]
        if obs:
            # clear the tallest / closest-to-center first
            c = self._final_block_xy()
            obs.sort(key=lambda n: np.hypot(*(self.objs[n][0][:2] - c)))
            n = obs[0]
            spot = self._free_spot(n)
            place_z = TABLE_Z
            self.task = dict(name=n, dest=spot, surf=place_z, yaw_dest=None)
        else:
            rp, rhe = self.objs['target_region']
            self.task = dict(name='target_block', dest=self._final_block_xy(),
                             surf=rp[2] + rhe[2], yaw_dest=None)
        n = self.task['name']
        p, he = self.objs[n]
        att = self.fail.get(('grasp', n), 0)
        self.task['yaw'] = self._choose_yaw(n, p[:2], p[2] + he[2] + GRASP_DZ - 0.05, att)
        self.task['yaw_place'] = self._match_yaw(self.task['yaw'], self._yaw_for(self.task['dest']))
        self.phase = 'to_pick'
        tool = fk(self.base, self.q)[:3, 3]
        sz = self._safe_z(None, 0.05)
        pick_above = np.array([p[0], p[1], sz])
        path = []
        if tool[2] < sz - 0.01:
            path += self._line(tool, np.array([tool[0], tool[1], sz]), VSTEP)
            tool = np.array([tool[0], tool[1], sz])
        path += self._line(tool, pick_above, HSTEP)
        path += self._line(pick_above, np.array([p[0], p[1], p[2] + he[2] + GRASP_DZ]), VSTEP)
        self._set_path(path, self.task['yaw'])

    def _footprint_hits(self, name, xy, yaw, bottom):
        """Count collisions of gripper footprint (at xy, yaw, lowest z=bottom) with other objects."""
        c, s_ = np.cos(yaw), np.sin(yaw)
        ax = np.array([c, s_]); ay = np.array([-s_, c])
        gx, gy = 0.065, 0.03
        hits = 0.0
        for n, (p, he) in self.objs.items():
            if n == name or n == 'target_region':
                continue
            if p[2] + he[2] < bottom:
                continue
            d = p[:2] - xy
            # SAT between rotated rect (gx,gy) and AABB he
            sep = False
            for axis, r1 in ((np.array([1.0, 0]), abs(ax[0]) * gx + abs(ay[0]) * gy),
                             (np.array([0, 1.0]), abs(ax[1]) * gx + abs(ay[1]) * gy)):
                if abs(d @ axis) > r1 + (he[0] if axis[0] else he[1]):
                    sep = True
            for axis, r1 in ((ax, gx), (ay, gy)):
                r2 = abs(axis[0]) * he[0] + abs(axis[1]) * he[1]
                if abs(d @ axis) > r1 + r2:
                    sep = True
            if not sep:
                hits += 1
        return hits

    def _choose_yaw(self, name, xy, bottom, attempt=0):
        """Object-axis-aligned yaw; fingers (tool x) along the smaller extent
        when possible, avoiding neighbours."""
        p, he = self.objs[name]
        rad = self._yaw_for(xy)
        cands = []
        for k in range(4):
            y = k * np.pi / 2
            finger_ext = he[0] if k % 2 == 0 else he[1]
            hits = self._footprint_hits(name, xy, y, bottom)
            dev = abs(wrap(y - rad))
            cands.append((hits * 10 + (finger_ext > 0.036) * 5 + finger_ext * 10 + 0.01 * dev, y))
        cands.sort()
        return cands[attempt % 4][1]

    def _yaw_for(self, xy):
        mx = self.base[0] + 0.12 * np.cos(self.base[2])
        my = self.base[1] + 0.12 * np.sin(self.base[2])
        return np.arctan2(xy[1] - my, xy[0] - mx)

    @staticmethod
    def _match_yaw(y0, ydes):
        # object must keep orientation up to pi
        k = np.round((ydes - y0) / np.pi)
        return y0 + k * np.pi

    def _safe_z(self, held, depth):
        top = TABLE_Z
        for n, (p, he) in self.objs.items():
            if n != held:
                top = max(top, p[2] + he[2])
        return max(top + depth + SAFE_MARGIN, 0.18)

    @staticmethod
    def _line(a, b, step):
        d = np.linalg.norm(b - a)
        n = max(1, int(np.ceil(d / step)))
        return [a + (b - a) * (i / n) for i in range(1, n + 1)]

    def _set_path(self, pts, yaw, yaw_end=None):
        if yaw_end is None:
            yaw_end = yaw
        n = len(pts)
        self.path = [(p, yaw + (yaw_end - yaw) * (i + 1) / n) for i, p in enumerate(pts)]

    # -------------------------------------------------------------- control
    def _ik(self, pos, yaw):
        q, err = ik(self.base, self.q, pos, down_R(yaw), iters=60)
        for i, lim in JLIM.items():
            q[i] = np.clip(q[i], -lim, lim)
        return q, err

    def _track(self):
        """Return joint delta toward current path, or None when path done."""
        while self.path:
            pos, yaw = self.path[0]
            M = fk(self.base, self.q)
            final = len(self.path) == 1
            tol = 5e-4 if final else 0.03
            e = np.linalg.norm(M[:3, 3] - pos)
            eo = np.linalg.norm(rot_err(M[:3, :3], down_R(yaw)))
            if e < tol and (eo < (0.01 if final else 0.1)):
                self.path.pop(0)
                continue
            qt, err = self._ik(pos, yaw)
            dq = qt - self.q
            m = np.max(np.abs(dq))
            if m > MAX_DQ:
                dq = dq * (MAX_DQ / m)
            return dq * self.scale
        return None

    def _act(self, dq=None, grip=0.0):
        a = np.zeros(11, dtype=np.float32)
        if dq is not None:
            a[3:10] = dq
        a[10] = grip
        self.last_q = self.q.copy()
        self.last_cmd = a.copy()
        return a

    def get_action(self, state):
        self._read(state)
        self.t += 1
        # detect blocked motion
        blocked = False
        if self.last_cmd is not None and np.max(np.abs(self.last_cmd[3:10])) > 1e-6:
            if np.allclose(self.q, self.last_q, atol=1e-7):
                blocked = True
        if self.last_cmd is not None and not blocked:
            self.scale = 1.0
        if blocked and self.scale > 1.0 / 16:
            self.scale *= 0.5
            blocked = False
        elif blocked:
            self.scale = 1.0
        self.last_cmd = None

        for _ in range(8):
            a = self._step_fsm(blocked)
            if a is not None:
                return a
            blocked = False
        return self._act()

    def _step_fsm(self, blocked):
        ph = self.phase
        if ph == 'plan':
            if self.grasped:
                # holding something unexpectedly: lower & release
                self.phase = 'release'
                return None
            self._plan_next()
            return None
        n = self.task['name']
        if ph == 'to_pick':
            if blocked:
                # blocked while approaching: close anyway if near, else lift
                self.phase = 'grasp'
                return None
            dq = self._track()
            if dq is None:
                self.phase = 'grasp'
                return None
            return self._act(dq)
        if ph == 'grasp':
            if self.grasped:
                self.phase = 'to_place'
                p, he = self.objs[n]
                tool = fk(self.base, self.q)[:3, 3]
                self.grasp_off = tool[2] - p[2]   # tool z above object center
                dest = self.task['dest']
                sz = self._safe_z(n, self.grasp_off + he[2])
                up = np.array([tool[0], tool[1], sz])
                above = np.array([dest[0], dest[1], sz])
                place = np.array([dest[0], dest[1], self.task['surf'] + he[2] + self.grasp_off + PLACE_EPS])
                pts = self._line(tool, up, VSTEP)
                pts2 = self._line(up, above, HSTEP)
                pts3 = self._line(above, place, VSTEP)
                y0, y1 = self.task['yaw'], self.task['yaw_place']
                self.path = [(p_, y0) for p_ in pts]
                k = len(pts2)
                self.path += [(p_, y0 + (y1 - y0) * (i + 1) / k) for i, p_ in enumerate(pts2)]
                self.path += [(p_, y1) for p_ in pts3]
                return None
            self.wait += 1
            if self.wait == 1:
                return self._act(grip=-1.0)
            self.wait = 0
            self.fail[('grasp', n)] = self.fail.get(('grasp', n), 0) + 1
            self.phase = 'plan'
            return None
        if ph == 'to_place':
            if not self.grasped:
                self.phase = 'plan'
                return None
            if blocked:
                self.phase = 'release'
                return None
            dq = self._track()
            if dq is None:
                self.phase = 'release'
                return None
            return self._act(dq)
        if ph == 'release':
            if not self.grasped:
                self.phase = 'retreat'
                tool = fk(self.base, self.q)[:3, 3]
                self.path = [(p_, self.task['yaw_place'] if self.task else 0.0)
                             for p_ in self._line(tool, np.array([tool[0], tool[1], tool[2] + 0.06]), 0.05)]
                self.wait = 0
                return None
            self.wait += 1
            if self.wait <= 2:
                return self._act(grip=1.0)
            # could not release: move down a little
            self.wait = 0
            tool = fk(self.base, self.q)[:3, 3]
            yaw = self.task['yaw_place'] if self.task else 0.0
            self.path = [(tool - np.array([0, 0, 0.003]), yaw)]
            dq = self._track()
            return self._act(dq, grip=1.0)
        if ph == 'retreat':
            dq = self._track()
            if dq is None or blocked:
                self.phase = 'plan'
                return None
            return self._act(dq)
        return self._act()
