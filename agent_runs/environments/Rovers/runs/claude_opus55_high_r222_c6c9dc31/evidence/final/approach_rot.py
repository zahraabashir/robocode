"""Rovers approach: per-rover layered grid BFS + Held-Karp over task subsets,
joint assignment of tasks to the two rovers (they cannot cross the middle wall)."""
import math
import time
import numpy as np
from scipy.ndimage import maximum_filter, minimum_filter

H = 0.025
K = 8
INF = 10 ** 6
SEL = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "none": 1 / 6,
       "send": 0.5, "drop": 5 / 6}

ARENA = 2.2729 - 0.004
WALL = 0.227 + 0.006
MOUND_R = 0.177 + 0.006
SQ_HALF = 0.21
OCT_SUM = 0.44
LANDER_HALF = (0.69 + 0.012, 0.514 + 0.012)
CAM_OFF = 0.0875
CAM_ANG = math.radians(188.0)
OBJ_RANGE = 1.99 + 0.0875
LANDER_RANGE = 3.98 + 0.0875
ROVER_BLOCK_R = 0.26
SAMPLE_R = 0.245
LOS_MARGIN = 0.012
OBJ_RANGE_LIB = 2.005
PILLAR_LOS_STRICT = 0.08
PILLAR_LOS_LIB = -1.0
NEAR_MARGIN = 0.03
HOME_R = 0.245
HOME_THETA = {"rover0": math.pi, "rover1": 0.0}


def wrap(a):
    return (a + math.pi) % (2 * math.pi) - math.pi


def seg_point_dist(ax, ay, bx, by, px, py):
    """Distance arrays from point (px,py) to segments a->b (a arrays)."""
    dx = bx - ax
    dy = by - ay
    L2 = dx * dx + dy * dy + 1e-12
    t = np.clip(((px - ax) * dx + (py - ay) * dy) / L2, 0.0, 1.0)
    qx = ax + t * dx - px
    qy = ay + t * dy - py
    return np.sqrt(qx * qx + qy * qy)


def seg_hits_box(ax, ay, bx, by, cx, cy, hx, hy):
    """Vectorised: does segment (ax,ay)->(bx,by) intersect box centred (cx,cy)?"""
    dx = bx - ax
    dy = by - ay
    t0 = np.zeros(np.shape(ax))
    t1 = np.ones(np.shape(ax))
    for d, a, c, h in ((dx, ax, cx, hx), (dy, ay, cy, hy)):
        d = np.where(np.abs(d) < 1e-12, 1e-12, d)
        u = (c - h - a) / d
        v = (c + h - a) / d
        lo = np.minimum(u, v)
        hi = np.maximum(u, v)
        t0 = np.maximum(t0, lo)
        t1 = np.minimum(t1, hi)
    return t0 <= t1


