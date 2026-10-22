import math
import numpy as np


class GeneratedApproach:
    """Fast reactive baseline: get behind the block and push its centre to goal."""

    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float)
        self.high = np.asarray(action_space.high, dtype=float)
        self.step = 0

    def reset(self, state, info):
        self.step = 0

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        block = s[0:2]
        robot = s[16:18]
        goal = s[29:31]
        delta = goal - block
        distance = float(np.linalg.norm(delta))
        if distance < 1e-9:
            direction = np.array([1.0, 0.0])
        else:
            direction = delta / distance
        # Aim through the block. Collision constrains the robot at the boundary;
        # continuing toward a point beyond the centre supplies the push.
        target = block + direction * 0.5
        # The server checks the open interval despite the advertised Box bounds.
        move = np.clip(target - robot, self.low + 1e-6, self.high - 1e-6)
        self.step += 1
        return move.astype(float)
