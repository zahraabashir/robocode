import heapq
import math
import numpy as np


class GeneratedApproach:
    """Geometry-aware quasi-static manipulation of the T-shaped rigid body."""

    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float) + 1e-6
        self.high = np.asarray(action_space.high, dtype=float) - 1e-6

    @staticmethod
    def _wrap(a):
        return (a + math.pi) % (2.0 * math.pi) - math.pi

    @staticmethod
    def _rot(a):
        c, q = math.cos(a), math.sin(a)
        return np.array([[c, -q], [q, c]])

    def reset(self, state, info):
        self.mode = "idle"
        self.path = []
        self.next_mode = None
        self.force_local = np.zeros(2)
        self.push_start = None
        self.push_count = 0
        self.retreat_count = 0
        self.after_retreat = "idle"
        self.pair_sign = 0.0
        self.pair_start_theta = 0.0
        self.pair_amount = 0.0
        self.translate_amount = 0.0

    def _local_to_world(self, s, point):
        return s[0:2] + self._rot(float(s[2])).dot(np.asarray(point, dtype=float))

    def _world_to_local(self, s, point):
        return self._rot(-float(s[2])).dot(np.asarray(point, dtype=float) - s[0:2])

    def _blocked(self, s, world, margin=0.14):
        xw, yw = world
        if xw < 0.105 or xw > 4.895 or yw < 0.105 or yw > 4.895:
            return True
        x, y = self._world_to_local(s, world)
        w, lh, lv = float(s[12]), float(s[13]), float(s[14])
        bar = (-lh / 2 - margin <= x <= lh / 2 + margin and
               -w - margin <= y <= margin)
        stem = (-w / 2 - margin <= x <= w / 2 + margin and
                -w - lv - margin <= y <= -w + margin)
        return bar or stem

    def _plan(self, s, goal_local):
        """Small 4-neighbour A* around an inflated T and arena walls."""
        start = np.asarray(s[16:18], dtype=float)
        goal = self._local_to_world(s, goal_local)
        res = 0.10
        to_key = lambda p: (int(round((p[0] - 0.1) / res)),
                            int(round((p[1] - 0.1) / res)))
        to_pos = lambda k: np.array([0.1 + res * k[0], 0.1 + res * k[1]])
        sk, raw_gk = to_key(start), to_key(goal)
        candidates = []
        for radius in range(0, 5):
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if max(abs(dx), abs(dy)) != radius:
                        continue
                    k = (raw_gk[0] + dx, raw_gk[1] + dy)
                    p = to_pos(k)
                    if not self._blocked(s, p):
                        candidates.append((float(np.linalg.norm(p - goal)), k))
            if candidates:
                break
        if not candidates:
            return [goal]
        gk = min(candidates)[1]
        frontier = [(0.0, sk)]
        came = {sk: None}
        cost = {sk: 0.0}
        found = False
        while frontier and len(came) < 5000:
            _, cur = heapq.heappop(frontier)
            if cur == gk:
                found = True
                break
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt = (cur[0] + dx, cur[1] + dy)
                p = to_pos(nxt)
                if nxt != sk and self._blocked(s, p):
                    continue
                nc = cost[cur] + 1.0
                if nxt not in cost or nc < cost[nxt]:
                    cost[nxt] = nc
                    came[nxt] = cur
                    h = abs(nxt[0] - gk[0]) + abs(nxt[1] - gk[1])
                    heapq.heappush(frontier, (nc + h, nxt))
        if not found:
            return [goal]
        keys, cur = [], gk
        while cur is not None:
            keys.append(cur)
            cur = came[cur]
        keys.reverse()
        pts = [to_pos(k) for k in keys[1:]]
        compact = []
        for p in pts:
            if len(compact) >= 2:
                a, b = compact[-1] - compact[-2], p - compact[-1]
                if abs(a[0] * b[1] - a[1] * b[0]) < 1e-8:
                    compact[-1] = p
                    continue
            compact.append(p)
        compact.append(goal)
        return compact

    def _start_nav(self, s, target_local, next_mode, force_local):
        self.path = self._plan(s, target_local)
        self.next_mode = next_mode
        self.force_local = np.asarray(force_local, dtype=float)
        self.mode = "nav"

    def _begin_decision(self, s):
        angle_error = self._wrap(float(s[31] - s[2]))
        w, lh, lv = float(s[12]), float(s[13]), float(s[14])
        if abs(angle_error) > 0.065:
            self.pair_sign = 1.0 if angle_error > 0 else -1.0
            self.pair_start_theta = float(s[2])
            self.pair_amount = min(0.22, abs(angle_error))
            target = [self.pair_sign * 0.40 * lh, -w - 0.20]
            self._start_nav(s, target, "rot1", [0.0, 0.049])
            return

        delta_local = self._rot(-float(s[2])).dot(s[29:31] - s[0:2])
        axis = 0 if abs(delta_local[0]) >= abs(delta_local[1]) else 1
        component = float(delta_local[axis])
        if abs(component) < 0.016:
            axis = 1 - axis
            component = float(delta_local[axis])
        sign = 1.0 if component >= 0 else -1.0
        self.translate_amount = max(0.0, min(0.28, abs(component) - 0.010))
        if self.translate_amount <= 0.002:
            self.mode = "idle"
            return
        com_y = -(lh * w / 2.0 + lv * w + lv * lv / 2.0) / (lh + lv)
        if axis == 0:
            target = [-sign * (w / 2.0 + 0.20), com_y]
            force = [sign * 0.049, 0.0]
        elif sign > 0:
            target = [0.0, -w - lv - 0.20]
            force = [0.0, 0.049]
        else:
            target = [0.0, 0.20]
            force = [0.0, -0.049]
        self._start_nav(s, target, "translate", force)

    def _finish_push(self, next_after_retreat):
        self.mode = "retreat"
        self.retreat_count = 0
        self.after_retreat = next_after_retreat

    def _action(self, vec):
        return np.clip(np.asarray(vec, dtype=float), self.low, self.high)

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        if self.mode == "idle":
            self._begin_decision(s)

        if self.mode == "nav":
            robot = s[16:18]
            while self.path and np.linalg.norm(self.path[0] - robot) < 0.028:
                self.path.pop(0)
            if self.path:
                return self._action(self.path[0] - robot)
            self.mode = self.next_mode
            self.push_start = s.copy()
            self.push_count = 0

        if self.mode == "retreat":
            self.retreat_count += 1
            force_world = self._rot(float(s[2])).dot(self.force_local)
            if self.retreat_count >= 5:
                self.mode = self.after_retreat
                if self.mode == "rot2nav":
                    w, lh = float(s[12]), float(s[13])
                    target = [-self.pair_sign * 0.40 * lh, 0.20]
                    self._start_nav(s, target, "rot2", [0.0, -0.049])
                return np.zeros(2, dtype=float)
            return self._action(-force_world)

        if self.mode == "rot1":
            signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
            self.push_count += 1
            if signed >= 0.45 * self.pair_amount or self.push_count >= 14:
                self._finish_push("rot2nav")
                return np.zeros(2, dtype=float)
            return self._action(self._rot(float(s[2])).dot(self.force_local))

        if self.mode == "rot2":
            signed = self.pair_sign * self._wrap(float(s[2] - self.pair_start_theta))
            self.push_count += 1
            if signed >= 0.92 * self.pair_amount or self.push_count >= 14:
                self._finish_push("idle")
                return np.zeros(2, dtype=float)
            return self._action(self._rot(float(s[2])).dot(self.force_local))

        if self.mode == "translate":
            force_world = self._rot(float(self.push_start[2])).dot(self.force_local)
            direction = force_world / max(1e-9, np.linalg.norm(force_world))
            progress = float(np.dot(s[0:2] - self.push_start[0:2], direction))
            self.push_count += 1
            if progress >= self.translate_amount or self.push_count >= 18:
                self._finish_push("idle")
                return np.zeros(2, dtype=float)
            remaining = self.translate_amount - max(0.0, progress)
            scale = min(1.0, max(0.20, remaining / 0.06))
            return self._action(force_world * scale)

        return np.zeros(2, dtype=float)
