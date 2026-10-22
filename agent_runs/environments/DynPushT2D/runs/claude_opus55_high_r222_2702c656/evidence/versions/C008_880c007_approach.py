import math
import heapq
import numpy as np

R_ROBOT = 0.1
MAXS = 0.0499
LO, HI = 0.11, 4.87


def wrap(a):
    return (a + math.pi) % (2 * math.pi) - math.pi


def rot(th):
    c, s = math.cos(th), math.sin(th)
    return np.array([[c, -s], [s, c]])


class Block:
    def __init__(self, obs):
        self.x, self.y, self.th = obs[0], obs[1], obs[2]
        self.w, self.Lh, self.Lv = obs[12], obs[13], obs[14]
        w, Lh, Lv = self.w, self.Lh, self.Lv
        self.yc = (Lh * (-w / 2) + Lv * (-w - Lv / 2)) / (Lh + Lv)
        self.rects = [(-Lh / 2, Lh / 2, -w, 0.0), (-w / 2, w / 2, -(w + Lv), -w)]
        self.Rm = rot(self.th)
        self.p = np.array([self.x, self.y])

    def to_world(self, lp):
        return self.p + self.Rm @ np.asarray(lp)

    def to_local(self, wp):
        return self.Rm.T @ (np.asarray(wp) - self.p)

    def dir_world(self, ld):
        return self.Rm @ np.asarray(ld)

    def dist(self, wp):
        lp = self.to_local(wp)
        best = 1e9
        for (x0, x1, y0, y1) in self.rects:
            dx = max(x0 - lp[0], 0, lp[0] - x1)
            dy = max(y0 - lp[1], 0, lp[1] - y1)
            if dx == 0 and dy == 0:
                d = -min(lp[0] - x0, x1 - lp[0], lp[1] - y0, y1 - lp[1])
            else:
                d = math.hypot(dx, dy)
            best = min(best, d)
        return best

    def seg_hits(self, a, b, infl):
        la, lb = self.to_local(a), self.to_local(b)
        for (x0, x1, y0, y1) in self.rects:
            if _seg_box(la, lb, x0 - infl, x1 + infl, y0 - infl, y1 + infl):
                return True
        return False


