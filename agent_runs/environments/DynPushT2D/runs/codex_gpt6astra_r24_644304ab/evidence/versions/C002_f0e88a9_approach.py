import numpy as np
import math

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.reset(None, {})

    def reset(self, state, info):
        self.steps = 0

    def get_action(self, state):
        s = np.asarray(state)
        self.steps += 1
        delta = s[29:31] - s[:2]
        d = delta / max(np.linalg.norm(delta), 1e-9)
        target = s[:2] - 0.8*d
        if np.linalg.norm(s[16:18]-target) < .15:
            target = s[:2] + delta
        a = target-s[16:18]
        return a * min(1., .05/max(np.max(np.abs(a)), 1e-9))
