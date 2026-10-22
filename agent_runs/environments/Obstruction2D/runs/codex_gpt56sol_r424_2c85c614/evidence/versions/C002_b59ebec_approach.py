"""Reactive policy for Obstruction2DEnv."""

import math
import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.types = {t.name: t for t in observation_space.types}
        self.phase = "approach"

    def reset(self, state, info):
        self.phase = "approach"

    def _one(self, state, type_name):
        return state.get_objects(self.types[type_name])[0]

    def get_action(self, state):
        robot = self._one(state, "crv_robot")
        block = self._one(state, "target_block")
        surface = self._one(state, "target_surface")
        rx, ry = state.get(robot, "x"), state.get(robot, "y")
        theta = state.get(robot, "theta")
        arm = state.get(robot, "arm_joint")
        vacuum = state.get(robot, "vacuum")
        bx, by = state.get(block, "x"), state.get(block, "y")
        sx, sy = state.get(surface, "x"), state.get(surface, "y")

        # First baseline: approach/grasp the block, then translate it to the surface.
        carrying = vacuum > 0.5 and math.hypot(bx - sx, by - sy) > 0.03
        tx, ty = (sx, sy) if carrying else (bx, by)
        desired = math.atan2(ty - ry, tx - rx)
        err = (desired - theta + math.pi) % (2 * math.pi) - math.pi
        dist = math.hypot(tx - rx, ty - ry)
        target_arm = max(0.0, dist - 0.02)
        action = np.zeros(5, dtype=np.float32)
        if abs(err) > 0.05:
            action[2] = np.clip(err, -0.196, 0.196)
        else:
            action[3] = np.clip(target_arm - arm, -0.1, 0.1)
        action[4] = 1.0
        return np.clip(action, self.action_space.low, self.action_space.high).astype(np.float32)
