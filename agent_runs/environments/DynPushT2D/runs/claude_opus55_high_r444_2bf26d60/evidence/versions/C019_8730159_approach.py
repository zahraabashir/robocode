"""Push-T controller: model-based greedy push selection + visibility-graph navigation."""
import heapq
import time
import math

import numpy as np

from model_v import VModel

R_ROBOT = 0.1
WALL_LO = 0.0
WALL_HI = 5.0
MAXD = 0.049


def wrap(a):
    return (a + math.pi) % (2 * math.pi) - math.pi


def local_poly(w, lh, lv):
    """T polygon in the block frame, CCW order."""
    a, h = lh / 2.0, w / 2.0
    return np.array([
        [-a, 0], [-a, -w], [-h, -w], [-h, -w - lv], [h, -w - lv], [h, -w], [a, -w], [a, 0],
    ])


def rects_local(w, lh, lv):
    a, h = lh / 2.0, w / 2.0
    # (xmin, xmax, ymin, ymax)
    return [(-a, a, -w, 0.0), (-h, h, -w - lv, -w)]


def to_world(pts, pose):
    c, s = math.cos(pose[2]), math.sin(pose[2])
    R = np.array([[c, -s], [s, c]])
    return pts @ R.T + np.asarray(pose[:2])


def to_local(pts, pose):
    c, s = math.cos(pose[2]), math.sin(pose[2])
    R = np.array([[c, -s], [s, c]])
    return (np.asarray(pts) - np.asarray(pose[:2])) @ R


def dist_to_T_local(p, rects):
    """Signed-ish distance from local point(s) p (N,2) to the union of rects (positive outside)."""
    p = np.atleast_2d(p)
    best = None
    for (x0, x1, y0, y1) in rects:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        hx, hy = (x1 - x0) / 2, (y1 - y0) / 2
        dx = np.abs(p[:, 0] - cx) - hx
        dy = np.abs(p[:, 1] - cy) - hy
        out = np.hypot(np.maximum(dx, 0), np.maximum(dy, 0))
        ins = np.minimum(np.maximum(dx, dy), 0)
        d = out + ins
        best = d if best is None else np.minimum(best, d)
    return best


