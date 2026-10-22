"""Rovers approach: grid planner + Held-Karp task assignment + DP-field execution."""
import itertools
import math

import numpy as np
from scipy.ndimage import minimum_filter

RES = 0.05
LIM = 2.25
N = int(round(2 * LIM / RES)) + 1  # 91
COORDS = -LIM + RES * np.arange(N)
GX, GY = np.meshgrid(COORDS, COORDS, indexing="ij")  # [i,j] -> x=COORDS[i], y=COORDS[j]
STEP_CELLS = 4  # 0.2 / 0.05

SEL = {"sample": -5 / 6, "calibrate": -0.5, "image": -1 / 6, "noop": 0.0,
       "send": 0.5, "drop": 5 / 6}

# geometry margins
WALL_X = 0.25
MOUND_CLEAR = 0.19
PILLAR_CLEAR = 0.165
LANDER_CLEAR = 0.76
OBJ_RANGE = 1.975
LANDER_RANGE = 3.965
LOS_PILLAR = 0.085
LOS_ROVER = 0.24
SAMPLE_RANGE = 0.24
TRUE_OBJ = 1.99
TRUE_LANDER = 3.98
TRUE_PILLAR = 0.075
TRUE_ROVER = 0.24
SENSE_BACK = 0.087
SENSE_RIGHT = 0.012
INF = 1e9


def _val(s, o, f):
    return float(s.get(o, f))


def parse(state):
    d = {"objective": [], "sample": [], "obstacle": [], "rover": {}, "lander": None}
    for name in state.get_object_names():
        o = state.get_object_from_name(name)
        t = o.type.name
        if t == "rover":
            d["rover"][name] = {f: _val(state, o, f) for f in
                                ("x", "y", "theta", "store_full", "calibrated", "at_home")}
        elif t == "lander":
            d["lander"] = (_val(state, o, "x"), _val(state, o, "y"))
        elif t == "objective":
            d["objective"].append((name, {f: _val(state, o, f) for f in
                                          ("x", "y", "z", "have_image_rover0", "have_image_rover1",
                                           "received_image")}))
        elif t == "sample":
            d["sample"].append((name, {f: _val(state, o, f) for f in
                                       ("x", "y", "z", "is_soil", "analyzed_rover0",
                                        "analyzed_rover1", "received_analysis")}))
        elif t == "obstacle":
            d["obstacle"].append((name, {f: _val(state, o, f) for f in
                                         ("x", "y", "z", "half_x", "half_y", "half_z")}))
    d["objective"].sort(key=lambda t: t[0])
    d["sample"].sort(key=lambda t: t[0])
    return d


def sense_offset(theta):
    # sensing point = base + R(theta) @ (-0.087, -0.012)
    c, s = math.cos(theta), math.sin(theta)
    return (-SENSE_BACK * c + SENSE_RIGHT * s, -SENSE_BACK * s - SENSE_RIGHT * c)


def seg_dist_grid(ex, ey, tx, ty, px, py):
    """Distance from point (px,py) to segments (ex,ey)->(tx,ty); ex,ey arrays."""
    dx = tx - ex
    dy = ty - ey
    L2 = dx * dx + dy * dy + 1e-12
    t = ((px - ex) * dx + (py - ey) * dy) / L2
    t = np.clip(t, 0.0, 1.0)
    qx = ex + t * dx - px
    qy = ey + t * dy - py
    return np.sqrt(qx * qx + qy * qy)


def bfs_field(free, init):
    """Min steps field: D(x) = min over y within Chebyshev-4 of D(y)+1, restricted to free."""
    D = np.where(free, init, INF)
    for _ in range(400):
        nb = minimum_filter(D, size=2 * STEP_CELLS + 1, mode="constant", cval=INF) + 1.0
        nb[~free] = INF
        D2 = np.minimum(D, nb)
        if np.array_equal(D2, D):
            break
        D = D2
    return D


