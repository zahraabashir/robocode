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
        self.target_q = np.array([0.0, 0.8, -np.pi, -1.5, 0.0, -0.5,
                                  np.pi / 2])

    @staticmethod
    def _v(state, name, feature):
        return state.get(state.get_object_from_name(name), feature)

    def get_action(self, state):
        self.t += 1
        a = np.zeros(self.action_space.shape, dtype=self.action_space.dtype)
        robot_y = self._v(state, "robot", "pos_base_y")
        a[1] = np.clip(self.target_y - 0.00135 - robot_y, -0.2, 0.2)
        robot = state.get_object_from_name("robot")
        joints = np.array([state.get(robot, "joint_%d" % j) for j in range(1, 8)])
        a[3:10] = np.clip(self.target_q - joints, -0.2, 0.2)
        # Keep open during this reach calibration.
        a[10] = 1.0
        return a
