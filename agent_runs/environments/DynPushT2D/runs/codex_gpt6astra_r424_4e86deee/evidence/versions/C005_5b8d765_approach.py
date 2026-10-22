"""Feedback pushing policy for a rigid T block."""
import numpy as np
import math

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.reset(None, {})

    def reset(self, state, info):
        self.step = 0

    def get_action(self, state):
        s = np.asarray(state)
        direction = s[29:31] - s[:2]
        direction /= max(np.linalg.norm(direction), 1e-9)
        target = s[:2] - .8 * direction
        self.step += 1
        return np.clip(target - s[16:18], -.049, .049)
