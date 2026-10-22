"""Model-based pushing controller for DynPushT2D.

Uses an empirically-fitted quasi-static impulse push model (see push_model.py
notes) vectorised over many candidate pushes. Each decision: sample contact
points on the T boundary x push directions x step sizes, roll out, choose best
(cost + step penalty), navigate (A*) to pre-contact point, execute push, replan.
"""
import heapq
import math

import numpy as np

C_GAP = 0.265
MU = 1.0
LO, HI = 0.1, 4.9  # robot centre bounds
AMAX = 0.049


def _wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def geometry(obs):
    w, L, V = float(obs[12]), float(obs[13]), float(obs[14])
    A1, A2 = L * w, V * w
    y1, y2 = -w / 2, -w - V / 2
    yc = (A1 * y1 + A2 * y2) / (A1 + A2)
    I = (A1 * (L * L + w * w) / 12 + A1 * (y1 - yc) ** 2
         + A2 * (V * V + w * w) / 12 + A2 * (y2 - yc) ** 2)
    rects = np.array([(-L / 2, L / 2, -w, 0.0), (-w / 2, w / 2, -w - V, -w)])
    return rects, np.array([0.0, yc]), I / (A1 + A2)


class Model:
    def __init__(self, obs):
        self.rects, self.com, self.k2 = geometry(obs)
        self.r = float(obs[28])
        w, L, V = float(obs[12]), float(obs[13]), float(obs[14])
        self.corners = np.array([(-L / 2, 0), (L / 2, 0), (L / 2, -w), (-L / 2, -w),
                                 (w / 2, -w - V), (-w / 2, -w - V)])

    def closest(self, q):
        """q: (N,2) local points. returns p (N,2), d (N,), n (N,2) outward normal."""
        best_p = None
        best_d = None
        for x0, x1, y0, y1 in self.rects:
            p = np.stack([np.clip(q[:, 0], x0, x1), np.clip(q[:, 1], y0, y1)], 1)
            d = np.linalg.norm(q - p, axis=1)
            if best_p is None:
                best_p, best_d = p, d
            else:
                m = d < best_d
                best_p = np.where(m[:, None], p, best_p)
                best_d = np.where(m, d, best_d)
        n = (q - best_p) / np.maximum(best_d, 1e-12)[:, None]
        return best_p, best_d, n

    def world_dist(self, pos, th, pts):
        """distance from world points pts (N,2) to T with pose (pos (N,2), th (N,))."""
        c, s = np.cos(th), np.sin(th)
        rel = pts - pos
        q = np.stack([c * rel[:, 0] + s * rel[:, 1], -s * rel[:, 0] + c * rel[:, 1]], 1)
        _, d, _ = self.closest(q)
        return d

    def step(self, pos, th, rob, a, n_sub=2):
        for _ in range(n_sub):
            pos, th = self._step1(pos, th, rob, a / n_sub, C_GAP * n_sub)
            rob = rob + a / n_sub
        return pos, th

    def _step1(self, pos, th, rob, a, c_gap):
        c, s = np.cos(th), np.sin(th)
        rob1 = rob + a
        rel = rob1 - pos
        q = np.stack([c * rel[:, 0] + s * rel[:, 1], -s * rel[:, 0] + c * rel[:, 1]], 1)
        al = np.stack([c * a[:, 0] + s * a[:, 1], -s * a[:, 0] + c * a[:, 1]], 1)
        p, d, n = self.closest(q)
        a_n = -(al * n).sum(1)
        gstar = self.r + c_gap * np.maximum(a_n, 0.0)
        active = (d < gstar) & (a_n > 1e-12)
        if not active.any():
            return pos, th
        frac = np.clip((gstar - d) / np.maximum(a_n, 1e-12), 0.0, 1.0)
        u = al * frac[:, None]
        rc = p - self.com
        k2 = self.k2
        K00 = 1 + rc[:, 1] ** 2 / k2
        K01 = -rc[:, 0] * rc[:, 1] / k2
        K11 = 1 + rc[:, 0] ** 2 / k2
        det = K00 * K11 - K01 * K01
        J0 = (K11 * u[:, 0] - K01 * u[:, 1]) / det
        J1 = (-K01 * u[:, 0] + K00 * u[:, 1]) / det
        nin = -n
        t = np.stack([-nin[:, 1], nin[:, 0]], 1)
        jn = J0 * nin[:, 0] + J1 * nin[:, 1]
        jt = J0 * t[:, 0] + J1 * t[:, 1]
        slide = np.abs(jt) > MU * jn
        if slide.any():
            dJ = nin + (MU * np.sign(jt))[:, None] * t
            KdJ0 = K00 * dJ[:, 0] + K01 * dJ[:, 1]
            KdJ1 = K01 * dJ[:, 0] + K11 * dJ[:, 1]
            den = nin[:, 0] * KdJ0 + nin[:, 1] * KdJ1
            un = (u * nin).sum(1)
            j = un / np.where(np.abs(den) < 1e-12, 1e-12, den)
            J0 = np.where(slide, j * dJ[:, 0], J0)
            J1 = np.where(slide, j * dJ[:, 1], J1)
        J0 = np.where(active, J0, 0.0)
        J1 = np.where(active, J1, 0.0)
        om = (rc[:, 0] * J1 - rc[:, 1] * J0) / k2
        # COM world
        cx, cy = self.com
        comw = pos + np.stack([c * cx - s * cy, s * cx + c * cy], 1)
        comw = comw + np.stack([c * J0 - s * J1, s * J0 + c * J1], 1)
        th2 = th + om
        c2, s2 = np.cos(th2), np.sin(th2)
        pos2 = comw - np.stack([c2 * cx - s2 * cy, s2 * cx + c2 * cy], 1)
        return pos2, th2


