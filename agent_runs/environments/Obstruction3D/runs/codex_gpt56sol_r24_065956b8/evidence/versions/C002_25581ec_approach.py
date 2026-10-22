"""Policy for the Obstruction3D black-box manipulation task."""

import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space

    def reset(self, state, info):
        pass

    def get_action(self, state):
        # Safe baseline; replaced as dynamics are identified.
        return np.zeros(self.action_space.shape, dtype=np.float32)