class TModel:
    """Quasi-static single point contact push model (placeholder / fitted params)."""

    def __init__(self, w, lh, lv, com=(0.0, None), rho2=None, mu=0.3):
        self.w, self.lh, self.lv = w, lh, lv
        self.rects = rects_local(w, lh, lv)
        self.poly = local_poly(w, lh, lv)
        # geometric centroid
        a1 = lh * w
        a2 = lv * w
        cy = (a1 * (-w / 2) + a2 * (-w - lv / 2)) / (a1 + a2)
        self.com = np.array([0.0, cy if com[1] is None else com[1]])
        if rho2 is None:
            # radius of gyration^2 about com (uniform density)
            i1 = a1 * (lh ** 2 + w ** 2) / 12 + a1 * (-w / 2 - self.com[1]) ** 2
            i2 = a2 * (lv ** 2 + w ** 2) / 12 + a2 * (-w - lv / 2 - self.com[1]) ** 2
            rho2 = (i1 + i2) / (a1 + a2)
        self.rho2 = rho2
        self.mu = mu

    def closest_local(self, p):
        """Closest boundary point and outward normal for local points p (N,2)."""
        p = np.atleast_2d(p)
        best_d = np.full(len(p), np.inf)
        best_q = np.zeros_like(p)
        best_n = np.zeros_like(p)
        poly = self.poly
        n = len(poly)
        for i in range(n):
            a = poly[i]
            b = poly[(i + 1) % n]
            ab = b - a
            L2 = ab @ ab
            t = np.clip(((p - a) @ ab) / L2, 0, 1)
            q = a + t[:, None] * ab
            d = np.hypot(p[:, 0] - q[:, 0], p[:, 1] - q[:, 1])
            m = d < best_d
            best_d = np.where(m, d, best_d)
            best_q[m] = q[m]
            # outward normal for CCW polygon: (dy, -dx)
            nn = np.array([ab[1], -ab[0]]) / math.sqrt(L2)
            best_n[m] = nn
        return best_q, best_n, best_d

    def step(self, pose, robot, act):
        """Vectorized: pose (N,3), robot (N,2), act (N,2) -> new pose (N,3), new robot (N,2)."""
        pose = np.atleast_2d(pose).astype(float)
        robot = np.atleast_2d(robot).astype(float)
        act = np.atleast_2d(act).astype(float)
        newr = robot + act
        th = pose[:, 2]
        c, s = np.cos(th), np.sin(th)
        # to local
        d = newr - pose[:, :2]
        pl = np.stack([c * d[:, 0] + s * d[:, 1], -s * d[:, 0] + c * d[:, 1]], 1)
        al = np.stack([c * act[:, 0] + s * act[:, 1], -s * act[:, 0] + c * act[:, 1]], 1)
        inside = dist_to_T_local(pl, self.rects) < 0
        q, n, dist = self.closest_local(pl)
        # for points inside the polygon, closest boundary normal is correct (pointing out)
        pen = np.where(inside, R_ROBOT + dist, R_ROBOT - dist)
        active = pen > 1e-9
        out = pose.copy()
        if not np.any(active):
            return out, newr
        # contact point approx q, push direction into block = -n
        r = q - self.com
        # frictional: push direction within friction cone around -n toward -al projection
        fn = -n
        tdir = np.stack([-fn[:, 1], fn[:, 0]], 1)
        at = np.sum(al * tdir, 1)
        an = np.sum(al * fn, 1)
        # force direction: normal + mu*sign(tangential motion) (sticking approx if small)
        ratio = np.clip(np.where(an > 1e-9, at / np.maximum(an, 1e-9), 0.0), -self.mu, self.mu)
        f = fn + ratio[:, None] * tdir
        tau = r[:, 0] * f[:, 1] - r[:, 1] * f[:, 0]
        v = f
        om = tau / self.rho2
        # velocity of contact point along fn per unit scale
        vc = v + np.stack([-om * r[:, 1], om * r[:, 0]], 1)
        vn = np.sum(vc * fn, 1)
        k = np.where(active, pen / np.maximum(vn, 1e-6), 0.0)
        # block displacement (local, of com)
        dv = v * k[:, None]
        dom = om * k
        # new com position local: com + dv; origin moves as rotation about com
        cd, sd = np.cos(dom), np.sin(dom)
        oc = -self.com  # origin relative to com
        oc_new = np.stack([cd * oc[0] - sd * oc[1], sd * oc[0] + cd * oc[1]], 1)
        o_new_local = self.com + dv + oc_new
        wx = c * o_new_local[:, 0] - s * o_new_local[:, 1]
        wy = s * o_new_local[:, 0] + c * o_new_local[:, 1]
        out[:, 0] = pose[:, 0] + wx
        out[:, 1] = pose[:, 1] + wy
        out[:, 2] = th + dom
        return out, newr


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.goal_bonus = 0.05
        self.overhead = 2.0
        self.wa = 0.4
        self.cost_mode = 0
        self.M = 0
        self.infl = R_ROBOT + 0.015
        self.wall_margin = 0.01
        self.stuck_rate = 1e-3
        self.stage = 0
        self.pre_clear = 0.035
        self.final_infl = R_ROBOT + 0.008
        self.sub_clear = 1.0
        self.H2 = 30
        self.H = 40
        self.replan_every = 8
        self.model = None

    # ------------------------------------------------------------------
    def reset(self, state, info):
        s = np.asarray(state, dtype=float)
        self.w, self.lh, self.lv = s[12], s[13], s[14]
        self._cand_cache = {}
        self.t0 = time.time()
        self.model = TModel(self.w, self.lh, self.lv)
        self.sim = VModel(self.w, self.lh, self.lv)
        self.goal = s[29:32].copy()
        tol = math.radians(8) - 0.004
        lo = max(self.goal[2] - tol, -math.pi)
        hi = min(self.goal[2] + tol, math.pi)
        self.gc = 0.5 * (lo + hi)   # centre of the valid (wrapped) angle interval
        self.ghw = 0.5 * (hi - lo)
        self.real_tgt = np.array([self.goal[0], self.goal[1], self.gc, self.ghw, 0.03])
        self.tgt = self.real_tgt.copy()
        self.sub_active = False
        self.mode = "plan"
        self.path = []
        self.push = None
        self.push_left = 0
        self.stall = 0
        self.last_cmd = None
        self.last_robot = None
        self.last_pose = None
        self.blacklist = []
        self.bl_pose = None

    # ------------------------------------------------------------------
    def cost(self, pose):
        pose = np.atleast_2d(pose)
        dp = pose[:, :2] - self.tgt[:2]
        da = np.abs(wrap_arr(pose[:, 2] - self.tgt[2]))
        if self.cost_mode == 1:
            return np.sqrt(dp[:, 0] ** 2 + dp[:, 1] ** 2 + (self.wa * da) ** 2)
        return np.hypot(dp[:, 0], dp[:, 1]) + self.wa * da

    def solved(self, pose):
        return (abs(pose[0] - self.goal[0]) < 0.03 and abs(pose[1] - self.goal[1]) < 0.03
                and abs(wrap(pose[2] - self.gc)) < self.ghw)

    # ------------------------------------------------------------------
    def local_candidates(self, spacing, angs):
        key = (spacing, tuple(angs))
        if key in self._cand_cache:
            return self._cand_cache[key]
        poly = self.model.poly
        n = len(poly)
        starts, dirs = [], []
        for i in range(n):
            a, b = poly[i], poly[(i + 1) % n]
            ab = b - a
            L = np.linalg.norm(ab)
            if L < 0.05:
                continue
            nn = np.array([ab[1], -ab[0]]) / L
            m = max(2, int(L / spacing))
            for t in (np.linspace(0.04 / L, 1 - 0.04 / L, m) if L > 0.1 else [0.5]):
                q = a + t * ab
                for ang in angs:
                    ca, sa = math.cos(ang), math.sin(ang)
                    d = -nn
                    d = np.array([ca * d[0] - sa * d[1], sa * d[0] + ca * d[1]])
                    starts.append(q + nn * (R_ROBOT + 0.02))
                    dirs.append(d)
        res = (np.array(starts), np.array(dirs))
        self._cand_cache[key] = res
        return res

    def candidates(self, pose, coarse=False):
        if coarse:
            st, dr = self.local_candidates(0.12, (-0.4, 0.0, 0.4))
        else:
            st, dr = self.local_candidates(0.06, (-0.5, -0.25, 0.0, 0.25, 0.5))
        return to_world(st, pose), to_world(dr, (0, 0, pose[2]))

    def eval_pushes(self, pose, robot, coarse=False, H=None):
        """Simulate all candidate pushes; return dict of arrays."""
        sw, dw = self.candidates(pose, coarse)
        dr = dist_to_T_local(to_local(robot[None], pose), self.model.rects)[0]
        nh = 12 if coarse else 24
        if dr < R_ROBOT + 0.06:
            angs = np.linspace(0, 2 * np.pi, nh, endpoint=False)
            sw = np.vstack([sw, np.repeat(robot[None], nh, 0)])
            dw = np.vstack([dw, np.stack([np.cos(angs), np.sin(angs)], 1)])
            here = np.zeros(len(sw), bool)
            here[-nh:] = True
        else:
            here = np.zeros(len(sw), bool)
        ok = np.all((sw > WALL_LO + R_ROBOT + 0.01) & (sw < WALL_HI - R_ROBOT - 0.01), 1)
        pre = sw - dw * 0.12
        ds = dist_to_T_local(to_local(sw, pose), self.model.rects)
        dp = dist_to_T_local(to_local(pre, pose), self.model.rects)
        ok &= (ds > R_ROBOT + 0.005) & (dp > R_ROBOT + self.pre_clear)
        ok &= np.all((pre > WALL_LO + R_ROBOT + 0.02) & (pre < WALL_HI - R_ROBOT - 0.02), 1)
        ok |= here
        if self.blacklist:
            sl = to_local(sw, pose)
            dl = to_local(dw, (0, 0, pose[2]))
            for (bp, bd) in self.blacklist:
                bdn = bd / (np.linalg.norm(bd) + 1e-9)
                near = np.hypot(*(sl - bp).T) < 0.12
                same = (dl @ bdn) > 0.8
                ok &= ~(near & same)
        sw, dw, pre, here = sw[ok], dw[ok], pre[ok], here[ok]
        c0 = self.cost(pose[None])[0]
        speeds = [MAXD] if (c0 > 0.35 or coarse) else [MAXD, 0.02]
        ns = len(sw)
        SW = np.vstack([sw] * len(speeds))
        DW = np.vstack([dw] * len(speeds))
        PRE = np.vstack([pre] * len(speeds))
        HERE = np.concatenate([here] * len(speeds))
        SP = np.repeat(np.array(speeds), ns)
        N = len(SW)
        if self.stage:
            travel = np.where(HERE, 0.0, self.travel_est(robot, PRE, pose) + 0.12 / MAXD)
        else:
            travel = np.where(HERE, 0.0, self.travel_est(robot, SW, pose))
        cur = np.repeat(pose[None], N, 0)
        rob = SW.copy()
        bestscore = np.full(N, -np.inf)
        bestk = np.zeros(N, int)
        bestpose = cur.copy()
        bestrob = rob.copy()
        bestc = np.full(N, c0)
        H = H or self.H
        act = DW * SP[:, None]
        valid = np.ones(N, bool)
        poly = self.model.poly
        for k in range(1, H + 1):
            cur, rob = self.sim.step(cur, rob, act)
            # wall check: all T vertices must stay inside the arena
            c, s_ = np.cos(cur[:, 2]), np.sin(cur[:, 2])
            vx = cur[:, 0:1] + c[:, None] * poly[None, :, 0] - s_[:, None] * poly[None, :, 1]
            vy = cur[:, 1:2] + s_[:, None] * poly[None, :, 0] + c[:, None] * poly[None, :, 1]
            m_ = self.wall_margin
            inside = ((vx.min(1) > m_) & (vx.max(1) < 5.0 - m_) & (vy.min(1) > m_) & (vy.max(1) < 5.0 - m_))
            valid &= inside
            cst = self.cost(cur)
            done = self.in_goal(cur, 0.75)
            cst = np.where(done, -self.goal_bonus, cst)
            score = (c0 - cst) / (k + travel + self.overhead)
            score = np.where(valid, score, -np.inf)
            m = score > bestscore
            bestscore[m] = score[m]
            bestk[m] = k
            bestpose[m] = cur[m]
            bestrob[m] = rob[m]
            bestc[m] = cst[m]
        return dict(start=SW, act=act, k=bestk, rate=bestscore, pose=bestpose, rob=bestrob,
                    c=bestc, here=HERE, travel=travel, c0=c0)

    def plan_push(self, pose, robot):
        el = time.time() - self.t0
        if el > 35.0:
            E = self.eval_pushes(pose, robot, coarse=True, H=20 if el > 45 else 30)
        else:
            E = self.eval_pushes(pose, robot)
        order = np.argsort(-E["rate"])
        best_i = int(order[0])
        if self.M > 0:
            best_T = np.inf
            for i in order[: self.M]:
                if E["rate"][i] <= 0:
                    break
                T1 = E["travel"][i] + E["k"][i]
                if E["c"][i] < 0:
                    T = T1
                else:
                    E2 = self.eval_pushes(E["pose"][i], E["rob"][i], coarse=True, H=self.H2)
                    j = int(np.argmax(E2["rate"]))
                    r2 = E2["rate"][j]
                    if r2 <= 0:
                        continue
                    T = T1 + (E2["c0"] + self.goal_bonus) / r2
                if T < best_T:
                    best_T = T
                    best_i = int(i)
        i = best_i
        return E["start"][i], E["act"][i], E["k"][i], E["rate"][i], E["c0"], E["here"][i]

    def make_subgoal(self, pose):
        """Goal orientation at a position with the COM clamped away from the walls."""
        th = self.gc
        c, s_ = math.cos(th), math.sin(th)
        com = self.sim.com
        gcom = self.goal[:2] + np.array([c * com[0] - s_ * com[1], s_ * com[0] + c * com[1]])
        m = self.sub_clear
        ncom = np.clip(gcom, m, 5.0 - m)
        if np.linalg.norm(ncom - gcom) < 0.05:
            # goal is interior: use current COM pulled toward centre
            cc, sc_ = math.cos(pose[2]), math.sin(pose[2])
            pcom = pose[:2] + np.array([cc * com[0] - sc_ * com[1], sc_ * com[0] + cc * com[1]])
            ncom = np.clip(pcom, m, 5.0 - m)
            if np.linalg.norm(ncom - pcom) < 0.05:
                return None
            xy = ncom - np.array([cc * com[0] - sc_ * com[1], sc_ * com[0] + cc * com[1]])
            return np.array([xy[0], xy[1], pose[2], 0.3, 0.08])
        xy = self.goal[:2] + (ncom - gcom)
        return np.array([xy[0], xy[1], th, 0.1, 0.1])

    def in_goal(self, poses, frac=1.0):
        dp = np.abs(poses[:, :2] - self.tgt[:2])
        da = np.abs(wrap_arr(poses[:, 2] - self.tgt[2]))
        return (dp[:, 0] < self.tgt[4] * frac) & (dp[:, 1] < self.tgt[4] * frac) & (da < self.tgt[3] * frac)

    def _nodes(self, pose):
        infl = self.infl
        a, h, w, lv = self.lh / 2, self.w / 2, self.w, self.lv
        e = infl + 0.04
        nodes_local = np.array([
            [-a - e, e], [a + e, e], [a + e, -w - e], [-a - e, -w - e],
            [h + e, -w - e], [-h - e, -w - e], [h + e, -w - lv - e], [-h - e, -w - lv - e],
            [0, e + 0.02], [0, -w - lv - e - 0.02],
        ])
        nodes = to_world(nodes_local, pose)
        ok = np.all((nodes > WALL_LO + R_ROBOT + 0.01) & (nodes < WALL_HI - R_ROBOT - 0.01), 1)
        return nodes[ok]

    def _seg_free(self, P, Q, pose, ns=24, infl=None):
        """Vectorized: segments P[i]->Q[i] free of inflated T."""
        infl = self.infl if infl is None else infl
        ts = np.linspace(0, 1, ns)
        pts = P[:, None, :] + ts[None, :, None] * (Q - P)[:, None, :]
        dd = dist_to_T_local(to_local(pts.reshape(-1, 2), pose), self.model.rects).reshape(len(P), ns)
        return np.all(dd > infl - 1e-6, 1)

    def travel_est(self, robot, pts, pose):
        """Travel steps from robot to each pt via visibility graph around block."""
        nodes = self._nodes(pose)
        K = len(nodes)
        allp = np.vstack([robot[None], nodes])
        # graph among robot+nodes
        I, J = np.triu_indices(K + 1, 1)
        free = self._seg_free(allp[I], allp[J], pose)
        # allow robot escaping if robot starts inside inflation
        D = np.full((K + 1, K + 1), np.inf)
        L = np.hypot(*(allp[I] - allp[J]).T)
        D[I[free], J[free]] = L[free]
        D[J[free], I[free]] = L[free]
        r0 = dist_to_T_local(to_local(robot[None], pose), self.model.rects)[0]
        if r0 <= self.infl:
            # robot too close to block: allow direct moves to all nodes (escape)
            Ln = np.hypot(*(nodes - robot).T)
            D[0, 1:] = np.minimum(D[0, 1:], Ln * 1.2)
        dist = np.full(K + 1, np.inf)
        dist[0] = 0.0
        done = np.zeros(K + 1, bool)
        for _ in range(K + 1):
            u = int(np.argmin(np.where(done, np.inf, dist)))
            if not np.isfinite(dist[u]):
                break
            done[u] = True
            dist = np.minimum(dist, dist[u] + D[u])
        N = len(pts)
        direct = np.hypot(*(pts - robot).T)
        tinf = self.final_infl if self.stage == 0 else self.infl
        dfree = self._seg_free(np.repeat(robot[None], N, 0), pts, pose, infl=tinf)
        if r0 <= self.infl:
            dfree |= True  # handled by staging (robot adjacent) - approximate
        best = np.where(dfree, direct, np.inf)
        if K > 0:
            PP = np.repeat(nodes, N, 0)
            QQ = np.tile(pts, (K, 1))
            f = self._seg_free(PP, QQ, pose, infl=tinf).reshape(K, N)
            dn = np.hypot(*(PP - QQ).T).reshape(K, N)
            via = np.where(f, dist[1:, None] + dn, np.inf).min(0)
            best = np.minimum(best, via)
        best = np.where(np.isfinite(best), best, direct * 2.5)
        return best / MAXD

    # ------------------------------------------------------------------
    def nav_path(self, robot, target, pose):
        """Visibility-graph path around inflated T."""
        infl = self.infl
        rects = self.model.rects

        tinf = self.final_infl

        def free_seg(p, q, tol=infl):
            pl = to_local(np.array([p, q]), pose)
            ts = np.linspace(0, 1, max(2, int(np.linalg.norm(q - p) / 0.02) + 2))
            pts = pl[0] + ts[:, None] * (pl[1] - pl[0])
            return np.all(dist_to_T_local(pts, rects) > tol - 1e-6)

        if free_seg(robot, target, tinf):
            return [target]
        nodes = list(self._nodes(pose))
        pts = [np.asarray(robot)] + nodes + [np.asarray(target)]
        n = len(pts)
        dist = [np.inf] * n
        prev = [-1] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                break
            for v in range(n):
                if v == u:
                    continue
                tol = tinf if v == n - 1 else infl
                if not free_seg(pts[u], pts[v], tol) and not (u == 0 and self._escape_ok(pts[u], pts[v], pose)):
                    continue
                nd = d + np.linalg.norm(pts[v] - pts[u])
                if nd < dist[v]:
                    dist[v] = nd
                    prev[v] = u
                    heapq.heappush(pq, (nd, v))
        if dist[n - 1] == np.inf:
            return [target]
        path = []
        v = n - 1
        while v != 0:
            path.append(pts[v])
            v = prev[v]
        return path[::-1]

    def _escape_ok(self, p, q, pose):
        # allow leaving if robot currently inside inflated zone and moving away
        pl = to_local(np.array([p, q]), pose)
        d0 = dist_to_T_local(pl[:1], self.model.rects)[0]
        if d0 > R_ROBOT + 0.03:
            return False
        ts = np.linspace(0, 1, 20)
        pts = pl[0] + ts[:, None] * (pl[1] - pl[0])
        dd = dist_to_T_local(pts, self.model.rects)
        return np.all(dd >= d0 - 1e-6) and dd[-1] > R_ROBOT + 0.03

    # ------------------------------------------------------------------
    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        pose = s[0:3].copy()
        robot = s[16:18].copy()
        if self.model is None:
            self.reset(state, {})
        # clear blacklist once block moved noticeably
        if self.bl_pose is not None and (np.linalg.norm(pose[:2] - self.bl_pose[:2]) > 0.03
                                         or abs(wrap(pose[2] - self.bl_pose[2])) > 0.05):
            self.blacklist = []
            self.bl_pose = None
        if self.last_cmd is not None and self.mode == "push":
            moved = np.linalg.norm(robot - self.last_robot)
            pred_pose, _ = self.sim.step(self.last_pose, self.last_robot, self.last_cmd)
            perr = np.linalg.norm(pred_pose[0, :2] - pose[:2]) + 0.5 * abs(wrap(pred_pose[0, 2] - pose[2]))
            if moved < 0.3 * np.linalg.norm(self.last_cmd) or perr > 0.01:
                self.mode = "plan"
                self.blacklist.append((to_local(self.last_robot[None], pose)[0],
                                       to_local(self.last_cmd[None], (0, 0, pose[2]))[0]))
                if self.bl_pose is None:
                    self.bl_pose = pose.copy()
        if self.last_cmd is not None and self.mode == "nav":
            moved = np.linalg.norm(robot - self.last_robot)
            if moved < 0.3 * np.linalg.norm(self.last_cmd) and np.linalg.norm(self.last_cmd) > 1e-3:
                self.stall += 1
            else:
                self.stall = 0
            if self.stall >= 3:
                self.stall = 0
                self.mode = "plan"
        self.last_robot = robot
        self.last_pose = pose.copy()
        if self.solved(pose):
            self.last_cmd = None
            return np.zeros(2)
        if self.sub_active and self.in_goal(pose[None])[0]:
            self.sub_active = False
            self.tgt = self.real_tgt.copy()
            self.mode = "plan"
        a = self._act(pose, robot)
        a = np.clip(np.asarray(a, float), -MAXD, MAXD)
        self.last_cmd = a
        return a

    def _act(self, pose, robot):
        for _ in range(4):
            if self.mode == "plan":
                st, d, k, sc, c0, here = self.plan_push(pose, robot)
                if sc < self.stuck_rate and not self.sub_active:
                    sub = self.make_subgoal(pose)
                    if sub is not None:
                        self.sub_active = True
                        self.tgt = sub
                        st, d, k, sc, c0, here = self.plan_push(pose, robot)
                elif sc < self.stuck_rate and self.sub_active:
                    self.sub_active = False
                    self.tgt = self.real_tgt.copy()
                    st, d, k, sc, c0, here = self.plan_push(pose, robot)
                self.push = (st, d)
                self.push_left = min(k, self.replan_every)
                dn = d / np.linalg.norm(d)
                if here:
                    self.path = []
                else:
                    if self.stage:
                        self.path = self.nav_path(robot, st - dn * 0.12, pose) + [st]
                    else:
                        self.path = self.nav_path(robot, st, pose)
                self.plan_pose = pose.copy()
                self.mode = "nav"
            if self.mode == "nav":
                if not self.path:
                    self.mode = "push"
                    continue
                tgt = self.path[0]
                dv = tgt - robot
                dn = np.linalg.norm(dv)
                if dn < 1e-3:
                    self.path.pop(0)
                    continue
                if dn <= MAXD:
                    self.path.pop(0)
                    return dv
                return dv / dn * MAXD
            if self.mode == "push":
                if self.push_left <= 0:
                    self.mode = "plan"
                    continue
                self.push_left -= 1
                return self.push[1]
        return np.zeros(2)


def wrap_arr(a):
    return (a + np.pi) % (2 * np.pi) - np.pi