def to_cell(x, y):
    i = int(round((x + LIM) / RES))
    j = int(round((y + LIM) / RES))
    return min(max(i, 0), N - 1), min(max(j, 0), N - 1)


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self._predicting = False
        self._pred_cache = None
        self.bad_cells = {"rover0": set(), "rover1": set()}
        self._last = None
        self.topk = 12
        self.observation_space = observation_space

    # ------------------------------------------------------------------ setup
    def reset(self, state, info):
        d = parse(state)
        self.d0 = d
        self.rovers = ["rover0", "rover1"]
        self.home = {r: (d["rover"][r]["x"], d["rover"][r]["y"], d["rover"][r]["theta"])
                     for r in self.rovers}
        self.lander = d["lander"]
        self.mounds = []
        self.pillars = []
        for _, ob in d["obstacle"]:
            if ob["half_x"] > 0.1:
                self.mounds.append(ob)
            else:
                self.pillars.append(ob)
        self.objs = [n for n, _ in d["objective"]]
        self.obj_pos = {n: (o["x"], o["y"]) for n, o in d["objective"]}
        self.samples = {n: (o["x"], o["y"], o["is_soil"] > 0.5) for n, o in d["sample"]}
        self._build_free()
        self.side = {r: (1 if self.home[r][0] > 0 else -1) for r in self.rovers}
        self.free_r = {r: self.free & ((GX * self.side[r]) > 0) for r in self.rovers}
        import time as _time
        t0 = _time.time()
        self._pf_cache = {}
        self._best_steps = 150
        r0, r1 = self.rovers
        cands = []
        for a in (self.home[r0][2], -math.pi / 2):
            for b in (self.home[r1][2], -math.pi / 2):
                cands.append({r0: a, r1: b})
        best = None
        last = None
        for ci, pth in enumerate(cands):
            if ci > 0 and _time.time() - t0 > 20.0:
                break
            self._set_heading_plan(pth)
            last = ci
            key = (self.plan_cost, ci)
            if best is None or key < best[0]:
                best = (key, ci)
        if best[1] != last:
            self._set_heading_plan(cands[best[1]])
        self.stage_fields = {}
        self.t = 0
        self._pred_cache = None
        self._last = None
        self.bad_cells = {r: set() for r in self.rovers}

    def _set_heading_plan(self, pth):
        self.plan_th = dict(pth)
        self.sense = {r: sense_offset(self.plan_th[r]) for r in self.rovers}
        self._pred_cache = None
        self._build_regions()
        self._plan()

    def _target_theta(self, d, r):
        order = self.fields[r]["order"]
        for t in order:
            if t[0] == "obj":
                ob = [o for n, o in d["objective"] if n == t[1]][0]
                if ob["have_image_" + r] < 0.5:
                    return self.plan_th[r]
        return self.home[r][2]

    def _build_free(self):
        free = np.ones((N, N), dtype=bool)
        free &= np.abs(GX) >= WALL_X
        for m in self.mounds:
            dx = np.maximum(np.abs(GX - m["x"]) - m["half_x"], 0)
            dy = np.maximum(np.abs(GY - m["y"]) - m["half_y"], 0)
            free &= np.sqrt(dx * dx + dy * dy) >= MOUND_CLEAR
        for p in self.pillars:
            ax = np.maximum(np.abs(GX - p["x"]) - 0.1, 0)
            ay = np.maximum(np.abs(GY - p["y"]) - 0.1, 0)
            free &= np.hypot(ax, ay) >= PILLAR_CLEAR
        lx, ly = self.lander
        free &= np.hypot(GX - lx, GY - ly) >= LANDER_CLEAR
        self.free = free

    def _vis_mask(self, r, tx, ty, rng, other_rover=None):
        ox, oy = self.sense[r]
        ex = GX + ox
        ey = GY + oy
        m = np.hypot(ex - tx, ey - ty) <= rng
        for p in self.pillars:
            m &= seg_dist_grid(ex, ey, tx, ty, p["x"], p["y"]) > LOS_PILLAR
        if other_rover is not None:
            m &= seg_dist_grid(ex, ey, tx, ty, other_rover[0], other_rover[1]) > LOS_ROVER
        return m

    def _build_regions(self):
        self.obj_vis = {}
        self.send_reg = {}
        for r in self.rovers:
            fr = self.free_r[r]
            for o in self.objs:
                tx, ty = self.obj_pos[o]
                self.obj_vis[(r, o)] = self._vis_mask(r, tx, ty, OBJ_RANGE) & fr
            other = [q for q in self.rovers if q != r][0]
            oh = self.home[other]
            self.send_reg[r] = self._vis_mask(r, self.lander[0], self.lander[1], LANDER_RANGE) & fr
        self.samp_reg = {}
        for s, (sx, sy, _) in self.samples.items():
            self.samp_reg[s] = (np.hypot(GX - sx, GY - sy) <= SAMPLE_RANGE) & self.free
        # home & send-then-home fields
        self.V_home = {}
        self.V_send = {}
        Vh0 = {}
        self.home_mask = {}
        lsign = 1 if self.lander[0] > 0 else -1
        self.blocked_rover = None
        for r in self.rovers:
            if self.side[r] != lsign:
                self.blocked_rover = r
        for r in self.rovers:
            hx, hy, _ = self.home[r]
            init = np.full((N, N), INF)
            hm = (np.hypot(GX - hx, GY - hy) <= 0.235) & self.free_r[r]
            hi, hj = to_cell(hx, hy)
            hm[hi, hj] = True
            init[hm] = 0.0
            Vh0[r] = (bfs_field(self.free_r[r], init), hm)
        for r in self.rovers:
            q = [o for o in self.rovers if o != r][0]
            Vh, hm = Vh0[r]
            # choose home cells for r that do not occlude q's sends near q's home
            Vq = Vh0[q][0]
            near = self.send_reg[q] & (Vq <= 8)
            if near.any():
                ox, oy = self.sense[q]
                ex = GX[near] + ox
                ey = GY[near] + oy
                w = 1.0 / (1.0 + Vq[near])
                cells = np.argwhere(hm)
                scores = []
                hx, hy, _ = self.home[r]
                for ci, cj in cells:
                    blk = seg_dist_grid(ex, ey, self.lander[0], self.lander[1],
                                        COORDS[ci], COORDS[cj]) <= LOS_ROVER
                    scores.append(float((w * blk).sum()))
                scores = np.array(scores)
                good = scores <= scores.min() + 1e-9
                hm2 = np.zeros_like(hm)
                for (ci, cj), g in zip(cells, good):
                    if g:
                        hm2[ci, cj] = True
                if scores.min() < scores.max():
                    init = np.where(hm2, 0.0, INF)
                    Vh = bfs_field(self.free_r[r], init)
                    hm = hm2
            self.home_mask[r] = hm
            self.V_home[r] = Vh
            init2 = np.where(self.send_reg[r], Vh, INF)
            self.V_send[r] = bfs_field(self.free_r[r], init2)

    # -------------------------------------------------------------- planning
    def _task_region(self, r, task, held=()):
        kind, name = task
        if kind == "obj":
            reg = self.obj_vis[(r, name)].copy()
            # prefer cells where this objective is the nearest visible non-held one
            ox, oy = self.sense[r]
            tx, ty = self.obj_pos[name]
            dme = np.hypot(GX + ox - tx, GY + oy - ty)
            for o2 in self.objs:
                if o2 == name or o2 in held:
                    continue
                t2x, t2y = self.obj_pos[o2]
                d2 = np.hypot(GX + ox - t2x, GY + oy - t2y)
                reg &= ~((d2 <= TRUE_OBJ + 0.03) & (d2 < dme + 0.03))
            return reg
        return self.samp_reg[name] & self.free_r[self.rovers[0] if False else r]

    def _candidates(self, reg, k=8):
        idx = np.argwhere(reg)
        if len(idx) == 0:
            return []
        if len(idx) <= k:
            return [tuple(x) for x in idx]
        pts = idx.astype(float)
        chosen = [len(idx) // 2]
        dmin = np.linalg.norm(pts - pts[chosen[0]], axis=1)
        while len(chosen) < k:
            nxt = int(np.argmax(dmin))
            chosen.append(nxt)
            dmin = np.minimum(dmin, np.linalg.norm(pts - pts[nxt], axis=1))
        return [tuple(idx[c]) for c in chosen]

    def _point_field(self, r, cell):
        key = (r, int(cell[0]), int(cell[1]))
        c = self._pf_cache.get(key)
        if c is None:
            init = np.full((N, N), INF)
            init[cell] = 0.0
            c = bfs_field(self.free_r[r], init)
            c.setflags(write=False)
            self._pf_cache[key] = c
        return c

    def _rover_tasks(self, r):
        tasks = []
        for o in self.objs:
            if self.obj_vis[(r, o)].any():
                tasks.append(("obj", o))
        for s, (sx, sy, soil) in self.samples.items():
            if sx * self.side[r] > 0 and (self.samp_reg[s] & self.free_r[r]).any():
                tasks.append(("stone" if not soil else "soil", s))
        return tasks

    def _held_karp(self, r, tasks):
        """Return dict: frozenset(task idx) -> (cost, order list)."""
        hx, hy, _ = self.home[r]
        start = to_cell(hx, hy)
        nodes = []  # (task_idx, cell)
        for ti, t in enumerate(tasks):
            reg = self._task_region(r, (t[0] if t[0] == "obj" else "samp", t[1]))
            if not reg.any():
                reg = self.obj_vis[(r, t[1])] if t[0] == "obj" else self.samp_reg[t[1]] & self.free_r[r]
            cands = self._candidates(reg, 14)
            # add cells closest to start
            Fstart = None
            for c in cands:
                nodes.append((ti, c))
        fields = [self._point_field(r, c) for _, c in nodes]
        nn = len(nodes)
        dist = np.full((nn, nn), INF)
        for a in range(nn):
            for b in range(nn):
                dist[a, b] = fields[b][nodes[a][1]]
        dstart = np.array([fields[b][start] for b in range(nn)])
        dend = np.array([self.V_send[r][nodes[a][1]] for a in range(nn)])
        T = len(tasks)
        kinds = [t[0] for t in tasks]
        # DP over masks
        best = {}
        for a in range(nn):
            m = 1 << nodes[a][0]
            v = dstart[a]
            key = (m, a)
            if v < best.get(key, (INF,))[0]:
                best[key] = (v, None)
        masks = sorted(set(k[0] for k in best))
        by_mask = {}
        for (m, a), v in best.items():
            by_mask.setdefault(m, {})[a] = v
        results = {0: (self.V_send[r][start], [])}
        order_masks = sorted(range(1 << T), key=lambda m: bin(m).count("1"))
        valid = {}
        for m in order_masks:
            ns = sum(1 for i in range(T) if m >> i & 1 and kinds[i] == "stone")
            nl = sum(1 for i in range(T) if m >> i & 1 and kinds[i] == "soil")
            valid[m] = ns <= 1 and nl <= 1
        for m in order_masks:
            if m == 0 or not valid[m] or m not in by_mask:
                continue
            ent = by_mask[m]
            # finalize
            bestfin = INF
            bestA = None
            for a, (v, _) in ent.items():
                f = v + dend[a]
                if f < bestfin:
                    bestfin, bestA = f, a
            if bestA is not None and bestfin < INF:
                # reconstruct order
                order = []
                mm, aa = m, bestA
                while aa is not None:
                    order.append(nodes[aa])
                    prev = by_mask[mm][aa][1]
                    mm = mm & ~(1 << nodes[aa][0])
                    aa = prev
                results[m] = (bestfin, [tasks[ti] for ti, _ in reversed(order)])
            for a, (v, _) in ent.items():
                for b in range(nn):
                    tb = nodes[b][0]
                    if m >> tb & 1:
                        continue
                    m2 = m | (1 << tb)
                    if not valid[m2]:
                        continue
                    nv = v + dist[a, b]
                    cur = by_mask.setdefault(m2, {})
                    if b not in cur or nv < cur[b][0]:
                        cur[b] = (nv, a)
        return results

    def _plan(self):
        tasks = {r: self._rover_tasks(r) for r in self.rovers}
        hk = {r: self._held_karp(r, tasks[r]) for r in self.rovers}
        objs = self.objs
        r0, r1 = self.rovers
        cands = []
        for m0, (c0, ord0) in hk[r0].items():
            s0 = set(t for t in ord0)
            for m1, (c1, ord1) in hk[r1].items():
                s1 = set(t for t in ord1)
                if s0 & s1:
                    continue
                allt = s0 | s1
                ok = all(("obj", o) in allt for o in objs)
                ok = ok and any(t[0] == "stone" for t in allt) and any(t[0] == "soil" for t in allt)
                if not ok:
                    continue
                cost = max(c0, c1) + 0.01 * (c0 + c1)
                cands.append((cost, tuple(ord0), tuple(ord1)))
        cands.sort(key=lambda c: c[0])
        self._field_cache = {}
        best = None
        for cost, ord0, ord1 in cands[:self.topk]:
            fields = {r0: self._get_stage_fields(r0, ord0), r1: self._get_stage_fields(r1, ord1)}
            self.fields = fields
            steps = self._simulate(self.d0, max_steps=min(150, self._best_steps))
            self._best_steps = min(self._best_steps, steps)
            key = (steps, cost)
            if best is None or key < best[0]:
                best = (key, fields, {r0: list(ord0), r1: list(ord1)})
        if best is None:
            self.orders = {r: [] for r in self.rovers}
            self.fields = {r: self._layer_fields(r, []) for r in self.rovers}
            self.plan_cost = INF
        else:
            self.fields = best[1]
            self.orders = best[2]
            self.plan_cost = best[0][0]

    def _get_stage_fields(self, r, order):
        key = (r, tuple(order))
        if key not in self._field_cache:
            self._field_cache[key] = self._layer_fields(r, list(order))
        return self._field_cache[key]

    # ------------------------------------------------------------ model sim
    def _free_pt(self, r, x, y):
        if abs(x) > 2.27 or abs(y) > 2.27 or abs(x) < 0.228:
            return False
        for m in self.mounds:
            dx = max(abs(x - m["x"]) - m["half_x"], 0)
            dy = max(abs(y - m["y"]) - m["half_y"], 0)
            if math.hypot(dx, dy) < 0.178:
                return False
        for p in self.pillars:
            if math.hypot(max(abs(x - p["x"]) - 0.1, 0), max(abs(y - p["y"]) - 0.1, 0)) < 0.15:
                return False
        if math.hypot(x - self.lander[0], y - self.lander[1]) < 0.72:
            return False
        return True

    def _goal(self, d):
        if not all(o["received_image"] > 0.5 for _, o in d["objective"]):
            return False
        st = any(s["received_analysis"] > 0.5 and s["is_soil"] < 0.5 for _, s in d["sample"])
        so = any(s["received_analysis"] > 0.5 and s["is_soil"] > 0.5 for _, s in d["sample"])
        if not (st and so):
            return False
        for r in self.rovers:
            ro = d["rover"][r]
            if ro["store_full"] > 0.5 or ro["at_home"] < 0.5:
                return False
        return True

    def _model_step(self, d, act):
        d2 = dict(d)
        d2["objective"] = [(n, dict(o)) for n, o in d["objective"]]
        d2["sample"] = [(n, dict(o)) for n, o in d["sample"]]
        d2["rover"] = {k: dict(v) for k, v in d["rover"].items()}
        for k, r in enumerate(self.rovers):
            ro = d2["rover"][r]
            dx = float(np.clip(act[4 * k], -0.2, 0.2))
            dy = float(np.clip(act[4 * k + 1], -0.2, 0.2))
            nx, ny = ro["x"] + dx, ro["y"] + dy
            if self._free_pt(r, nx, ny):
                ro["x"], ro["y"] = nx, ny
                dth = float(np.clip(act[4 * k + 2], -0.4, 0.4))
                ro["theta"] = (ro["theta"] + dth + math.pi) % (2 * math.pi) - math.pi
        for k, r in enumerate(self.rovers):
            ro = d2["rover"][r]
            other = d2["rover"][[q for q in self.rovers if q != r][0]]
            sel = float(act[4 * k + 3])
            band = min(int((sel + 1.0) * 3.0), 5)
            x, y, th = ro["x"], ro["y"], ro["theta"]
            if band == 0:
                if ro["store_full"] < 0.5:
                    bestd, bn = 0.25, None
                    for n, sm in d2["sample"]:
                        dd = math.hypot(sm["x"] - x, sm["y"] - y)
                        if dd <= bestd:
                            bestd, bn = dd, sm
                    if bn is not None:
                        bn["analyzed_" + r] = 1.0
                        ro["store_full"] = 1.0
            elif band == 1:
                if self._visible_objs(r, x, y, th):
                    ro["calibrated"] = 1.0
            elif band == 2:
                vis = self._visible_objs(r, x, y, th)
                if ro["calibrated"] > 0.5 and vis:
                    ro["calibrated"] = 0.0
                    for dd, on in self._inrange_objs(r, x, y, th):
                        ob = [o for n, o in d2["objective"] if n == on][0]
                        if ob["have_image_" + r] < 0.5:
                            ob["have_image_" + r] = 1.0
                            break
            elif band == 4:
                if self._lander_visible(r, x, y, th, (other["x"], other["y"])):
                    for _, o in d2["objective"]:
                        if o["have_image_" + r] > 0.5:
                            o["received_image"] = 1.0
                    for _, sm in d2["sample"]:
                        if sm["analyzed_" + r] > 0.5:
                            sm["received_analysis"] = 1.0
            elif band == 5:
                ro["store_full"] = 0.0
        for r in self.rovers:
            ro = d2["rover"][r]
            hx, hy, hth = self.home[r]
            dth = abs((ro["theta"] - hth + math.pi) % (2 * math.pi) - math.pi)
            ro["at_home"] = 1.0 if (math.hypot(ro["x"] - hx, ro["y"] - hy) < 0.25 and dth < 0.4) else 0.0
        return d2

    def _simulate(self, d, max_steps=150):
        self._pred_cache = None
        for t in range(max_steps):
            act = self._policy(d)
            d = self._model_step(d, act)
            d["_t"] = t + 1
            if self._goal(d):
                return t + 1
        return max_steps + 100

    def _stage_fields(self, r, order):
        """fields[i] = cost-to-go when tasks order[i:] remain (then send+home)."""
        k = len(order)
        fields = [None] * (k + 1)
        regs = [None] * k
        fields[k] = self.V_send[r]
        for i in range(k - 1, -1, -1):
            t = order[i]
            held = tuple(o for kk, o in order[:i] if kk == "obj")
            if t[0] == "obj":
                reg = self._task_region(r, ("obj", t[1]), held)
                if not reg.any():
                    reg = self.obj_vis[(r, t[1])]
            else:
                reg = self.samp_reg[t[1]] & self.free_r[r]
            regs[i] = reg
            init = np.where(reg, fields[i + 1], INF)
            fields[i] = bfs_field(self.free_r[r], init)
        return {"fields": fields, "regs": regs, "order": order}

    # -------------------------------------------------------------- execution
    def _visible_objs(self, r, x, y, theta):
        ox, oy = sense_offset(theta)
        ex, ey = x + ox, y + oy
        res = []
        for o in self.objs:
            tx, ty = self.obj_pos[o]
            dd = math.hypot(ex - tx, ey - ty)
            if dd > TRUE_OBJ:
                continue
            ok = True
            for p in self.pillars:
                if float(seg_dist_grid(ex, ey, tx, ty, p["x"], p["y"])) <= TRUE_PILLAR:
                    ok = False
                    break
            if ok:
                res.append((dd, o))
        res.sort()
        return res

    def _inrange_objs(self, r, x, y, theta):
        ox, oy = sense_offset(theta)
        ex, ey = x + ox, y + oy
        res = []
        for o in self.objs:
            tx, ty = self.obj_pos[o]
            dd = math.hypot(ex - tx, ey - ty)
            if dd <= TRUE_OBJ + 0.03:
                res.append((dd, o))
        res.sort()
        return res

    def _lander_visible(self, r, x, y, theta, other):
        ox, oy = sense_offset(theta)
        ex, ey = x + ox, y + oy
        tx, ty = self.lander
        if math.hypot(ex - tx, ey - ty) > TRUE_LANDER:
            return False
        for p in self.pillars:
            if float(seg_dist_grid(ex, ey, tx, ty, p["x"], p["y"])) <= TRUE_PILLAR:
                return False
        if other is not None and float(seg_dist_grid(ex, ey, tx, ty, other[0], other[1])) <= TRUE_ROVER:
            return False
        return True

    def _task_done(self, d, r, t):
        if t[0] == "obj":
            for n, o in d["objective"]:
                if n == t[1]:
                    return o["have_image_" + r] > 0.5 or o["received_image"] > 0.5
            return True
        for n, s in d["sample"]:
            if n == t[1]:
                if s["analyzed_" + r] > 0.5:
                    return True
        # any analysis of the same kind already done by anyone counts
        soil = t[0] == "soil"
        for n, s in d["sample"]:
            if (s["is_soil"] > 0.5) == soil and (s["analyzed_rover0"] > 0.5 or s["analyzed_rover1"] > 0.5):
                return True
        return False

    def get_action(self, state):
        d = parse(state)
        d["_t"] = self.t
        # stuck detection: commanded move rejected -> mark target cell bad
        if self._last is not None:
            for k, r in enumerate(self.rovers):
                px, py, cdx, cdy = self._last[r]
                ro = d["rover"][r]
                if (abs(cdx) > 1e-6 or abs(cdy) > 1e-6) and abs(ro["x"] - px) < 1e-6 and abs(ro["y"] - py) < 1e-6:
                    self.bad_cells[r].add(to_cell(px + cdx, py + cdy))
        act = self._policy(d)
        self._last = {r: (d["rover"][r]["x"], d["rover"][r]["y"], float(act[4 * k]), float(act[4 * k + 1]))
                      for k, r in enumerate(self.rovers)}
        self.t += 1
        return act

    def _predict_other(self, d, r, H=45):
        """Predict positions of the other rover after each of the next H steps."""
        other = [q for q in self.rovers if q != r][0]
        key = (d.get("_t", 0), other, round(d["rover"][other]["x"], 3), round(d["rover"][other]["y"], 3))
        c = self._pred_cache
        if c is not None:
            t0, traj = c
            k = d.get("_t", 0) - t0
            if 0 <= k < len(traj) and abs(traj[k][0] - d["rover"][other]["x"]) < 1e-6 and \
                    abs(traj[k][1] - d["rover"][other]["y"]) < 1e-6 and \
                    len(traj) - k > H // 2:
                return traj[k + 1:]
        prev = self._predicting
        self._predicting = True
        dd = d
        traj = [(d["rover"][other]["x"], d["rover"][other]["y"])]
        for kk in range(H + 25):
            act = self._policy(dd)
            dd = self._model_step(dd, act)
            dd["_t"] = d.get("_t", 0) + kk + 1
            traj.append((dd["rover"][other]["x"], dd["rover"][other]["y"]))
        self._predicting = prev
        self._pred_cache = (d.get("_t", 0), traj)
        return traj[1:]

    def _final_send_target(self, d, r, H=45):
        ro = d["rover"][r]
        x, y = ro["x"], ro["y"]
        a = to_cell(x, y)
        Fa = self._point_field(r, a)
        pred = self._predict_other(d, r, H)
        ox, oy = self.sense[r]
        ex = GX + ox
        ey = GY + oy
        tx, ty = self.lander
        best = None
        Vh = self.V_home[r]
        base = self.send_reg[r] & (Fa < INF)
        for k in range(0, H):
            if k >= len(pred):
                break
            if best is not None and k >= best[0]:
                break
            reach = base & (Fa <= k + 1)
            if not reach.any():
                continue
            px, py = pred[k]
            ok = reach & (seg_dist_grid(ex, ey, tx, ty, px, py) > LOS_ROVER)
            if not ok.any():
                continue
            tot = np.where(ok, Vh + (k + 1), INF)
            idx = np.unravel_index(np.argmin(tot), tot.shape)
            v = tot[idx]
            if best is None or v < best[0]:
                best = (v, k, idx)
        if best is None:
            return None
        _, k, idx = best
        Fp = self._point_field(r, idx)
        # cost-to-go: reach idx then home; encode as field
        return np.where(Fp < INF, Fp, INF)

    def _policy(self, d):
        act = np.zeros(8, dtype=np.float32)
        for k, r in enumerate(self.rovers):
            other = [q for q in self.rovers if q != r][0]
            ro = d["rover"][r]
            orv = d["rover"][other]
            th = ro["theta"]
            err = (self._target_theta(d, r) - th + math.pi) % (2 * math.pi) - math.pi
            dth = float(np.clip(err, -0.4, 0.4))
            if abs(dth) < 1e-3:
                dth = 0.0
            ro2 = dict(ro)
            ro2["theta"] = th + dth
            dx, dy, op = self._rover_action(d, r, ro2, (orv["x"], orv["y"]))
            op = self._guard_op(d, r, ro2["x"] + dx, ro2["y"] + dy, ro2["theta"], op)
            act[4 * k + 0] = dx
            act[4 * k + 1] = dy
            act[4 * k + 2] = dth
            act[4 * k + 3] = SEL[op]
        return act

    def _guard_op(self, d, r, px, py, th, op):
        if op == "image":
            ro = d["rover"][r]
            if ro["calibrated"] < 0.5:
                return "noop"
            held = set(n for n, o in d["objective"] if o["have_image_" + r] > 0.5)
            vis = [o for dd, o in self._visible_objs(r, px, py, th) if o not in held]
            inr = [o for dd, o in self._inrange_objs(r, px, py, th) if o not in held]
            if not vis or not inr or vis[0] != inr[0]:
                return "noop"
        elif op == "calibrate":
            if not self._visible_objs(r, px, py, th):
                return "noop"
        return op

    def _layer_solve(self, free, H0, home=None):
        M = H0.copy()
        G = None
        for _ in range(400):
            G = minimum_filter(M, size=2 * STEP_CELLS + 1, mode="constant", cval=INF) + 1.0
            G[~free] = INF
            if home is not None:
                G[home] = 0.0
            M2 = np.minimum(H0, G)
            if np.array_equal(M2, M):
                break
            M = M2
        return G

    def _layer_fields(self, r, order):
        order = list(order)
        k = len(order)
        free = self.free_r[r]
        U = np.zeros((N, N), dtype=bool)
        for o in self.objs:
            U |= self.obj_vis[(r, o)]
        regs = []
        for i, t in enumerate(order):
            if t[0] == "obj":
                held = tuple(o for kk, o in order[:i] if kk == "obj")
                reg = self._task_region(r, ("obj", t[1]), held)
                if not reg.any():
                    reg = self.obj_vis[(r, t[1])]
            else:
                reg = self.samp_reg[t[1]] & free
            regs.append(reg)
        S = self.send_reg[r]
        hx, hy, _ = self.home[r]
        home = self.home_mask[r]
        G = {}
        INFA = np.full((N, N), INF)
        for i in range(k, -1, -1):
            sents = [1, 0] if i == k else [0]
            for sent in sents:
                for full in (0, 1):
                    for cal in (1, 0):
                        H0 = INFA.copy()
                        if cal == 0:
                            H0 = np.where(U, np.minimum(H0, G[(i, 1, full, sent)]), H0)
                        if full == 1:
                            H0 = np.minimum(H0, G[(i, cal, 0, sent)])
                        if i < k:
                            nxt_sent = 0
                            t = order[i]
                            if t[0] == "obj" and cal == 1:
                                H0 = np.where(regs[i], np.minimum(H0, G[(i + 1, 0, full, nxt_sent)]), H0)
                            if t[0] != "obj" and full == 0:
                                H0 = np.where(regs[i], np.minimum(H0, G[(i + 1, cal, 1, nxt_sent)]), H0)
                        if i == k and sent == 0:
                            H0 = np.where(S, np.minimum(H0, G[(i, cal, full, 1)]), H0)
                        term = (i == k and sent == 1 and full == 0)
                        G[(i, cal, full, sent)] = self._layer_solve(free, H0, home if term else None)
        if k == 0:
            for full in (0, 1):
                for cal in (0, 1):
                    G[(0, cal, full, 0)] = G[(0, cal, full, 1)]
        return {"G": G, "regs": regs, "U": U, "order": order}

    def _rover_action(self, d, r, ro, other_xy):
        plan = self.fields[r]
        order = plan["order"]
        k = len(order)
        stage = 0
        while stage < k and self._task_done(d, r, order[stage]):
            stage += 1
        pending = False
        for n, o in d["objective"]:
            if o["have_image_" + r] > 0.5 and o["received_image"] < 0.5:
                pending = True
        for n, sm in d["sample"]:
            if sm["analyzed_" + r] > 0.5 and sm["received_analysis"] < 0.5:
                pending = True
        x, y, th = ro["x"], ro["y"], ro["theta"]
        cal = 1 if ro["calibrated"] > 0.5 else 0
        full = 1 if ro["store_full"] > 0.5 else 0
        if stage == k and pending and not self._predicting and r == self.blocked_rover:
            return self._rover_action_old(d, r, ro, other_xy)
        sent = 1 if (stage == k and not pending) else 0
        G = plan["G"]
        i, j = to_cell(x, y)
        i0, i1 = max(i - STEP_CELLS, 0), min(i + STEP_CELLS, N - 1)
        j0, j1 = max(j - STEP_CELLS, 0), min(j + STEP_CELLS, N - 1)
        win = (slice(i0, i1 + 1), slice(j0, j1 + 1))
        opts = [(G[(stage, cal, full, sent)][win], "noop")]
        if cal == 0:
            opts.append((np.where(plan["U"][win], G[(stage, 1, full, sent)][win], INF), "calibrate"))
        if full == 1:
            opts.append((G[(stage, cal, 0, sent)][win], "drop"))
        if stage < k:
            t = order[stage]
            reg = plan["regs"][stage][win]
            if t[0] == "obj" and cal == 1:
                opts.append((np.where(reg, G[(stage + 1, 0, full, 0)][win], INF), "image"))
            if t[0] != "obj" and full == 0:
                opts.append((np.where(reg, G[(stage + 1, cal, 1, 0)][win], INF), "sample"))
        if stage == k and sent == 0:
            opts.append((np.where(self.send_reg[r][win], G[(stage, cal, full, 1)][win], INF), "send"))
        ii, jj = np.meshgrid(np.arange(i0, i1 + 1), np.arange(j0, j1 + 1), indexing="ij")
        mv = np.maximum(np.abs(ii - i), np.abs(jj - j)) * 1e-3 + np.hypot(ii - i, jj - j) * 1e-4
        if self.bad_cells[r] and not self._predicting:
            for (bi, bj) in self.bad_cells[r]:
                if i0 <= bi <= i1 and j0 <= bj <= j1:
                    mv[bi - i0, bj - j0] += INF
        best = None
        for arr, opname in opts:
            sc = arr + mv + (2e-3 if opname == "noop" else 0.0)
            idx = np.unravel_index(np.argmin(sc), sc.shape)
            v = sc[idx]
            if best is None or v < best[0]:
                best = (v, idx, opname)
        if best is None or best[0] >= INF / 2:
            return self._rover_action_old(d, r, ro, other_xy)
        _, (ci, cj), op = best
        ti, tj = i0 + ci, j0 + cj
        mdx = float(np.clip(COORDS[ti] - x, -0.2, 0.2))
        mdy = float(np.clip(COORDS[tj] - y, -0.2, 0.2))
        px, py = x + mdx, y + mdy
        if op == "noop":
            vis = self._visible_objs(r, px, py, th)
            need_imgs = [t[1] for t in order[stage:] if t[0] == "obj"]
            if full:
                op = "drop"
            elif not cal and need_imgs and vis:
                op = "calibrate"
            elif pending and self._lander_visible(r, px, py, th, None):
                op = "send"
        return mdx, mdy, op

    def _rover_action_old(self, d, r, ro, other_xy):
        plan = self.fields[r]
        order = plan["order"]
        stage = 0
        while stage < len(order) and self._task_done(d, r, order[stage]):
            stage += 1
        x, y, th = ro["x"], ro["y"], ro["theta"]
        i, j = to_cell(x, y)
        # pending results to send?
        pending = False
        for n, o in d["objective"]:
            if o["have_image_" + r] > 0.5 and o["received_image"] < 0.5:
                pending = True
        for n, s in d["sample"]:
            if s["analyzed_" + r] > 0.5 and s["received_analysis"] < 0.5:
                pending = True
        if stage < len(order) and "fields" not in plan:
            F = self.V_send[r]
            reg = None
        elif stage < len(order):
            F = plan["fields"][stage]
            reg = plan["regs"][stage]
        else:
            if pending:
                F = self.V_send[r]
                reg = None
                if not self._predicting:
                    tgt = self._final_send_target(d, r)
                    if tgt is not None:
                        F = tgt
            else:
                F = self.V_home[r]
                reg = None
        # choose next cell
        best = None
        i0, i1 = max(i - STEP_CELLS, 0), min(i + STEP_CELLS, N - 1)
        j0, j1 = max(j - STEP_CELLS, 0), min(j + STEP_CELLS, N - 1)
        sub = F[i0:i1 + 1, j0:j1 + 1]
        cur = F[i, j]
        # stay if current cell is a goal (in region) for this stage
        ready = True
        if stage < len(order):
            t0 = order[stage]
            if t0[0] == "obj":
                ready = ro["calibrated"] > 0.5
            else:
                ready = ro["store_full"] < 0.5
        if (not ready) and reg is not None and reg[i, j]:
            rsub = reg[i0:i1 + 1, j0:j1 + 1]
            sub = np.where(rsub, sub, INF)
        mn = sub.min()
        cands = np.argwhere(sub <= mn + 1e-9)
        # tie-break: prefer staying close (smaller move) -- then toward straight
        bestc = None
        bestscore = None
        for ci, cj in cands:
            ii, jj = i0 + ci, j0 + cj
            score = max(abs(ii - i), abs(jj - j)) * 0.01 + math.hypot(ii - i, jj - j) * 0.001
            if bestscore is None or score < bestscore:
                bestscore, bestc = score, (ii, jj)
        ti, tj = bestc
        if cur <= mn + 1e-9 and reg is not None and reg[i, j]:
            ti, tj = i, j
        nx, ny = COORDS[ti], COORDS[tj]
        mdx = float(np.clip(nx - x, -0.2, 0.2))
        mdy = float(np.clip(ny - y, -0.2, 0.2))
        px, py = x + mdx, y + mdy
        # ---- operator selection (evaluated at post-move position)
        op = "noop"
        vis = self._visible_objs(r, px, py, th)
        held = set(n for n, o in d["objective"] if o["have_image_" + r] > 0.5)
        notheld = [o for dd, o in vis if o not in held]
        need_imgs = [t[1] for t in order[stage:] if t[0] == "obj"]
        cal = ro["calibrated"] > 0.5
        store_full = ro["store_full"] > 0.5
        if stage < len(order):
            t = order[stage]
            if t[0] in ("stone", "soil"):
                sx, sy, _ = self.samples[t[1]]
                if not store_full and math.hypot(px - sx, py - sy) <= 0.24:
                    return mdx, mdy, "sample"
        inr = [o for dd, o in self._inrange_objs(r, px, py, th) if o not in held]
        if cal and notheld and inr and inr[0] == notheld[0] and notheld[0] in need_imgs:
            return mdx, mdy, "image"
        if store_full:
            return mdx, mdy, "drop"
        if not cal and need_imgs and vis:
            return mdx, mdy, "calibrate"
        if pending and self._lander_visible(r, px, py, th, None):
            return mdx, mdy, "send"
        return mdx, mdy, op
