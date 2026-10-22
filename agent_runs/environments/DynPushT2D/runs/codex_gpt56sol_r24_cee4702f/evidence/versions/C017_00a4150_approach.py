import math
import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float)
        self.high = np.asarray(action_space.high, dtype=float)
        self.reset(None, None)

    def reset(self, state, info):
        self.step = 0
        self.mode = "rotate_approach"
        self.push_dir = None
        self.stroke_theta = 0.0
        self.lever_local = None

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        obj = s[0:2]
        robot = s[16:18]
        goal = s[29:31]
        theta = float(s[2])
        goal_theta = float(s[31])
        angle_error = (goal_theta - theta + math.pi) % (2.0 * math.pi) - math.pi
        delta = goal - obj
        dist = float(np.linalg.norm(delta))
        if dist > 1e-9:
            direction = delta / dist
        else:
            direction = np.array([1.0, 0.0])
        width, lh, lv = map(float, s[12:15])
        c, sn = math.cos(theta), math.sin(theta)
        # Stem runs along local -y.  Use whichever of its tip or the two cap
        # ends offers an accessible tangential rotation contact.
        stem_dir = np.array([sn, -c])
        turn = 1.0 if angle_error > 0.0 else -1.0

        if self.mode == "rotate_approach" and self.lever_local is None:
            local_options = [np.array([0.0, -(lv - width * 0.5)]),
                             np.array([lh * 0.5 - width * 0.5, 0.0]),
                             np.array([-lh * 0.5 + width * 0.5, 0.0])]
            def clearance(local):
                r = np.array([c*local[0] - sn*local[1],
                              sn*local[0] + c*local[1]])
                f = np.array([-r[1], r[0]]) * turn / np.linalg.norm(r)
                stage = obj + r - f * 0.24
                return min(stage[0] - 0.11, 4.89 - stage[0],
                           stage[1] - 0.11, 4.89 - stage[1])
            self.lever_local = max(local_options, key=clearance)
        local = self.lever_local if self.lever_local is not None else np.array([0.0, -lv])
        lever = np.array([c*local[0] - sn*local[1], sn*local[0] + c*local[1]])
        tip = obj + lever
        tangent = np.array([-lever[1], lever[0]]) * turn / np.linalg.norm(lever)

        if self.mode.startswith("rotate") and abs(angle_error) < 0.065:
            self.mode = "approach"
            self.push_dir = direction.copy()
        elif not self.mode.startswith("rotate") and abs(angle_error) > 0.16:
            self.mode = "rotate_approach"
            self.lever_local = None

        if self.mode == "rotate_approach":
            target = tip - tangent * 0.24
            if np.linalg.norm(robot - target) < 0.045:
                self.mode = "rotate_push"
                self.stroke_theta = theta
        elif self.mode == "rotate_push":
            target = tip + tangent * 0.35
            turned = abs((theta - self.stroke_theta + math.pi) % (2*math.pi) - math.pi)
            if turned > 0.25 or np.linalg.norm(robot - tip) > 0.55:
                self.mode = "rotate_approach"
                self.lever_local = None
        elif self.mode == "approach":
            self.push_dir = direction.copy()
            # Approximate COM is down the stem; pushing through it reduces spin.
            com = obj + stem_dir * (0.22 * lv)
            stand = com - self.push_dir * 0.78
            stand = np.clip(stand, 0.13, 4.87)
            target = stand
            if np.linalg.norm(robot - stand) < 0.045:
                self.mode = "push"
        else:
            # Aim through the centre and keep contact rather than oscillating
            # between the moving staging point and the object.
            com = obj + stem_dir * (0.22 * lv)
            target = com + self.push_dir * 0.30
            if np.dot(delta, self.push_dir) < -0.04:
                self.mode = "approach"
        action = np.clip(target - robot, self.low, self.high)
        # The robot has a Euclidean displacement cap in addition to Box bounds.
        norm = float(np.linalg.norm(action))
        if norm > 0.049:
            action *= 0.049 / norm
        self.step += 1
        return action.astype(float)