class World:
    def __init__(self, state, obs_space):
        self.space = obs_space
        T = lambda n: obs_space.get_type(n) if hasattr(obs_space, "get_type") else n
        self.rovers = {}
        for o in state.get_objects(T("rover")):
            self.rovers[o.name] = o
        self.lander = list(state.get_objects(T("lander")))[0]
        self.objectives = sorted(state.get_objects(T("objective")), key=lambda o: o.name)
        self.samples = sorted(state.get_objects(T("sample")), key=lambda o: o.name)
        self.obstacles = list(state.get_objects(T("obstacle")))


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.obs_space = observation_space
        self.plans = None

    # ------------------------------------------------------------------ utils
    def _get(self, state, o, f):
        return float(state.get(o, f))

    def reset(self, state, info):
        self.w = World(state, self.obs_space)
        self.home = {}
        for n, o in self.w.rovers.items():
            self.home[n] = (self._get(state, o, "x"), self._get(state, o, "y"))
        self.home_theta = {}
        for n, o in self.w.rovers.items():
            self.home_theta[n] = self._get(state, o, "theta")
        self.plans = None
        self.bad_points = []
        self.bad_view = {n: [] for n in self.w.rovers}
        self.bad_send = {n: [] for n in self.w.rovers}
        self.expect = None
        self.nreplan = 0
        self.plan_time = 0.0
        self.log = []
        self._plan(state)

    # --------------------------------------------------------------- planning
    def _grid(self, state, rname):
        o = self.w.rovers[rname]
        x0 = self._get(state, o, "x")
        y0 = self._get(state, o, "y")
        right = self.home[rname][0] > 0
        xmin, xmax = (WALL, ARENA) if right else (-ARENA, -WALL)
        ymin, ymax = -ARENA, ARENA
        i0 = math.ceil((xmin - x0) / H - 1e-9)
        i1 = math.floor((xmax - x0) / H + 1e-9)
        j0 = math.ceil((ymin - y0) / H - 1e-9)
        j1 = math.floor((ymax - y0) / H + 1e-9)
        # ensure start included
        i0 = min(i0, 0); i1 = max(i1, 0); j0 = min(j0, 0); j1 = max(j1, 0)
        xs = x0 + H * np.arange(i0, i1 + 1)
        ys = y0 + H * np.arange(j0, j1 + 1)
        X, Y = np.meshgrid(xs, ys, indexing="ij")
        start = (-i0, -j0)
        return X, Y, start

    def _free(self, state, X, Y):
        free = np.ones(X.shape, bool)
        for ob in self.w.obstacles:
            ox = self._get(state, ob, "x"); oy = self._get(state, ob, "y")
            hx = self._get(state, ob, "half_x"); hy = self._get(state, ob, "half_y")
            ddx = np.maximum(np.abs(X - ox) - hx, 0)
            ddy = np.maximum(np.abs(Y - oy) - hy, 0)
            blocked = np.sqrt(ddx ** 2 + ddy ** 2) < MOUND_R
            if hx < 0.12 and hy < 0.12:
                ax = np.abs(X - ox); ay = np.abs(Y - oy)
                blocked |= (ax < hx + SQ_HALF) & (ay < hy + SQ_HALF) & (ax + ay < OCT_SUM + hx + hy - 0.1)
            free &= ~blocked
        lx = self._get(state, self.w.lander, "x"); ly = self._get(state, self.w.lander, "y")
        free &= ~((np.abs(X - lx) < LANDER_HALF[0]) & (np.abs(Y - ly) < LANDER_HALF[1]))
        for (bx, by) in self.bad_points:
            free &= np.hypot(X - bx, Y - by) > 0.04
        return free

    def _cam(self, rname, X, Y):
        th = self.home_theta[rname]
        return X + CAM_OFF * math.cos(th + CAM_ANG), Y + CAM_OFF * math.sin(th + CAM_ANG)

    def _plan(self, state):
        t0 = time.time()
        try:
            self._plan_inner(state)
        finally:
            self.plan_time += time.time() - t0

    def _plan_inner(self, state):
        w = self.w
        g = lambda o, f: self._get(state, o, f)
        rnames = sorted(w.rovers.keys())
        # ---- remaining requirements
        need_img = []           # objectives needing imaging
        must_send = {r: False for r in rnames}
        for ob in w.objectives:
            if g(ob, "received_image") > 0.5:
                continue
            held = False
            for r in rnames:
                if g(ob, "have_image_" + r) > 0.5:
                    must_send[r] = True
                    held = True
            if not held:
                need_img.append(ob)
        need_kind = []          # 'stone' / 'soil' needing sampling
        for kind, soil in (("stone", 0.0), ("soil", 1.0)):
            ss = [s for s in w.samples if abs(g(s, "is_soil") - soil) < 0.5]
            if any(g(s, "received_analysis") > 0.5 for s in ss):
                continue
            held = False
            for r in rnames:
                if any(g(s, "analyzed_" + r) > 0.5 for s in ss):
                    must_send[r] = True
                    held = True
            if not held:
                need_kind.append(kind)

        blockers = {r: [] for r in rnames}
        per = {}
        for it in range(4):
            for r in rnames:
                if r not in per:
                    per[r] = self._rover_hk(state, r, need_img, need_kind, must_send[r], rnames, blockers[r])
            self._assign(per, rnames, need_img, need_kind)
            changed = False
            for k, r in enumerate(rnames):
                other = rnames[1 - k]
                op_ = self.plans[other]
                ox0 = g(w.rovers[other], "x"); oy0 = g(w.rovers[other], "y")
                for t, ((x, y), op) in enumerate(self.plans[r]):
                    if op != "send":
                        continue
                    if t < len(op_):
                        p = op_[t][0]
                    elif op_:
                        p = op_[-1][0]
                    else:
                        p = (ox0, oy0)
                    th = self.home_theta[r]
                    cx = x + CAM_OFF * math.cos(th + CAM_ANG); cy = y + CAM_OFF * math.sin(th + CAM_ANG)
                    lx, ly = g(w.lander, "x"), g(w.lander, "y")
                    dd = float(seg_point_dist(np.array(cx), np.array(cy), lx, ly, p[0], p[1]))
                    if dd <= ROVER_BLOCK_R:
                        blockers[r].append(p)
                        per.pop(r, None)
                        changed = True
            if not changed:
                break

    def _assign(self, per, rnames, need_img, need_kind):
        best = None
        tasks_all = [("img", ob.name) for ob in need_img] + [("kind", k) for k in need_kind]
        r0, r1 = rnames
        res0, res1 = per[r0], per[r1]
        for S0, v0 in res0["final"].items():
            for S1, v1 in res1["final"].items():
                cov = set(res0["names"][i] for i in range(len(res0["names"])) if S0 >> i & 1)
                cov |= set(res1["names"][i] for i in range(len(res1["names"])) if S1 >> i & 1)
                if not all(t in cov for t in tasks_all):
                    continue
                key = (max(v0[0], v1[0]), v0[0] + v1[0], bin(S0).count("1") + bin(S1).count("1"))
                if best is None or key < best[0]:
                    best = (key, S0, S1)
        self.plans = {}
        if best is None:
            for r in rnames:
                self.plans[r] = self._extract(per[r], per[r]["final_any_empty"])
        else:
            _, S0, S1 = best
            self.plans[r0] = self._extract(res0, S0)
            self.plans[r1] = self._extract(res1, S1)
        self.t = 0

    def _propagate(self, sU, sC, free, vany):
        TU = np.full(free.shape, INF, np.int32)
        TC = np.full(free.shape, INF, np.int32)
        AU = np.full(free.shape, INF, np.int32)
        AC = np.full(free.shape, INF, np.int32)
        RU = np.zeros(free.shape, bool)
        RC = np.zeros(free.shape, bool)
        mU = sU.min(); mC = sC.min()
        t = int(min(mU, mC))
        if t >= INF:
            return TU, TC, AU, AC
        maxseed = max(int(sU[sU < INF].max()) if mU < INF else 0,
                      int(sC[sC < INF].max()) if mC < INF else 0)
        nfree = int(free.sum())
        while True:
            RU |= sU == t
            RC |= sC == t
            TU[RU & (TU == INF)] = t
            TC[RC & (TC == INF)] = t
            if t >= maxseed and RU.sum() + RC.sum() >= 2 * nfree:
                break
            dU = maximum_filter(RU, size=2 * K + 1, mode="constant") & free
            dC = maximum_filter(RC, size=2 * K + 1, mode="constant") & free
            AU[dU & (AU == INF)] = t + 1
            AC[dC & (AC == INF)] = t + 1
            nRU = RU | dU
            nRC = RC | dC | (dU & vany)
            if t >= maxseed and (nRU == RU).all() and (nRC == RC).all():
                break
            RU, RC = nRU, nRC
            t += 1
            if t > 600:
                break
        return TU, TC, AU, AC

    def _rover_hk(self, state, r, need_img, need_kind, must_send, rnames, blockers=()):
        w = self.w
        g = lambda o, f: self._get(state, o, f)
        X, Y, start = self._grid(state, r)
        free = self._free(state, X, Y)
        free[start] = True
        CX, CY = X, Y
        regions = []
        names = []
        vany = np.zeros(X.shape, bool)
        pillars = [(g(o, "x"), g(o, "y"), g(o, "half_x") + LOS_MARGIN, g(o, "half_y") + LOS_MARGIN)
                   for o in w.obstacles if g(o, "half_x") < 0.12 and g(o, "half_y") < 0.12]
        badv = np.zeros(X.shape, bool)
        for (bx, by) in self.bad_view[r]:
            badv |= np.hypot(X - bx, Y - by) < 0.04
        held0 = set(ob.name for ob in w.objectives if g(ob, "have_image_" + r) > 0.5)
        odist = {}
        ovis_lib = {}
        img_obj = {}
        for ob in w.objectives:
            ox, oy = g(ob, "x"), g(ob, "y")
            d = np.hypot(CX - ox, CY - oy)
            vis = (d <= OBJ_RANGE) & free & ~badv
            vlib = d <= OBJ_RANGE_LIB
            for (px, py, phx, phy) in pillars:
                dseg = seg_point_dist(CX, CY, ox, oy, px, py)
                vis &= dseg > PILLAR_LOS_STRICT
                if math.hypot(px - ox, py - oy) < 0.95:
                    vlib &= dseg > PILLAR_LOS_LIB
            odist[ob.name] = d
            ovis_lib[ob.name] = vlib
            vany |= vis
            if ob in need_img and vis.any():
                img_obj[len(regions)] = ob.name
                regions.append(("img", vis)); names.append(("img", ob.name))
        for kind in need_kind:
            soil = 1.0 if kind == "soil" else 0.0
            dme = np.full(X.shape, 9.0)
            doth = np.full(X.shape, 9.0)
            for s in w.samples:
                dd = np.hypot(X - g(s, "x"), Y - g(s, "y"))
                if abs(g(s, "is_soil") - soil) < 0.5:
                    dme = np.minimum(dme, dd)
                else:
                    doth = np.minimum(doth, dd)
            reg = (dme < SAMPLE_R) & ((doth > 0.26) | (dme < doth - 0.02)) & free
            if reg.any():
                regions.append(("sample", reg)); names.append(("kind", kind))
        # send region
        lx, ly = g(w.lander, "x"), g(w.lander, "y")
        send = (np.hypot(CX - lx, CY - ly) <= LANDER_RANGE) & free
        for (px, py, phx, phy) in pillars:
            send &= seg_point_dist(CX, CY, lx, ly, px, py) > PILLAR_LOS_STRICT
        for (bx, by, sector) in self.bad_send[r]:
            send &= np.hypot(X - bx, Y - by) > 0.04
            if sector:
                bcx, bcy = self._cam(r, bx, by)
                bd = math.hypot(bcx - lx, bcy - ly)
                bb = math.atan2(bcy - ly, bcx - lx)
                ang = np.abs(np.angle(np.exp(1j * (np.arctan2(CY - ly, CX - lx) - bb))))
                send &= ~((np.hypot(CX - lx, CY - ly) >= bd - 0.15) & (ang < math.radians(12)))
        for other in rnames:
            if other == r:
                continue
            for (px, py) in [self.home[other], (g(w.rovers[other], "x"), g(w.rovers[other], "y"))] + list(blockers):
                send &= seg_point_dist(CX, CY, lx, ly, px, py) > ROVER_BLOCK_R
        hx, hy = self.home[r]
        homereg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
        if not homereg.any():
            homereg = np.zeros(X.shape, bool)
            d = np.hypot(X - hx, Y - hy) + (~free) * 100
            homereg[np.unravel_index(np.argmin(d), d.shape)] = True

        n = len(regions)
        calib = g(w.rovers[r], "calibrated") > 0.5
        s0U = np.full(X.shape, INF, np.int32)
        s0C = np.full(X.shape, INF, np.int32)
        (s0C if calib else s0U)[start] = 0
        maps = {}      # (S, j) -> (seedU, seedC, TU, TC, AU, AC)
        seeds = {}
        def drop_step(a):
            m = minimum_filter(a, size=2 * K + 1, mode="constant", cval=INF)
            return np.where(free & (m < INF), m + 1, INF).astype(np.int32)

        store_full = g(w.rovers[r], "store_full") > 0.5
        if store_full:
            s0U, s0C = drop_step(s0U), drop_step(s0C)
        start_maps = self._propagate(s0U, s0C, free, vany)

        reg_cache = {}

        def img_region(j, S):
            imask = 0
            for i in img_obj:
                if S >> i & 1:
                    imask |= 1 << i
            key = (j, imask)
            if key in reg_cache:
                return reg_cache[key]
            held = set(held0) | set(img_obj[i] for i in img_obj if imask >> i & 1)
            me = img_obj[j]
            reg = regions[j][1].copy()
            for ob in w.objectives:
                if ob.name == me or ob.name in held:
                    continue
                reg &= ~(ovis_lib[ob.name] & (odist[ob.name] <= odist[me] + NEAR_MARGIN))
            reg_cache[key] = reg
            return reg

        def op_maps(M, j, S=0):
            TU, TC, AU, AC = M
            kind, reg = regions[j]
            if kind == "img":
                reg = img_region(j, S)
                return np.where(reg, AC, INF), np.full(X.shape, INF, np.int32)
            return drop_step(np.where(reg, AU, INF)), drop_step(np.where(reg, AC, INF))

        for j in range(n):
            seeds[(1 << j, j)] = op_maps(start_maps, j)
        order = sorted(seeds.keys(), key=lambda k: bin(k[0]).count("1"))
        full = (1 << n) - 1
        # BFS over subsets in increasing size
        for size in range(1, n + 1):
            for S in range(1, full + 1):
                if bin(S).count("1") != size:
                    continue
                for j in range(n):
                    if (S, j) not in seeds:
                        continue
                    sU, sC = seeds[(S, j)]
                    if min(sU.min(), sC.min()) >= INF:
                        continue
                    M = self._propagate(sU, sC, free, vany)
                    maps[(S, j)] = M
                    for k in range(n):
                        if S >> k & 1:
                            continue
                        nU, nC = op_maps(M, k, S)
                        key = (S | 1 << k, k)
                        if key in seeds:
                            oU, oC = seeds[key]
                            seeds[key] = (np.minimum(oU, nU), np.minimum(oC, nC))
                        else:
                            seeds[key] = (nU, nC)
        # completions
        final = {}
        comp = {}

        def complete(M, need_send):
            TU, TC, AU, AC = M
            if need_send:
                op = np.where(send, np.minimum(AU, AC), INF)
                if op.min() >= INF:
                    return INF, None
                M2 = self._propagate(op, np.full(X.shape, INF, np.int32), free, vany)
                at = np.minimum(M2[0], M2[1])
                v = np.where(homereg, at, INF)
                return int(v.min()), (op, M2)
            at = np.minimum(TU, TC)
            v = np.where(homereg, at, INF)
            return int(v.min()), None

        v, extra = complete(start_maps, must_send)
        if v < INF:
            final[0] = (v, None, extra)
        for (S, j), M in maps.items():
            v, extra = complete(M, True)
            if v >= INF:
                continue
            if S not in final or v < final[S][0]:
                final[S] = (v, j, extra)
        res = dict(img_obj=img_obj, X=X, Y=Y, free=free, vany=vany, regions=regions, names=names,
                   maps=maps, seeds=seeds, start_maps=start_maps, s0=(s0U, s0C),
                   final=final, store_full=store_full, homereg=homereg, send=send, must_send=must_send, r=r)
        res["final_any_empty"] = 0 if 0 in final else (min(final, key=lambda s: final[s][0]) if final else None)
        return res

    # ------------------------------------------------------------ extraction
    def _back_stage(self, M, sU, sC, vany, free, c, t, L, steps):
        """Backtrack within stage until hitting a seed. Appends (cell, op) in
        reverse order. Returns (cell, t, layer) at the seed."""
        TU, TC, AU, AC = M
        nx, ny = free.shape
        while True:
            if L == "U" and sU[c] == t:
                return c, t, "U"
            if L == "C" and sC[c] == t:
                return c, t, "C"
            T = TU if L == "U" else TC
            if T[c] < t:
                steps.append((c, "none")); t -= 1
                continue
            i, j = c
            i0, i1 = max(0, i - K), min(nx, i + K + 1)
            j0, j1 = max(0, j - K), min(ny, j + K + 1)
            found = None
            sub = T[i0:i1, j0:j1]
            cand = np.argwhere(sub <= t - 1)
            if len(cand):
                # prefer farthest-consistent (any)
                a, b = cand[0]
                found = ((i0 + a, j0 + b), L, "none")
            elif L == "C" and vany[c]:
                cand = np.argwhere(TU[i0:i1, j0:j1] <= t - 1)
                if len(cand):
                    a, b = cand[0]
                    found = ((i0 + a, j0 + b), "U", "calibrate")
            if found is None:
                raise RuntimeError("backtrack failed")
            steps.append((c, found[2]))
            c, L, t = found[0], found[1], t - 1

    def _arrive(self, M, c, t, L, op, vany, free, steps):
        """c reached by a move arrival at time t in layer L (for op)."""
        TU, TC, AU, AC = M
        nx, ny = free.shape
        T = TU if L == "U" else TC
        i, j = c
        i0, i1 = max(0, i - K), min(nx, i + K + 1)
        j0, j1 = max(0, j - K), min(ny, j + K + 1)
        cand = np.argwhere(T[i0:i1, j0:j1] <= t - 1)
        a, b = cand[0]
        steps.append((c, op))
        return (i0 + a, j0 + b), t - 1, L

    def _extract(self, res, S):
        if S is None or S not in res["final"]:
            return []
        X, Y, free, vany = res["X"], res["Y"], res["free"], res["vany"]
        v, j, extra = res["final"][S]
        steps = []
        homereg = res["homereg"]
        # final stage maps
        if extra is not None:
            op, M2 = extra
            at = np.minimum(M2[0], M2[1])
            vv = np.where(homereg, at, INF)
            c = np.unravel_index(np.argmin(vv), vv.shape); t = int(vv[c])
            L = "U" if M2[0][c] <= t else "C"
            # send stage seeds are U only
            c, t, L = self._back_stage(M2, op, np.full(op.shape, INF, np.int32), vany, free, c, t, L, steps)
            Mprev = res["maps"][(S, j)] if S else res["start_maps"]
            TU, TC, AU, AC = Mprev
            Lp = "U" if AU[c] == t else "C"
            c, t, L = self._arrive(Mprev, c, t, Lp, "send", vany, free, steps)
        else:
            Mprev = res["maps"][(S, j)] if S else res["start_maps"]
            at = np.minimum(Mprev[0], Mprev[1])
            vv = np.where(homereg, at, INF)
            c = np.unravel_index(np.argmin(vv), vv.shape); t = int(vv[c])
            L = "U" if Mprev[0][c] <= t else "C"
        # walk back through task stages
        curS, curj = S, j
        while curS:
            M = res["maps"][(curS, curj)]
            sU, sC = res["seeds"][(curS, curj)]
            c, t, L = self._back_stage(M, sU, sC, vany, free, c, t, L, steps)
            kind = res["regions"][curj][0]
            prevS = curS & ~(1 << curj)
            # find predecessor
            found = None
            if prevS == 0:
                cands = [(None, res["start_maps"])]
            else:
                cands = [(pj, res["maps"][(prevS, pj)]) for pj in range(len(res["regions"]))
                         if (prevS >> pj & 1) and (prevS, pj) in res["maps"]]
            if kind != "img":
                # undo the forced drop step
                reg = res["regions"][curj][1]
                nx, ny = free.shape
                i, jj = c
                i0, i1 = max(0, i - K), min(nx, i + K + 1)
                j0, j1 = max(0, jj - K), min(ny, jj + K + 1)
                hit = None
                for pj, Mp in cands:
                    A = Mp[2] if L == "U" else Mp[3]
                    sub = np.where(reg[i0:i1, j0:j1], A[i0:i1, j0:j1], INF)
                    cand = np.argwhere(sub == t - 1)
                    if len(cand):
                        hit = (pj, Mp, (i0 + cand[0][0], j0 + cand[0][1]))
                        break
                if hit is None:
                    raise RuntimeError("drop pred not found")
                steps.append((c, "drop"))
                c = hit[2]; t -= 1
                cands = [(hit[0], hit[1])]
            for pj, Mp in cands:
                TU, TC, AU, AC = Mp
                if kind == "img":
                    if L == "U" and AC[c] == t:
                        found = (pj, Mp, "C"); break
                else:
                    if L == "U" and AU[c] == t:
                        found = (pj, Mp, "U"); break
                    if L == "C" and AC[c] == t:
                        found = (pj, Mp, "C"); break
            if found is None:
                raise RuntimeError("pred not found")
            pj, Mp, Lp = found
            c, t, L = self._arrive(Mp, c, t, Lp, ("image:" + res["img_obj"][curj]) if kind == "img" else ("sample:" + res["names"][curj][1]), vany, free, steps)
            curS, curj = prevS, pj
        # back to start
        sU, sC = res["s0"]
        c, t, L = self._back_stage(res["start_maps"], sU, sC, vany, free, c, t, L, steps)
        if res["store_full"] and t == 1:
            steps.append((c, "drop"))
        steps.reverse()
        return [((float(X[c]), float(Y[c])), op) for c, op in steps]

    # -------------------------------------------------------------- acting
    def get_action(self, state):
        rnames = sorted(self.w.rovers.keys())
        if self.expect is not None and self._deviated(state):
            self.nreplan += 1
            if self.plan_time < 40.0:
                try:
                    self._plan(state)
                except Exception:
                    self.plans = {r: [] for r in rnames}
                    self.t = 0
        act = np.zeros(8, np.float32)
        self.expect = {}
        for k, r in enumerate(rnames):
            o = self.w.rovers[r]
            x = self._get(state, o, "x"); y = self._get(state, o, "y")
            th = self._get(state, o, "theta")
            plan = self.plans.get(r, [])
            if self.t < len(plan):
                (tx, ty), op = plan[self.t]
            else:
                tx, ty = x, y
                op = "none"
                hx, hy = self.home[r]
                if math.hypot(x - hx, y - hy) > HOME_R:
                    tx, ty = hx, hy
            store = self._get(state, o, "store_full") > 0.5
            if op == "none" and store:
                op = "drop"
            dx = float(np.clip(tx - x, -0.2, 0.2)); dy = float(np.clip(ty - y, -0.2, 0.2))
            dth = float(np.clip(wrap(self.home_theta[r] - th), -0.4, 0.4))
            act[4 * k:4 * k + 4] = [dx, dy, dth, SEL[op.split(":")[0]]]
            self.expect[r] = (x + dx, y + dy, op, self._snapshot(state, r))
        self.t += 1
        return act

    def _snapshot(self, state, r):
        o = self.w.rovers[r]
        g = lambda ob, f: self._get(state, ob, f)
        imgs = sum(g(ob, "have_image_" + r) for ob in self.w.objectives)
        recv = sum(g(ob, "received_image") for ob in self.w.objectives) + \
            sum(g(s, "received_analysis") for s in self.w.samples)
        return (g(o, "store_full"), g(o, "calibrated"), imgs, recv)

    def _deviated(self, state):
        for r, (ex, ey, op, snap) in self.expect.items():
            o = self.w.rovers[r]
            x = self._get(state, o, "x"); y = self._get(state, o, "y")
            if abs(x - ex) > 1e-3 or abs(y - ey) > 1e-3:
                self.bad_points.append((ex, ey))
                self.log.append(("move", r, round(ex, 3), round(ey, 3)))
                return True
            store, cal, imgs, recv = self._snapshot(state, r)
            if op.startswith("sample") and store < 0.5:
                self.log.append(("sample", r, op, round(x, 3), round(y, 3)))
                return True
            if op.startswith("sample:"):
                soil = 1.0 if op[7:] == "soil" else 0.0
                if not any(self._get(state, sm, "analyzed_" + r) > 0.5 for sm in self.w.samples
                           if abs(self._get(state, sm, "is_soil") - soil) < 0.5):
                    self.log.append(("samplekind", r, op, round(x, 3), round(y, 3)))
                    return True
            if op == "calibrate" and cal < 0.5:
                self.bad_view[r].append((x, y))
                self.log.append(("calib", r, round(x, 3), round(y, 3)))
                return True
            if op.startswith("image:"):
                tgt = [ob for ob in self.w.objectives if ob.name == op[6:]][0]
                if self._get(state, tgt, "have_image_" + r) < 0.5:
                    self.log.append(("image", r, op, round(x, 3), round(y, 3), imgs > snap[2]))
                    if imgs <= snap[2]:
                        self.bad_view[r].append((x, y))
                    return True
            if op == "image" and imgs <= snap[2]:
                self.bad_view[r].append((x, y))
                return True
            if op == "send" and self._unsent(state, r):
                lx = self._get(state, self.w.lander, "x"); ly = self._get(state, self.w.lander, "y")
                cx, cy = self._cam(r, x, y)
                sector = True
                for o2, ob2 in self.w.rovers.items():
                    if o2 != r:
                        ox = self._get(state, ob2, "x"); oy = self._get(state, ob2, "y")
                        if float(seg_point_dist(np.array(cx), np.array(cy), lx, ly, ox, oy)) < 0.45:
                            sector = False
                self.bad_send[r].append((x, y, sector))
                self.log.append(("send", r, round(x, 3), round(y, 3)))
                return True
        return False

    def _unsent(self, state, r):
        g = lambda ob, f: self._get(state, ob, f)
        for ob in self.w.objectives:
            if g(ob, "have_image_" + r) > 0.5 and g(ob, "received_image") < 0.5:
                return True
        for s in self.w.samples:
            if g(s, "analyzed_" + r) > 0.5 and g(s, "received_analysis") < 0.5:
                return True
        return False
