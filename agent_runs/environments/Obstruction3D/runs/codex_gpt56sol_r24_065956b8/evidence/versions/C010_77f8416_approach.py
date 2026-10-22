"""Geometry-driven policy for the Obstruction3D manipulation task."""

import numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation

_ORIGINS = (
    ((0, 0, .15643), (np.pi, 0, 0)),
    ((0, .005375, -.12838), (np.pi / 2, 0, 0)),
    ((0, -.21038, -.006375), (-np.pi / 2, 0, 0)),
    ((0, .006375, -.21038), (np.pi / 2, 0, 0)),
    ((0, -.20843, -.006375), (-np.pi / 2, 0, 0)),
    ((0, .00017505, -.10593), (np.pi / 2, 0, 0)),
    ((0, -.10593, -.00017505), (-np.pi / 2, 0, 0)),
)
_HOME = np.array((0, -.35, -np.pi, -2.5, 0, -.87, np.pi / 2))


def _fk(q):
    t = np.eye(4)
    for angle, (xyz, rpy) in zip(q, _ORIGINS):
        a = np.eye(4)
        a[:3, :3] = Rotation.from_euler("xyz", rpy).as_matrix()
        a[:3, 3] = xyz
        z = np.eye(4)
        z[:3, :3] = Rotation.from_euler("z", angle).as_matrix()
        t = t @ a @ z
    a = np.eye(4)
    a[:3, :3] = Rotation.from_euler("x", np.pi).as_matrix()
    a[:3, 3] = (0, 0, -.061525)
    return t @ a


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space

    @staticmethod
    def _get(state, name, feature):
        return float(state.get(state.get_object_from_name(name), feature))

    def _solve(self, xyz, seed=None):
        start = _HOME if seed is None else seed
        base = np.array((self.base_x, self.base_y, 0.0))
        def residual(q):
            t = _fk(q)
            grasp = base + t[:3, 3] + .12 * t[:3, 2]
            return np.r_[8 * (grasp - xyz), 1.5 * t[:2, 2], .03 * (q - _HOME)]
        return least_squares(residual, start, max_nfev=180).x

    def reset(self, state, info):
        self.step = 0
        self.base_x = self._get(state, "robot", "pos_base_x")
        self.base_y = self._get(state, "robot", "pos_base_y")
        block = np.array([self._get(state, "target_block", f"pose_{c}") for c in "xyz"])
        region = np.array([self._get(state, "target_region", f"pose_{c}") for c in "xyz"])
        self.pick_q = self._solve(block)
        self.lift_q = self._solve(block + (0, 0, .18), self.pick_q)
        self.place_q = self._solve(region + (0, 0, .08), self.lift_q)
        self.drop_q = self._solve(region + (0, 0, .03), self.place_q)

    def get_action(self, state):
        self.step += 1
        robot = state.get_object_from_name("robot")
        q = np.array([float(state.get(robot, f"joint_{i}")) for i in range(1, 8)])
        grasped = float(state.get(robot, "grasp_active")) > .5
        if self.step <= 18:
            goal, grip = self.pick_q, 1.0
        elif self.step <= 21:
            goal, grip = self.pick_q, -1.0
        elif self.step <= 35:
            goal, grip = self.lift_q, 0.0
        elif self.step <= 51:
            goal, grip = self.place_q, 0.0
        elif self.step <= 60:
            goal, grip = self.drop_q, 0.0
        else:
            goal, grip = self.drop_q, 1.0
        if 22 <= self.step <= 35 and not grasped:
            goal, grip = self.pick_q, -1.0
        action = np.zeros(self.action_space.shape, dtype=np.float32)
        action[3:10] = np.clip(goal - q, -.2, .2)
        action[10] = grip
        return action
