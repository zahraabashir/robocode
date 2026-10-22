import itertools
import numpy as np

H = 0.1            # lattice spacing (a step can move up to 2 cells per axis)
R_STEP = 2         # cells per step
IMG_R = 1.96       # imaging range (true ~2.0)
SAMP_R = 0.235     # sampling range (true 0.25)
SEND_R = 3.85      # send range (true ~4.0)
BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
        "send": 0.5, "drop": 5 / 6}
INF = 1e9


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
            m = (self.X - o[0]) ** 2 + (self.Y - o[1]) ** 2 <= IMG_R ** 2
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

    def _choose_op(self, state, i, p, at_visit_tasks):
        sc = self.sc
        g = state.get
        rv = sc.rovers[i]
        me = "rover%d" % i
        other = "rover%d" % (1 - i)
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
        visible = [k for k in range(len(sc.objectives)) if np.linalg.norm(sc.opos[k] - p) <= IMG_R]
        need = [k for k in range(len(sc.objectives)) if not self._task_done(state, ("obj", k))]
        vis_need = [k for k in visible if k in need]
        if vis_need:
            if calibrated:
                cands = [k for k in visible if g(sc.objectives[k], "have_image_" + me) < 0.5]
                if cands:
                    return "image"
            else:
                return "calibrate"
        # calibrate early if I still have images to take and something is visible
        mine_left = [t for t in self.my_tasks[i] if t[0] == "obj" and not self._task_done(state, t)]
        if not calibrated and mine_left and any(
                np.linalg.norm(sc.opos[k] - p) <= IMG_R for k in range(len(sc.objectives))):
            return "calibrate"
        if store_full:
            # is my store's analysis already recorded? (store full => yes)
            return "drop"
        # send
        all_done = all(self._task_done(state, t) for t in self.my_tasks[i])
        holding = False
        for o in sc.objectives:
            if g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5:
                holding = True
        for s in sc.samples:
            if g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5:
                holding = True
        if holding and all_done and np.linalg.norm(p - sc.lpos) <= SEND_R:
            return "send"
        return "noop"

    def _rover_action(self, state, i):
        sc = self.sc
        g = state.get
        rv = sc.rovers[i]
        cur = np.array([g(rv, "x"), g(rv, "y")])
        plan = self.plans[i]
        path = plan["path"]
        P = self.planners[i]
        k = plan["k"]
        # verify position
        exp = P.pos(path[k])
        if np.linalg.norm(exp - cur) > 0.02:
            # previous move blocked or drifted; find closest path index or stay
            plan["stuck"] += 1
            if plan["stuck"] > 3:
                self._replan(state, i, cur)
                plan = self.plans[i]
                path = plan["path"]
                k = plan["k"]
            else:
                # step back on k to retry previous move
                if k > 0 and np.linalg.norm(P.pos(path[k - 1]) - cur) < 0.02:
                    k = k - 1
                    plan["k"] = k
        # decide whether to stay at current index
        stay = False
        vt = plan["visits"].get(k, [])
        for t in vt:
            if not self._task_done(state, t) and plan["wait"] < 12:
                stay = True
        if k >= len(path) - 1:
            stay = True
        if stay:
            plan["wait"] += 1
            nxt = k
        else:
            plan["wait"] = 0
            nxt = k + 1
            # don't leave if next index arrival leaves region needed... (handled by visits)
        target = P.pos(path[nxt])
        d = target - cur
        d = np.clip(d, -0.2, 0.2)
        newp = cur + d
        op = self._choose_op(state, i, newp, vt)
        plan["k"] = nxt
        return np.array([d[0], d[1], 0.0, BAND[op]], dtype=np.float32)

    def _replan(self, state, i, cur):
        P = self.planners[i]
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
