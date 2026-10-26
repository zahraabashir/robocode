# Shared example from the planning-explanations write-up: Appendix A.3, with its dependency reactive.py (A.4).
# Transcribed from the PDF; only quotes and line wraps were normalised.
import heapq
import time

import numpy as np

from reactive import ReactiveApproach

MAXD = 0.4 - 1e-4
RADIUS = 0.05


def _wrap_ok(rot, dr):
    return -np.pi + 1e-3 <= rot + dr <= np.pi - 1e-3


class GeneratedApproach:
    """A* over base poses using an internal copy of the env as a simulator.

    Falls back to a reactive straight-line policy with collision recovery
    if the simulator is unavailable or the search fails / times out.
    """

    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.reactive = ReactiveApproach(action_space, observation_space, primitives)
        self.sim = None
        try:
            from robocode.environments.kinder_geom3d_env import KinderGeom3DEnv
            self.sim = KinderGeom3DEnv("kinder/BaseMotion3D-v0")
            self.sim.reset(seed=0)
        except Exception:
            self.sim = None
        self.plan = []
        self.expected = []

    # ---------------------------------------------------------------
    def _simulate(self, state, a):
        self.sim.set_state(np.asarray(state, dtype=np.float32))
        obs, _, term, _, _ = self.sim.step(a.astype(np.float32))
        return np.asarray(obs, dtype=np.float64), bool(term)

    def _h(self, s):
        d = np.abs(s[19:21] - s[0:2])
        cheb = max(0.0, d.max() - 0.035)
        return int(np.ceil(cheb / MAXD - 1e-9))

    def _actions(self, s):
        acts = []
        tx, ty = s[19], s[20]
        x, y = s[0], s[1]
        base = np.arctan2(y - ty, x - tx)
        offs = [np.zeros(2)]
        if np.abs([tx - x, ty - y]).max() < MAXD + RADIUS:
            for r in (0.02, 0.035, 0.046):
                for k in range(16):
                    th = base + k * np.pi / 8
                    offs.append(r * np.array([np.cos(th), np.sin(th)]))
        moves = []
        for off in offs:
            moves.append(np.clip([tx + off[0] - x, ty + off[1] - y], -MAXD, MAXD))
        for k in range(8):
            th = k * np.pi / 4
            for m in (MAXD, MAXD / 2):
                v = np.array([np.cos(th), np.sin(th)]) * m
                if k % 2 == 1:
                    v = np.sign(v) * m
                moves.append(v)
        for drot in (0.0, 0.4, -0.4):
            if not _wrap_ok(s[2], drot):
                continue
            for mv in moves:
                a = np.zeros(11)
                a[0:2] = mv
                a[2] = drot
                acts.append(a)
            if drot != 0.0:
                a = np.zeros(11)
                a[2] = drot
                acts.append(a)
        return acts

    def _key(self, s):
        return (round(s[0] / 0.02), round(s[1] / 0.02), round(s[2] / 0.1))

    def _search(self, start, time_limit):
        t0 = time.time()
        cnt = 0
        openl = [(self._h(start), self._h(start), cnt, start, [])]
        seen = {self._key(start)}
        while openl:
            if time.time() - t0 > time_limit:
                return None
            f, hh, _, s, path = heapq.heappop(openl)
            g = len(path)
            # greedy-first: evaluate successors; return as soon as goal found
            for a in self._actions(s):
                ns, term = self._simulate(s, a)
                if np.allclose(ns[:3], s[:3], atol=1e-7):
                    continue  # collision / no-op
                if term:
                    return path + [(a, ns)]
                k = self._key(ns)
                if k in seen:
                    continue
                seen.add(k)
                cnt += 1
                heapq.heappush(openl, (g + 1 + self._h(ns), self._h(ns), cnt, ns,
                                       path + [(a, ns)]))
        return None

    def _rollout(self, start, info, max_steps=60):
        r = ReactiveApproach(self.action_space, None, {})
        r.reset(start, info)
        s = start
        path = []
        for _ in range(max_steps):
            a = np.asarray(r.get_action(s), dtype=np.float64)
            ns, term = self._simulate(s, a)
            path.append((a, ns))
            if term:
                return path
            s = ns
        return None

    # ---------------------------------------------------------------
    def reset(self, state, info):
        self.reactive.reset(state, info)
        self.plan = []
        self.use_reactive = True
        self._expected = None
        if self.sim is not None:
            try:
                st = np.asarray(state, dtype=np.float64)
                res = self._rollout(st, info)
                if res is None or len(res) > self._h(st):
                    res2 = self._search(st, 20.0)
                    if res2 is not None and (res is None or len(res2) < len(res)):
                        res = res2
                if res is not None:
                    self.plan = res
                    self.use_reactive = False
            except Exception:
                self.plan = []
                self.use_reactive = True

    def get_action(self, state):
        state = np.asarray(state, dtype=np.float64)
        if not self.use_reactive:
            exp = getattr(self, "_expected", None)
            if exp is not None and not np.allclose(exp[:3], state[:3], atol=1e-3):
                self.use_reactive = True  # sim diverged from real env
            elif self.plan:
                a, ns = self.plan.pop(0)
                self._expected = ns
                return a.astype(np.float32)
            else:
                self.use_reactive = True
        return self.reactive.get_action(state)
