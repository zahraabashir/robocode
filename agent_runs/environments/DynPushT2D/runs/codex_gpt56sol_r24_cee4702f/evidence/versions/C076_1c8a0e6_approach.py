import math
import heapq
import numpy as np


class GeneratedApproach:
    """Closed-loop contact controller for the asymmetric T pusher."""
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float)
        self.high = np.asarray(action_space.high, dtype=float)
        self.reset(None, None)

    def reset(self, state, info):
        self.mode = "choose"
        self.count = 0
        self.turn_sign = 1.0
        self.push_dir = np.array([1.0, 0.0])
        self.start_pose = np.zeros(3)
        self.nav = []
        self.rot_y = -0.7
        self.rot_cap = False
        self.cap_preferred = False
        self.line_offset = 0.0
        self.force_move = False
        self.start_pd = 0.0
        self.retreat_count = 0

    @staticmethod
    def _angle(x):
        return (x + math.pi) % (2.0 * math.pi) - math.pi

    @staticmethod
    def _world(local, theta):
        c, sn = math.cos(theta), math.sin(theta)
        return np.array([c*local[0] - sn*local[1], sn*local[0] + c*local[1]])

    def _safe(self, delta, speed=0.049):
        a = np.asarray(delta, dtype=float)
        n = float(np.linalg.norm(a))
        if n > speed:
            a *= speed / n
        return np.clip(a, self.low, self.high).astype(float)

    def _plan(self, start, target, obj, theta, width, lh, lv):
        """Small A* route for the robot centre around the expanded T."""
        lo, hi, res = 0.11, 4.89, 0.12
        n = int((hi-lo)/res) + 1
        c, sn = math.cos(theta), math.sin(theta)
        margin = 0.145
        def blocked(ix, iy):
            p = np.array([lo + ix*res, lo + iy*res]) - obj
            x, y = c*p[0] + sn*p[1], -sn*p[0] + c*p[1]
            bar = abs(x) < lh*0.5+margin and abs(y) < width*0.5+margin
            stem = abs(x) < width*0.5+margin and -lv-margin < y < width*0.5+margin
            return bar or stem
        def node(p):
            return (max(0, min(n-1, int(round((p[0]-lo)/res)))),
                    max(0, min(n-1, int(round((p[1]-lo)/res)))))
        st, gl = node(start), node(np.clip(target, lo, hi))
        # Pick a nearby free goal lattice point.
        if blocked(*gl):
            choices = [(i, j) for i in range(max(0,gl[0]-2),min(n,gl[0]+3))
                       for j in range(max(0,gl[1]-2),min(n,gl[1]+3)) if not blocked(i,j)]
            if choices:
                gl = min(choices, key=lambda q:(q[0]-gl[0])**2+(q[1]-gl[1])**2)
        heap = [(0.0, st)]
        cost, parent = {st: 0.0}, {}
        moves = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        while heap:
            _, cur = heapq.heappop(heap)
            if cur == gl:
                break
            for dx, dy in moves:
                q = (cur[0]+dx, cur[1]+dy)
                if not (0 <= q[0] < n and 0 <= q[1] < n) or (q != st and blocked(*q)):
                    continue
                if dx and dy and (blocked(cur[0]+dx, cur[1]) or blocked(cur[0], cur[1]+dy)):
                    continue
                nc = cost[cur] + math.hypot(dx,dy)
                if nc < cost.get(q, 1e30):
                    cost[q], parent[q] = nc, cur
                    h = math.hypot(q[0]-gl[0],q[1]-gl[1])
                    heapq.heappush(heap, (nc+h, q))
        if gl not in cost:
            return []
        path, q = [], gl
        while q != st:
            path.append(np.array([lo+q[0]*res, lo+q[1]*res]))
            q = parent[q]
        path.reverse()
        # Retain only turning points to reduce jitter.
        compact = []
        last_dir = None
        for i, p in enumerate(path):
            d = None if i+1 == len(path) else tuple(np.sign(path[i+1]-p))
            if i == 0 or d != last_dir:
                compact.append(p)
            last_dir = d
        compact.append(np.clip(target, lo, hi))
        return compact

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        obj, robot, goal = s[0:2], s[16:18], s[29:31]
        theta, goal_theta = float(s[2]), float(s[31])
        width, lh, lv = map(float, s[12:15])
        ae = self._angle(goal_theta - theta)
        dp = goal - obj
        pd = float(np.linalg.norm(dp))

        if self.mode == "choose":
            branch_mismatch = pd < 0.06 and abs(goal_theta-theta) > 0.14
            boundary_recover = min(obj) < 0.92 or max(obj) > 4.08
            if (abs(ae) > 0.11 or branch_mismatch) and not boundary_recover and not self.force_move:
                self.turn_sign = 1.0 if ae > 0.0 else -1.0
                self.mode = "rot_far"
                side = -self.turn_sign
                # Move the lever up the stem when the distal contact would
                # crowd a robot boundary.
                def lever_clear(frac):
                    pts = [np.array([side*(width*.5+.34), -frac*lv]),
                           np.array([side*(width*.5+.115), -frac*lv])]
                    world = [obj+self._world(p,theta) for p in pts]
                    return min(min(q[0]-.105,4.895-q[0],q[1]-.105,4.895-q[1]) for q in world)
                frac = max((0.80, 0.68, 0.56), key=lever_clear)
                if (frac < 0.60 and self.turn_sign > 0.0 and
                        (obj[1] < 1.30 or obj[1] > 3.70)):
                    self.cap_preferred = True
                stem_force_world = self._world(np.array([self.turn_sign, 0.0]), theta)
                # Stem-side and cap-end contacts create the same torque with
                # opposite linear components. Prefer the one that also moves
                # toward the goal instead of later undoing rotation drift.
                helps_position = float(np.dot(stem_force_world, dp)) >= -0.20*pd
                self.rot_cap = self.cap_preferred or not helps_position
                self.rot_y = -frac*lv
                if self.rot_cap:
                    far_local0 = np.array([self.turn_sign*(lh*.5+.34), 0.0])
                else:
                    far_local0 = np.array([side*(width*.5+.34), self.rot_y])
                far0 = obj + self._world(far_local0, theta)
                self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
            elif pd > 0.018:
                self.push_dir = dp / max(pd, 1e-9)
                self.mode = "move_far"
                self.start_pd = pd
                com0 = obj + self._world(np.array([0.0, -0.36*lv]), theta)
                com0 = com0 + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
                far0 = np.clip(com0 - self.push_dir*0.76, 0.105, 4.895)
                self.nav = self._plan(robot, far0, obj, theta, width, lh, lv)
                if pd < 0.15:
                    self.nav = []
            else:
                return np.zeros(2, dtype=float)
            self.count = 0
            self.start_pose = np.array([obj[0], obj[1], theta])

        if self.mode.startswith("rot"):
            # Distal-stem side contact is a reliable long rotation lever.
            side = -self.turn_sign
            if self.rot_cap:
                far_local = np.array([self.turn_sign*(lh*.5+.34), 0.0])
                contact_local = np.array([self.turn_sign*(lh*.5+.115), 0.0])
                local_force = np.array([-self.turn_sign, 0.0])
            else:
                far_local = np.array([side * (width * 0.5 + 0.34), self.rot_y])
                contact_local = np.array([side * (width * 0.5 + 0.115), self.rot_y])
                local_force = np.array([self.turn_sign, 0.0])
            far = obj + self._world(far_local, theta)
            contact = obj + self._world(contact_local, theta)
            force = self._world(local_force, theta)
            if self.mode == "rot_far":
                disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
                             abs(self._angle(theta-self.start_pose[2])) > 0.018)
                if disturbed:
                    self.mode, self.nav = "choose", []
                    return self._safe(robot-obj, 0.035)
                while self.nav and np.linalg.norm(robot-self.nav[0]) < 0.05:
                    self.nav.pop(0)
                if self.nav:
                    return self._safe(self.nav[0]-robot)
                if np.linalg.norm(robot - far) < 0.035:
                    self.mode = "rot_contact"
                return self._safe(far - robot)
            if self.mode == "rot_contact":
                if np.linalg.norm(robot - contact) < 0.018:
                    self.mode = "rot_push"
                    self.count = 0
                    self.start_pose = np.array([obj[0], obj[1], theta])
                    self.start_pd = pd
                return self._safe(contact - robot, 0.025)
            if self.mode == "rot_push":
                self.count += 1
                current_ae = self._angle(goal_theta - theta)
                turned = abs(self._angle(theta - self.start_pose[2]))
                crowded = min(obj) < 0.95 or max(obj) > 4.05
                edge_zone = min(obj) < 1.20 or max(obj) > 3.80
                turn_limit = 0.12 if crowded else (0.22 if edge_zone else 0.18)
                count_limit = 8 if crowded else (11 if edge_zone else 9)
                if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
                        or turned > turn_limit or self.count >= count_limit):
                    self.mode = "rot_retreat"
                speed = 0.014 if crowded else 0.022
                return self._safe(force, speed)
            if np.linalg.norm(robot - far) < 0.04:
                if pd > 0.30 and pd > self.start_pd + 0.18:
                    self.force_move = True
                self.mode = "choose"
            return self._safe(far - robot, 0.035)

        # The effective COM lies down the stem from the reported junction.
        com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
        com = com + np.array([-self.push_dir[1], self.push_dir[0]])*self.line_offset
        far = np.clip(com - self.push_dir * 0.76, 0.105, 4.895)
        if self.mode == "move_far":
            disturbed = (np.linalg.norm(obj-self.start_pose[:2]) > 0.012 or
                         abs(self._angle(theta-self.start_pose[2])) > 0.018)
            if disturbed:
                self.mode, self.nav = "choose", []
                return self._safe(robot-obj, 0.035)
            while self.nav and np.linalg.norm(robot - self.nav[0]) < 0.045:
                self.nav.pop(0)
            if self.nav:
                return self._safe(self.nav[0] - robot)
            if np.linalg.norm(robot - far) < 0.035:
                self.mode = "move_push"
                self.count = 0
                self.start_pose = np.array([obj[0], obj[1], theta])
            return self._safe(far - robot)
        if self.mode == "move_push":
            self.count += 1
            moved = float(np.linalg.norm(obj - self.start_pose[:2]))
            now_ae = abs(self._angle(goal_theta - theta))
            # Release immediately upon arrival or after crossing the goal;
            # another inward step can overshoot substantially under contact.
            if pd < 0.022 or np.dot(dp, self.push_dir) < 0.0:
                self.force_move = False
                self.mode = "move_retreat"
                self.retreat_count = 0
                return self._safe(-self.push_dir, 0.018)
            # Once contact is established, keep following through in short
            # closed-loop segments instead of paying to reacquire every time.
            near_boundary = min(obj) < 0.96 or max(obj) > 4.04
            if self.force_move and moved > 0.55:
                self.force_move = False
                self.mode = "move_retreat"
                self.retreat_count = 0
                return self._safe(-self.push_dir, 0.018)
            if (not self.force_move and moved > 0.11 and
                    (now_ae < 0.14 or near_boundary) and pd > 0.05):
                dtheta = self._angle(theta-self.start_pose[2])
                self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
                self.start_pose = np.array([obj[0], obj[1], theta])
                self.push_dir = dp / max(pd, 1e-9)
                self.count = 0
            elif self.count >= 60 or (now_ae > 0.13 and not near_boundary and not self.force_move):
                if moved > 0.02 and pd < 0.30:
                    dtheta = self._angle(theta-self.start_pose[2])
                    self.line_offset = float(np.clip(self.line_offset + 0.7*dtheta, -0.24, 0.24))
                self.mode = "move_retreat"
                self.retreat_count = 0
            speed = 0.016 if pd < 0.12 else (0.032 if pd > 0.55 else 0.024)
            return self._safe((com + self.push_dir * 0.20) - robot, speed)
        # Break contact along the exact reverse push direction. Recomputing a
        # COM-relative far point after the T rotates can route through the T.
        self.retreat_count += 1
        if self.retreat_count >= 8:
            self.mode = "choose"
        return self._safe(-self.push_dir, 0.035)
