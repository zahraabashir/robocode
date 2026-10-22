"""Rovers approach: staged grid BFS planner per rover + joint task assignment."""
import itertools
import math

import numpy as np
from scipy.ndimage import minimum_filter

INF = 10 ** 6
RES = 0.05            # grid resolution
WIN = 4               # max cells per step per axis (0.2 / RES)
SEL = {"sample": -0.8333, "cal": -0.5, "img": -0.1667, "noop": 0.1667,
       "send": 0.5, "drop": 0.8333}

# geometry constants (empirically probed)
WALL_IN = 0.2271 + 0.004
ARENA = 2.2729 - 0.004
PILLAR_R = 0.245
MOUND_R = 0.185
LANDER_XMIN = -1.15
LANDER_YMIN = -1.42
OBJ_RANGE = 1.993
LANDER_RANGE = 3.995
SAMPLE_R = 0.246
HOME_R = 0.235
IMG_TH = -math.pi / 2
ROT_IMG = 4.0
FINE_RES = 0.025
PILLAR_INFL_OBJ = 0.015
PILLAR_INFL_LAND = 0.04
ROVER_OCC_R = 0.26
CAM_OFF = (-0.087, -0.0125)
OBJ_BACK_DEG = 108.0     # if |rel bearing| > this, pillars don't occlude objectives
LAND_BACK_DEG = 110.0    # same quirk for lander (sending)
USE_BACK_OBJ = True
USE_BACK_LAND = True


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def rot_steps(a, b):
    d = abs(float(_wrap(b - a)))
    return int(math.ceil(d / 0.4 - 1e-6))


def approach_angle(a, b, dmax):
    d = float(_wrap(b - a))
    if abs(d) <= dmax:
        return float(_wrap(b))
    return float(_wrap(a + math.copysign(dmax, d)))


def seg_hits_box(px, py, qx, qy, cx, cy, hx, hy):
    """Vectorised: does segment p->q (p arrays, q scalar) intersect AABB?"""
    dx = qx - px
    dy = qy - py
    t0 = np.zeros_like(px)
    t1 = np.ones_like(px)
    ok = np.ones(px.shape, dtype=bool)
    for d, p, lo, hi in ((dx, px, cx - hx, cx + hx), (dy, py, cy - hy, cy + hy)):
        small = np.abs(d) < 1e-12
        ok &= ~(small & ((p < lo) | (p > hi)))
        with np.errstate(divide="ignore", invalid="ignore"):
            ta = (lo - p) / d
            tb = (hi - p) / d
        tmin = np.where(small, -np.inf, np.minimum(ta, tb))
        tmax = np.where(small, np.inf, np.maximum(ta, tb))
        t0 = np.maximum(t0, tmin)
        t1 = np.minimum(t1, tmax)
    return ok & (t0 <= t1)


def seg_hits_disk(px, py, qx, qy, cx, cy, r):
    dx = qx - px
    dy = qy - py
    L2 = dx * dx + dy * dy + 1e-12
    t = np.clip(((cx - px) * dx + (cy - py) * dy) / L2, 0, 1)
    ex = px + t * dx - cx
    ey = py + t * dy - cy
    return ex * ex + ey * ey < r * r


def box_dist(px, py, cx, cy, hx, hy):
    ddx = np.maximum(np.abs(px - cx) - hx, 0)
    ddy = np.maximum(np.abs(py - cy) - hy, 0)
    return np.hypot(ddx, ddy)


def propagate(f, free, win=WIN):
    f = np.where(free, f, INF)
    while True:
        m = minimum_filter(f, size=2 * win + 1, mode="constant", cval=INF) + 1
        nf = np.where(free, np.minimum(f, m), INF)
        if np.array_equal(nf, f):
            return f
        f = nf


def op_stage(fprev, region, win=WIN):
    m = minimum_filter(fprev, size=2 * win + 1, mode="constant", cval=INF) + 1
    return np.where(region, np.minimum(m, INF), INF)


