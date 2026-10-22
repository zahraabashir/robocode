"""Experimental policy for DynPushT2D, kept separate from the submitted approach."""
import math
import numpy as np


def wrap_angle(x):
    return (x + math.pi) % (2.0 * math.pi) - math.pi


class CandidateStrategy:
    def __init__(self, action_space, observation_space, primitives):
        self.low = np.asarray(action_space.low, dtype=float)
        self.high = np.asarray(action_space.high, dtype=float)
        self.phase = "select"
        self.mode = None
        self.side = 1.0
        self.ticks = 0

    def reset(self, state, info):
        self.phase = "select"
        self.mode = None
        self.side = 1.0
        self.ticks = 0

    @staticmethod
    def _unit(v):
        n = float(np.linalg.norm(v))
        return v / n if n > 1e-9 else np.zeros(2)

    def _move(self, robot, target, gain=1.0, maxnorm=0.049):
        # The server also enforces a Euclidean displacement cap despite the Box
        # metadata being per-axis, so diagonal commands must be normalized.
        action = np.clip((target - robot) * gain, self.low, self.high)
        norm = float(np.linalg.norm(action))
        if norm > maxnorm:
            action *= maxnorm / norm
        return action

    def _select(self, s):
        c = s[0:2]
        goal = s[29:31]
        ae = wrap_angle(float(s[31] - s[2]))
        pe = float(np.linalg.norm(goal - c))
        # Pose accuracy requires repeatedly correcting the orientation disturbed by
        # translation.  Angle gets priority except very close to its tolerance.
        if abs(ae) > 0.10:
            self.mode = "rotate"
            self.side = 1.0 if ae >= 0 else -1.0
        elif pe > 0.022:
            self.mode = "translate"
        else:
            self.mode = "rotate"
            self.side = 1.0 if ae >= 0 else -1.0
        self.phase = "retreat"
        self.ticks = 0

    def _geometry(self, s):
        c = np.asarray(s[0:2], dtype=float)
        robot = np.asarray(s[16:18], dtype=float)
        if self.mode == "translate":
            force = self._unit(np.asarray(s[29:31]) - c)
            # Contact somewhere on the rear-facing support surface.
            contact = c - force * 0.52
            setup = c - force * 0.64
        else:
            th = float(s[2])
            ex = np.array([math.cos(th), math.sin(th)])
            ey = np.array([-math.sin(th), math.cos(th)])
            # Push tangentially on the positive local-x end. side is torque sign.
            contact = c + ex * (0.40 * float(s[13]))
            force = ey * self.side
            # Robot-center staging point: one radius plus a small margin behind
            # the intended material contact point.
            setup = contact - force * 0.12
        return c, robot, contact, setup, force

    def get_action(self, state):
        s = np.asarray(state, dtype=float)
        self.ticks += 1
        if self.phase == "select":
            self._select(s)
        c, robot, contact, setup, force = self._geometry(s)

        # Use a collision-free polar repositioning maneuver around the object.
        ray = self._unit(setup - c)
        # The T's longest corner is about 0.7 from its reference point; less
        # clearance makes the robot accidentally shove it while repositioning.
        radius = 0.88
        rvec = robot - c
        rdist = float(np.linalg.norm(rvec))
        rang = math.atan2(rvec[1], rvec[0])
        tang = math.atan2(ray[1], ray[0])
        adiff = wrap_angle(tang - rang)

        if self.phase == "retreat":
            if rdist >= radius - 0.04:
                self.phase = "orbit"
            else:
                outward = self._unit(rvec)
                if np.linalg.norm(outward) < 0.5:
                    outward = ray
                return self._move(robot, c + outward * radius)

        if self.phase == "orbit":
            if abs(adiff) < 0.10:
                self.phase = "approach"
            else:
                # A look-ahead point gives smooth travel around the clearance circle.
                direction = 1.0 if adiff > 0 else -1.0
                stepang = rang + direction * min(0.25, abs(adiff))
                waypoint = c + radius * np.array([math.cos(stepang), math.sin(stepang)])
                # If the short arc runs into a wall, take the long way around.
                if np.any(waypoint < 0.12) or np.any(waypoint > 4.88):
                    stepang = rang - direction * 0.25
                    waypoint = c + radius * np.array([math.cos(stepang), math.sin(stepang)])
                waypoint = np.clip(waypoint, 0.12, 4.88)
                return self._move(robot, waypoint)

        if self.phase == "approach":
            if np.linalg.norm(robot - setup) < 0.055:
                self.phase = "push"
                self.ticks = 0
            else:
                return self._move(robot, setup)

        if self.phase == "push":
            ae = wrap_angle(float(s[31] - s[2]))
            pe = float(np.linalg.norm(s[29:31] - c))
            omega = float(s[5])
            done = ((self.mode == "rotate" and
                     (abs(ae) < 0.075 or omega * self.side > 0.12 or self.ticks > 8)) or
                    (self.mode == "translate" and
                     (pe < 0.020 or abs(ae) > 0.14 or self.ticks > 35)))
            if done:
                self.phase = "select"
            # Aim through the selected contact, then continue in the desired force direction.
            aim = contact + force * 0.10
            return self._move(robot, aim, maxnorm=(0.006 if self.mode == "rotate" else 0.010))

        return np.zeros(2)


# Allows the same test harness shape as approach.py.
GeneratedApproach = CandidateStrategy
