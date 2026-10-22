"""Fast geometry-based controller for the object-centric Rovers task."""

import heapq
import math
import numpy as np


SAMPLE = -5.0 / 6.0
CALIBRATE = -0.5
IMAGE = -1.0 / 6.0
NOOP = 1.0 / 6.0
SEND = 0.5
DROP = 5.0 / 6.0


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.space = observation_space
        self.types = {t.name: t for t in observation_space.types}

    def _objs(self, state, kind):
        return list(state.get_objects(self.types[kind]))

    @staticmethod
    def _name(obj):
        return obj.name

    def _v(self, state, obj, feat):
        return float(state.get(obj, feat))

    def _xy(self, state, obj):
        return (self._v(state, obj, "x"), self._v(state, obj, "y"))

    def reset(self, state, info):
        self.homes = {}
        rovers = sorted(self._objs(state, "rover"), key=self._name)
        for i, rover in enumerate(rovers):
            self.homes[i] = self._xy(state, rover)
        self.obstacles = []
        for ob in self._objs(state, "obstacle"):
            x, y = self._xy(state, ob)
            hx = self._v(state, ob, "half_x")
            hy = self._v(state, ob, "half_y")
            self.obstacles.append((x, y, hx, hy))
        samples = self._objs(state, "sample")
        stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
        soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
        self.sample_names = {
            0: self._closest_name(state, stones, self.homes[0]),
            1: self._closest_name(state, soils, self.homes[1]),
        }
        self.phase = ["sample", "sample"]
        self.targets = [None, None]
        self.paths = [[], []]
        self.last_pos = [self.homes[0], self.homes[1]]
        self.stuck = [0, 0]
        self.image_site_index = 0
        self.image_attempts = 0
        self.send_attempts = [0, 0]

    def _closest_name(self, state, objs, point):
        if not objs:
            return None
        return min(objs, key=lambda o: self._dist(self._xy(state, o), point)).name

    @staticmethod
    def _dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    def _blocked(self, p, extra=None, margin=0.27):
        x, y = p
        if x < -2.38 or x > 2.38 or y < -2.38 or y > 2.38:
            return True
        for ox, oy, hx, hy in self.obstacles:
            if abs(x - ox) <= hx + margin and abs(y - oy) <= hy + margin:
                return True
        if extra is not None and self._dist(p, extra) < 0.28:
            return True
        return False

    def _line_free(self, a, b, extra=None):
        d = self._dist(a, b)
        n = max(1, int(d / 0.08))
        for i in range(1, n + 1):
            q = (a[0] + (b[0] - a[0]) * i / n,
                 a[1] + (b[1] - a[1]) * i / n)
            if self._blocked(q, extra):
                return False
        return True

    def _plan(self, start, goal, extra=None):
        # A compact 0.1 m grid A*. Endpoints are connected separately so exact
        # sample and home coordinates remain attainable.
        res = 0.1
        lo = -2.4
        conv = lambda p: (int(round((p[0] - lo) / res)),
                          int(round((p[1] - lo) / res)))
        pos = lambda n: (lo + n[0] * res, lo + n[1] * res)
        s, g = conv(start), conv(goal)
        if self._line_free(start, goal, extra):
            return [goal]
        frontier = [(0.0, s)]
        came = {s: None}
        cost = {s: 0.0}
        moves = ((1, 0), (-1, 0), (0, 1), (0, -1),
                 (1, 1), (1, -1), (-1, 1), (-1, -1))
        found = None
        while frontier:
            _, cur = heapq.heappop(frontier)
            if cur == g or self._dist(pos(cur), goal) < 0.16:
                found = cur
                break
            for dx, dy in moves:
                nb = (cur[0] + dx, cur[1] + dy)
                q = pos(nb)
                if self._blocked(q, extra):
                    continue
                nc = cost[cur] + (1.414 if dx and dy else 1.0)
                if nc < cost.get(nb, 1e30):
                    cost[nb] = nc
                    came[nb] = cur
                    h = math.hypot(nb[0] - g[0], nb[1] - g[1])
                    heapq.heappush(frontier, (nc + h, nb))
        if found is None:
            return [goal]
        rev = []
        cur = found
        while cur != s:
            rev.append(pos(cur))
            cur = came[cur]
        rev.reverse()
        rev.append(goal)
        # String-pull the grid route to reduce action count.
        route = []
        anchor = start
        i = 0
        while i < len(rev):
            j = len(rev) - 1
            while j > i and not self._line_free(anchor, rev[j], extra):
                j -= 1
            route.append(rev[j])
            anchor = rev[j]
            i = j + 1
        return route

    def _move(self, idx, pos, goal, other):
        if self.targets[idx] != goal or not self.paths[idx] or self.stuck[idx] >= 2:
            self.targets[idx] = goal
            self.paths[idx] = self._plan(pos, goal, other)
            self.stuck[idx] = 0
        while self.paths[idx] and self._dist(pos, self.paths[idx][0]) < 0.075:
            self.paths[idx].pop(0)
        waypoint = self.paths[idx][0] if self.paths[idx] else goal
        dx = max(-0.2, min(0.2, waypoint[0] - pos[0]))
        dy = max(-0.2, min(0.2, waypoint[1] - pos[1]))
        return dx, dy

    def _objective_sites(self, state):
        objs = sorted(self._objs(state, "objective"), key=self._name)
        sites = []
        # South is normally shortest and clear of the mound row; alternate
        # directions handle pillars that happen to occlude a particular view.
        directions = ((0, -1), (1, 0), (-1, 0), (0, 1),
                      (0.707, -0.707), (-0.707, -0.707))
        for ob in objs:
            x, y = self._xy(state, ob)
            for ux, uy in directions:
                q = (x + 0.62 * ux, y + 0.62 * uy)
                if not self._blocked(q):
                    sites.append(q)
        return sites

    def _all_images_taken(self, state):
        return all(self._v(state, o, "have_image_rover0") > 0.5
                   for o in self._objs(state, "objective"))

    def _all_images_received(self, state):
        return all(self._v(state, o, "received_image") > 0.5
                   for o in self._objs(state, "objective"))

    def _sample_obj(self, state, idx):
        name = self.sample_names[idx]
        if name is None:
            return None
        return state.get_object_from_name(name)

    def _received_own_sample(self, state, idx):
        ob = self._sample_obj(state, idx)
        return ob is None or self._v(state, ob, "received_analysis") > 0.5

    def _set_op(self, action, idx, value):
        action[4 * idx + 3] = value

    def get_action(self, state):
        action = np.zeros(8, dtype=np.float32)
        action[3] = NOOP
        action[7] = NOOP
        rovers = sorted(self._objs(state, "rover"), key=self._name)
        positions = [self._xy(state, r) for r in rovers]

        for i in range(2):
            moved = self._dist(positions[i], self.last_pos[i])
            self.stuck[i] = self.stuck[i] + 1 if moved < 0.015 else 0
            self.last_pos[i] = positions[i]
            r = rovers[i]
            full = self._v(state, r, "store_full") > 0.5
            calibrated = self._v(state, r, "calibrated") > 0.5

            if self.phase[i] == "sample":
                sob = self._sample_obj(state, i)
                analyzed = sob is None or self._v(state, sob, "analyzed_rover%d" % i) > 0.5
                if analyzed:
                    self.phase[i] = "images" if i == 0 else "send"
                    self.targets[i] = None
                elif self._dist(positions[i], self._xy(state, sob)) <= 0.235:
                    self._set_op(action, i, SAMPLE)
                    continue
                else:
                    dx, dy = self._move(i, positions[i], self._xy(state, sob), positions[1-i])
                    action[4*i] = dx
                    action[4*i+1] = dy
                    continue

            if self.phase[i] == "images":
                if self._all_images_taken(state):
                    self.phase[i] = "send"
                    self.targets[i] = None
                else:
                    sites = self._objective_sites(state)
                    if not sites:
                        sites = [(0.0, 1.25)]
                    site = sites[self.image_site_index % len(sites)]
                    if self._dist(positions[i], site) > 0.12:
                        dx, dy = self._move(i, positions[i], site, positions[1-i])
                        action[4*i] = dx
                        action[4*i+1] = dy
                        continue
                    if calibrated:
                        self._set_op(action, i, IMAGE)
                    else:
                        self._set_op(action, i, CALIBRATE)
                    self.image_attempts += 1
                    if self.image_attempts >= 3:
                        self.image_attempts = 0
                        self.image_site_index += 1
                        self.targets[i] = None
                    continue

            if self.phase[i] == "send":
                need = (not self._received_own_sample(state, i) or
                        (i == 0 and not self._all_images_received(state)))
                if not need:
                    self.phase[i] = "drop"
                else:
                    lander = self._xy(state, self._objs(state, "lander")[0])
                    # Close, unobstructed points around the lander.
                    send_sites = [(lander[0] + 0.48, lander[1] + 0.15),
                                  (lander[0] + 0.15, lander[1] + 0.48),
                                  (lander[0] - 0.35, lander[1] + 0.25)]
                    site = send_sites[(self.send_attempts[i] // 2) % len(send_sites)]
                    if self._dist(positions[i], site) > 0.13:
                        dx, dy = self._move(i, positions[i], site, positions[1-i])
                        action[4*i] = dx
                        action[4*i+1] = dy
                        # Sending is cheap and may already be possible anywhere
                        # along the route (range is 4m), avoiding needless travel.
                        self._set_op(action, i, SEND)
                    else:
                        self._set_op(action, i, SEND)
                        self.send_attempts[i] += 1
                        if self.send_attempts[i] % 2 == 0:
                            self.targets[i] = None
                    continue

            if self.phase[i] == "drop":
                if full:
                    self._set_op(action, i, DROP)
                    continue
                self.phase[i] = "home"
                self.targets[i] = None

            if self.phase[i] == "home":
                if self._v(state, r, "at_home") < 0.5:
                    dx, dy = self._move(i, positions[i], self.homes[i], positions[1-i])
                    action[4*i] = dx
                    action[4*i+1] = dy
                continue

        return action