class Scene:
    def __init__(self, state):
        self.rovers = {}
        self.objectives = []
        self.samples = []
        self.pillars = []
        self.mounds = []
        self.lander = (-1.9, -2.0)
        objs = [state.get_object_from_name(nm) for nm in sorted(state.get_object_names())]
        for o in objs:
            t = o.type.name
            g = lambda f: state.get(o, f)
            if t == "rover":
                self.rovers[o.name] = dict(x=g("x"), y=g("y"), th=g("theta"),
                                           full=g("store_full") > 0.5,
                                           cal=g("calibrated") > 0.5)
            elif t == "lander":
                self.lander = (g("x"), g("y"))
            elif t == "objective":
                self.objectives.append(dict(name=o.name, x=g("x"), y=g("y"),
                                            img=(g("have_image_rover0") > 0.5,
                                                 g("have_image_rover1") > 0.5),
                                            recv=g("received_image") > 0.5))
            elif t == "sample":
                self.samples.append(dict(name=o.name, x=g("x"), y=g("y"),
                                         soil=g("is_soil") > 0.5,
                                         an=(g("analyzed_rover0") > 0.5,
                                             g("analyzed_rover1") > 0.5),
                                         recv=g("received_analysis") > 0.5))
            elif t == "obstacle":
                d = (g("x"), g("y"), g("half_x"), g("half_y"))
                if g("half_x") > 0.15:
                    self.mounds.append(d)
                else:
                    self.pillars.append(d)


