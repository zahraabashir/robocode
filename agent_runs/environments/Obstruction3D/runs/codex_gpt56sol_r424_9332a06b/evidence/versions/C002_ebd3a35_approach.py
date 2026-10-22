"""Reactive policy for the variable-count Obstruction3D task."""

import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.t = 0

    def reset(self, state, info):
        self.t = 0

    def get_action(self, state):
        self.t += 1
        # Safe valid placeholder while the manipulation controller is calibrated.
        return np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
