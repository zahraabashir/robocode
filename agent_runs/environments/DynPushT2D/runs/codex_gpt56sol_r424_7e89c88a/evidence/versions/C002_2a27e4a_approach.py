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
        # Conservative clearance for the initial positioning phase.
        staging = block - direction * 0.13
        target = staging if np.linalg.norm(robot - staging) > 0.035 else block + direction * 0.08
        move = np.clip(target - robot, self.low, self.high)
        self.step += 1
        return move.astype(float)
