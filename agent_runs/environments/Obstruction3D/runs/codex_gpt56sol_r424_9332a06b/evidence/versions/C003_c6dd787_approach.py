"""Reactive policy for the variable-count Obstruction3D task."""

import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.t = 0

    def reset(self, state, info):
        self.t = 0
        self.target_y = self._v(state, "target_block", "pose_y")

    @staticmethod
    def _v(state, name, feature):
        return state.get(state.get_object_from_name(name), feature)

    def get_action(self, state):
        self.t += 1
        a = np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
        robot_y = self._v(state, "robot", "pos_base_y")
        a[1] = np.clip(self.target_y - robot_y, -0.2, 0.2)
        if self.t >= 3:
            a[10] = -1.0
        return a