def _seg_box(a, b, x0, x1, y0, y1):
    t0, t1 = 0.0, 1.0
    d = b - a
    for p, q in ((-d[0], a[0] - x0), (d[0], x1 - a[0]), (-d[1], a[1] - y0), (d[1], y1 - a[1])):
        if abs(p) < 1e-12:
            if q < 0:
                return False
        else:
            t = q / p
            if p < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
            if t0 > t1:
                return False
    return True


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.pos_tol = 0.012
        self.ang_tol = math.radians(3.5)

    def goal_theta(self, obs):
        g = float(obs[31])
        tol = math.radians(8.0)
        lo, hi = max(g - tol, -math.pi), min(g + tol, math.pi)
        return 0.5 * (lo + hi)

    def reset(self, state, info):
        self.banned = set()
        self.approach_steps = 0
        self.nav_fail = 0
        self.mode = 'plan'
        self.push = None
        self.push_steps = 0
        self.retreat_dir = None

    # ------------------------------------------------------------ primitives
    def primitives_list(self, B):
        w, Lh, Lv, yc = B.w, B.Lh, B.Lv, B.yc
        a = Lh / 2 - 0.04
        tipy = -(w + Lv) + 0.04
        prims = []
        # (name, local contact, local normal into block, kind)
        prims.append(('T-y', (0.0, 0.0), (0.0, -1.0), 't'))
        prims.append(('T+y', (0.0, -(w + Lv)), (0.0, 1.0), 't'))
        prims.append(('T+x', (-w / 2, yc), (1.0, 0.0), 't'))
        prims.append(('T-x', (w / 2, yc), (-1.0, 0.0), 't'))
        xo = w / 2 + R_ROBOT + 0.03
        prims.append(('F+y_a', (xo, -w), (0.0, 1.0), 'f'))
        prims.append(('F+y_b', (-xo, -w), (0.0, 1.0), 'f'))
        prims.append(('F-y_a', (0.25, 0.0), (0.0, -1.0), 'f'))
        prims.append(('F-y_b', (-0.25, 0.0), (0.0, -1.0), 'f'))
        prims.append(('F-x', (Lh / 2, -w / 2), (-1.0, 0.0), 'f'))
        prims.append(('F+x', (-Lh / 2, -w / 2), (1.0, 0.0), 'f'))
        prims.append(('Rtop+', (a, 0.0), (0.0, -1.0), 'r'))
        prims.append(('Rtop-', (-a, 0.0), (0.0, -1.0), 'r'))
        prims.append(('Rbot+', (a, -w), (0.0, 1.0), 'r'))
        prims.append(('Rbot-', (-a, -w), (0.0, 1.0), 'r'))
        prims.append(('Rsl', (-w / 2, tipy), (1.0, 0.0), 'r'))
        prims.append(('Rsr', (w / 2, tipy), (-1.0, 0.0), 'r'))
        out = []
        for name, p, n, k in prims:
            p = np.array(p)
            n = np.array(n)
            r = p - np.array([0.0, yc])
            torque = r[0] * n[1] - r[1] * n[0]
            out.append((name, p, n, k, torque))
        return out

    def wall_margin(self, B, shift):
        m = 1e9
        for (x0, x1, y0, y1) in B.rects:
            for c in ((x0, y0), (x0, y1), (x1, y0), (x1, y1)):
                wp = B.to_world(c) + shift
                m = min(m, wp[0], wp[1], 5.0 - wp[0], 5.0 - wp[1])
        return m

    def reachable(self, B, p, n):
        pre = B.to_world(p - n * (R_ROBOT + 0.04))
        return LO <= pre[0] <= HI and LO <= pre[1] <= HI

    def choose(self, obs):
        B = Block(obs)
        g = np.array([obs[29], obs[30]])
        gth = self.goal_theta(obs)
        err = g - B.p
        dth = wrap(gth - B.th)
        prims = self.primitives_list(B)
        dist = np.linalg.norm(err)
        need_rot = abs(dth) > self.ang_tol
        need_pos = abs(err[0]) > self.pos_tol or abs(err[1]) > self.pos_tol
        if not need_rot and not need_pos:
            return None
        # rotate if angle error large
        if need_rot and (abs(dth) > math.radians(6) or not need_pos or dist < 0.05):
            best, bs = None, -1e9
            for pr in prims:
                name, p, n, k, tq = pr
                if k != 'r' or tq * dth <= 0 or name in self.banned:
                    continue
                if not self.reachable(B, p, n):
                    continue
                nw = B.dir_world(n)
                s = abs(tq) * 0.5 + (float(nw @ err) / (dist + 1e-9)) * min(dist, 1.0)
                m = self.wall_margin(B, nw * 0.3)
                if m < 0.25:
                    s -= 10 + (0.25 - m) * 10
                if s > bs:
                    bs, best = s, pr
            if best is not None and bs > -5:
                return best, dth, g
            if best is not None and self.wall_margin(B, np.zeros(2)) > 0.45:
                return best, dth, g
            # recenter: move the block away from walls
            c = np.array([2.5, 2.5]) - B.p
            cn = np.linalg.norm(c)
            if cn > 0.05:
                tr = self.pick_trans(B, prims, c / cn)
                if tr is not None:
                    return tr, dth, B.p + c / cn * min(cn, 0.5)
            if best is not None:
                return best, dth, g
        tr = self.pick_trans(B, prims, err)
        if tr is not None and float(B.dir_world(tr[2]) @ err) > 0.004:
            return tr, dth, g
        c = np.array([2.5, 2.5]) - B.p
        cn = np.linalg.norm(c)
        tr2 = self.pick_trans(B, prims, c / (cn + 1e-9))
        if tr2 is not None:
            return tr2, dth, B.p + c / (cn + 1e-9) * min(cn, 0.3)
        return tr, dth, g

    def pick_trans(self, B, prims, err):
        best, bs = None, -1e9
        for pr in prims:
            name, p, n, k, tq = pr
            if k not in ('t', 'f') or name in self.banned:
                continue
            if not self.reachable(B, p, n):
                continue
            nw = B.dir_world(n)
            s = float(nw @ err)
            if k == 'f':
                s = s * 0.6 - 0.01
            if s > bs:
                bs, best = s, pr
        return best

    # ------------------------------------------------------------ navigation
    def nav_step(self, B, rp, target):
        infl = R_ROBOT + 0.015
        d0 = B.dist(rp)
        if not B.seg_hits(rp, target, min(infl, d0 - 0.003)):
            return target
        # waypoints around inflated rects
        e = R_ROBOT + 0.05
        pts = []
        for (x0, x1, y0, y1) in B.rects:
            for cx, cy in ((x0 - e, y0 - e), (x0 - e, y1 + e), (x1 + e, y0 - e), (x1 + e, y1 + e)):
                wp = B.to_world((cx, cy))
                wp = np.clip(wp, LO, HI)
                if B.dist(wp) > infl + 0.005:
                    pts.append(wp)
        nodes = [rp] + pts + [target]
        N = len(nodes)
        distv = [1e18] * N
        prev = [-1] * N
        distv[0] = 0
        pq = [(0.0, 0)]
        while pq:
            d, i = heapq.heappop(pq)
            if d > distv[i]:
                continue
            if i == N - 1:
                break
            for j in range(1, N):
                if j == i:
                    continue
                inf_ij = infl if i != 0 else min(infl, d0 - 0.003)
                if B.seg_hits(nodes[i], nodes[j], inf_ij):
                    continue
                nd = d + float(np.linalg.norm(nodes[j] - nodes[i]))
                if nd < distv[j]:
                    distv[j] = nd
                    prev[j] = i
                    heapq.heappush(pq, (nd, j))
        if prev[N - 1] == -1:
            # no path; move away from block
            return None
        j = N - 1
        while prev[j] != 0:
            j = prev[j]
        return nodes[j]

    # ------------------------------------------------------------ main
    def get_action(self, state):
        obs = np.asarray(state, dtype=float)
        B = Block(obs)
        rp = obs[16:18].copy()
        for _ in range(4):
            act = self._act(obs, B, rp)
            if act is not None:
                return np.clip(act, -MAXS, MAXS).astype(np.float32)
        return np.zeros(2, dtype=np.float32)

    def _move_to(self, rp, tgt, speed=MAXS):
        d = tgt - rp
        n = np.linalg.norm(d)
        if n > speed:
            d = d / n * speed
        return d

    def _act(self, obs, B, rp):
        if self.mode == 'plan':
            res = self.choose(obs)
            if res is None:
                return np.zeros(2)
            pr, dth, self.push_goal = res
            if pr is None:
                if self.banned:
                    self.banned.clear()
                    return None
                return np.zeros(2)
            self.push = pr
            self.push_dth0 = dth
            self.push_err0 = np.array([obs[29] - obs[0], obs[30] - obs[1]])
            self.mode = 'approach'
            self.push_steps = 0
            self.approach_steps = 0
            self.nav_fail = 0
        name, p, n, k, tq = self.push
        if self.mode == 'approach':
            self.approach_steps += 1
            if self.approach_steps > 150 or self.nav_fail > 15:
                self.banned.add(name)
                self.mode = 'plan'
                return None
            pre = B.to_world(p - n * (R_ROBOT + 0.04))
            if np.linalg.norm(pre - rp) < 0.004:
                self.mode = 'push'
                self.push_steps = 0
            else:
                d = B.dist(rp)
                wp = None
                if d > R_ROBOT - 0.01:
                    wp = self.nav_step(B, rp, pre)
                if wp is None:
                    self.nav_fail += 1
                    # too close: move away from block
                    lp = B.to_local(rp)
                    away = rp - B.to_world((0.0, B.yc))
                    # push outward along the direction from nearest point
                    best = None
                    for ang in np.linspace(0, 2 * math.pi, 16, endpoint=False):
                        cand = np.clip(rp + 0.03 * np.array([math.cos(ang), math.sin(ang)]), 0.105, 4.88)
                        dd = B.dist(cand)
                        if best is None or dd > best[0]:
                            best = (dd, cand)
                    return best[1] - rp
                return self._move_to(rp, wp)
        if self.mode == 'push':
            self.push_steps += 1
            err = self.push_goal - B.p
            dth = wrap(self.goal_theta(obs) - B.th)
            nw = B.dir_world(n)
            done = False
            if k in ('t', 'f'):
                rem = float(nw @ err)
                if rem < 0.004:
                    done = True
                speed = min(MAXS, max(0.6 * rem, 0.002))
                # stop to re-evaluate if angle drifts
                if abs(dth) > math.radians(6):
                    done = True
            else:
                rem = abs(dth)
                if dth * self.push_dth0 <= 0 or rem < math.radians(1.0):
                    done = True
                speed = MAXS if rem > math.radians(10) else max(0.005, MAXS * rem / math.radians(10))
            if self.push_steps == 1:
                self.push_start = (B.p.copy(), B.th)
            if self.push_steps > 40:
                done = True
            if self.push_steps == 12:
                moved = np.linalg.norm(B.p - self.push_start[0]) + abs(B.th - self.push_start[1])
                if moved < 0.01:
                    self.banned.add(name)
                    done = True
                else:
                    self.banned.clear()
            if done:
                self.mode = 'plan'
                return None
            cp = B.to_world(p - n * (R_ROBOT - 0.002))
            # desired robot pos: contact point moved by speed along push dir
            tgt = cp + nw * speed
            return self._move_to(rp, tgt, MAXS)
        return np.zeros(2)