class GeneratedApproach:
    W_TH = 0.35
    STEP_PEN = 0.0015
    KMAX = 30
    NAV_OVER = 3.0
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.rng = np.random.default_rng(0)

    # ------------------------------------------------------------------
    def reset(self, state, info):
        self.model = Model(state)
        self.goal = np.array(state[29:32], float)
        self.plan = []  # list of actions
        self.expect_block = None
        self.nsteps = 0
        self._build_candidates(state)

    def _build_candidates(self, obs):
        m = self.model
        w, L, V = float(obs[12]), float(obs[13]), float(obs[14])
        pts, nrm = [], []

        def edge(p0, p1, n, k):
            for f in np.linspace(0, 1, k):
                pts.append(np.array(p0) * (1 - f) + np.array(p1) * f)
                nrm.append(n)
        e = 0.02
        edge((-L / 2 + e, 0), (L / 2 - e, 0), (0, 1), 13)          # top
        edge((-L / 2, -e), (-L / 2, -w + e), (-1, 0), 1)             # left end
        edge((L / 2, -e), (L / 2, -w + e), (1, 0), 1)                # right end
        edge((-L / 2 + e, -w), (-w / 2 - 0.12, -w), (0, -1), 5)      # bottom left
        edge((w / 2 + 0.12, -w), (L / 2 - e, -w), (0, -1), 5)       # bottom right
        edge((-w / 2, -w - 0.12), (-w / 2, -w - V + e), (-1, 0), 9)  # stem left
        edge((w / 2, -w - 0.12), (w / 2, -w - V + e), (1, 0), 9)     # stem right
        edge((0, -w - V), (0, -w - V), (0, -1), 1)                    # stem tip
        pts = np.array(pts, float)
        nrm = np.array(nrm, float)
        # side edges: only mid point, use exact mid
        angs = np.deg2rad(np.array([-50, -35, -20, -8, 0, 8, 20, 35, 50]))
        P, Nn, A = [], [], []
        for i in range(len(pts)):
            for a in angs:
                P.append(pts[i])
                Nn.append(nrm[i])
                A.append(a)
        self.c_pts = np.array(P)
        self.c_nrm = np.array(Nn)
        self.c_ang = np.array(A)

    # ------------------------------------------------------------------
    def _cost(self, pos, th):
        ex = pos[..., 0] - self.goal[0]
        ey = pos[..., 1] - self.goal[1]
        et = _wrap(th - self.goal[2])
        return np.sqrt(ex ** 2 + ey ** 2) + self.W_TH * np.abs(et)

    def _solved(self, pos, th):
        return (abs(pos[0] - self.goal[0]) < 0.03 and abs(pos[1] - self.goal[1]) < 0.03
                and abs(_wrap(th - self.goal[2])) < np.deg2rad(8))

    def _cost_tight(self, pos, th):
        ex = np.abs(pos[..., 0] - self.goal[0]) / 0.03
        ey = np.abs(pos[..., 1] - self.goal[1]) / 0.03
        et = np.abs(_wrap(th - self.goal[2])) / np.deg2rad(8)
        return np.maximum(np.maximum(ex, ey), et)

    def _plan_push(self, obs):
        m = self.model
        pos0 = np.array(obs[0:2], float)
        th0 = float(obs[2])
        rob0 = np.array(obs[16:18], float)
        c, s = math.cos(th0), math.sin(th0)
        Rm = np.array([[c, -s], [s, c]])
        r = m.r
        cands_start, cands_dir = [], []
        # world contact points + normals
        pw = self.c_pts @ Rm.T + pos0
        nw = self.c_nrm @ Rm.T
        start = pw + nw * (r + 0.03)
        ca, sa = np.cos(self.c_ang), np.sin(self.c_ang)
        nin = -nw
        dirs = np.stack([ca * nin[:, 0] - sa * nin[:, 1], sa * nin[:, 0] + ca * nin[:, 1]], 1)
        # also: continue from current robot position in a set of directions
        cur_d = np.linspace(-np.pi, np.pi, 24, endpoint=False)
        cstart = np.repeat(rob0[None], len(cur_d), 0)
        cdirs = np.stack([np.cos(cur_d), np.sin(cur_d)], 1)
        starts = np.concatenate([start, cstart])
        dirs = np.concatenate([dirs, cdirs])
        # validity of starts
        ok = (starts[:, 0] >= LO + 0.01) & (starts[:, 0] <= HI - 0.01) & \
             (starts[:, 1] >= LO + 0.01) & (starts[:, 1] <= HI - 0.01)
        dstart = m.world_dist(np.repeat(pos0[None], len(starts), 0), np.full(len(starts), th0), starts)
        ok &= (dstart > r + 0.02) | (np.arange(len(starts)) >= len(start))
        starts, dirs = starts[ok], dirs[ok]
        # navigation cost estimate
        nav = np.linalg.norm(starts - rob0, axis=1) / AMAX
        nav = nav * 1.3 + np.where(nav > 1e-6, self.NAV_OVER, 0.0)
        cost0 = float(self._cost(pos0, th0))
        err_pos = np.linalg.norm(pos0 - self.goal[:2])
        err_th = abs(_wrap(th0 - self.goal[2]))
        steps_opts = [AMAX, 0.02, 0.008]
        best = None
        KMAX = self.KMAX
        tight0 = float(self._cost_tight(pos0, th0))
        for ss in steps_opts:
            N = len(starts)
            pos = np.repeat(pos0[None], N, 0)
            th = np.full(N, th0)
            rob = starts.copy()
            a = dirs * ss
            alive = np.ones(N, bool)
            for k in range(1, KMAX + 1):
                nrob = rob + a
                inb = (nrob[:, 0] >= LO) & (nrob[:, 0] <= HI) & (nrob[:, 1] >= LO) & (nrob[:, 1] <= HI)
                alive &= inb
                pos_n, th_n = m.step(pos, th, rob, a)
                pos = np.where(alive[:, None], pos_n, pos)
                th = np.where(alive, th_n, th)
                rob = np.where(alive[:, None], nrob, rob)
                # block corners within walls
                cc, sc = np.cos(th), np.sin(th)
                cx = pos[:, 0:1] + cc[:, None] * m.corners[None, :, 0] - sc[:, None] * m.corners[None, :, 1]
                cy = pos[:, 1:2] + sc[:, None] * m.corners[None, :, 0] + cc[:, None] * m.corners[None, :, 1]
                wall = (cx.min(1) < 0.02) | (cx.max(1) > 4.98) | (cy.min(1) < 0.02) | (cy.max(1) > 4.98)
                alive &= ~wall
                cst = self._cost(pos, th)
                tc = self._cost_tight(pos, th)
                total = nav + k
                score = cst + self.STEP_PEN * total + np.where(tc < 1.0, -1.0, 0.0) * 0
                score = np.where(tc < 0.8, -10.0 + 0.001 * total, score)
                score = np.where(alive, score, np.inf)
                i = int(np.argmin(score))
                if best is None or score[i] < best[0]:
                    best = (float(score[i]), starts[i].copy(), a[i].copy(), k, float(cst[i]))
        return best, cost0

    # ------------------------------------------------------------------
    def _navigate(self, obs, target):
        """Return list of actions from robot pos to target avoiding the block."""
        m = self.model
        rob = np.array(obs[16:18], float)
        pos0 = np.array(obs[0:2], float)
        th0 = float(obs[2])
        clear = m.r + 0.015

        def seg_clear(p, q):
            n = max(2, int(np.linalg.norm(q - p) / 0.01) + 1)
            f = np.linspace(0, 1, n)[:, None]
            pts = p * (1 - f) + q * f
            d = m.world_dist(np.repeat(pos0[None], n, 0), np.full(n, th0), pts)
            d0 = d[0]
            # allow starting inside margin as long as we don't get closer
            return bool(np.all((d >= clear) | (d >= d0 - 1e-9) & (np.arange(n) < 10)))

        if seg_clear(rob, target):
            path = [rob, target]
        else:
            path = self._astar(rob, target, pos0, th0, clear)
            if path is None:
                path = [rob, target]
        acts = []
        cur = rob.copy()
        for wp in path[1:]:
            wp = np.asarray(wp, float)
            while True:
                d = wp - cur
                dist = np.linalg.norm(d)
                if dist < 1e-9:
                    break
                n = int(math.ceil(dist / AMAX - 1e-9))
                stp = d / n
                for _ in range(n):
                    acts.append(stp.copy())
                cur = wp.copy()
                break
        return acts

    def _astar(self, start, goal, pos0, th0, clear):
        m = self.model
        res = 0.04
        n = int(round((HI - LO) / res)) + 1
        xs = LO + np.arange(n) * res
        X, Y = np.meshgrid(xs, xs, indexing="ij")
        pts = np.stack([X.ravel(), Y.ravel()], 1)
        d = m.world_dist(np.repeat(pos0[None], len(pts), 0), np.full(len(pts), th0), pts)
        free = (d >= clear + 0.01).reshape(n, n)

        def cell(p):
            i = int(round((p[0] - LO) / res))
            j = int(round((p[1] - LO) / res))
            return min(max(i, 0), n - 1), min(max(j, 0), n - 1)

        s = cell(start)
        g = cell(goal)
        # ensure start/goal free (search nearest free)
        def nearest_free(c):
            if free[c]:
                return c
            idx = np.argwhere(free)
            dd = ((idx - np.array(c)) ** 2).sum(1)
            k = int(np.argmin(dd))
            return tuple(idx[k])
        s2 = nearest_free(s)
        g2 = nearest_free(g)
        nbrs = [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (1, 1, 1.4142), (1, -1, 1.4142),
                (-1, 1, 1.4142), (-1, -1, 1.4142)]
        dist = {s2: 0.0}
        prev = {}
        h = lambda c: math.hypot(c[0] - g2[0], c[1] - g2[1])
        pq = [(h(s2), 0.0, s2)]
        found = False
        while pq:
            f, gc, c = heapq.heappop(pq)
            if c == g2:
                found = True
                break
            if gc > dist.get(c, 1e18):
                continue
            for di, dj, w in nbrs:
                nc = (c[0] + di, c[1] + dj)
                if 0 <= nc[0] < n and 0 <= nc[1] < n and free[nc]:
                    ng = gc + w
                    if ng < dist.get(nc, 1e18):
                        dist[nc] = ng
                        prev[nc] = c
                        heapq.heappush(pq, (ng + h(nc), ng, nc))
        if not found:
            return None
        cells = [g2]
        while cells[-1] != s2:
            cells.append(prev[cells[-1]])
        cells.reverse()
        raw = [np.array(start)] + [np.array([xs[i], xs[j]]) for i, j in cells] + [np.array(goal)]
        # shortcut smoothing
        def seg_ok(p, q):
            k = max(2, int(np.linalg.norm(q - p) / 0.01) + 1)
            f = np.linspace(0, 1, k)[:, None]
            pp = p * (1 - f) + q * f
            dd = m.world_dist(np.repeat(pos0[None], k, 0), np.full(k, th0), pp)
            return bool(np.all(dd >= clear))
        out = [raw[0]]
        i = 0
        while i < len(raw) - 1:
            j = len(raw) - 1
            while j > i + 1 and not seg_ok(raw[i], raw[j]):
                j -= 1
            out.append(raw[j])
            i = j
        return out

    # ------------------------------------------------------------------
    def get_action(self, state):
        obs = np.asarray(state, float)
        self.nsteps += 1
        pos = obs[0:3]
        if self.plan and self.expect_block is not None:
            # replan if block moved unexpectedly during navigation
            if np.abs(pos[0:2] - self.expect_block[0:2]).max() > 0.01 or \
                    abs(_wrap(pos[2] - self.expect_block[2])) > 0.02:
                self.plan = []
        if not self.plan:
            best, cost0 = self._plan_push(obs)
            if best is None:
                return np.zeros(2)
            _, start, a, k, cst = best
            acts = self._navigate(obs, start) if np.linalg.norm(start - obs[16:18]) > 1e-9 else []
            self.expect_block = obs[0:3].copy()
            self.nav_len = len(acts)
            self.plan = acts + [a.copy() for _ in range(k)]
        act = self.plan.pop(0)
        if self.nav_len > 0:
            self.nav_len -= 1
            if self.nav_len == 0:
                self.expect_block = None
        else:
            self.expect_block = None
        return np.clip(act, -AMAX, AMAX)
