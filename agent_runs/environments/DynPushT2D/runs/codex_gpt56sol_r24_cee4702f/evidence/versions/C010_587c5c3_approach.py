import math
import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float)
        self.high = np.asarray(action_space.high, dtype=float)
        self.reset(None, None)

    def reset(self, state, info):
        self.step = 0
        self.mode = "approach"
        self.push_dir = None

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        obj = s[0:2]
        robot = s[16:18]
        goal = s[29:31]
        delta = goal - obj
        dist = float(np.linalg.norm(delta))
        if dist > 1e-9:
            direction = delta / dist
        else:
            direction = np.array([1.0, 0.0])
        if self.push_dir is None:
            self.push_dir = direction.copy()
        if self.mode == "approach":
            self.push_dir = direction.copy()
            # Outside the T's roughly 0.6 radius bounding box.
            stand = obj - self.push_dir * 0.78
            target = stand
            if np.linalg.norm(robot - stand) < 0.045:
                self.mode = "push"
        else:
            # Aim through the centre and keep contact rather than oscillating
            # between the moving staging point and the object.
            target = obj + self.push_dir * 0.25
            if np.dot(delta, self.push_dir) < -0.04:
                self.mode = "approach"
        action = np.clip(target - robot, self.low, self.high)
        # The robot has a Euclidean displacement cap in addition to Box bounds.
        norm = float(np.linalg.norm(action))
        if norm > 0.049:
            action *= 0.049 / norm
        self.step += 1
        return action.astype(float)
