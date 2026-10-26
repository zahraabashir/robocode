import numpy as np


class ReactiveApproach:
    """Drive base straight to target (world-frame deltas, max 0.4/axis).

    If a step is rejected (collision -> no motion), try a sequence of
    recovery actions: aim at points on a small circle around the target
    (the exact target may be in collision but anywhere within 0.05 counts),
    rotate the base, and random lateral moves.
    """

    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.max_d = 0.4 - 1e-4
        self.rng = np.random.default_rng(0)

    def reset(self, state, info):
        self.prev = None
        self.last_act = None
        self.queue = []
        self.offset = self._best_offset(np.asarray(state, dtype=np.float64))

    def _best_offset(self, state):
        d = np.array([state[19] - state[0], state[20] - state[1]])
        best, bestkey = np.zeros(2), None
        cands = [np.zeros(2)] + [0.04 * np.array([np.cos(t), np.sin(t)])
                                 for t in np.linspace(0, 2 * np.pi, 72, endpoint=False)]
        for off in cands:
            dd = d + off
            n = int(np.ceil(np.abs(dd).max() / self.max_d - 1e-9))
            key = (n, np.linalg.norm(off))
            if bestkey is None or key < bestkey:
                best, bestkey = off, key
        return best

    def _toward(self, state, off=None):
        off = self.offset if off is None else off
        d = np.array([state[19] + off[0] - state[0], state[20] + off[1] - state[1]])
        return np.clip(d, -self.max_d, self.max_d)

    def _recovery_plan(self, state):
        tx, ty = state[19], state[20]
        x, y = state[0], state[1]
        base = np.arctan2(y - ty, x - tx)
        plan = []
        # offsets around target, starting from robot side
        for r in [0.035, 0.046, 0.02]:
            for k in [0, 1, -1, 2, -2, 3, -3, 4]:
                th = base + k * np.pi / 4
                plan.append(("off", np.array([r * np.cos(th), r * np.sin(th)])))
        plan.append(("rot", 0.4))
        plan.append(("rot", -0.8))
        for _ in range(6):
            plan.append(("rand", None))
        return plan

    def get_action(self, state):
        state = np.asarray(state, dtype=np.float64)
        moved_cmd = self.last_act is not None and np.abs(self.last_act[:3]).max() > 1e-6
        stuck = moved_cmd and np.allclose(self.prev, state[:3], atol=1e-7)
        self.prev = state[:3].copy()
        act = np.zeros(11, dtype=np.float32)
        if not stuck:
            act[0:2] = self._toward(state)
        else:
            if not self.queue:
                self.queue = self._recovery_plan(state)
            kind, val = self.queue.pop(0)
            if kind == "off":
                self.offset = val
                act[0:2] = self._toward(state)
            elif kind == "rot":
                r = state[2] + val
                if r > np.pi or r < -np.pi:
                    val = -val
                act[2] = np.clip(val, -0.4, 0.4)
            else:
                ang = self.rng.uniform(-np.pi, np.pi)
                act[0:2] = 0.3 * np.array([np.cos(ang), np.sin(ang)])
        if not stuck and self.queue and np.abs(act[:2]).max() > 0:
            pass
        self.last_act = act.copy()
        return act
