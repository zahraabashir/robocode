import itertools
import numpy as np

H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
R_STEP = 2         # cells per step
IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
SAMP_R = 0.235     # sampling range (true 0.25)
SEND_R = 3.85      # send range (true ~4.0)
BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
        "send": 0.5, "drop": 5 / 6}
INF = 1e9


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def _type(space, name):
    for t in space.types:
        if t.name == name:
            return t
    return None


class Scene:
    def __init__(self, state, space):
        self.T = {n: _type(space, n) for n in ["rover", "lander", "objective", "sample", "obstacle"]}
        g = state.get
        self.rovers = sorted(state.get_objects(self.T["rover"]), key=lambda o: o.name)
        self.lander = state.get_objects(self.T["lander"])[0]
        self.objectives = sorted(state.get_objects(self.T["objective"]), key=lambda o: o.name)
        self.samples = sorted(state.get_objects(self.T["sample"]), key=lambda o: o.name)
        self.obstacles = state.get_objects(self.T["obstacle"])
        self.lpos = np.array([g(self.lander, "x"), g(self.lander, "y")])
        self.obs_boxes = []
        for o in self.obstacles:
            self.obs_boxes.append((g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z")))
        self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
        self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
        self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]


class RoverPlanner:
    """Lattice anchored at the rover's home; subset DP over task regions."""

    def __init__(self, scene, idx, home):
        self.scene = scene
        self.idx = idx
        self.home = np.array(home, dtype=float)
        side = 1.0 if home[0] > 0 else -1.0
        self.side = side
        self.img_r = IMG_R
        xs = []
        x = self.home[0]
        while x - H >= -2.27:
            x -= H
        while x <= 2.27:
            xs.append(x)
            x += H
        ys = []
        y = self.home[1]
        while y - H >= -2.27:
            y -= H
        while y <= 2.27:
            ys.append(y)
            y += H
        self.xs = np.array(xs)
        self.ys = np.array(ys)
        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
        self.X, self.Y = X, Y
        free = (np.abs(X) <= 2.265) & (np.abs(Y) <= 2.265) & (X * side >= 0.235)
        for (ox, oy, hx, hy, hz) in scene.obs_boxes:
            margin = 0.21 if max(hx, hy) >= 0.15 else 0.25
            dx = np.maximum(np.abs(X - ox) - hx, 0.0)
            dy = np.maximum(np.abs(Y - oy) - hy, 0.0)
            free &= (dx * dx + dy * dy) >= margin * margin
        lx, ly = scene.lpos
        free &= ~((X < lx + 0.71) & (Y < ly + 0.54))
        self.hi = int(np.argmin(np.abs(self.xs - self.home[0])))
        self.hj = int(np.argmin(np.abs(self.ys - self.home[1])))
        free[self.hi, self.hj] = True
        self.free = free
        self.shape = free.shape
        self.offsets = [(a, b) for a in range(-R_STEP, R_STEP + 1) for b in range(-R_STEP, R_STEP + 1)
                        if (a, b) != (0, 0)]

    def pos(self, c):
        return np.array([self.xs[c[0]], self.ys[c[1]]])

    def cell(self, p):
        i = int(np.argmin(np.abs(self.xs - p[0])))
        j = int(np.argmin(np.abs(self.ys - p[1])))
        return (i, j)

    def region_mask(self, task):
        kind, k = task
        sc = self.scene
        if kind == "obj":
            o = sc.opos[k]
            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= self.img_r ** 2
        else:  # 'stone' or 'soil'
            want_soil = kind == "soil"
            m = np.zeros(self.shape, bool)
            for s, soil in zip(sc.spos, sc.ssoil):
                if soil == want_soil:
                    m |= (self.X - s[0]) ** 2 + (self.Y - s[1]) ** 2 <= SAMP_R ** 2
        return m & self.free

    def propagate(self, F):
        G = F.copy()
        R = R_STEP
        W, Hh = self.shape
        free = self.free
        while True:
            P = np.full((W + 2 * R, Hh + 2 * R), INF)
            P[R:R + W, R:R + Hh] = G
            best = G.copy()
            for a, b in self.offsets:
                np.minimum(best, P[R + a:R + a + W, R + b:R + b + Hh] + 1.0, out=best)
            best[~free] = INF
            if np.array_equal(best, G):
                return G
            G = best

    def dp(self, tasks, start=None):
        """Returns dict subset(bitmask)->cost of tour start->tasks->home, and stores fields."""
        if start is None:
            start = (self.hi, self.hj)
        n = len(tasks)
        masks = [self.region_mask(t) for t in tasks]
        F0 = np.full(self.shape, INF)
        F0[start] = 0.0
        Fs = {0: F0}
        Gs = {}
        order = sorted(range(1 << n), key=lambda s: bin(s).count("1"))
        for s in order:
            F = Fs.get(s)
            if F is None:
                continue
            G = self.propagate(F)
            Gs[s] = G
            for r in range(n):
                if s & (1 << r):
                    continue
                if not masks[r].any():
                    continue
                s2 = s | (1 << r)
                cand = np.where(masks[r], G, INF)
                if s2 in Fs:
                    np.minimum(Fs[s2], cand, out=Fs[s2])
                else:
                    Fs[s2] = cand
        self._tasks = tasks
        self._masks = masks
        self._Fs = Fs
        self._Gs = Gs
        self._start = start
        costs = {}
        for s, G in Gs.items():
            costs[s] = G[self.hi, self.hj]
        return costs

    def extract(self, s):
        """Backtrack path for subset s (from last dp). Returns list of cells and visits dict idx->[tasks]."""
        Gs, Fs, masks = self._Gs, self._Fs, self._masks
        c = (self.hi, self.hj)
        v = Gs[s][c]
        rev = [c]
        rev_visits = []  # (position in rev, task index)
        W, Hh = self.shape
        guard = 0
        while True:
            guard += 1
            if guard > 10000:
                break
            if s == 0 and c == self._start:
                break
            # try region entry at c
            moved = False
            if s != 0 and Fs[s][c] <= v + 1e-9:
                for r in range(len(masks)):
                    if s & (1 << r) and masks[r][c]:
                        s2 = s & ~(1 << r)
                        if s2 in Gs and Gs[s2][c] <= v + 1e-9:
                            rev_visits.append((len(rev) - 1, r))
                            s = s2
                            moved = True
                            break
            if moved:
                continue
            for a, b in self.offsets:
                n = (c[0] + a, c[1] + b)
                if 0 <= n[0] < W and 0 <= n[1] < Hh and Gs[s][n] <= v - 1 + 1e-9:
                    c = n
                    v = Gs[s][n]
                    rev.append(c)
                    moved = True
                    break
            if not moved:
                break
        L = len(rev)
        path = rev[::-1]
        visits = {}
        for (ri, r) in rev_visits:
            visits.setdefault(L - 1 - ri, []).append(self._tasks[r])
        return path, visits


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.space = observation_space

    # ------------------------------------------------------------------
    def reset(self, state, info):
        self.sc = Scene(state, self.space)
        sc = self.sc
        g = state.get
        self.homes = [np.array([g(r, "x"), g(r, "y")]) for r in sc.rovers]
        self.home_th = [g(r, "theta") for r in sc.rovers]
        self.planners = [RoverPlanner(sc, i, self.homes[i]) for i in range(2)]
        nobj = len(sc.objectives)
        tasks = [("obj", k) for k in range(nobj)] + [("stone", 0), ("soil", 0)]
        self.tasks = tasks
        costs = []
        for i in range(2):
            costs.append(self.planners[i].dp(tasks))
        # store fields per rover (dp overwrote): re-run later for chosen subset
        n = len(tasks)
        full = (1 << n) - 1
        best = None
        for s0 in range(1 << n):
            s1 = full & ~s0
            c0 = costs[0].get(s0, INF)
            c1 = costs[1].get(s1, INF)
            if c0 >= INF or c1 >= INF:
                continue
            ops0 = self._ops(tasks, s0)
            ops1 = self._ops(tasks, s1)
            k0 = max(c0, ops0) + 0.5 * self._extra(tasks, s0)
            k1 = max(c1, ops1) + 0.5 * self._extra(tasks, s1)
            key = (max(k0, k1), k0 + k1)
            if best is None or key < best[0]:
                best = (key, s0, s1)
        self.assign = [best[1], best[2]] if best else [full, 0]
        self.plans = []
        for i in range(2):
            p = self.planners[i]
            p.dp(tasks)
            path, visits = p.extract(self.assign[i])
            self.plans.append({"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0})
        self.my_tasks = [[tasks[r] for r in range(n) if self.assign[i] & (1 << r)] for i in range(2)]
        self.last_target = [None, None]

    def _ops(self, tasks, s):
        c = 0
        for r, t in enumerate(tasks):
            if s & (1 << r):
                c += 2 if t[0] == "obj" else 2
        return c + 1

    def _extra(self, tasks, s):
        return 0

    # ------------------------------------------------------------------
    def _task_done(self, state, t):
        sc = self.sc
        g = state.get
        if t[0] == "obj":
            o = sc.objectives[t[1]]
            return g(o, "have_image_rover0") > 0.5 or g(o, "have_image_rover1") > 0.5 or g(o, "received_image") > 0.5
        want_soil = t[0] == "soil"
        for s, soil in zip(sc.samples, sc.ssoil):
            if soil == want_soil and (g(s, "analyzed_rover0") > 0.5 or g(s, "analyzed_rover1") > 0.5
                                      or g(s, "received_analysis") > 0.5):
                return True
        return False

    # ---------------- visibility models ----------------
    def _pillars(self):
        return [(b[0], b[1]) for b in self.sc.obs_boxes if max(b[2], b[3]) < 0.15]

    @staticmethod
    def _seg_dist(p, a, b):
        ab = b - a
        t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
        return np.linalg.norm(a + t * ab - p)

    def _visible(self, p, th, k, margin=0.03):
        c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
        o = self.sc.opos[k]
        v = o - c
        if np.linalg.norm(v) > 1.9972 - margin:
            return False, np.linalg.norm(v)
        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
        if ang < np.radians(108):
            for pc in self._pillars():
                if self._seg_dist(np.array(pc), c, o) < 0.11:
                    return False, np.linalg.norm(v)
        return True, np.linalg.norm(v)

    def _can_send(self, state, i, p, th):
        sc = self.sc
        v = sc.lpos - p
        d = np.linalg.norm(v)
        if d > SEND_R:
            return False
        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
        if ang >= np.radians(115):
            return True
        g = state.get
        orv = sc.rovers[1 - i]
        op = np.array([g(orv, "x"), g(orv, "y")])
        if self._seg_dist(op, p, sc.lpos) < 0.27:
            return False
        for pc in self._pillars():
            if self._seg_dist(np.array(pc), p, sc.lpos) < 0.13:
                return False
        return True

    def _choose_op(self, state, i, p, th):
        sc = self.sc
        g = state.get
        rv = sc.rovers[i]
        me = "rover%d" % i
        store_full = g(rv, "store_full") > 0.5
        calibrated = g(rv, "calibrated") > 0.5
        # sample
        if not store_full:
            for s, soil, sp in zip(sc.samples, sc.ssoil, sc.spos):
                if np.linalg.norm(sp - p) <= SAMP_R:
                    t = ("soil", 0) if soil else ("stone", 0)
                    if not self._task_done(state, t):
                        return "sample"
        # imaging
        nobj = len(sc.objectives)
        vis = {}
        for k in range(nobj):
            ok, d = self._visible(p, th, k)
            if ok:
                vis[k] = d
        need = [k for k in range(nobj) if not self._task_done(state, ("obj", k))]
        if any(k in vis for k in need):
            if calibrated:
                cands = [k for k in vis if g(sc.objectives[k], "have_image_" + me) < 0.5]
                if cands:
                    kbest = min(cands, key=lambda k: vis[k])
                    if kbest in need:
                        return "image"
            else:
                return "calibrate"
        mine_left = [t for t in self.my_tasks[i] if t[0] == "obj" and not self._task_done(state, t)]
        if not calibrated and mine_left and vis:
            return "calibrate"
        if store_full:
            return "drop"
        all_done = all(self._task_done(state, t) for t in self.my_tasks[i])
        holding = False
        for o in sc.objectives:
            if g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5:
                holding = True
        for s in sc.samples:
            if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
                holding = True
        if holding and all_done and self._can_send(state, i, p, th):
            return "send"
        return "noop"

    def _desired_heading(self, state, i, p, k):
        """Face away from the next objective still to image on my path; else away from lander."""
        sc = self.sc
        plan = self.plans[i]
        visits = plan["visits"]
        for idx in sorted(visits):
            if idx < k:
                continue
            for t in visits[idx]:
                if t[0] == "obj" and not self._task_done(state, t):
                    v = p - sc.opos[t[1]]
                    return np.arctan2(v[1], v[0])
        # any of my objectives left (e.g. skipped)
        for t in self.my_tasks[i]:
            if t[0] == "obj" and not self._task_done(state, t):
                v = p - sc.opos[t[1]]
                return np.arctan2(v[1], v[0])
        # images done: head back to home heading unless stuck at home without having sent
        g = state.get
        me = "rover%d" % i
        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
        if holding and k >= len(plan["path"]) - 1:
            v = p - sc.lpos
            away = np.arctan2(v[1], v[0])
            # heading within the send cone (+-60 deg of away) closest to home heading
            dlt = float(np.clip(_wrap(self.home_th[i] - away), -np.radians(60), np.radians(60)))
            return away + dlt
        return self.home_th[i]

    def _rover_action(self, state, i):
        sc = self.sc
        g = state.get
        rv = sc.rovers[i]
        cur = np.array([g(rv, "x"), g(rv, "y")])
        th = g(rv, "theta")
        plan = self.plans[i]
        P = self.planners[i]
        k = plan["k"]
        exp = P.pos(plan["path"][k])
        if np.linalg.norm(exp - cur) > 0.02:
            plan["stuck"] += 1
            if k > 0 and np.linalg.norm(P.pos(plan["path"][k - 1]) - cur) < 0.02 and plan["stuck"] <= 3:
                k = k - 1
                plan["k"] = k
            else:
                self._replan(state, i, cur)
                plan = self.plans[i]
                k = plan["k"]
        else:
            plan["stuck"] = 0
        path = plan["path"]
        stay = False
        vt = plan["visits"].get(k, [])
        for t in vt:
            if not self._task_done(state, t) and plan["wait"] < 10:
                stay = True
        if k >= len(path) - 1:
            stay = True
            # path finished but my tasks undone -> replan
            rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
            if rem and plan["wait"] >= 10:
                self._replan(state, i, cur, shrink=True)
                plan = self.plans[i]
                path = plan["path"]
                k = plan["k"]
                stay = len(path) <= 1
        if stay:
            plan["wait"] += 1
            nxt = k
        else:
            plan["wait"] = 0
            nxt = k + 1
        target = P.pos(path[nxt])
        d = np.clip(target - cur, -0.2, 0.2)
        newp = cur + d
        dth_des = _wrap(self._desired_heading(state, i, newp, nxt) - th)
        dth = float(np.clip(dth_des, -0.4, 0.4))
        newth = _wrap(th + dth)
        op = self._choose_op(state, i, newp, newth)
        plan["k"] = nxt
        return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)

    def _replan(self, state, i, cur, shrink=False):
        P = self.planners[i]
        if shrink:
            P.img_r = max(1.6, P.img_r - 0.1)
        rem = [t for t in self.my_tasks[i] if not self._task_done(state, t)]
        start = P.cell(cur)
        P.free[start] = True
        costs = P.dp(rem, start=start)
        path, visits = P.extract((1 << len(rem)) - 1)
        self.plans[i] = {"path": path, "visits": visits, "k": 0, "wait": 0, "stuck": 0}

    def get_action(self, state):
        a0 = self._rover_action(state, 0)
        a1 = self._rover_action(state, 1)
        return np.concatenate([a0, a1]).astype(np.float32)
