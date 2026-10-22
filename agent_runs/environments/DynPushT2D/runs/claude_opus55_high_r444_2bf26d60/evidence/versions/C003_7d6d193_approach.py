"""Push-T controller: model-based greedy push selection + visibility-graph navigation."""
import heapq
import math

import numpy as np

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
        self.model = None

    # ------------------------------------------------------------------
    def reset(self, state, info):
        s = np.asarray(state, dtype=float)
        self.w, self.lh, self.lv = s[12], s[13], s[14]
        self.model = TModel(self.w, self.lh, self.lv)
        self.goal = s[29:32].copy()
        self.mode = "plan"
        self.path = []
        self.push = None
        self.push_left = 0
        self.stall = 0

    # ------------------------------------------------------------------
    def cost(self, pose):
        pose = np.atleast_2d(pose)
        dp = pose[:, :2] - self.goal[:2]
        da = np.abs(wrap_arr(pose[:, 2] - self.goal[2]))
        return np.hypot(dp[:, 0], dp[:, 1]) + 0.6 * da

    def solved(self, pose):
        return (abs(pose[0] - self.goal[0]) < 0.03 and abs(pose[1] - self.goal[1]) < 0.03
                and abs(wrap(pose[2] - self.goal[2])) < math.radians(8))

    # ------------------------------------------------------------------
    def candidates(self, pose):
        """Candidate pushes: list of (start_pt_world, dir_world)."""
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
            m = max(2, int(L / 0.06))
            for t in np.linspace(0.04 / L, 1 - 0.04 / L, m) if L > 0.1 else [0.5]:
                q = a + t * ab
                for ang in (-0.5, -0.25, 0.0, 0.25, 0.5):
                    ca, sa = math.cos(ang), math.sin(ang)
                    d = -nn
                    d = np.array([ca * d[0] - sa * d[1], sa * d[0] + ca * d[1]])
                    starts.append(q + nn * (R_ROBOT + 0.02))
                    dirs.append(d)
        starts = np.array(starts)
        dirs = np.array(dirs)
        return to_world(starts, pose), to_world(dirs, (0, 0, pose[2]))

    def plan_push(self, pose, robot):
        sw, dw = self.candidates(pose)
        N = len(sw)
        # filter starts that are outside walls
        ok = np.all((sw > WALL_LO + R_ROBOT + 0.01) & (sw < WALL_HI - R_ROBOT - 0.01), 1)
        sw, dw = sw[ok], dw[ok]
        N = len(sw)
        poses = np.repeat(pose[None], N, 0)
        rob = sw.copy()
        c0 = self.cost(pose)[0]
        best = (np.inf, None)
        H = 40
        steplen = MAXD
        travel = np.hypot(*(sw - robot).T) / MAXD
        cur = poses
        bestscore = np.full(N, np.inf)
        bestk = np.zeros(N, int)
        for k in range(1, H + 1):
            cur, rob = self.model.step(cur, rob, dw * steplen)
            cst = self.cost(cur)
            # score: resulting cost + time penalty
            score = cst + 0.004 * (k + travel)
            m = score < bestscore
            bestscore[m] = score[m]
            bestk[m] = k
        i = int(np.argmin(bestscore))
        return sw[i], dw[i], bestk[i], bestscore[i], c0

    # ------------------------------------------------------------------
    def nav_path(self, robot, target, pose):
        """Visibility-graph path around inflated T."""
        infl = R_ROBOT + 0.03
        rects = self.model.rects

        def free_seg(p, q):
            pl = to_local(np.array([p, q]), pose)
            ts = np.linspace(0, 1, max(2, int(np.linalg.norm(q - p) / 0.02) + 2))
            pts = pl[0] + ts[:, None] * (pl[1] - pl[0])
            return np.all(dist_to_T_local(pts, rects) > infl - 1e-6)

        if free_seg(robot, target):
            return [target]
        a, h = self.lh / 2, self.w / 2
        e = infl + 0.05
        lv = self.lv
        w = self.w
        nodes_local = np.array([
            [-a - e, e], [a + e, e], [a + e, -w - e], [-a - e, -w - e],
            [h + e, -w - e], [-h - e, -w - e], [h + e, -w - lv - e], [-h - e, -w - lv - e],
            [0, e], [0, -w - lv - e],
        ])
        nodes = list(to_world(nodes_local, pose))
        nodes = [p for p in nodes if np.all(p > WALL_LO + R_ROBOT) and np.all(p < WALL_HI - R_ROBOT)]
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
                if not free_seg(pts[u], pts[v]) and not (u == 0 and self._escape_ok(pts[u], pts[v], pose)):
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
        for _ in range(4):
            if self.mode == "plan":
                st, d, k, sc, c0 = self.plan_push(pose, robot)
                self.push = (st, d)
                self.push_left = k + 3
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
                d = self.push[1]
                # slow down near goal
                c = self.cost(pose)[0]
                sp = MAXD if c > 0.2 else max(0.01, MAXD * c / 0.2)
                return d * sp
        return np.zeros(2)


def wrap_arr(a):
    return (a + np.pi) % (2 * np.pi) - np.pi
