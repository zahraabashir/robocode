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
        # The reported x=-.12 is the mobile-base bound; the arm pedestal is
        # mounted +.12 from it.  Hence the initial arm frame is world origin.
        base = np.array((self.base_x + .12, self.base_y, 0.0))
        def residual(q):
            t = _fk(q)
            grasp = base + t[:3, 3] + .16 * t[:3, 2]
            if self.carry_rotation is None:
                orientation = t[:2, 2]
            else:
                orientation = Rotation.from_matrix(self.carry_rotation.T @ t[:3, :3]).as_rotvec()
            return np.r_[10 * (grasp - xyz), 1.8 * orientation, .02 * (q - start)]
        return least_squares(residual, start, max_nfev=180).x

    def _xyz(self, state, name):
        return np.array([self._get(state, name, f"pose_{c}") for c in "xyz"])

    def _robot_q(self, state):
        robot = state.get_object_from_name("robot")
        return np.array([float(state.get(robot, f"joint_{i}")) for i in range(1, 8)])

    def _held(self, state):
        for name in state.get_object_names():
            if name != "robot":
                try:
                    if self._get(state, name, "grasp_active") > .5:
                        return name
                except (KeyError, ValueError):
                    pass
        return None

    def _blocking(self, state, name):
        if not name.startswith("obstruction"):
            return False
        rx, ry = self._xyz(state, "target_region")[:2]
        ox, oy = self._xyz(state, name)[:2]
        rhx = self._get(state, "target_region", "half_extent_x")
        rhy = self._get(state, "target_region", "half_extent_y")
        ohx = self._get(state, name, "half_extent_x")
        ohy = self._get(state, name, "half_extent_y")
        return abs(ox-rx) < rhx+ohx+.006 and abs(oy-ry) < rhy+ohy+.006

    def _choose_task(self, state):
        blockers = sorted((n for n in state.get_object_names() if self._blocking(state, n)),
                          key=lambda n: (n in self.deferred, -self._xyz(state, n)[2]))
        if blockers:
            self.object = blockers[0]
            # Use rows opposite the goal. Staggering x prevents a pile even
            # when many independently sampled obstructions must be cleared.
            ry = self._xyz(state, "target_region")[1]
            if self.object not in self.park_spots:
                i = len(self.park_spots)
                side = -.34 if ry >= 0 else .34
                px = .13 + .12*(i % 4)
                py = side - np.sign(side)*.07*(i // 4)
                self.park_spots[self.object] = (px, py)
            px, py = self.park_spots[self.object]
            self.destination = np.array((px, py, .078 + self._get(state, self.object, "half_extent_z")))
            return
        self.object = "target_block"
        reg = self._xyz(state, "target_region")
        z = reg[2] + self._get(state, "target_region", "half_extent_z")
        # Contact is recognized a few millimeters above the analytical surface.
        # Airborne objects intentionally cannot be released by this environment.
        z += self._get(state, "target_block", "half_extent_z") + .003
        self.destination = np.array((reg[0], reg[1], z))

    def _set_goal_for_object_delta(self, state, desired_object_xyz):
        q = self._robot_q(state)
        t = _fk(q)
        model_grasp = np.array((self.base_x + .12, self.base_y, 0.0)) + t[:3, 3] + .16*t[:3, 2]
        desired_grasp = model_grasp + desired_object_xyz - self._xyz(state, self._held(state))
        self.goal_q = self._solve(desired_grasp, q)

    def _act_to(self, q, goal, grip=0.0):
        action = np.zeros(self.action_space.shape, dtype=np.float32)
        action[3:10] = np.clip(goal - q, -.2, .2)
        action[10] = grip
        return action

    def reset(self, state, info):
        self.step = 0
        self.phase = "choose"
        self.phase_steps = 0
        self.park_count = 0
        self.park_spots = {}
        self.deferred = set()
        self.abandoning = False
        self.carry_rotation = None
        self.base_x = self._get(state, "robot", "pos_base_x")
        self.base_y = self._get(state, "robot", "pos_base_y")

    def get_action(self, state):
        self.step += 1
        self.phase_steps += 1
        q = self._robot_q(state)
        held = self._held(state)
        self.base_x = self._get(state, "robot", "pos_base_x")
        self.base_y = self._get(state, "robot", "pos_base_y")

        if self.phase == "choose":
            self._choose_task(state)
            self.carry_rotation = None
            self.pick_xyz = self._xyz(state, self.object)
            if self.object.startswith("obstruction"):
                # Pinch near the top: center-height grasps can put fingertips
                # into the target plate or an immediately adjacent blocker.
                self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
            # A calibrated vertical grasp pose plus base translation is more
            # collision-robust than interpolating through a low joint-space IK
            # path. It works for both target-sized and small obstruction blocks.
            u = np.clip((self.pick_xyz[0]-.3359817)/(.4644086-.3359817), 0, 1)
            center_z = self._xyz(state, self.object)[2]
            height_q = (.1-center_z)/.3445
            self.anchor_q = np.array((0, .25+.2*u, -np.pi, -2.30+.2*u,
                                      0, -.47+.2*u, np.pi/2))
            self.anchor_q[1] += height_q
            self.anchor_bx = self.pick_xyz[0]-.4559817 if self.pick_xyz[0] <= .3359817 else -.12
            if self.pick_xyz[0] <= .3359817:
                self.anchor_bx += .1625*height_q
            self.anchor_by = self.pick_xyz[1]
            self.goal_q = _HOME.copy()
            self.phase, self.phase_steps = "target_home", 0

        if self.phase == "prepick_base":
            bxerr, byerr = self.pick_bx-self.base_x, self.pick_by-self.base_y
            if (np.max(np.abs(self.goal_q-q)) < .012 and
                    max(abs(bxerr), abs(byerr)) < .005) or self.phase_steps > 30:
                self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
                self.phase, self.phase_steps = "prepick", 0
            else:
                action = self._act_to(q, self.goal_q, 1.0)
                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
                return action

        if self.phase == "target_home":
            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 25:
                self.goal_q = self.anchor_q
                self.phase, self.phase_steps = "target_anchor", 0
            else:
                return self._act_to(q, self.goal_q, 1.0)

        if self.phase == "target_anchor":
            bxerr, byerr = self.anchor_bx-self.base_x, self.anchor_by-self.base_y
            base_error = max(abs(bxerr), abs(byerr))
            if np.max(np.abs(self.goal_q-q)) < .012 and base_error < .005:
                self.phase, self.phase_steps = "close", 0
            elif base_error >= .005:
                # Translate with the arm fully retracted. Combining these with
                # low-arm joint deltas can make collision rejection atomic.
                action = self._act_to(q, q, 1.0)
                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
                return action
            else:
                action = self._act_to(q, self.goal_q, 1.0)
                return action

        if self.phase == "choose":
            self.goal_q = self._solve(self.pick_xyz + (0, 0, .18), q)
            self.phase, self.phase_steps = "prepick", 0

        if self.phase == "prepick":
            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
                self.carry_rotation = _fk(q)[:3, :3].copy()
                self.pick_z = [self.pick_xyz[2]+d for d in (.10, .05, 0)]
                self.pick_index = 0
                waypoint = self.pick_xyz.copy(); waypoint[2] = self.pick_z[0]
                self.goal_q = self._solve(waypoint, q)
                self.phase, self.phase_steps = "pick", 0
            else:
                return self._act_to(q, self.goal_q, 1.0)

        if self.phase == "pick":
            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 30:
                self.pick_index += 1
                if self.pick_index >= len(self.pick_z):
                    self.phase, self.phase_steps = "close", 0
                else:
                    waypoint = self.pick_xyz.copy(); waypoint[2] = self.pick_z[self.pick_index]
                    self.goal_q = self._solve(waypoint, q)
                    self.phase_steps = 0
                    return self._act_to(q, self.goal_q, 1.0)
            else:
                return self._act_to(q, self.goal_q, 1.0)

        if self.phase == "close":
            if held is not None:
                self.object = held  # handle a neighboring obstruction gracefully
                self.carry_rotation = _fk(q)[:3, :3].copy()
                self.lift_start_z = self._xyz(state, held)[2]
                self.abandoning = False
                self.phase, self.phase_steps = "lift", 0
            elif self.phase_steps > 5:
                # Retry through a collision-safe overhead approach.
                self.carry_rotation = None
                self.pick_xyz = self._xyz(state, self.object)
                if self.object.startswith("obstruction"):
                    self.pick_xyz[2] += .3*self._get(state, self.object, "half_extent_z")
                if self.object != "target_block":
                    self.deferred.add(self.object)
                    self.phase, self.phase_steps = "retract", 0
                else:
                    self.goal_q = _HOME.copy()
                    self.phase, self.phase_steps = "target_home", 0
                return self._act_to(q, self.goal_q, 1.0)
            else:
                return self._act_to(q, q, -1.0)

        if self.phase == "lift":
            # At table height a simultaneous Cartesian move may be rejected by
            # collision checking. Joint 4 positive is a reliable vertical escape.
            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 14:
                action = self._act_to(q, q)
                if self.phase_steps % 2 == 0:
                    action[4] = -.05
                else:
                    region_y = self._xyz(state, "target_region")[1]
                    away = np.sign(self._xyz(state, held)[1] - region_y)
                    action[5] = -.04 * (away if away != 0 else 1)
                return action
            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 22:
                action = self._act_to(q, q)
                action[6] = .04
                return action
            if self._xyz(state, held)[2] < self.lift_start_z + .10 and self.phase_steps <= 29:
                action = self._act_to(q, q)
                action[4], action[6] = -.03, .03
                return action
            if self._xyz(state, held)[2] < self.lift_start_z + .06:
                self.deferred.add(self.object)
                self.abandoning = True
                self.phase, self.phase_steps = "release", 0
                return self._act_to(q, q, 1.0)
            self.transport_bx = self.destination[0]-.4559817 if self.destination[0] <= .3359817 else -.12
            self.transport_by = self.destination[1]
            self.phase, self.phase_steps = "base_transfer", 0

        if self.phase == "base_transfer":
            bxerr, byerr = self.transport_bx-self.base_x, self.transport_by-self.base_y
            if max(abs(bxerr), abs(byerr)) < .005 or self.phase_steps > 20:
                hover = self.destination.copy()
                hover[2] = max(.27, self.destination[2] + .16)
                self._set_goal_for_object_delta(state, hover)
                self.phase, self.phase_steps = "transfer", 0
            else:
                action = self._act_to(q, q)
                action[0], action[1] = np.clip(bxerr, -.2, .2), np.clip(byerr, -.2, .2)
                return action

        if self.phase == "transfer":
            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 40:
                # Short Cartesian-like descent segments avoid a joint-space
                # interpolation arc that can sweep the object into the table.
                self.descent_z = [self.destination[2]+d for d in (.142, .092, .052, .027, .007, 0)]
                self.descent_index = 0
                waypoint = self.destination.copy()
                waypoint[2] = self.descent_z[0]
                self._set_goal_for_object_delta(state, waypoint)
                self.phase, self.phase_steps = "lower", 0
            else:
                return self._act_to(q, self.goal_q)

        if self.phase == "lower":
            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 35:
                self.descent_index += 1
                if self.descent_index >= len(self.descent_z):
                    self.phase, self.phase_steps = "release", 0
                else:
                    waypoint = self.destination.copy()
                    waypoint[2] = self.descent_z[self.descent_index]
                    self._set_goal_for_object_delta(state, waypoint)
                    self.phase_steps = 0
                    return self._act_to(q, self.goal_q)
            else:
                return self._act_to(q, self.goal_q)

        if self.phase == "release":
            if held is None and self.phase_steps > 1:
                if self.object == "target_block":
                    # Keep open and let physics settle/termination register.
                    return self._act_to(q, q, 1.0)
                if not self.abandoning:
                    self.deferred.discard(self.object)
                self.phase, self.phase_steps = "retract", 0
                self.carry_rotation = None
            return self._act_to(q, q, 1.0)

        if self.phase == "retract":
            if self.phase_steps <= 5:
                action = self._act_to(q, q, 1.0)
                action[4] = -.12
                return action
            self.goal_q = _HOME.copy()
            self.phase, self.phase_steps = "home", 0

        if self.phase == "home":
            if np.max(np.abs(self.goal_q-q)) < .012 or self.phase_steps > 30:
                self.phase, self.phase_steps = "choose", 0
            else:
                return self._act_to(q, self.goal_q, 1.0)

        return self._act_to(q, q, 1.0)
