"""Rovers: per-rover time-expanded BFS over (cell, done-set, calibrated, store, sent)."""
import numpy as np

H = 0.1            # lattice spacing; a step moves up to 2 cells per axis (0.2m)
IMG_R = 2.0        # imaging range from base when facing away (true ~2.08)
SAMP_R = 0.235     # sampling range (true 0.25)
SEND_R = 3.85      # send range (true ~4.0)
TMAX = 120
BAND = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 1 / 6,
        "send": 0.5, "drop": 5 / 6}
SEND_PEN = 0
NOOP, CAL, IMG, SAMP, DROP, SEND = "noop", "calibrate", "image", "sample", "drop", "send"


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def _type(space, name):
    for t in space.types:
        if t.name == name:
            return t
    return None


def _seg_dist(p, a, b):
    ab = b - a
    t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-12), 0.0, 1.0)
    return float(np.linalg.norm(a + t * ab - p))


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
        self.obs_boxes = [(g(o, "x"), g(o, "y"), g(o, "half_x"), g(o, "half_y"), g(o, "half_z"))
                          for o in self.obstacles]
        self.pillars = [np.array([b[0], b[1]]) for b in self.obs_boxes if max(b[2], b[3]) < 0.15]
        self.opos = [np.array([g(o, "x"), g(o, "y")]) for o in self.objectives]
        self.spos = [np.array([g(o, "x"), g(o, "y")]) for o in self.samples]
        self.ssoil = [g(o, "is_soil") > 0.5 for o in self.samples]


def _shift_or(A, a, b):
    """OR of A shifted so that out[i,j] |= A[i-a, j-b]."""
    out = np.zeros_like(A)
    W, Hh = A.shape
    xs0, xs1 = max(0, a), min(W, W + a)
    ys0, ys1 = max(0, b), min(Hh, Hh + b)
    out[xs0:xs1, ys0:ys1] = A[xs0 - a:xs1 - a, ys0 - b:ys1 - b]
    return out


