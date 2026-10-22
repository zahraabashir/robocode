import math
import numpy as np

WORLD_X = (0.0, 1.618)
ROBOT_Y_MAX = 0.895
FLOOR = 0.1
ARM = 0.2          # extended arm length we use
GW = 0.01          # gripper width (along arm)
GH = 0.07          # gripper height (perpendicular)
BASE_R = 0.1
RX_MIN = 0.1 + 0.002
RX_MAX = 1.618 - 0.1 - 0.002
TIP = ARM + GW     # distance from robot center to gripper tip (pointing down)


def _rect_bbox(state, o):
    x = float(state.get(o, "x")); y = float(state.get(o, "y"))
    w = float(state.get(o, "width")); h = float(state.get(o, "height"))
    th = float(state.get(o, "theta"))
    if abs(th) < 1e-6:
        return (x, y, x + w, y + h)
    c, s = math.cos(th), math.sin(th)
    pts = [(x, y), (x + w * c, y + w * s), (x - h * s, y + h * c),
           (x + w * c - h * s, y + w * s + h * c)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def _circle_rect_dist(cx, cy, b):
    dx = max(b[0] - cx, 0.0, cx - b[2])
    dy = max(b[1] - cy, 0.0, cy - b[3])
    return math.hypot(dx, dy)


def _overlap(a, b, m=0.0):
    return a[0] < b[2] + m and b[0] < a[2] + m and a[1] < b[3] + m and b[1] < a[3] + m


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.array(action_space.low, dtype=np.float32)
        self.high = np.array(action_space.high, dtype=np.float32)

    # ------------------------------------------------------------------
    K_RERANK = 20
    ORDER = 'near'
    TOP_MAX = 0.46
    USE_ARM_DP = True

    def reset(self, state, info):
        self.state = state
        self.gen = self._plan()
        self.vac = 0.0

    def get_action(self, state):
        self.state = state
        try:
            a = next(self.gen)
        except StopIteration:
            self.gen = self._plan()
            try:
                a = next(self.gen)
            except StopIteration:
                a = np.zeros(5, dtype=np.float32)
        a = np.clip(np.asarray(a, dtype=np.float32), self.low, self.high)
        return a

    # ------------------------------------------------------------------
    def _objs(self):
        s = self.state
        robot = None; block = None; surf = None; obst = []
        for n in sorted(s.get_object_names()):
            o = s.get_object_from_name(n)
            tn = o.type.name
            if tn == "crv_robot":
                robot = o
            elif tn == "target_block":
                block = o
            elif tn == "target_surface":
                surf = o
            else:
                obst.append(o)
        return robot, block, surf, obst

    def _rpos(self):
        r = self._objs()[0]
        s = self.state
        return (float(s.get(r, "x")), float(s.get(r, "y")),
                float(s.get(r, "theta")), float(s.get(r, "arm_joint")))

    # ------------------------------------------------------------------
    def _act(self, dx=0.0, dy=0.0, dth=0.0, darm=0.0):
        return np.array([dx, dy, dth, darm, self.vac], dtype=np.float32)

    def _goto(self, tx=None, ty=None, tol=1e-4, max_steps=200, tarm=ARM, final_vac=None):
        """Straight-line move towards (tx, ty). Returns True on success."""
        stuck = 0
        last = None
        for _ in range(max_steps):
            x, y, th, aj = self._rpos()
            gx = x if tx is None else tx
            gy = y if ty is None else ty
            ex, ey = gx - x, gy - y
            eth = math.atan2(math.sin(-math.pi / 2 - th), math.cos(-math.pi / 2 - th))
            ea = tarm - aj
            if abs(ex) <= tol and abs(ey) <= tol:
                if abs(eth) < 1e-4 and abs(ea) < 1e-4:
                    return True
            if last is not None and abs(last[0] - x) < 1e-7 and abs(last[1] - y) < 1e-7 \
                    and abs(last[2] - aj) < 1e-7 and abs(last[3] - th) < 1e-7:
                stuck += 1
                if stuck >= 2:
                    return False
            else:
                stuck = 0
            last = (x, y, aj, th)
            n = max(1, int(math.ceil(max(abs(ex) / 0.05, abs(ey) / 0.05, abs(ea) / 0.1) - 1e-6)))
            if final_vac is not None and n == 1:
                self.vac = final_vac
            yield np.array([ex / n, ey / n, np.clip(eth, -0.19, 0.19),
                            ea / n, self.vac], dtype=np.float32)
        return False

    def _collides(self, x, y, obstacles, crel, m=0.008):
        if y > ROBOT_Y_MAX + 1e-6 or x < RX_MIN - 1e-6 or x > RX_MAX + 1e-6:
            return True
        col = (x - GH / 2, y - TIP, x + GH / 2, y)
        cb = None
        if crel is not None:
            cb = (x + crel[0], y + crel[1], x + crel[2], y + crel[3])
            if cb[1] < FLOOR - 1e-3:
                return True
        for b in obstacles:
            if _circle_rect_dist(x, y, b) < BASE_R + m:
                return True
            if _overlap(col, b, 0.001):
                return True
            if cb is not None and _overlap(cb, b, m * 0.6):
                return True
        return False

    def _seg_free(self, p, q, obstacles, crel):
        d = max(abs(q[0] - p[0]), abs(q[1] - p[1]))
        n = max(1, int(math.ceil(d / 0.008)))
        for i in range(1, n + 1):
            t = i / n
            if self._collides(p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]), obstacles, crel):
                return False
        return True

    def _free_pts(self, X, Y, obstacles, crel, m=0.008):
        X = np.asarray(X, dtype=float); Y = np.asarray(Y, dtype=float)
        free = (X >= RX_MIN - 1e-6) & (X <= RX_MAX + 1e-6) & (Y <= ROBOT_Y_MAX + 1e-6)
        if crel is not None:
            free &= (Y + crel[1]) >= FLOOR - 1e-3
        for b in obstacles:
            ddx = np.maximum(np.maximum(b[0] - X, 0.0), X - b[2])
            ddy = np.maximum(np.maximum(b[1] - Y, 0.0), Y - b[3])
            free &= (ddx * ddx + ddy * ddy) >= (BASE_R + m) ** 2
            e = 0.001
            ov = (X - GH / 2 < b[2] + e) & (b[0] < X + GH / 2 + e) & (Y - TIP < b[3] + e) & (b[1] < Y + e)
            free &= ~ov
            if crel is not None:
                e = m * 0.6
                ov = (X + crel[0] < b[2] + e) & (b[0] < X + crel[2] + e) & \
                     (Y + crel[1] < b[3] + e) & (b[1] < Y + crel[3] + e)
                free &= ~ov
        return free

    def _dp_path(self, x0, y0, x1, y1, obstacles, crel):
        """DP over x-columns / y-levels. Returns (cost, waypoints) or None."""
        res = 0.005
        ylo = 0.3
        nl = int(round((ROBOT_Y_MAX - ylo) / res)) + 1
        levels = ylo + res * np.arange(nl)
        K = int(round(0.05 / res))
        j0 = int(min(nl - 1, max(0, math.ceil((y0 - ylo) / res - 1e-6))))
        j1 = int(min(nl - 1, max(0, math.ceil((y1 - ylo) / res - 1e-6))))
        dx = x1 - x0
        N = int(math.ceil(abs(dx) / 0.05 - 1e-6))
        # columns at half steps
        cols = x0 + dx * (np.arange(2 * N + 1) / max(1, 2 * N)) if N > 0 else np.array([x0])
        XX = np.repeat(cols[:, None], nl, axis=1)
        YY = np.repeat(levels[None, :], len(cols), axis=0)
        F = self._free_pts(XX, YY, obstacles, crel)
        INF = 1e9
        # vertical cost matrix within a column
        J = np.arange(nl)
        vc = np.ceil(np.abs(J[:, None] - J[None, :]) / K)

        def vert_relax(cost, free):
            # segments of contiguous free cells
            seg = np.cumsum(~free)
            same = (seg[:, None] == seg[None, :]) & free[:, None] & free[None, :]
            M = np.where(same, cost[None, :] + vc, INF)
            arg = np.argmin(M, axis=1)
            return M[J, arg], arg

        cost = np.full(nl, INF)
        if not F[0, j0]:
            # allow starting cell even if flagged (numerical contact)
            F[0, j0] = True
        cost[j0] = 0.0
        costs = []
        backs = []
        c, arg = vert_relax(cost, F[0])
        costs.append(c); backs.append(("v", arg))
        for i in range(1, N + 1):
            fm = F[2 * i - 1]; fe = F[2 * i]
            new = np.full(nl, INF)
            parent = np.full(nl, -1)
            prev = costs[-1]
            for d in range(-K, K + 1):
                # from j to j+d; midpoint level j + d/2
                src_j = np.arange(max(0, -d), min(nl, nl - d))
                dst_j = src_j + d
                mid = src_j + d / 2.0
                mlo = np.floor(mid).astype(int); mhi = np.ceil(mid).astype(int)
                ok = fe[dst_j] & fm[mlo] & fm[mhi] & (prev[src_j] < INF)
                cand = prev[src_j] + 1.0
                better = ok & (cand < new[dst_j])
                new[dst_j[better]] = cand[better]
                parent[dst_j[better]] = src_j[better]
            if i == N and not fe[j1]:
                fe = fe.copy(); fe[j1] = True
            c, arg = vert_relax(new, fe)
            costs.append(new); backs.append(("h", parent))
            costs[-1] = c; backs.append(("v", arg))
            # note: backs holds pairs per column after the first
        final = costs[-1]
        if final[j1] >= INF:
            return None
        # backtrack
        pts = []
        j = j1
        ci = N
        bi = len(backs) - 1
        while bi >= 0:
            kind, arr = backs[bi]
            if kind == "v":
                jp = int(arr[j])
                # vertical moves from jp to j at column ci
                if jp != j:
                    steps = int(math.ceil(abs(j - jp) / K))
                    for s_ in range(steps, 0, -1):
                        jj = jp + int(round((j - jp) * s_ / steps))
                        pts.append((float(cols[2 * ci]), float(levels[jj])))
                j = jp
            else:
                jp = int(arr[j])
                pts.append((float(cols[2 * ci]), float(levels[j])))
                j = jp
                ci -= 1
            bi -= 1
        pts.reverse()
        # dedupe and fix endpoints
        out = []
        for p in pts:
            if not out or abs(out[-1][0] - p[0]) > 1e-9 or abs(out[-1][1] - p[1]) > 1e-9:
                out.append(p)
        if out and abs(out[0][0] - x0) < 1e-9 and abs(out[0][1] - levels[j0]) < 1e-9:
            # first waypoint is the snapped start
            if abs(levels[j0] - y0) < 1e-9:
                out = out[1:]
        if out and abs(out[-1][0] - x1) < 1e-6 and abs(out[-1][1] - levels[j1]) <= res + 1e-9:
            out[-1] = (x1, y1)
        else:
            out.append((x1, y1))
        return float(final[j1]), out

    def _plan_path(self, x1, y1, obstacles, crel, start=None):
        if start is None:
            x0, y0, _, _ = self._rpos()
        else:
            x0, y0 = start
        r = self._dp_path(x0, y0, x1, y1, obstacles, crel)
        if r is not None:
            return r[1]
        return self._plan_path_old(x1, y1, obstacles, crel, (x0, y0))

    def _plan_path_old(self, x1, y1, obstacles, crel, start=None):
        if start is None:
            x0, y0, _, _ = self._rpos()
        else:
            x0, y0 = start
        p0 = (x0, y0)
        if self._seg_free(p0, (x1, y1), obstacles, crel):
            return [(x1, y1)]
        dx = x1 - x0
        sg = 1.0 if dx >= 0 else -1.0
        tys = sorted(set([round(v, 4) for v in np.arange(max(y0, y1) + 0.01, ROBOT_Y_MAX, 0.02)]
                         + [ROBOT_Y_MAX]))
        for ty in tys:
            a = min(abs(dx), ty - y0)
            b = min(abs(dx) - a, ty - y1)
            pa = (x0 + sg * a, ty)
            pb = (x1 - sg * b, ty)
            path = [pa, pb, (x1, y1)]
            pts = [p0] + path
            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
                return path
            path = [(x0, ty), (x1, ty), (x1, y1)]
            pts = [p0] + path
            if all(self._seg_free(pts[i], pts[i + 1], obstacles, crel) for i in range(3)):
                return path
        return [(x0, ROBOT_Y_MAX), (x1, ROBOT_Y_MAX), (x1, y1)]

    COST3 = False

    def _path_cost(self, p0, p1, obstacles, crel, arm0=ARM):
        if self.COST3:
            ctip = None
            if crel is not None:
                ctip = (crel[0], crel[1] + arm0 + GW, crel[2], crel[3] + arm0 + GW)
            path = self._dp_path3(p0[0], p0[1], arm0, p1[0], p1[1] - TIP, obstacles, ctip)
            if path is not None:
                c = 0.0
                prev = (p0[0], p0[1], arm0)
                for q in path:
                    c += max(1, math.ceil(max(abs(q[0] - prev[0]) / 0.05, abs(q[1] - prev[1]) / 0.05,
                                              abs(q[2] - prev[2]) / 0.1) - 1e-6)) if q != prev else 0
                    prev = q
                return c
        path = self._plan_path(p1[0], p1[1], obstacles, crel, start=p0)
        pts = [p0] + path
        c = 0.0
        for i in range(len(pts) - 1):
            c += math.ceil(max(abs(pts[i + 1][0] - pts[i][0]), abs(pts[i + 1][1] - pts[i][1])) / 0.05 - 1e-6)
        return c

    ARMS = (0.1, 0.2)

    def _free_pts3(self, X, Y, obstacles, ctip, arm, m=0.008):
        """Free check for robot base at (X, Y) with arm length `arm`.
        ctip: carried bbox relative to the gripper tip point (x, y - arm - GW)."""
        tipl = arm + GW
        free = (X >= RX_MIN - 1e-6) & (X <= RX_MAX + 1e-6) & (Y <= ROBOT_Y_MAX + 1e-6)
        free &= (Y - tipl) >= FLOOR - 0.004
        if ctip is not None:
            free &= (Y - tipl + ctip[1]) >= FLOOR - 1e-3
        for b in obstacles:
            ddx = np.maximum(np.maximum(b[0] - X, 0.0), X - b[2])
            ddy = np.maximum(np.maximum(b[1] - Y, 0.0), Y - b[3])
            free &= (ddx * ddx + ddy * ddy) >= (BASE_R + m) ** 2
            e = 0.001
            ov = (X - GH / 2 < b[2] + e) & (b[0] < X + GH / 2 + e) & (Y - tipl < b[3] + e) & (b[1] < Y + e)
            free &= ~ov
            if ctip is not None:
                e = m * 0.6
                ov = (X + ctip[0] < b[2] + e) & (b[0] < X + ctip[2] + e) & \
                     (Y - tipl + ctip[1] < b[3] + e) & (b[1] < Y - tipl + ctip[3] + e)
                free &= ~ov
        return free

    def _dp_path3(self, x0, y0, arm0, x1, tipy1, obstacles, ctip):
        """DP over (column, y-level, arm in ARMS). Goal is a tip position.
        Returns list of waypoints (x, y, arm) or None."""
        res = 0.005
        ylo = 0.2
        nl = int(round((ROBOT_Y_MAX - ylo) / res)) + 1
        levels = ylo + res * np.arange(nl)
        K = int(round(0.05 / res))
        A = self.ARMS
        NA = len(A)
        a0 = int(np.argmin([abs(arm0 - v) for v in A]))
        j0 = int(min(nl - 1, max(0, math.ceil((y0 - ylo) / res - 1e-6))))
        jg = [int(min(nl - 1, max(0, math.ceil((tipy1 + A[a] + GW - ylo) / res - 1e-6)))) for a in range(NA)]
        dx = x1 - x0
        N = int(math.ceil(abs(dx) / 0.05 - 1e-6))
        cols = x0 + dx * (np.arange(2 * N + 1) / max(1, 2 * N)) if N > 0 else np.array([x0])
        XX = np.repeat(cols[:, None], nl, axis=1)
        YY = np.repeat(levels[None, :], len(cols), axis=0)
        F = [self._free_pts3(XX, YY, obstacles, ctip, A[a]) for a in range(NA)]
        for a in range(NA):
            for ci_ in ({0, 2 * N}):
                F[a][ci_] |= self._free_pts3(XX[ci_], YY[ci_], obstacles, ctip, A[a], m=0.001)
        F[a0][0, j0] = True
        for a in range(NA):
            gok = self._free_pts3(np.array([x1]), np.array([tipy1 + A[a] + GW]), obstacles, ctip, A[a], m=0.001)[0]
            F[a][2 * N, jg[a]] = bool(gok)
        INF = 1e9
        J = np.arange(nl)
        vc = np.ceil(np.abs(J[:, None] - J[None, :]) / K)

        def vlayer(C, ci):
            newC = []; par = []
            for a in range(NA):
                free = F[a][2 * ci]
                seg = np.cumsum(~free)
                same = (seg[:, None] == seg[None, :]) & free[:, None] & free[None, :]
                M = np.where(same, C[a][None, :] + vc, INF)
                arg = np.argmin(M, axis=1)
                c = M[J, arg]
                keep = C[a] <= c
                c = np.where(keep, C[a], c)
                pj = np.where(keep | (c >= INF), -1, arg)
                newC.append(c); par.append((np.full(nl, a), pj))
            return newC, ("v", par)

        def slayer(C, ci):
            both = np.ones(nl, dtype=bool)
            for a in range(NA):
                both &= F[a][2 * ci]
            bad = np.concatenate([[0], np.cumsum(~both)])
            newC = [c.copy() for c in C]
            par = [(np.full(nl, -1), np.full(nl, -1)) for _ in range(NA)]
            for a in range(NA):
                for asrc in range(NA):
                    if asrc == a:
                        continue
                    for d in range(-K, K + 1):
                        sj = np.arange(max(0, -d), min(nl, nl - d))
                        dj = sj + d
                        lo = np.minimum(sj, dj); hi = np.maximum(sj, dj)
                        ok = (bad[hi + 1] - bad[lo]) == 0
                        cand = C[asrc][sj] + 1.0
                        better = ok & (cand < newC[a][dj])
                        newC[a][dj[better]] = cand[better]
                        par[a][0][dj[better]] = asrc
                        par[a][1][dj[better]] = sj[better]
            return newC, ("s", par)

        def hlayer(Cprev, i):
            fm = [F[a][2 * i - 1] for a in range(NA)]
            fe = [F[a][2 * i] for a in range(NA)]
            newC = [np.full(nl, INF) for _ in range(NA)]
            par = [(np.full(nl, -1), np.full(nl, -1)) for _ in range(NA)]
            for a in range(NA):
                for asrc in range(NA):
                    for d in range(-K, K + 1):
                        sj = np.arange(max(0, -d), min(nl, nl - d))
                        dj = sj + d
                        mid = sj + d / 2.0
                        mlo = np.floor(mid).astype(int); mhi = np.ceil(mid).astype(int)
                        ok = fe[a][dj] & fm[a][mlo] & fm[a][mhi] & fm[asrc][mlo] & fm[asrc][mhi]
                        cand = Cprev[asrc][sj] + 1.0
                        better = ok & (cand < newC[a][dj])
                        newC[a][dj[better]] = cand[better]
                        par[a][0][dj[better]] = asrc
                        par[a][1][dj[better]] = sj[better]
            return newC, ("h", par)

        layers = []  # (column, kind, par)
        C = [np.full(nl, INF) for _ in range(NA)]
        C[a0][j0] = 0.0
        for ci in range(N + 1):
            if ci > 0:
                C, L = hlayer(C, ci); layers.append((ci,) + L)
            for _ in range(2):
                C, L = vlayer(C, ci); layers.append((ci,) + L)
                C, L = slayer(C, ci); layers.append((ci,) + L)
        best_a = int(np.argmin([C[a][jg[a]] for a in range(NA)]))
        if C[best_a][jg[best_a]] >= INF:
            return None
        # backtrack
        pts = []
        a, j = best_a, jg[best_a]
        for ci, kind, par in reversed(layers):
            pa, pj = par[a][0][j], par[a][1][j]
            if pj < 0:
                continue
            x = float(cols[2 * ci])
            if kind == "v":
                steps = int(math.ceil(abs(j - pj) / K))
                for s_ in range(steps, 0, -1):
                    jj = pj + int(round((j - pj) * s_ / steps))
                    pts.append((x, float(levels[jj]), A[a]))
            else:
                pts.append((x, float(levels[j]), A[a]))
            a, j = int(pa), int(pj)
        pts.reverse()
        if pts:
            ex, ey, ea = pts[-1]
            pts[-1] = (x1, tipy1 + ea + GW, ea)
        else:
            pts = [(x1, tipy1 + A[best_a] + GW, A[best_a])]
        return pts

    def _move(self, x1, y1, carried=None, last_vac=None):
        """Plan & execute a collision-free path. (x1, y1) is the robot target assuming
        arm length ARM; the planner may use other arm lengths (same tip target)."""
        x0, y0, _, aj = self._rpos()
        excl = [carried] if carried is not None else []
        obstacles = self._others_bboxes(excl)
        robot, block, surf, obst = self._objs()
        obstacles.append(_rect_bbox(self.state, surf))
        crel = None
        ctip = None
        if carried is not None:
            cb = _rect_bbox(self.state, carried)
            crel = (cb[0] - x0, cb[1] - y0, cb[2] - x0, cb[3] - y0)
            ty0 = y0 - aj - GW
            ctip = (cb[0] - x0, cb[1] - ty0, cb[2] - x0, cb[3] - ty0)
        path = None
        if self.USE_ARM_DP:
            path = self._dp_path3(x0, y0, aj, x1, y1 - TIP, obstacles, ctip)
        if path is None:
            if abs(aj - ARM) > 1e-4:
                crel = None if ctip is None else (ctip[0], ctip[1] - TIP, ctip[2], ctip[3] - TIP)
            path = [(px, py, ARM) for (px, py) in self._plan_path(x1, y1, obstacles, crel)]
        for i, (px, py, pa) in enumerate(path):
            fv = last_vac if i == len(path) - 1 else None
            ok = yield from self._goto(px, py, tarm=pa, final_vac=fv)
            if not ok:
                return False
        return True

    # ------------------------------------------------------------------
    def _others_bboxes(self, exclude):
        robot, block, surf, obst = self._objs()
        out = []
        for o in [block] + obst:
            if o in exclude:
                continue
            out.append(_rect_bbox(self.state, o))
        return out

    def _descent_free(self, rx, ry_final, carried_bbox_final, others, margin=0.01):
        """Check vertical descent from travel height to ry_final at x=rx is collision free."""
        # base circle sweep: check at the final (lowest) position -- sweep is vertical,
        # and anything below is covered by checking the column.
        for b in others:
            # circle swept vertically from ry_final upwards
            cy = min(max(ry_final, b[1]), ROBOT_Y_MAX)
            cy = max(cy, ry_final)
            if _circle_rect_dist(rx, cy, b) < BASE_R + margin:
                return False
            # arm + gripper column
            col = (rx - GH / 2, ry_final - TIP, rx + GH / 2, ROBOT_Y_MAX)
            if _overlap(col, b, margin * 0.3):
                return False
            if carried_bbox_final is not None:
                cb = carried_bbox_final
                colc = (cb[0], cb[1], cb[2], cb[3] + (ROBOT_Y_MAX - ry_final))
                if _overlap(colc, b, margin * 0.5):
                    return False
        return True

    def _grasp_cands(self, b, pref=None):
        lo = b[0] + 0.012 - (GH / 2 - 0.02)
        hi = b[2] - 0.012 + (GH / 2 - 0.02)
        cx = (b[0] + b[2]) / 2 if pref is None else pref
        if hi < lo:
            lo = hi = (b[0] + b[2]) / 2
        full_lo = b[0] + GH / 2
        full_hi = b[2] - GH / 2
        vals = np.linspace(lo, hi, 41).tolist() + [min(max(cx, lo), hi)]

        def key(v):
            # prefer full gripper contact, then closeness to preferred
            pen = 0.0
            if full_lo <= full_hi:
                pen = max(0.0, full_lo - v, v - full_hi)
            return (round(pen, 4) > 0.0, abs(v - cx))
        return sorted(vals, key=key)

    def _choose_grasp_x(self, o, others, pref=None):
        b = _rect_bbox(self.state, o)
        ry = b[3] + TIP + 0.003
        for gx in self._grasp_cands(b, pref):
            if gx < RX_MIN or gx > RX_MAX:
                continue
            if self._descent_free(gx, ry, None, others):
                return gx
        return None

    def _pick(self, o, pref=None):
        others = self._others_bboxes([o])
        gx = self._choose_grasp_x(o, others, pref)
        if gx is None:
            return False
        b = _rect_bbox(self.state, o)
        ry = b[3] + TIP + 0.003
        yield from self._move(gx, ry, None, last_vac=1.0)
        self.vac = 1.0
        return True

    def _place_at(self, o, target_left, target_bottom, check=True, release=False):
        x, y, _, _ = self._rpos()
        b0 = _rect_bbox(self.state, o)
        rx = x + (target_left - b0[0])
        ry = y - (b0[1] - target_bottom) + (ARM - self._rpos()[3])
        gen = self._move(rx, ry, o, last_vac=(0.0 if release else None))
        first = True
        while True:
            try:
                a = next(gen)
            except StopIteration as e:
                return True
            yield a
            if first and check:
                first = False
                nb = _rect_bbox(self.state, o)
                if abs(nb[0] - b0[0]) + abs(nb[1] - b0[1]) < 1e-6:
                    # grasp failed
                    self.vac = 0.0
                    yield self._act()
                    return False

    # ------------------------------------------------------------------
    def _final_placement(self):
        """Returns (left, bottom, surface_bbox, grasp_offset_from_block_left)."""
        robot, block, surf, obst = self._objs()
        s = self.state
        sb = _rect_bbox(s, surf)
        bb = _rect_bbox(s, block)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        bottom = sb[3] + 0.014
        Llo = sb[0] + min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
        Lhi = sb[2] - bw - min(0.004, max(0.0, (sb[2] - sb[0] - bw) / 2))
        Lc = sb[0] + (sb[2] - sb[0] - bw) / 2
        if Lhi < Llo:
            Llo = Lhi = Lc
        obbs = [_rect_bbox(s, o) for o in obst]
        gs = []
        for g in self._grasp_cands((0.0, 0.0, bw, 1.0)):
            if all(abs(g - g2) > 0.004 for g2 in gs):
                gs.append(g)
            if len(gs) >= 7:
                break
        Ls = np.linspace(Llo, Lhi, 25).tolist() + [Lc]
        best = None
        for gi, g in enumerate(gs):
            for L in Ls:
                rx = L + g
                if not (RX_MIN <= rx <= RX_MAX):
                    continue
                fbb = (L, bottom, L + bw, bottom + bh)
                ry = bottom + bh + TIP + 0.003
                nb = 0
                for ob in obbs:
                    if not self._descent_free(rx, ry, fbb, [ob], margin=0.015):
                        nb += 1
                cost = nb * 100.0 + abs(L - bb[0]) / 0.05 + gi * 0.01 + abs(L - Lc) * 0.01
                if best is None or cost < best[0]:
                    best = (cost, L, g)
        if best is None:
            return Lc, bottom, sb, bw / 2
        return best[1], bottom, sb, best[2]

    def _blocking(self):
        """Obstructions that interfere with placing the block on the surface."""
        robot, block, surf, obst = self._objs()
        s = self.state
        left, bottom, sb, g = self._final_placement()
        bb = _rect_bbox(s, block)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        final_bb = (left, bottom, left + bw, bottom + bh)
        rx = left + g
        ry = bottom + bh + TIP + 0.003
        res = []
        for o in obst:
            ob = _rect_bbox(s, o)
            if not self._descent_free(rx, ry, final_bb, [ob], margin=0.015):
                res.append(o)
        return res

    def _final_sweep(self):
        """(rx, ry, final_bb) for the final block placement."""
        robot, block, surf, obst = self._objs()
        left, bottom, sb, g = self._final_placement()
        bb = _rect_bbox(self.state, block)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        final_bb = (left, bottom, left + bw, bottom + bh)
        return left + g, bottom + bh + TIP + 0.003, final_bb

    def _find_spot(self, o):
        """Find (left, bottom) to park the (currently grasped) obstruction o."""
        robot, block, surf, obst = self._objs()
        s = self.state
        ob = _rect_bbox(s, o)
        w, h = ob[2] - ob[0], ob[3] - ob[1]
        x, y, _, _ = self._rpos()
        goff = x - ob[0]
        hang = y - ob[3]  # robot y minus object top
        sb = _rect_bbox(s, surf)
        others = self._others_bboxes([o])
        frx, fry, fbb = self._final_sweep()
        # target block pickup sweep
        _, _, _, g = self._final_placement()
        bb = _rect_bbox(s, block)
        brx = bb[0] + g
        bry = bb[3] + TIP + 0.003
        levels = [(v, 0.0) for v in np.arange(FLOOR + 0.005, self.TOP_MAX - h, 0.02)]
        # remaining blockers' pickup columns must stay free
        cols = []
        for ob2 in self._blocking():
            if ob2 == o:
                continue
            b2 = _rect_bbox(s, ob2)
            cols.append(((b2[0] + b2[2]) / 2, b2[3] + TIP + 0.003, b2))
        cands = []
        xs = np.arange(WORLD_X[0] + 0.002, WORLD_X[1] - w - 0.002, 0.01)
        for bottom, pen in levels:
            for lx in xs:
                rx = lx + goff
                if rx < RX_MIN or rx > RX_MAX:
                    continue
                cand = (lx, bottom, lx + w, bottom + h)
                if cand[0] < sb[2] + 0.01 and cand[2] > sb[0] - 0.01:
                    continue
                bad = False
                for b in others:
                    if _overlap(cand, b, 0.01):
                        bad = True
                        break
                if bad:
                    continue
                if not self._descent_free(frx, fry, fbb, [cand], margin=0.02):
                    continue
                if not self._descent_free(brx, bry, bb, [cand], margin=0.02):
                    continue
                if any(not self._descent_free(cx2, cy2, b2, [cand], margin=0.01)
                       for cx2, cy2, b2 in cols):
                    continue
                ry = bottom + h + hang
                if not self._descent_free(rx, ry, cand, others, margin=0.012):
                    continue
                cost = max(abs(rx - x), abs(ry - y)) + max(abs(rx - brx), abs(ry - bry)) + pen
                cands.append((cost, lx, bottom, rx, ry, cand))
        if not cands:
            return None
        cands.sort(key=lambda c: c[0])
        binned = {}
        for c in cands:
            k = int(c[3] / 0.08)
            if k not in binned:
                binned[k] = c
        cands = sorted(binned.values(), key=lambda c: c[0])
        # rerank a few best candidates by planned path costs
        surf_bb = sb
        crel_o = (ob[0] - x, ob[1] - y, ob[2] - x, ob[3] - y)
        crel_b = (bb[0] - brx, bb[1] - bry, bb[2] - brx, bb[3] - bry)
        best = None
        for cost, lx, bottom, rx, ry, cand in cands[:self.K_RERANK]:
            obs1 = others + [surf_bb]
            c1 = self._path_cost((x, y), (rx, ry), obs1, crel_o, arm0=self._rpos()[3])
            obs2 = [bx for bx in others] + [cand, surf_bb]
            if cols:
                nx, ny = min(((cx2, cy2) for cx2, cy2, _ in cols),
                             key=lambda p: max(abs(p[0] - rx), abs(p[1] - ry)))
                c2 = self._path_cost((rx, ry + 0.01), (nx, ny), obs2, None)
                c2 += max(abs(nx - brx), abs(ny - bry)) / 0.05 * 0.5
            else:
                c2 = self._path_cost((rx, ry + 0.01), (brx, bry), obs2, None)
            obs3 = [bx for bx in others if bx != bb] + [cand, surf_bb]
            c3 = self._path_cost((brx, bry), (frx, fry), obs3, crel_b)
            tot = c1 + c2 + c3
            if best is None or tot < best[0]:
                best = (tot, lx, bottom)
        return best[1], best[2]

    def _plan(self):
        self.vac = 0.0
        failures = 0
        for _ in range(30):
            blockers = self._blocking()
            if not blockers:
                break
            robot, block, surf, obst = self._objs()
            x, y, _, _ = self._rpos()
            if self.ORDER == "tall":
                blockers.sort(key=lambda o: (-_rect_bbox(self.state, o)[3]))
            else:
                def _d(o):
                    b = _rect_bbox(self.state, o)
                    return max(abs((b[0] + b[2]) / 2 - x), abs(b[3] + TIP - y))
                blockers.sort(key=_d)
            picked = False
            for o in blockers:
                others = self._others_bboxes([o])
                if self._choose_grasp_x(o, others) is None:
                    continue
                ok = yield from self._pick(o)
                if not ok:
                    failures += 1
                    continue
                spot = self._find_spot(o)
                if spot is None:
                    spot = (_rect_bbox(self.state, o)[0], FLOOR + 0.005)
                    failures += 1
                left, bottom = spot
                ok = yield from self._place_at(o, left, bottom, release=True)
                if self.vac > 0.5:
                    self.vac = 0.0
                    yield self._act()
                self.vac = 0.0
                if not ok:
                    failures += 1
                    continue
                picked = True
                break
            if not picked:
                failures += 1
                if failures > 5:
                    break
        # now the target block
        robot, block, surf, obst = self._objs()
        for _ in range(10):
            left, bottom, sb, g = self._final_placement()
            bb = _rect_bbox(self.state, block)
            ok = yield from self._pick(block, pref=bb[0] + g)
            if not ok:
                self.vac = 0.0
                yield self._act()
                continue
            left, bottom, sb, g = self._final_placement()
            ok = yield from self._place_at(block, left, bottom)
            if ok:
                break
        self.vac = 0.0
        for _ in range(5):
            yield self._act()