class RoverPlanner:
    """Grid + regions for one rover."""

    def __init__(self, idx, home, scene, other_pos_list, cur_th=None, bad=(), img_th=None,
                 res=RES):
        self.ctor = (idx, home, scene, other_pos_list, cur_th, bad, img_th)
        self.res = res
        self.win = int(round(0.2 / res))
        self.idx = idx
        self.home = home  # (x, y, th)
        hx, hy, th = home
        self.th = th
        side = 1 if hx > 0 else -1
        lo_x, hi_x = (WALL_IN, ARENA) if side > 0 else (-ARENA, -WALL_IN)
        i0 = math.ceil((lo_x - hx) / res - 1e-9)
        i1 = math.floor((hi_x - hx) / res + 1e-9)
        j0 = math.ceil((-ARENA - hy) / res - 1e-9)
        j1 = math.floor((ARENA - hy) / res + 1e-9)
        self.xs = hx + res * np.arange(i0, i1 + 1)
        self.ys = hy + res * np.arange(j0, j1 + 1)
        self.hi = -i0
        self.hj = -j0
        X, Y = np.meshgrid(self.xs, self.ys, indexing="ij")
        self.X, self.Y = X, Y
        free = np.ones(X.shape, dtype=bool)
        for (cx, cy, ax, ay) in scene.pillars:
            free &= box_dist(X, Y, cx, cy, ax, ay) > PILLAR_R
        for (cx, cy, ax, ay) in scene.mounds:
            free &= box_dist(X, Y, cx, cy, ax, ay) > MOUND_R
        free &= (X >= LANDER_XMIN) | (Y >= LANDER_YMIN)
        for (bx, by) in bad:
            free &= np.hypot(X - bx, Y - by) > 0.03
        free[self.hi, self.hj] = True
        self.free = free
        self.home_reg = (np.hypot(X - hx, Y - hy) <= HOME_R) & free
        self.home_reg[self.hi, self.hj] = True
        c, s = math.cos(th), math.sin(th)
        self.camx = X + c * CAM_OFF[0] - s * CAM_OFF[1]
        self.camy = Y + s * CAM_OFF[0] + c * CAM_OFF[1]
        self.scene = scene
        ith = th if img_th is None else img_th
        self.img_th = ith
        cur = th if cur_th is None else cur_th
        self.cur_th = cur
        self.nrot_in = rot_steps(cur, ith)
        self.nrot_out = rot_steps(ith, th)
        hs = [cur, ith, th]
        for k in range(1, 9):
            hs.append(approach_angle(cur, ith, 0.4 * k))
            hs.append(approach_angle(ith, th, 0.4 * k))
            hs.append(approach_angle(cur, th, 0.4 * k))
        self.headings = hs
        ci, si = math.cos(ith), math.sin(ith)
        camx_i = X + ci * CAM_OFF[0] - si * CAM_OFF[1]
        camy_i = Y + si * CAM_OFF[0] + ci * CAM_OFF[1]
        # objective visibility
        self.vis = []
        self.objd = []
        for ob in scene.objectives:
            ox, oy = ob["x"], ob["y"]
            d = np.hypot(ox - camx_i, oy - camy_i)
            v = (d <= OBJ_RANGE)
            occ = np.zeros(X.shape, dtype=bool)
            for (cx, cy, ax, ay) in scene.pillars:
                e = PILLAR_INFL_OBJ
                occ |= seg_hits_box(camx_i, camy_i, ox, oy, cx, cy, ax + e, ay + e)
                occ |= seg_hits_box(X, Y, ox, oy, cx, cy, ax + e, ay + e)
            if USE_BACK_OBJ:
                rel = np.abs(_wrap(np.arctan2(oy - Y, ox - X) - ith))
                back = rel > math.radians(OBJ_BACK_DEG)
            else:
                back = np.zeros(X.shape, dtype=bool)
            occ2 = np.zeros(X.shape, dtype=bool)
            for (px, py) in other_pos_list:
                occ2 |= seg_hits_disk(camx_i, camy_i, ox, oy, px, py, ROVER_OCC_R)
            self.vis.append(v & ((~occ) | back) & ~occ2 & free)
            self.objd.append(d)
        self.any_vis = np.zeros(X.shape, dtype=bool)
        for v in self.vis:
            self.any_vis |= v
        # lander visibility (must hold for every heading along the rotation path)
        lx, ly = scene.lander
        land = free.copy()
        land_free = free.copy()
        for hh in self.headings:
            ch, sh = math.cos(hh), math.sin(hh)
            cx_ = X + ch * CAM_OFF[0] - sh * CAM_OFF[1]
            cy_ = Y + sh * CAM_OFF[0] + ch * CAM_OFF[1]
            v = (np.hypot(lx - X, ly - Y) <= LANDER_RANGE) & \
                (np.hypot(lx - cx_, ly - cy_) <= LANDER_RANGE)
            occ = np.zeros(X.shape, dtype=bool)
            for (cx, cy, ax, ay) in scene.pillars:
                e = PILLAR_INFL_LAND
                occ |= seg_hits_box(X, Y, lx, ly, cx, cy, ax + e, ay + e)
                occ |= seg_hits_box(cx_, cy_, lx, ly, cx, cy, ax + e, ay + e)
            if USE_BACK_LAND:
                rel = np.abs(_wrap(np.arctan2(ly - Y, lx - X) - hh))
                back = rel > math.radians(LAND_BACK_DEG)
            else:
                back = np.zeros(X.shape, dtype=bool)
            occ2 = np.zeros(X.shape, dtype=bool)
            for (px, py) in other_pos_list:
                occ2 |= seg_hits_disk(X, Y, lx, ly, px, py, ROVER_OCC_R)
                occ2 |= seg_hits_disk(cx_, cy_, lx, ly, px, py, ROVER_OCC_R)
            land &= v & ((~occ) | back) & ~occ2
            land_free &= v & ((~occ) | back)
        self.land = land
        self.land_free = land_free
        self.camx_i, self.camy_i = camx_i, camy_i
        # samples
        self.sreg = {}
        dk = {}
        for kind in ("stone", "soil"):
            d = np.full(X.shape, 1e9)
            for sm in scene.samples:
                if sm["soil"] == (kind == "soil"):
                    d = np.minimum(d, np.hypot(sm["x"] - X, sm["y"] - Y))
            dk[kind] = d
        for kind, oth in (("stone", "soil"), ("soil", "stone")):
            r = (dk[kind] <= SAMPLE_R) & ((dk[oth] > 0.26) | (dk[oth] > dk[kind] + 0.03))
            self.sreg[kind] = r & free

    def cell_of(self, x, y):
        i = int(round((x - self.xs[0]) / self.res))
        j = int(round((y - self.ys[0]) / self.res))
        i = min(max(i, 0), len(self.xs) - 1)
        j = min(max(j, 0), len(self.ys) - 1)
        return i, j

    def img_region(self, k, imaged):
        """cells where image would photograph objective k given set imaged."""
        reg = self.vis[k].copy()
        if not reg.any():
            return reg
        dk = self.objd[k]
        for m in range(len(self.vis)):
            if m == k or m in imaged:
                continue
            reg &= ~((self.objd[m] <= 2.03) & (self.objd[m] < dk + 0.03))
        return reg


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.homes = None

    # ------------------------------------------------------------------
    def reset(self, state, info):
        sc = Scene(state)
        self.homes = {n: (r["x"], r["y"], r["th"]) for n, r in sc.rovers.items()}
        self.replans = 0
        self.fail_count = 0
        self.expect = [None, None]
        self.prev_sc = sc
        self.log = []
        self.bad = [[], []]
        import time as _t
        self.t_start = _t.time()
        self._plan(state)

    # ------------------------------------------------------------------
    def _rover_tables(self, ri, sc, need_objs, need_stone, need_soil, pending):
        name = "rover%d" % ri
        r = sc.rovers[name]
        other = sc.rovers["rover%d" % (1 - ri)]
        ohome = self.homes["rover%d" % (1 - ri)]
        occl = [(ohome[0], ohome[1])]
        if math.hypot(other["x"] - ohome[0], other["y"] - ohome[1]) > 0.05:
            occl.append((other["x"], other["y"]))
        merged = {}
        hth = self.homes[name][2]
        if IMG_TH is None:
            ths = [hth]
        else:
            d = float(_wrap(IMG_TH - hth))
            ths = [float(_wrap(hth + math.copysign(min(abs(d), ROT_IMG), d)))]
        for ith in ths:
            P, table = self._rover_tables_h(ri, sc, need_objs, need_stone, need_soil,
                                            pending, occl, ith)
            for k, (c, st) in table.items():
                if k not in merged or c < merged[k][0]:
                    merged[k] = (c, st, P)
        return None, merged

    def _rover_tables_h(self, ri, sc, need_objs, need_stone, need_soil, pending, occl, ith):
        name = "rover%d" % ri
        r = sc.rovers[name]
        P = RoverPlanner(ri, self.homes[name], sc, occl, r["th"], self.bad[ri], ith)
        self_planner = P
        start = P.cell_of(r["x"], r["y"])
        P.free[start] = True
        f0 = np.full(P.free.shape, INF, dtype=np.int64)
        f0[start] = 0
        stages0 = []
        F = propagate(f0, P.free, P.win)
        stages0.append(("start", None, f0, F))
        if r["full"]:
            G = op_stage(F, P.free, P.win)
            F = propagate(G, P.free, P.win)
            stages0.append(("drop", None, G, F))
        imaged0 = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
        tasks = []
        for k in need_objs:
            if P.vis[k].any():
                tasks.append(("obj", k))
        if need_stone and P.sreg["stone"].any():
            tasks.append(("stone", None))
        if need_soil and P.sreg["soil"].any():
            tasks.append(("soil", None))
        hcell = (P.hi, P.hj)
        table = {}  # frozenset(task keys) -> (cost, stages)

        def finish(F, stages, done_keys):
            if not done_keys and not pending:
                cost = F[P.home_reg].min()
                st = stages
            else:
                G = op_stage(F, P.land, P.win)
                F2 = propagate(G, P.free, P.win)
                cost = F2[P.home_reg].min()
                st = stages + [("send", None, G, F2)]
            if cost >= INF:
                return
            key = frozenset(done_keys)
            if key not in table or cost < table[key][0]:
                table[key] = (int(cost), st)

        def dfs(F, stages, done_keys, imaged, cal):
            finish(F, stages, done_keys)
            if F.min() >= INF:
                return
            for t in tasks:
                key = t if t[0] != "obj" else ("obj", t[1])
                if key in done_keys:
                    continue
                if t[0] == "obj":
                    k = t[1]
                    st = list(stages)
                    Fc = F
                    if not cal:
                        G = op_stage(F, P.any_vis, P.win)
                        G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
                        Fc = propagate(G, P.free, P.win)
                        st.append(("cal", None, G, Fc))
                    reg = P.img_region(k, imaged)
                    G = op_stage(Fc, reg, P.win)
                    G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
                    Fi = propagate(G, P.free, P.win)
                    st.append(("img", k, G, Fi))
                    dfs(Fi, st, done_keys | {key}, imaged | {k}, False)
                else:
                    G = op_stage(F, P.sreg[t[0]], P.win)
                    Fs = propagate(G, P.free, P.win)
                    G2 = op_stage(Fs, P.free, P.win)
                    Fd = propagate(G2, P.free, P.win)
                    st = stages + [("sample", t[0], G, Fs), ("drop", None, G2, Fd)]
                    dfs(Fd, st, done_keys | {key}, imaged, cal)

        dfs(F, stages0, frozenset(), imaged0, r["cal"])
        return P, table

    def _plan(self, state):
        import time as _t
        self._fine_cache = {}
        self._fast = (_t.time() - self.t_start) > 20.0
        sc = Scene(state)
        self.scene = sc
        # what is needed
        need_objs = [k for k, ob in enumerate(sc.objectives)
                     if not ob["recv"] and not ob["img"][0] and not ob["img"][1]]
        pending = [False, False]
        for k, ob in enumerate(sc.objectives):
            if not ob["recv"]:
                for ri in range(2):
                    if ob["img"][ri]:
                        pending[ri] = True
        need = {}
        for kind in ("stone", "soil"):
            recv = any(s["recv"] for s in sc.samples if s["soil"] == (kind == "soil"))
            holders = [ri for ri in range(2)
                       if any(s["an"][ri] for s in sc.samples if s["soil"] == (kind == "soil"))]
            if recv:
                need[kind] = False
            elif holders:
                need[kind] = False
                pending[holders[0]] = True
            else:
                need[kind] = True
        tabs = []
        for ri in range(2):
            tabs.append(self._rover_tables(ri, sc, need_objs, need["stone"], need["soil"],
                                           pending[ri]))
        # joint assignment
        best = None
        cands = []
        n = len(need_objs)
        stone_opts = [0, 1] if need["stone"] else [None]
        soil_opts = [0, 1] if need["soil"] else [None]
        for assign in itertools.product([0, 1], repeat=n):
            for so in stone_opts:
                for sl in soil_opts:
                    sets = [set(), set()]
                    for k, a in zip(need_objs, assign):
                        sets[a].add(("obj", k))
                    if so is not None:
                        sets[so].add(("stone", None))
                    if sl is not None:
                        sets[sl].add(("soil", None))
                    costs = []
                    for ri in range(2):
                        e = tabs[ri][1].get(frozenset(sets[ri]))
                        costs.append(e)
                    if costs[0] is None or costs[1] is None:
                        continue
                    key = (max(costs[0][0], costs[1][0]), costs[0][0] + costs[1][0])
                    cands.append((key, costs))
                    if best is None or key < best[0]:
                        self.pred = key
                        best = (key, costs)
        self.actions = [[], []]
        if best is None:
            return
        cands.sort(key=lambda c: c[0])
        seen = set()
        bestreal = None
        for key, costs in cands:
            sig = (id(costs[0][1]), id(costs[1][1]))
            if sig in seen:
                continue
            seen.add(sig)
            if len(seen) > 6 or (bestreal is not None and key[0] >= bestreal[0][0]):
                break
            acts = self._realize(sc, tabs, costs)
            real = (max(len(acts[0]), len(acts[1])), len(acts[0]) + len(acts[1]))
            if bestreal is None or real < bestreal[0]:
                bestreal = (real, acts)
        self.actions = bestreal[1]

    def _refine(self, entry):
        """Replay a coarse stage sequence on a fine grid."""
        cost, stages, Pc = entry
        if FINE_RES is None or FINE_RES >= Pc.res or self._fast:
            return entry
        ri = Pc.ctor[0]
        ck = (ri, Pc.img_th)
        if ck in self._fine_cache:
            P = self._fine_cache[ck]
            P.free = P.free0.copy()
        else:
            P = RoverPlanner(*Pc.ctor, res=FINE_RES)
            P.free0 = P.free.copy()
            self._fine_cache[ck] = P
        sc = self.scene
        r = sc.rovers["rover%d" % ri]
        imaged = set(k for k, ob in enumerate(sc.objectives) if ob["img"][ri])
        start = P.cell_of(r["x"], r["y"])
        P.free[start] = True
        out = []
        F = None
        for name, arg, _, _ in stages:
            if name == "start":
                G = np.full(P.free.shape, INF, dtype=np.int64)
                G[start] = 0
            elif name == "drop":
                G = op_stage(F, P.free, P.win)
            elif name == "cal":
                G = op_stage(F, P.any_vis, P.win)
                G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
            elif name == "img":
                G = op_stage(F, P.img_region(arg, imaged), P.win)
                G = np.where(G < INF, np.maximum(G, P.nrot_in), INF)
                imaged = imaged | {arg}
            elif name == "sample":
                G = op_stage(F, P.sreg[arg], P.win)
            elif name == "send":
                G = op_stage(F, P.land, P.win)
            else:
                return entry
            F = propagate(G, P.free, P.win)
            out.append((name, arg, G, F))
        c = F[P.home_reg].min()
        if c >= INF:
            return entry
        return (int(c), out, P)

    def _realize(self, sc, tabs, costs):
        costs = [self._refine(costs[0]), self._refine(costs[1])]
        best = (None, costs)
        actions = [[], []]
        sc = self.scene
        for ri in range(2):
            P = costs[ri][2]
            actions[ri] = self._extract(P, best[1][ri][1])
        # time-aware re-plan of final send against other rover's trajectory
        trajs = []
        for ri in range(2):
            r = sc.rovers["rover%d" % ri]
            trajs.append([(r["x"], r["y"])] + [(a[0], a[1]) for a in actions[ri]])
        new_actions = list(actions)
        for ri in range(2):
            stages = best[1][ri][1]
            if stages[-1][0] != "send":
                continue
            P = costs[ri][2]
            Fprev = stages[-2][3]
            G0 = op_stage(Fprev, P.land_free, P.win)
            other = trajs[1 - ri]
            G = np.full(G0.shape, INF, dtype=G0.dtype)
            pending_mask = G0 < INF
            tmin = int(G0[pending_mask].min()) if pending_mask.any() else INF
            lx, ly = sc.lander
            t = tmin
            while pending_mask.any() and t < tmin + 200:
                blk = np.zeros(P.X.shape, dtype=bool)
                for tt in (t - 1, t):
                    ox, oy = other[max(0, min(tt, len(other) - 1))]
                    blk |= seg_hits_disk(P.camx, P.camy, lx, ly, ox, oy, ROVER_OCC_R)
                    blk |= seg_hits_disk(P.camx_i, P.camy_i, lx, ly, ox, oy, ROVER_OCC_R)
                ok = pending_mask & (G0 <= t) & ~blk
                G[ok] = t
                pending_mask &= ~ok
                if t >= len(other) - 1 and not ok.any() and (G0 <= t).all():
                    break
                t += 1
            F2 = propagate(G, P.free, P.win)
            if F2[P.home_reg].min() >= INF:
                continue
            st = stages[:-1] + [("send_t", None, G, F2)]
            new_actions[ri] = self._extract(P, st)
        return [self._schedule(costs[ri][2], new_actions[ri]) for ri in range(2)]

    def _schedule(self, P, seq):
        """Attach headings; append waits so the rover can rotate back home."""
        home_th = P.th
        t_img = [t for t, a in enumerate(seq, 1) if a[2] and a[2][0] in ("cal", "img")]
        seq = list(seq)
        out = []
        if t_img:
            last = max(t_img)
            while len(seq) < last + P.nrot_out:
                x, y = (seq[-1][0], seq[-1][1])
                seq.append((x, y, None))
            T = len(seq)
            for t, (x, y, op) in enumerate(seq, 1):
                if t <= T - P.nrot_out:
                    h = approach_angle(P.cur_th, P.img_th, 0.4 * t)
                else:
                    h = approach_angle(P.img_th, home_th, 0.4 * (t - (T - P.nrot_out)))
                out.append((x, y, op, h))
        else:
            while len(seq) < rot_steps(P.cur_th, home_th):
                x, y = (seq[-1][0], seq[-1][1]) if seq else (float(P.xs[P.hi]), float(P.ys[P.hj]))
                seq.append((x, y, None))
            for t, (x, y, op) in enumerate(seq, 1):
                out.append((x, y, op, approach_angle(P.cur_th, home_th, 0.4 * t)))
        return out

    def _extract(self, P, stages):
        """Backtrack through stage fields (waiting allowed); list of (x,y,op)."""
        k = len(stages) - 1
        Ff = np.where(P.home_reg, stages[k][3], INF)
        cell = np.unravel_index(int(np.argmin(Ff)), Ff.shape)
        cell = (int(cell[0]), int(cell[1]))
        v = int(stages[k][3][cell])
        seq = []
        W = P.win
        nx, ny = P.free.shape

        def nb(Fsrc, i, j, cond):
            best = None
            for di in range(-W, W + 1):
                for dj in range(-W, W + 1):
                    a, b = i + di, j + dj
                    if 0 <= a < nx and 0 <= b < ny and cond(Fsrc[a, b]):
                        c = abs(di) + abs(dj)
                        if best is None or c < best[1]:
                            best = ((a, b), c)
            return best[0] if best else None

        guard = 0
        while not (k == 0 and v == 0) and guard < 5000:
            guard += 1
            name, arg, G, F = stages[k]
            i, j = cell
            timed = name == "send_t"
            choice = None
            for mode in (0, 1):
                if k > 0:
                    okop = (G[cell] == v) if (mode == 0 or timed) else (G[cell] <= v)
                    if okop:
                        Fp = stages[k - 1][3]
                        c = nb(Fp, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
                        if c is not None:
                            choice = (c, (name.replace("_t", ""), arg), k - 1)
                            break
                c = nb(F, i, j, (lambda x: x == v - 1) if mode == 0 else (lambda x: x <= v - 1))
                if c is not None:
                    choice = (c, None, k)
                    break
            if choice is None:
                break
            seq.append((float(P.xs[cell[0]]), float(P.ys[cell[1]]), choice[1]))
            cell, k = choice[0], choice[2]
            v -= 1
        seq.reverse()
        return seq

    # ------------------------------------------------------------------
    def get_action(self, state):
        act = np.zeros(8, dtype=np.float32)
        sc = Scene(state)
        if self._deviated(sc) or (not self.actions[0] and not self.actions[1]):
            self.replans += 1
            import time as _t
            if self.replans < 60 and (_t.time() - self.t_start) < 45.0:
                self._plan(state)
        for ri in range(2):
            r = sc.rovers["rover%d" % ri]
            if self.actions[ri]:
                x, y, op, h = self.actions[ri].pop(0)
                dx = float(np.clip(x - r["x"], -0.2, 0.2))
                dy = float(np.clip(y - r["y"], -0.2, 0.2))
                act[4 * ri] = dx
                act[4 * ri + 1] = dy
                act[4 * ri + 3] = SEL[op[0]] if op else 0.0
                act[4 * ri + 2] = float(np.clip(_wrap(h - r["th"]), -0.4, 0.4))
                self.expect[ri] = (x, y, op, h)
            else:
                # at end: if at home do nothing
                self.expect[ri] = None
        return act

    def _deviated(self, sc):
        dev = False
        for ri in range(2):
            e = self.expect[ri]
            if e is None:
                continue
            d0 = dev
            dev = False
            r = sc.rovers["rover%d" % ri]
            if abs(r["x"] - e[0]) > 1e-3 or abs(r["y"] - e[1]) > 1e-3 or \
                    abs(float(_wrap(r["th"] - e[3]))) > 1e-3:
                dev = True
                self.log.append(("move", ri, e, r["x"], r["y"]))
                self.bad[ri].append((e[0], e[1]))
            op, arg = e[2] if e[2] else (None, None)
            pr = self.prev_sc.rovers["rover%d" % ri]
            if op == "img":
                ob = sc.objectives[arg]
                if not ob["img"][ri]:
                    dev = True
            if op == "sample":
                if not any(s["an"][ri] for s in sc.samples if s["soil"] == (arg == "soil")):
                    dev = True
            if op == "cal" and not r["cal"]:
                dev = True
            elif op == "img" and (r["cal"] or not pr["cal"]):
                dev = True
            elif op == "sample" and not r["full"]:
                dev = True
            elif op == "drop" and r["full"]:
                dev = True
            elif op == "send":
                for ob in sc.objectives:
                    if ob["img"][ri] and not ob["recv"]:
                        dev = True
                for s in sc.samples:
                    if s["an"][ri] and not s["recv"]:
                        dev = True
            if dev:
                self.log.append(("dev", ri, e, round(r["x"], 3), round(r["y"], 3), r["cal"], pr["cal"],
                                 [ob["img"][ri] for ob in sc.objectives]))
            dev = dev or d0
        self.prev_sc = sc
        self.expect = [None, None]
        return dev
