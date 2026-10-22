"""Model-based greedy push planner for DynPushT2D.

Block model: quasi-static, sticking point contact (mu~1), ellipsoidal limit surface
about the centre of mass with c^2 = I/m of a uniform T.
Body frame: origin = obs[0:2]; bar x in [-L/2,L/2], y in [-w,0]; stem x in [-w/2,w/2], y in [-w-Lv,-w].
"""
import heapq
import time
import numpy as np

RAD = 0.1
AMAX = 0.049
LO, HI = 0.1, 4.9


def wrap(a):
    return (a + np.pi) % (2 * np.pi) - np.pi


def rot(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[c, -s], [s, c]])


class Geom:
    def __init__(self, w, L, Lv):
        self.w, self.L, self.Lv = w, L, Lv
        a1, a2 = w * L, w * Lv
        y1, y2 = -w / 2, -w - Lv / 2
        yc = (a1 * y1 + a2 * y2) / (a1 + a2)
        I = a1 * ((L * L + w * w) / 12 + (y1 - yc) ** 2) + a2 * ((w * w + Lv * Lv) / 12 + (y2 - yc) ** 2)
        self.C = np.array([0.0, yc])
        self.c2 = I / (a1 + a2)
        self.rects = np.array([[-L / 2, L / 2, -w, 0.0], [-w / 2, w / 2, -w - Lv, -w]])
        self.corners = np.array([[-L / 2, 0], [L / 2, 0], [L / 2, -w], [-L / 2, -w],
                                 [-w / 2, -w - Lv], [w / 2, -w - Lv]])
        # contact candidates: (point, outward normal)
        cands = []
        h = L / 2
        for x in np.linspace(-h + 0.03, h - 0.03, 9):
            cands.append(((x, 0.0), (0, 1)))
        for x in np.linspace(w / 2 + 0.03, h - 0.03, 4):
            cands.append(((x, -w), (0, -1)))
            cands.append(((-x, -w), (0, -1)))
        cands.append(((h, -w / 2), (1, 0)))
        cands.append(((-h, -w / 2), (-1, 0)))
        for y in np.linspace(-w - 0.08, -w - Lv + 0.03, 6):
            cands.append(((w / 2, y), (1, 0)))
            cands.append(((-w / 2, y), (-1, 0)))
        cands.append(((0.0, -w - Lv), (0, -1)))
        self.cq = np.array([c[0] for c in cands], dtype=float)
        self.cn = np.array([c[1] for c in cands], dtype=float)

    def closest(self, p):
        best = None
        for (x0, x1, y0, y1) in self.rects:
            q = np.array([min(max(p[0], x0), x1), min(max(p[1], y0), y1)])
            d = np.linalg.norm(p - q)
            if d < 1e-9:
                continue
            if best is None or d < best[0]:
                best = (d, q, (p - q) / d)
        if best is None:
            return None, None
        return best[1], best[2]

    def dist_body(self, P):
        """min distance from body-frame points P (N,2) to T (0 inside)."""
        best = None
        for (x0, x1, y0, y1) in self.rects:
            dx = np.maximum(np.maximum(x0 - P[:, 0], P[:, 0] - x1), 0)
            dy = np.maximum(np.maximum(y0 - P[:, 1], P[:, 1] - y1), 0)
            d = np.hypot(dx, dy)
            best = d if best is None else np.minimum(best, d)
        return best


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.plan = []

    def reset(self, state, info):
        s = np.asarray(state, dtype=float)
        self.g = Geom(s[12], s[13], s[14])
        self.plan = []
        self.last_pose = None
        self.margin = (0.012, 0.03, 0.07)
        self.t_used = 0.0
        self.push_count = 0
        self.t_used = 0.0

    ANG_W = 2.2
    ANGS = (-35, -18, 0, 18, 35)
    STANDOFF = 0.04
    FRIC = 0.85
    NSTEPS = 150
    USE_CONTACT = True
    REPLAN_K = 10
    LOOK = 8

    # ---------------- helpers ----------------
    def err(self, ref, th, goal):
        g = self.g
        gref, gth = goal[0:2], goal[2]
        m = self.margin
        Rg = rot(gth)
        gcom = gref + Rg @ g.C
        # env checks |theta - theta_goal| WITHOUT wrapping; theta obs is in (-pi, pi]
        alo = max(gth - m[2], -np.pi + 0.015)
        ahi = min(gth + m[2], np.pi - 0.015)
        if alo > ahi:
            alo = ahi = gth
        dth = np.maximum(np.abs(wrap(th - 0.5 * (alo + ahi))) - 0.5 * (ahi - alo), 0)
        # com position
        c, s = np.cos(th), np.sin(th)
        comx = ref[..., 0] - s * g.C[1]
        comy = ref[..., 1] + c * g.C[1]
        e_ref = np.hypot(np.maximum(np.abs(ref[..., 0] - gref[0]) - m[0], 0),
                         np.maximum(np.abs(ref[..., 1] - gref[1]) - m[0], 0))
        e_com = np.hypot(np.maximum(np.abs(comx - gcom[0]) - m[1], 0),
                         np.maximum(np.abs(comy - gcom[1]) - m[1], 0))
        return e_ref + e_com + self.ANG_W * dth

    def seg_free(self, pose, a, b, clear):
        if a is self.start_pt:
            clear = min(clear, self.start_d - 0.004)
        n = max(2, int(np.linalg.norm(b - a) / 0.01) + 1)
        t = np.linspace(0, 1, n)[:, None]
        P = a[None] + t * (b - a)[None]
        Pb = (P - pose[0:2]) @ rot(pose[2])  # world->body: R^T (p - o)
        return bool(np.all(self.g.dist_body(Pb) > clear))

    def nav_path(self, pose, start, target):
        """visibility-graph shortest path; returns (waypoints, cost) or (None, inf)."""
        clear = RAD + 0.012
        if self.seg_free(pose, start, target, clear):
            return [target], self._plen([start, target])
        nodes = self.nodes
        pts = [start] + nodes + [target]
        N = len(pts)
        dist = [np.inf] * N
        prev = [-1] * N
        dist[0] = 0.0
        pq = [(0.0, 0)]
        while pq:
            d, i = heapq.heappop(pq)
            if d > dist[i]:
                continue
            if i == N - 1:
                break
            for j in range(1, N):
                if j == i:
                    continue
                key = (min(i, j), max(i, j))
                if i > 0 and j < N - 1:
                    ok = self.node_vis.get(key)
                    if ok is None:
                        ok = self.seg_free(pose, pts[i], pts[j], clear)
                        self.node_vis[key] = ok
                else:
                    ok = self.seg_free(pose, pts[i], pts[j], clear)
                if not ok:
                    continue
                nd = d + self._plen([pts[i], pts[j]])
                if nd < dist[j]:
                    dist[j] = nd
                    prev[j] = i
                    heapq.heappush(pq, (nd, j))
        if not np.isfinite(dist[N - 1]):
            return None, np.inf
        path = []
        k = N - 1
        while k > 0:
            path.append(pts[k])
            k = prev[k]
        return path[::-1], dist[N - 1]

    @staticmethod
    def _plen(pts):
        s = 0.0
        for a, b in zip(pts[:-1], pts[1:]):
            s += np.max(np.abs(b - a)) / AMAX
        return s

    def build_nodes(self, pose):
        g = self.g
        R = rot(pose[2])
        d = RAD + 0.05
        nodes = []
        for (x0, x1, y0, y1) in g.rects:
            for (x, y) in [(x0 - d, y0 - d), (x0 - d, y1 + d), (x1 + d, y0 - d), (x1 + d, y1 + d)]:
                nodes.append(np.array([x, y]))
        nb = np.array(nodes)
        ok = g.dist_body(nb) > RAD + 0.02
        out = []
        for p, o in zip(nb, ok):
            if not o:
                continue
            w = pose[0:2] + R @ p
            if LO + 0.01 <= w[0] <= HI - 0.01 and LO + 0.01 <= w[1] <= HI - 0.01:
                out.append(w)
        self.nodes = out
        self.node_vis = {}

    # ---------------- planning ----------------
    MODE = 'rate'
    RC = 4.0
    V = 0.03

    def score(self, E0, E, steps):
        if self.MODE in ('rate', 'rate_old'):
            return (E0 - E) / (steps + self.RC)
        return -(steps + E / self.V)

    def plan_push(self, s, lookahead=0):
        g = self.g
        pose = s[0:3].copy()
        goal = s[29:32]
        robot = s[16:18].copy()
        E0 = float(self.err(pose[0:2], pose[2], goal))

        angs = np.deg2rad(list(self.ANGS))
        R0 = rot(pose[2])
        cq, cn = g.cq, g.cn
        ncont = 0
        rb0 = (robot - pose[0:2]) @ R0
        if self.USE_CONTACT and g.dist_body(rb0[None])[0] < RAD + 0.012:
            q, n = g.closest(rb0)
            if q is not None:
                cq = np.vstack([cq, q[None]])
                cn = np.vstack([cn, n[None]])
                ncont = 1
        Q = np.repeat(cq, len(angs), 0)
        Nn = np.repeat(cn, len(angs), 0)
        A = np.tile(angs, len(cq))
        K = len(Q)
        is_cont = np.zeros(K, bool)
        if ncont:
            is_cont[-len(angs):] = True
        # push direction in body frame (inward normal rotated), then world
        inn = -Nn
        ca, sa = np.cos(A), np.sin(A)
        ub = np.stack([ca * inn[:, 0] - sa * inn[:, 1], sa * inn[:, 0] + ca * inn[:, 1]], 1)
        uw = ub @ R0.T
        pb_body = Q + Nn * RAD
        r = Q - g.C
        c2 = g.c2
        a11 = 1 + r[:, 1] ** 2 / c2
        a22 = 1 + r[:, 0] ** 2 / c2
        a12 = -r[:, 0] * r[:, 1] / c2
        det = a11 * a22 - a12 * a12
        tb = np.stack([-Nn[:, 1], Nn[:, 0]], 1)

        com = np.tile(pose[0:2] + R0 @ g.C, (K, 1))
        th = np.full(K, pose[2])
        valid = np.ones(K, bool)
        ds = 0.01
        nsteps = self.NSTEPS
        best = (-np.inf, None)
        # travel cost to each candidate start
        standoff = self.STANDOFF
        so = np.where(is_cont, 0.0, standoff)
        pre = pose[0:2] + pb_body @ R0.T - uw * so[:, None]
        pre[is_cont] = robot
        travel = np.full(K, np.inf)
        paths = [None] * K
        self.build_nodes(pose)
        start = robot.copy()
        prefix = []
        rb = (robot - pose[0:2]) @ R0
        dd = g.dist_body(rb[None])[0]
        if dd < RAD + 0.03:
            # retreat: pick direction maximizing clearance
            angs_r = np.linspace(0, 2 * np.pi, 24, endpoint=False)
            dirs = np.stack([np.cos(angs_r), np.sin(angs_r)], 1)
            bestd, bestp = -1, None
            for mag in (0.04, 0.08):
                P = rb[None] + dirs * mag
                Pw = pose[0:2] + P @ R0.T
                dv = g.dist_body(P)
                inb = np.all((Pw >= LO + 0.005) & (Pw <= HI - 0.005), 1)
                dv = np.where(inb, dv, -1)
                j = int(np.argmax(dv))
                if dv[j] > bestd + 0.01:
                    bestd, bestp = dv[j], Pw[j]
                if bestd > RAD + 0.02:
                    break
            if bestp is not None:
                prefix = [bestp]
                start = bestp
        self.start_d = g.dist_body(((start - pose[0:2]) @ R0)[None])[0]
        self.start_pt = start
        pre_body = (pre - pose[0:2]) @ R0
        pre_ok = g.dist_body(pre_body) > RAD + 0.015
        pre_ok &= np.all((pre >= LO + 0.005) & (pre <= HI - 0.005), 1)
        valid &= pre_ok | is_cont
        # lower bound travel (straight line) for pruning
        lb = np.max(np.abs(pre - start), 1) / AMAX + len(prefix)
        lb[is_cont] = 0.0

        cw = pose[0:2] + g.corners @ R0.T
        wlo = np.minimum(0.03, cw.min(0) - 0.01)
        whi = np.maximum(4.97, cw.max(0) + 0.01)
        results_len = np.zeros(K)
        results_E = np.full(K, np.inf)
        results_S = np.full(K, -np.inf)
        results_ref = np.zeros((K, 2))
        results_th = np.zeros(K)
        mcu = np.max(np.abs(uw), 1)
        stepcnt = standoff / ds
        for k in range(1, nsteps + 1):
            c, sn = np.cos(th), np.sin(th)
            # world->body of push dir
            db = np.stack([c * uw[:, 0] + sn * uw[:, 1], -sn * uw[:, 0] + c * uw[:, 1]], 1) * ds
            f0 = (a22 * db[:, 0] - a12 * db[:, 1]) / det
            f1 = (-a12 * db[:, 0] + a11 * db[:, 1]) / det
            fn = -(f0 * Nn[:, 0] + f1 * Nn[:, 1])
            ft = f0 * tb[:, 0] + f1 * tb[:, 1]
            valid &= (fn > 0) & (np.abs(ft) <= self.FRIC * fn)
            om = (r[:, 0] * f1 - r[:, 1] * f0) / c2
            com = com + np.stack([c * f0 - sn * f1, sn * f0 + c * f1], 1)
            th = th + om
            c, sn = np.cos(th), np.sin(th)
            ref = com - np.stack([-sn * g.C[1], c * g.C[1]], 1)
            # wall check on corners
            cx = ref[:, 0][:, None] + c[:, None] * g.corners[None, :, 0] - sn[:, None] * g.corners[None, :, 1]
            cy = ref[:, 1][:, None] + sn[:, None] * g.corners[None, :, 0] + c[:, None] * g.corners[None, :, 1]
            valid &= (cx.min(1) > wlo[0]) & (cx.max(1) < whi[0]) & (cy.min(1) > wlo[1]) & (cy.max(1) < whi[1])
            pw = pre + uw * (so[:, None] + k * ds)
            valid &= np.all((pw >= LO + 0.005) & (pw <= HI - 0.005), 1)
            if not valid.any():
                break
            E = self.err(ref, th, goal)
            sc = -E if self.MODE == 'rate_old' else self.score(E0, E, lb + k * ds * mcu / AMAX + 3)
            better = valid & (E < E0 - 1e-4) & (sc > results_S)
            results_S = np.where(better, sc, results_S)
            results_E = np.where(better, E, results_E)
            results_len = np.where(better, k * ds, results_len)
            results_ref = np.where(better[:, None], ref, results_ref)
            results_th = np.where(better, th, results_th)

        push_steps = results_len * mcu / AMAX + 3
        order = np.argsort(-results_S)
        feas = []
        best_rate = -np.inf
        for i in order[:60]:
            if not np.isfinite(results_S[i]):
                break
            if not lookahead and self.MODE != 'rate_old' and results_S[i] <= best_rate:
                break
            if is_cont[i]:
                path, cost = [], -len(prefix)
            else:
                path, cost = self.nav_path(pose, start, pre[i])
            if path is None:
                continue
            steps = cost + len(prefix) + push_steps[i]
            rate = self.score(E0, results_E[i], steps)
            feas.append((rate, i, path, steps))
            best_rate = max(best_rate, rate)
            if lookahead and len(feas) >= 3 * lookahead:
                break
        if not feas:
            return None
        feas.sort(key=lambda x: -x[0])
        best = feas[0]
        if lookahead and results_E[best[1]] > 0:
            best_c = -np.inf
            for (rate, i, path, steps) in feas[:lookahead]:
                s2 = s.copy()
                s2[0:2] = results_ref[i]
                s2[2] = wrap(results_th[i])
                s2[16:18] = pre[i] + uw[i] * (so[i] + results_len[i])
                p2 = self.plan_push(s2, 0)
                if p2 is None or results_E[i] <= 0:
                    c = self.score(E0, results_E[i], steps)
                else:
                    c = self.score(E0, p2['Epred'], steps + p2['steps'])
                if c > best_c:
                    best_c, best = c, (rate, i, path, steps)
        rate, i, path, steps = best
        return dict(path=(prefix + path) if not is_cont[i] else [], u=uw[i], L=results_len[i] + so[i],
                    Epred=results_E[i], E0=E0, steps=steps)

    # ---------------- execution ----------------
    def build_actions(self, robot, plan):
        acts = []
        p = robot.copy()
        for wp in plan['path']:
            while True:
                d = wp - p
                m = np.max(np.abs(d))
                if m < 1e-6:
                    break
                a = d if m <= AMAX else d * (AMAX / m)
                acts.append(('nav', a))
                p = p + a
        u = plan['u']
        Ltot = plan['L']
        done = 0.0
        while done < Ltot - 1e-6:
            rem = Ltot - done
            mc = max(abs(u[0]), abs(u[1]))
            st = AMAX / mc if rem > 0.15 else max(0.01, min(AMAX, rem / 3))
            st = min(st, rem)
            acts.append(('push', u * st))
            done += st
        return acts

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        if (self.plan and self.REPLAN_K > 0 and self.t_used < 40.0 and self.plan[0][0] == 'push'
                and self.push_count >= self.REPLAN_K and len(self.plan) > 2):
            self.plan = []
        if not self.plan:
            self.push_count = 0
            t0 = time.time()
            look = self.LOOK if self.t_used < 25.0 else 0
            try:
                p = self.plan_push(s, look)
                if p is None and max(self.margin) > 0:
                    # predicted success but env did not terminate: tighten margins
                    self.margin = tuple(0.5 * x for x in self.margin) if max(self.margin) > 0.01 else (0.0, 0.0, 0.0)
                    p = self.plan_push(s, look)
            except Exception:
                p = None
            self.t_used += time.time() - t0
            if p is None:
                # fallback: move away from the block, towards the arena centre
                com = s[0:2] + rot(s[2]) @ self.g.C
                d = s[16:18] - com
                d = d / (np.linalg.norm(d) + 1e-9) + 0.5 * (np.array([2.5, 2.5]) - s[16:18]) / 2.5
                d = d / (np.linalg.norm(d) + 1e-9)
                self.plan = [('nav', d * AMAX)] * 3
                _, a = self.plan.pop(0)
                return self._safe(s, a)
            self.plan = self.build_actions(s[16:18], p)
        kind, a = self.plan.pop(0)
        if kind == 'push':
            self.push_count += 1
        return self._safe(s, a)

    def _safe(self, s, a):
        a = np.clip(np.asarray(a, dtype=float), -AMAX, AMAX)
        rob = s[16:18]
        nxt = np.clip(rob + a, LO + 1e-3, HI - 1e-3)
        a = np.clip(nxt - rob, -AMAX, AMAX)
        return a.astype(np.float64)
