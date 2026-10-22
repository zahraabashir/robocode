import math
import numpy as np


class GeneratedApproach:
    """Closed-loop contact controller for the asymmetric T pusher."""
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float)
        self.high = np.asarray(action_space.high, dtype=float)
        self.reset(None, None)

    def reset(self, state, info):
        self.mode = "choose"
        self.count = 0
        self.turn_sign = 1.0
        self.push_dir = np.array([1.0, 0.0])
        self.start_pose = np.zeros(3)

    @staticmethod
    def _angle(x):
        return (x + math.pi) % (2.0 * math.pi) - math.pi

    @staticmethod
    def _world(local, theta):
        c, sn = math.cos(theta), math.sin(theta)
        return np.array([c*local[0] - sn*local[1], sn*local[0] + c*local[1]])

    def _safe(self, delta, speed=0.049):
        a = np.asarray(delta, dtype=float)
        n = float(np.linalg.norm(a))
        if n > speed:
            a *= speed / n
        return np.clip(a, self.low, self.high).astype(float)

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        obj, robot, goal = s[0:2], s[16:18], s[29:31]
        theta, goal_theta = float(s[2]), float(s[31])
        width, lh, lv = map(float, s[12:15])
        ae = self._angle(goal_theta - theta)
        dp = goal - obj
        pd = float(np.linalg.norm(dp))

        if self.mode == "choose":
            if abs(ae) > 0.075:
                self.turn_sign = 1.0 if ae > 0.0 else -1.0
                self.mode = "rot_far"
            elif pd > 0.018:
                self.push_dir = dp / max(pd, 1e-9)
                self.mode = "move_far"
            else:
                return np.zeros(2, dtype=float)
            self.count = 0
            self.start_pose = np.array([obj[0], obj[1], theta])

        if self.mode.startswith("rot"):
            # Distal-stem side contact is a reliable long rotation lever.
            side = -self.turn_sign
            far_local = np.array([side * (width * 0.5 + 0.34), -0.72 * lv])
            contact_local = np.array([side * (width * 0.5 + 0.115), -0.72 * lv])
            far = obj + self._world(far_local, theta)
            contact = obj + self._world(contact_local, theta)
            force = self._world(np.array([self.turn_sign, 0.0]), theta)
            if self.mode == "rot_far":
                if np.linalg.norm(robot - far) < 0.035:
                    self.mode = "rot_contact"
                return self._safe(far - robot)
            if self.mode == "rot_contact":
                if np.linalg.norm(robot - contact) < 0.018:
                    self.mode = "rot_push"
                    self.count = 0
                    self.start_pose = np.array([obj[0], obj[1], theta])
                return self._safe(contact - robot, 0.025)
            if self.mode == "rot_push":
                self.count += 1
                current_ae = self._angle(goal_theta - theta)
                turned = abs(self._angle(theta - self.start_pose[2]))
                if (current_ae * self.turn_sign < 0.0 or abs(current_ae) < 0.055
                        or turned > 0.16 or self.count >= 10):
                    self.mode = "rot_retreat"
                return self._safe(force, 0.016)
            if np.linalg.norm(robot - far) < 0.04:
                self.mode = "choose"
            return self._safe(far - robot, 0.035)

        # The effective COM lies down the stem from the reported junction.
        com = obj + self._world(np.array([0.0, -0.36 * lv]), theta)
        far = com - self.push_dir * 0.82
        if self.mode == "move_far":
            if np.linalg.norm(robot - far) < 0.035:
                self.mode = "move_push"
                self.count = 0
                self.start_pose = np.array([obj[0], obj[1], theta])
            return self._safe(far - robot)
        if self.mode == "move_push":
            self.count += 1
            moved = float(np.linalg.norm(obj - self.start_pose[:2]))
            now_ae = abs(self._angle(goal_theta - theta))
            if moved > 0.14 or self.count >= 18 or now_ae > 0.13:
                self.mode = "move_retreat"
            speed = 0.012 if pd < 0.12 else 0.025
            return self._safe((com + self.push_dir * 0.20) - robot, speed)
        if np.linalg.norm(robot - far) < 0.04:
            self.mode = "choose"
        return self._safe(far - robot, 0.035)