class RoverBFS:
    def __init__(self, scene, idx, home, img_r=IMG_R, home_th=0.0, other_home=None):
        self.sc = scene
        self.home_th = home_th
        self.other_home = other_home
        self.idx = idx
        self.home = np.array(home, dtype=float)
        side = 1.0 if home[0] > 0 else -1.0
        x0 = self.home[0] - H * np.floor((self.home[0] + 2.27) / H)
        y0 = self.home[1] - H * np.floor((self.home[1] + 2.27) / H)
        self.xs = np.arange(x0, 2.2701, H)
        self.ys = np.arange(y0, 2.2701, H)
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
        self.hc = (int(np.argmin(np.abs(self.xs - self.home[0]))), int(np.argmin(np.abs(self.ys - self.home[1]))))
        free[self.hc] = True
        self.free = free
        self.shape = free.shape
        self.nobj = len(scene.opos)
        self.n = self.nobj + 2
        self.STONE = 1 << self.nobj
        self.SOIL = 1 << (self.nobj + 1)
        self.CALB = 1 << self.n
        self.STOREB = 1 << (self.n + 1)
        self.SENTB = 1 << (self.n + 2)
        self.img_r = img_r
        self._prep()

    def _prep(self):
        X, Y = self.X, self.Y
        sc = self.sc
        self.odist = [np.sqrt((X - o[0]) ** 2 + (Y - o[1]) ** 2) for o in sc.opos]
        vis_any = np.zeros(self.shape, bool)
        for d in self.odist:
            vis_any |= d <= self.img_r
        self.vis_any = vis_any & self.free
        stone = np.zeros(self.shape, bool)
        soil = np.zeros(self.shape, bool)
        for s, so in zip(sc.spos, sc.ssoil):
            m = (X - s[0]) ** 2 + (Y - s[1]) ** 2 <= SAMP_R ** 2
            if so:
                soil |= m
            else:
                stone |= m
        both = stone & soil
        self.stone_m = stone & ~both & self.free
        self.soil_m = soil & ~both & self.free
        inr = ((X - sc.lpos[0]) ** 2 + (Y - sc.lpos[1]) ** 2 <= SEND_R ** 2) & self.free
        away = np.arctan2(Y - sc.lpos[1], X - sc.lpos[0])
        self.send_head_ok = inr & (np.abs(_wrap(self.home_th - away)) <= np.radians(60))
        pill = np.zeros(self.shape, bool)
        for pc in sc.pillars:
            pill |= self._segdist_grid(pc) < 0.14
        self.send_static = inr & ~pill
        self.send_m = inr
        self.other_traj = None
        self._send_t_cache = {}
        self._img_cache = {}

    def _segdist_grid(self, q):
        """Distance from point q to segment (cell -> lander) for every cell."""
        L = self.sc.lpos
        ax, ay = self.X, self.Y
        bx, by = L[0] - ax, L[1] - ay
        qx, qy = q[0] - ax, q[1] - ay
        t = np.clip((qx * bx + qy * by) / np.maximum(bx * bx + by * by, 1e-12), 0.0, 1.0)
        return np.sqrt((qx - t * bx) ** 2 + (qy - t * by) ** 2)

    def send_mask_t(self, t):
        if self.other_traj is None:
            return self.send_m
        q = self.other_traj[min(t, len(self.other_traj) - 1)]
        key = (round(float(q[0]), 3), round(float(q[1]), 3))
        m = self._send_t_cache.get(key)
        if m is None:
            m = self.send_head_ok | (self.send_static & (self._segdist_grid(q) >= 0.29))
            self._send_t_cache[key] = m
        return m

    def pos(self, c):
        return np.array([self.xs[c[0]], self.ys[c[1]]])

    def cell(self, p):
        return (int(np.argmin(np.abs(self.xs - p[0]))), int(np.argmin(np.abs(self.ys - p[1]))))

    def img_masks(self, S):
        """For image op with done-set S: list of (r, mask) where r is nearest visible not-yet-imaged."""
        key = S & ((1 << self.nobj) - 1)
        if key in self._img_cache:
            return self._img_cache[key]
        best = np.full(self.shape, np.inf)
        arg = np.full(self.shape, -1)
        for r in range(self.nobj):
            if key & (1 << r):
                continue
            d = np.where(self.odist[r] <= self.img_r, self.odist[r], np.inf)
            better = d < best
            best = np.where(better, d, best)
            arg = np.where(better, r, arg)
        res = []
        for r in range(self.nobj):
            m = (arg == r) & self.free
            if m.any():
                res.append((r, m))
        self._img_cache[key] = res
        return res

    def transitions(self, L):
        out = []
        S = L & ((1 << self.n) - 1)
        cal = L & self.CALB
        store = L & self.STOREB
        sent = L & self.SENTB
        if not sent:
            if not cal:
                out.append((CAL, L | self.CALB, self.vis_any))
            else:
                for r, m in self.img_masks(S):
                    out.append((IMG, (L | (1 << r)) & ~self.CALB, m))
            if not store:
                if not (S & self.STONE):
                    out.append((SAMP, L | self.STONE | self.STOREB, self.stone_m))
                if not (S & self.SOIL):
                    out.append((SAMP, L | self.SOIL | self.STOREB, self.soil_m))
            if S:
                out.append((SEND, L | self.SENTB, "SEND"))
        if store:
            out.append((DROP, L & ~self.STOREB, None))
        return out

    def dilate(self, R):
        A = R | _shift_or(R, 1, 0) | _shift_or(R, -1, 0)
        A = A | _shift_or(R, 2, 0) | _shift_or(R, -2, 0)
        B = A | _shift_or(A, 0, 1) | _shift_or(A, 0, -1)
        B = B | _shift_or(A, 0, 2) | _shift_or(A, 0, -2)
        return B & self.free

    def run(self, start_cell, L0, wanted=None, tmax=TMAX, time_budget=None):
        """Forward BFS. Returns dict S->earliest finish time (home, store empty, sent)."""
        import time as _t
        t_start = _t.time()
        R0 = np.zeros(self.shape, bool)
        R0[start_cell] = True
        self.layers = [{L0: R0}]
        self.rev = {}
        self.trans_cache = {}
        finish = {}
        hc = self.hc
        for t in range(1, tmax + 1):
            prev = self.layers[-1]
            new = {}
            for L, R in prev.items():
                D = self.dilate(R)
                if L in new:
                    new[L] |= D
                else:
                    new[L] = D.copy()
                tr = self.trans_cache.get(L)
                if tr is None:
                    tr = self.transitions(L)
                    self.trans_cache[L] = tr
                for op, L2, m in tr:
                    if isinstance(m, str):
                        m = self.send_mask_t(t)
                    M = D if m is None else (D & m)
                    if not M.any():
                        continue
                    if L2 in new:
                        new[L2] |= M
                    else:
                        new[L2] = M.copy()
            self.layers.append(new)
            for L, R in new.items():
                if (L & self.SENTB) and not (L & self.STOREB) and R[hc]:
                    S = L & ((1 << self.n) - 1)
                    if S not in finish:
                        finish[S] = (t, L)
            if wanted is not None and all(any((S & w) == w for S in finish) for w in wanted):
                break
            if time_budget is not None and _t.time() - t_start > time_budget:
                break
        return finish

    def extract(self, T, Lgoal):
        """Backtrack from (T, Lgoal, home). Returns list of (cell, op) for steps 1..T."""
        c = self.hc
        L = Lgoal
        steps = []
        W, Hh = self.shape
        for t in range(T, 0, -1):
            prev = self.layers[t - 1]
            # candidate predecessors: (Lp, op) such that transition Lp --op--> L valid at c
            cands = []
            if L in prev:
                cands.append((L, NOOP))
            for Lp in prev:
                tr = self.trans_cache.get(Lp)
                if tr is None:
                    tr = self.transitions(Lp)
                    self.trans_cache[Lp] = tr
                for op, L2, m in tr:
                    if isinstance(m, str):
                        m = self.send_mask_t(t)
                    if L2 == L and (m is None or m[c]):
                        cands.append((Lp, op))
            found = None
            # prefer real ops over noop when tie (keeps ops early); prefer staying still
            for Lp, op in cands:
                R = prev[Lp]
                i0, j0 = c
                best = None
                for a in range(-2, 3):
                    for b in range(-2, 3):
                        ii, jj = i0 + a, j0 + b
                        if 0 <= ii < W and 0 <= jj < Hh and R[ii, jj]:
                            score = max(abs(a), abs(b)) * 0.01 + (abs(a) + abs(b)) * 0.001
                            if best is None or score < best[0]:
                                best = (score, (ii, jj))
                if best is not None:
                    found = (Lp, op, best[1])
                    break
            if found is None:
                return None
            Lp, op, cp = found
            steps.append((c, op, L))
            c = cp
            L = Lp
        steps.reverse()
        return steps


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
        self.bfs = [RoverBFS(sc, i, self.homes[i], home_th=self.home_th[i], other_home=self.homes[1 - i])
                    for i in range(2)]
        nobj = len(sc.objectives)
        n = nobj + 2
        full = (1 << n) - 1
        fins = []
        for i in range(2):
            B = self.bfs[i]
            fins.append(B.run(B.hc, 0, wanted=[full], tmax=TMAX, time_budget=12.0))
        # best finish time for a superset-closed requirement: T_i(req) = min over S ⊇ req
        def best_for(fin, req):
            bt = None
            for S, (t, L) in fin.items():
                if (S & req) == req and (bt is None or t < bt[0]):
                    bt = (t, L, S)
            return bt
        best = None
        for s0 in range(1 << n):
            s1 = full & ~s0
            b0 = best_for(fins[0], s0) if s0 else (0, None, 0)
            b1 = best_for(fins[1], s1) if s1 else (0, None, 0)
            if b0 is None or b1 is None:
                continue
            key = (max(b0[0], b1[0]), b0[0] + b1[0])
            if best is None or key < best[0]:
                best = (key, b0, b1)
        self.plans = []
        self.my_req = [0, 0]
        for i in range(2):
            b = best[1 + i] if best else None
            steps = []
            if b is not None and b[1] is not None:
                # need layers from the run for rover i: rerun to be safe (layers overwritten? no: per-rover object)
                steps = self.bfs[i].extract(b[0], b[1]) or []
                self.my_req[i] = b[2]
            self.plans.append({"steps": steps, "k": 0, "fail": 0})
        # refine each rover's plan given the other's trajectory (send line-of-sight)
        for i in range(2):
            if not self.plans[i]["steps"]:
                continue
            B = self.bfs[i]
            B.other_traj = self._traj(1 - i)
            B._send_t_cache = {}
            req = self.my_req[i]
            fin = B.run(B.hc, 0, wanted=[req], tmax=TMAX, time_budget=8.0)
            bt = None
            for S2, (t, L) in fin.items():
                if (S2 & req) == req and (bt is None or t < bt[0]):
                    bt = (t, L)
            if bt is not None:
                st = B.extract(bt[0], bt[1])
                orig = self.plans[i]["steps"]
                pen = 0 if self._sends_feasible(B, orig) else SEND_PEN
                if st and len(st) <= len(orig) + pen:
                    self.plans[i] = {"steps": st, "k": 0, "fail": 0}
        self.done_flag = False

    def _sends_feasible(self, B, steps):
        """Check each planned SEND can happen with LOS given B.other_traj before the next acquisition."""
        n = len(steps)
        for j, (c, op, L) in enumerate(steps):
            if op != SEND:
                continue
            ok = False
            for j2 in range(j, n):
                if j2 > j and steps[j2][1] in (SAMP, IMG):
                    break
                if B.send_mask_t(j2 + 1)[steps[j2][0]]:
                    ok = True
                    break
            if not ok:
                return False
        return True

    def _traj(self, j):
        """Positions of rover j at times 0,1,2,... from its current plan pointer."""
        plan = self.plans[j]
        B = self.bfs[j]
        steps = plan["steps"]
        k = plan["k"]
        if k > 0 and k <= len(steps):
            cur = B.pos(steps[k - 1][0])
        else:
            cur = self.homes[j]
        out = [cur]
        for idx in range(k, len(steps)):
            out.append(B.pos(steps[idx][0]))
        return out

    # ------------------------------------------------------------------
    def _flags(self, state, i):
        sc = self.sc
        g = state.get
        me = "rover%d" % i
        S = 0
        for r, o in enumerate(sc.objectives):
            if g(o, "have_image_" + me) > 0.5:
                S |= 1 << r
        nobj = len(sc.objectives)
        for s, soil in zip(sc.samples, sc.ssoil):
            if g(s, "analyzed_" + me) > 0.5:
                S |= 1 << (nobj + (1 if soil else 0))
        cal = g(sc.rovers[i], "calibrated") > 0.5
        store = g(sc.rovers[i], "store_full") > 0.5
        holding = any(g(o, "have_image_" + me) > 0.5 and g(o, "received_image") < 0.5 for o in sc.objectives) or \
            any(g(s, "analyzed_" + me) > 0.5 and g(s, "received_analysis") < 0.5 for s in sc.samples)
        return S, cal, store, holding

    def _visible(self, p, th, k, margin=0.03):
        c = p + np.array([-0.087 * np.cos(th) + 0.0125 * np.sin(th), -0.087 * np.sin(th) - 0.0125 * np.cos(th)])
        o = self.sc.opos[k]
        v = o - c
        if np.linalg.norm(v) > 1.9972 - margin:
            return False
        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
        if ang < np.radians(108):
            for pc in self.sc.pillars:
                if _seg_dist(pc, c, o) < 0.11:
                    return False
        return True

    def _can_send(self, state, i, p, th):
        sc = self.sc
        v = sc.lpos - p
        if np.linalg.norm(v) > SEND_R:
            return False
        ang = abs(_wrap(np.arctan2(v[1], v[0]) - th))
        if ang >= np.radians(115):
            return True
        g = state.get
        orv = sc.rovers[1 - i]
        op = np.array([g(orv, "x"), g(orv, "y")])
        if _seg_dist(op, p, sc.lpos) < 0.27:
            return False
        for pc in sc.pillars:
            if _seg_dist(pc, p, sc.lpos) < 0.13:
                return False
        return True

    def _los_clear(self, p, q):
        sc = self.sc
        if np.linalg.norm(sc.lpos - p) > SEND_R:
            return False
        if _seg_dist(q, p, sc.lpos) < 0.29:
            return False
        for pc in sc.pillars:
            if _seg_dist(pc, p, sc.lpos) < 0.14:
                return False
        return True

    def _other_pos_at(self, i, dt, state):
        """Predicted position of rover (1-i) dt steps from now."""
        j = 1 - i
        plan = self.plans[j]
        steps = plan["steps"]
        B = self.bfs[j]
        if not steps:
            g = state.get
            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
        idx = min(len(steps) - 1, plan["k"] + dt - 1)
        if idx < 0:
            g = state.get
            return np.array([g(self.sc.rovers[j], "x"), g(self.sc.rovers[j], "y")])
        return B.pos(steps[idx][0])

    def _desired_heading(self, state, i, p, th, k, holding):
        sc = self.sc
        plan = self.plans[i]
        steps = plan["steps"]
        B = self.bfs[i]
        nobj = len(sc.objectives)
        # next image op in plan: face away from the objective it targets
        for idx in range(k, len(steps)):
            c, op, L = steps[idx]
            if op == IMG:
                # which objective: bit newly set in L vs previous
                Lp = steps[idx - 1][2] if idx > 0 else plan.get("L0", 0)
                newbits = (L & ~Lp) & ((1 << nobj) - 1)
                if newbits:
                    r = int(np.log2(newbits & -newbits))
                    v = B.pos(c) - sc.opos[r]
                    return np.arctan2(v[1], v[0])
        hth = self.home_th[i]
        if holding:
            # will a send be possible facing home-ish heading later?
            last = len(steps)
            ok = False
            for idx in range(k, last):
                q = self._other_pos_at(i, idx - k + 1, state)
                if self._los_clear(B.pos(steps[idx][0]), q):
                    ok = True
                    break
            if not ok and self._los_clear(p, self._other_pos_at(i, 0, state)):
                ok = True
            if not ok:
                v = p - sc.lpos
                away = np.arctan2(v[1], v[0])
                best, bc = None, None
                for c in np.linspace(-np.radians(60), np.radians(60), 25):
                    h = away + c
                    cost = abs(_wrap(h - th)) + abs(_wrap(hth - h)) + 0.01 * abs(_wrap(h - th))
                    if best is None or cost < best:
                        best, bc = cost, h
                return bc
        return hth

    def _replan(self, state, i, cur):
        B = self.bfs[i]
        S, cal, store, holding = self._flags(state, i)
        L0 = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
        if not holding and S:
            L0 |= B.SENTB
        c = B.cell(cur)
        B.free[c] = True
        req = self.my_req[i] | S
        B.other_traj = self._traj(1 - i)
        B._send_t_cache = {}
        fin = B.run(c, L0, wanted=[req], tmax=TMAX, time_budget=5.0)
        bt = None
        for S2, (t, L) in fin.items():
            if (S2 & req) == req and (bt is None or t < bt[0]):
                bt = (t, L)
        steps = B.extract(bt[0], bt[1]) if bt else []
        self.plans[i] = {"steps": steps or [], "k": 0, "fail": 0, "L0": L0}

    def _rover_action(self, state, i):
        sc = self.sc
        g = state.get
        rv = sc.rovers[i]
        cur = np.array([g(rv, "x"), g(rv, "y")])
        th = g(rv, "theta")
        B = self.bfs[i]
        plan = self.plans[i]
        S, cal, store, holding = self._flags(state, i)
        steps = plan["steps"]
        k = plan["k"]
        # verify previous step outcome
        if k > 0 and k <= len(steps):
            c, op, L = steps[k - 1]
            pos_ok = np.linalg.norm(B.pos(c) - cur) < 0.02
            Sp = L & ((1 << B.n) - 1)
            op_ok = True
            if op in (IMG, SAMP):
                op_ok = (S & Sp) == Sp
            elif op == CAL:
                op_ok = cal
            elif op == DROP:
                op_ok = not store
            if not (pos_ok and op_ok):
                plan["fail"] += 1
                Lpre = steps[k - 2][2] if k >= 2 else plan.get("L0", 0)
                mask = ((1 << B.n) - 1) | B.CALB | B.STOREB
                Lact = S | (B.CALB if cal else 0) | (B.STOREB if store else 0)
                changed = (Lact & mask) != (Lpre & mask)
                if plan["fail"] > 4 or (not pos_ok and plan["fail"] > 2) or (pos_ok and changed):
                    self._replan(state, i, cur)
                    plan = self.plans[i]
                    steps = plan["steps"]
                    k = 0
                else:
                    k = k - 1  # retry the step
            else:
                plan["fail"] = 0
        if k < len(steps):
            c, op, L = steps[k]
            target = B.pos(c)
            plan["k"] = k + 1
        else:
            target = cur if np.linalg.norm(cur - self.homes[i]) < 0.02 else self.homes[i]
            op = NOOP
            plan["k"] = len(steps) + 1 if steps else 1
            # finished plan: if tasks remain undone, replan
            if (S & self.my_req[i]) != self.my_req[i] or store:
                self._replan(state, i, cur)
                return self._rover_action_fresh(state, i)
        d = np.clip(target - cur, -0.2, 0.2)
        newp = cur + d
        dth = float(np.clip(_wrap(self._desired_heading(state, i, newp, th, k + 1, holding) - th), -0.4, 0.4))
        newth = _wrap(th + dth)
        # op adjustments
        if op == SEND:
            op = NOOP
        if op in (NOOP,) and holding and self._can_send(state, i, newp, newth):
            op = SEND
        elif op == NOOP and store and not any(s[1] == SAMP for s in steps[k:]):
            op = NOOP
        return np.array([d[0], d[1], dth, BAND[op]], dtype=np.float32)

    def _rover_action_fresh(self, state, i):
        plan = self.plans[i]
        if not plan["steps"]:
            return np.array([0, 0, 0, BAND[NOOP]], dtype=np.float32)
        plan["k"] = 0
        return self._rover_action(state, i)

    def get_action(self, state):
        a0 = self._rover_action(state, 0)
        a1 = self._rover_action(state, 1)
        return np.concatenate([a0, a1]).astype(np.float32)
