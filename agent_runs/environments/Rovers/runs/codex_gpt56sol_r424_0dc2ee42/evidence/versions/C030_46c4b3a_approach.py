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
        # The fixed separating wall is part of the arena but omitted from the
        # object list.  Treat it as a full-height divider: all useful tasks have
        # a reachable stance on their own side.
        self.obstacles.append((0.0, 0.0, 0.18, 2.6))
        self.lander_xy = self._xy(state, self._objs(state, "lander")[0])
        self.obstacles.append((self.lander_xy[0], self.lander_xy[1], 0.30, 0.22))
        samples = self._objs(state, "sample")
        stones = [s for s in samples if self._v(state, s, "is_soil") < 0.5]
        soils = [s for s in samples if self._v(state, s, "is_soil") > 0.5]
        def feasible(items, idx):
            # A sample near the wall can be reached from a stance at x=+/-0.43.
            result = [s for s in items if
                      (self._v(state, s, "x") >= 0.18 if idx == 0
                       else self._v(state, s, "x") <= -0.18)]
            away = [s for s in result if self._dist(
                self._xy(state, s), self.lander_xy) > 0.62]
            return away or result
        self.sample_queues = [[], []]
        # Assign each required type independently. Some layouts put both types
        # on one side, in which case one rover collects two samples sequentially.
        for items in (stones, soils):
            options = []
            for i in range(2):
                reachable = feasible(items, i)
                if reachable:
                    ob = min(reachable, key=lambda s: self._dist(
                        self._xy(state, s), self.homes[i]))
                    options.append((self._dist(self._xy(state, ob), self.homes[i]), i, ob))
            if options:
                _, owner, ob = min(options, key=lambda x: x[0])
                self.sample_queues[owner].append(ob.name)
        self.sample_index = [0, 0]
        self.phase = ["sample", "sample"]
        self.targets = [None, None]
        self.paths = [[], []]
        self.last_pos = [self.homes[0], self.homes[1]]
        self.stuck = [0, 0]
        self.image_site_index = [0, 0]
        self.image_attempts = [0, 0]
        self.send_attempts = [0, 0]

    def _closest_name(self, state, objs, point):
        if not objs:
            return None
        return min(objs, key=lambda o: self._dist(self._xy(state, o), point)).name

    @staticmethod
    def _dist(a, b):
        return math.hypot(a[0] - b[0], a[1] - b[1])

    def _blocked(self, p, extra=None, margin=0.20):
        x, y = p
        if x < -2.25 or x > 2.25 or y < -2.25 or y > 2.25:
            return True
        for ox, oy, hx, hy in self.obstacles:
            if abs(x - ox) <= hx + margin and abs(y - oy) <= hy + margin:
                return True
        if extra is not None and self._dist(p, extra) < 0.28:
            return True
        return False

    def _line_free(self, a, b, extra=None, margin=0.20):
        d = self._dist(a, b)
        n = max(1, int(d / 0.08))
        for i in range(1, n + 1):
            q = (a[0] + (b[0] - a[0]) * i / n,
                 a[1] + (b[1] - a[1]) * i / n)
            if self._blocked(q, extra, margin):
                return False
        return True

    def _plan(self, start, goal, extra=None):
        route = self._plan_with_margin(start, goal, extra, 0.21)
        if route is None:
            route = self._plan_with_margin(start, goal, extra, 0.195)
        return route if route is not None else [goal]

    def _plan_with_margin(self, start, goal, extra, margin):
        # A compact 0.1 m grid A*. Endpoints are connected separately so exact
        # sample and home coordinates remain attainable.
        res = 0.05
        lo = -2.4
        conv = lambda p: (int(round((p[0] - lo) / res)),
                          int(round((p[1] - lo) / res)))
        pos = lambda n: (lo + n[0] * res, lo + n[1] * res)
        s, g = conv(start), conv(goal)
        if self._line_free(start, goal, extra, margin):
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
                if self._blocked(q, extra, margin):
                    continue
                nc = cost[cur] + (1.414 if dx and dy else 1.0)
                if nc < cost.get(nb, 1e30):
                    cost[nb] = nc
                    came[nb] = cur
                    h = math.hypot(nb[0] - g[0], nb[1] - g[1])
                    heapq.heappush(frontier, (nc + h, nb))
        if found is None:
            return None
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
            while j > i and not self._line_free(anchor, rev[j], extra, margin):
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
        vx = waypoint[0] - pos[0]
        vy = waypoint[1] - pos[1]
        scale = min(1.0, 0.2 / max(abs(vx), abs(vy), 1e-9))
        dx = vx * scale
        dy = vy * scale
        return dx, dy

    def _objective_sites(self, state, idx):
        objs = sorted(self._objs(state, "objective"), key=self._name)
        objs = [o for o in objs if not self._image_done(state, o) and
                ((self._v(state, o, "x") >= 0) == (idx == 0))]
        sites = []
        # South is normally shortest and clear of the mound row; alternate
        # directions handle pillars that happen to occlude a particular view.
        directions = ((0, -1), (1, 0), (-1, 0), (0, 1),
                      (0.707, -0.707), (-0.707, -0.707))
        for ob in objs:
            x, y = self._xy(state, ob)
            for radius in (0.75, 1.0, 1.3):
                for ux, uy in directions:
                    q = (x + radius * ux, y + radius * uy)
                    if not self._blocked(q) and ((q[0] > 0) == (idx == 0)):
                        sites.append(q)
        return sites

    def _image_done(self, state, ob):
        return (self._v(state, ob, "received_image") > 0.5 or
                self._v(state, ob, "have_image_rover0") > 0.5 or
                self._v(state, ob, "have_image_rover1") > 0.5)

    def _side_images_done(self, state, idx):
        side = [o for o in self._objs(state, "objective")
                if ((self._v(state, o, "x") >= 0) == (idx == 0))]
        return all(self._image_done(state, o) for o in side)

    def _own_images_received(self, state, idx):
        own = "have_image_rover%d" % idx
        return all(self._v(state, o, own) < 0.5 or
                   self._v(state, o, "received_image") > 0.5
                   for o in self._objs(state, "objective"))

    def _all_images_received(self, state):
        return all(self._v(state, o, "received_image") > 0.5
                   for o in self._objs(state, "objective"))

    def _sample_obj(self, state, idx):
        if self.sample_index[idx] >= len(self.sample_queues[idx]):
            return None
        name = self.sample_queues[idx][self.sample_index[idx]]
        return state.get_object_from_name(name)

    @staticmethod
    def _same_side_goal(point, idx):
        x, y = point
        if idx == 0 and x < 0.43:
            x = 0.43
        if idx == 1 and x > -0.43:
            x = -0.43
        x = max(-2.25, min(2.25, x))
        y = max(-2.25, min(2.25, y))
        return (x, y)

    def _sample_goal(self, state, sample, idx, rover_pos):
        sx, sy = self._xy(state, sample)
        candidates = []
        for radius in (0.0, 0.20, 0.24):
            count = 1 if radius == 0 else 16
            for k in range(count):
                angle = 2.0 * math.pi * k / count
                q = (sx + radius * math.cos(angle),
                     sy + radius * math.sin(angle))
                q = self._same_side_goal(q, idx)
                if self._dist(q, (sx, sy)) <= 0.245 and not self._blocked(q):
                    # Strongly prefer a stance away from the collidable lander.
                    lander_penalty = max(0.0, 0.55 - self._dist(q, self.lander_xy)) * 20.0
                    candidates.append((self._dist(q, rover_pos) + lander_penalty, q))
        if candidates:
            return min(candidates, key=lambda x: x[0])[1]
        return self._same_side_goal((sx, sy), idx)

    def _received_own_sample(self, state, idx):
        return all(self._v(state, state.get_object_from_name(name),
                           "received_analysis") > 0.5
                   for name in self.sample_queues[idx])

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
                    if full:
                        self._set_op(action, i, DROP)
                        continue
                    if sob is not None:
                        self.sample_index[i] += 1
                        self.targets[i] = None
                    if self._sample_obj(state, i) is None:
                        self.phase[i] = "images"
                        self.targets[i] = None
                elif self._dist(positions[i], self._xy(state, sob)) <= 0.2495:
                    self._set_op(action, i, SAMPLE)
                    continue
                else:
                    goal = self._sample_goal(state, sob, i, positions[i])
                    dx, dy = self._move(i, positions[i], goal, positions[1-i])
                    action[4*i] = dx
                    action[4*i+1] = dy
                    continue

            if self.phase[i] == "images":
                if self._side_images_done(state, i):
                    self.phase[i] = "send"
                    self.targets[i] = None
                else:
                    sites = self._objective_sites(state, i)
                    if not sites:
                        sites = [(0.0, 1.25)]
                    site = sites[self.image_site_index[i] % len(sites)]
                    if self._dist(positions[i], site) > 0.12:
                        dx, dy = self._move(i, positions[i], site, positions[1-i])
                        action[4*i] = dx
                        action[4*i+1] = dy
                        continue
                    if calibrated:
                        self._set_op(action, i, IMAGE)
                    else:
                        self._set_op(action, i, CALIBRATE)
                    self.image_attempts[i] += 1
                    if self.image_attempts[i] >= 3:
                        self.image_attempts[i] = 0
                        self.image_site_index[i] += 1
                        self.targets[i] = None
                    continue

            if self.phase[i] == "send":
                need = (not self._received_own_sample(state, i) or
                        not self._own_images_received(state, i))
                if not need:
                    self.phase[i] = "drop"
                else:
                    lander = self._xy(state, self._objs(state, "lander")[0])
                    # Close, unobstructed points around the lander.
                    if i == 0:
                        send_sites = [(0.43, -1.95), (0.43, -2.15)]
                    else:
                        send_sites = [(-1.2, -1.8), (-1.45, -1.65)]
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
