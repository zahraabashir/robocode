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
        self.mode = "stage"
        self.push_steps = 0

    @staticmethod
    def _wrap(angle):
        return (angle + math.pi) % (2.0 * math.pi) - math.pi

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
        behind = -direction
        desired_angle = math.atan2(behind[1], behind[0])
        rel = robot - block
        radius = float(np.linalg.norm(rel))
        current_angle = math.atan2(rel[1], rel[0]) if radius > 1e-8 else desired_angle
        angle_error = self._wrap(desired_angle - current_angle)

        if self.mode == "push":
            # Periodically re-stage so angular or lateral errors cannot accumulate.
            target = block + direction * 0.45
            self.push_steps += 1
            if self.push_steps >= 35:
                self.mode = "stage"
        else:
            clearance = 0.78
            # Orbit outside the T's circumscribed radius; direct travel to the
            # far side would otherwise collide with and rotate the object.
            if radius < clearance - 0.04:
                target = block + clearance * np.array([math.cos(current_angle), math.sin(current_angle)])
            elif abs(angle_error) > 0.055:
                next_angle = current_angle + float(np.clip(angle_error, -0.10, 0.10))
                target = block + clearance * np.array([math.cos(next_angle), math.sin(next_angle)])
            else:
                target = block + clearance * behind
                if np.linalg.norm(robot - target) < 0.035:
                    self.mode = "push"
                    self.push_steps = 0
                    target = block + direction * 0.45
        # The server checks the open interval despite the advertised Box bounds.
        move = np.clip(target - robot, self.low + 1e-6, self.high - 1e-6)
        self.step += 1
        return move.astype(float)
