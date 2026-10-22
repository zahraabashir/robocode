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
PILLAR_CLEAR = 0.31
LANDER_CLEAR = 0.76
OBJ_RANGE = 1.95
LANDER_RANGE = 3.94
LOS_PILLAR = 0.085
LOS_ROVER = 0.30
SAMPLE_RANGE = 0.2
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
        self.sense = {r: sense_offset(self.home[r][2]) for r in self.rovers}
        self.side = {r: (1 if self.home[r][0] > 0 else -1) for r in self.rovers}
        self.free_r = {r: self.free & ((GX * self.side[r]) > 0) for r in self.rovers}
        self._build_regions()
        self._plan()
        self.stage_fields = {}
        self.t = 0

    def _build_free(self):
        free = np.ones((N, N), dtype=bool)
        free &= np.abs(GX) >= WALL_X
        for m in self.mounds:
            dx = np.maximum(np.abs(GX - m["x"]) - m["half_x"], 0)
            dy = np.maximum(np.abs(GY - m["y"]) - m["half_y"], 0)
            free &= np.sqrt(dx * dx + dy * dy) >= MOUND_CLEAR
        for p in self.pillars:
            free &= np.hypot(GX - p["x"], GY - p["y"]) >= PILLAR_CLEAR
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
            self.send_reg[r] = self._vis_mask(r, self.lander[0], self.lander[1], LANDER_RANGE,
                                              other_rover=(oh[0], oh[1])) & fr
        self.samp_reg = {}
        for s, (sx, sy, _) in self.samples.items():
            self.samp_reg[s] = (np.hypot(GX - sx, GY - sy) <= SAMPLE_RANGE) & self.free
        # home & send-then-home fields
        self.V_home = {}
        self.V_send = {}
        for r in self.rovers:
            hx, hy, _ = self.home[r]
            init = np.full((N, N), INF)
            hm = (np.hypot(GX - hx, GY - hy) <= 0.2) & self.free_r[r]
            hi, hj = to_cell(hx, hy)
            hm[hi, hj] = True
            init[hm] = 0.0
            Vh = bfs_field(self.free_r[r], init)
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
                reg &= ~(self.obj_vis[(r, o2)] & (d2 < dme))
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
        init = np.full((N, N), INF)
        init[cell] = 0.0
        return bfs_field(self.free_r[r], init)

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
            cands = self._candidates(reg, 8)
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
            steps = self._simulate(self.d0)
            key = (steps, cost)
            if best is None or key < best[0]:
                best = (key, fields, {r0: list(ord0), r1: list(ord1)})
        if best is None:
            self.orders = {r: [] for r in self.rovers}
            self.fields = {r: self._stage_fields(r, []) for r in self.rovers}
            self.plan_cost = INF
        else:
            self.fields = best[1]
            self.orders = best[2]
            self.plan_cost = best[0][0]

    def _get_stage_fields(self, r, order):
        key = (r, tuple(order))
        if key not in self._field_cache:
            self._field_cache[key] = self._stage_fields(r, list(order))
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
            if math.hypot(x - p["x"], y - p["y"]) < 0.28:
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
        import copy
        d2 = copy.deepcopy(d)
        for k, r in enumerate(self.rovers):
            ro = d2["rover"][r]
            dx = float(np.clip(act[4 * k], -0.2, 0.2))
            dy = float(np.clip(act[4 * k + 1], -0.2, 0.2))
            nx, ny = ro["x"] + dx, ro["y"] + dy
            if self._free_pt(r, nx, ny):
                ro["x"], ro["y"] = nx, ny
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
                    for dd, on in vis:
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
        for t in range(max_steps):
            act = self._policy(d)
            d = self._model_step(d, act)
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
            if dd > OBJ_RANGE + 0.03:
                continue
            ok = True
            for p in self.pillars:
                if float(seg_dist_grid(ex, ey, tx, ty, p["x"], p["y"])) <= LOS_PILLAR - 0.01:
                    ok = False
                    break
            if ok:
                res.append((dd, o))
        res.sort()
        return res

    def _lander_visible(self, r, x, y, theta, other):
        ox, oy = sense_offset(theta)
        ex, ey = x + ox, y + oy
        tx, ty = self.lander
        if math.hypot(ex - tx, ey - ty) > LANDER_RANGE + 0.03:
            return False
        for p in self.pillars:
            if float(seg_dist_grid(ex, ey, tx, ty, p["x"], p["y"])) <= LOS_PILLAR - 0.01:
                return False
        if float(seg_dist_grid(ex, ey, tx, ty, other[0], other[1])) <= LOS_ROVER - 0.03:
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
        act = self._policy(d)
        self.t += 1
        return act

    def _policy(self, d):
        act = np.zeros(8, dtype=np.float32)
        for k, r in enumerate(self.rovers):
            other = [q for q in self.rovers if q != r][0]
            ro = d["rover"][r]
            orv = d["rover"][other]
            dx, dy, op = self._rover_action(d, r, ro, (orv["x"], orv["y"]))
            act[4 * k + 0] = dx
            act[4 * k + 1] = dy
            act[4 * k + 2] = 0.0
            act[4 * k + 3] = SEL[op]
        return act

    def _rover_action(self, d, r, ro, other_xy):
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
        if stage < len(order):
            F = plan["fields"][stage]
            reg = plan["regs"][stage]
        else:
            if pending:
                F = self.V_send[r]
                reg = None
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
        if cal and notheld and notheld[0] in need_imgs:
            return mdx, mdy, "image"
        if store_full:
            return mdx, mdy, "drop"
        if not cal and need_imgs and vis:
            return mdx, mdy, "calibrate"
        if pending and self._lander_visible(r, px, py, th, other_xy):
            return mdx, mdy, "send"
        return mdx, mdy, op
