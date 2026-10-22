"""Feedback controller for variable-count Obstruction2D."""
import math
import numpy as np


class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.types = {t.name: t for t in observation_space.types}

    def reset(self, state, info):
        rects = state.get_objects(self.types["rectangle"])
        target_name = state.get_objects(self.types["target_block"])[0].name
        target = state.get_object_from_name(target_name)
        obstacles = [o for o in rects if o.type.name == "rectangle" and state.get(o, "static") < 0.5]
        obstacles.sort(key=lambda o: -state.get(o, "height"))
        # Temporarily lift the target only when it crowds an obstacle's access.
        tx, tw = state.get(target, "x"), state.get(target, "width")
        crowded = any(abs(tx - state.get(o, "x")) <
                      0.5 * (tw + state.get(o, "width")) + 0.14 for o in obstacles)
        tasks = list(obstacles)
        if crowded:
            tasks.append(target)
        def top_y(o):
            angle = state.get(o, "theta")
            vertical_half = 0.5 * (abs(math.sin(angle)) * state.get(o, "width") +
                                   abs(math.cos(angle)) * state.get(o, "height"))
            return state.get(o, "y") + vertical_half
        tasks.sort(key=top_y, reverse=True)
        self.todo = [o.name for o in tasks]
        self.todo.append(target_name)  # retrieve it last for the actual placement
        surface = state.get_objects(self.types["target_surface"])[0]
        sx, sw = state.get(surface, "x"), state.get(surface, "width")
        # Greedily reserve floor-clear parking columns, preferring positions far
        # from both the pickup and goal.  The grid is count-independent.
        # Keep parking poses one base radius away from both side walls.
        candidates = [0.20 + 0.10 * k for k in range(12)]
        candidates.sort(key=lambda x: min(abs(x - tx) - tw / 2,
                                           abs(x - sx) - sw / 2), reverse=True)
        self.parking = {}
        used = []
        self.target_park = tx
        if crowded:
            self.target_park = candidates[0]
            used.append((self.target_park, tw))
        for o in obstacles:
            ow = state.get(o, "width")
            goal_clearance = sw / 2 + tw / 2 + ow / 2 + 0.03
            valid = [x for x in candidates
                     if abs(x - sx) > goal_clearance
                     and all(abs(x - px) > (ow + pw) / 2 + 0.12
                             for px, pw in used)]
            px = valid[0] if valid else candidates[len(used) % len(candidates)]
            self.parking[o.name] = px
            used.append((px, ow))
        self.final_index = len(self.todo) - 1
        xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
        self.initial_x = {n: state.get(state.get_object_from_name(n), "x")
                          for n in state.get_object_names()}
        self.park_base = max(xs) + 0.45
        robot = state.get_objects(self.types["crv_robot"])[0]
        self.safe_y = state.get(robot, "y")
        self.index, self.phase, self.retry = 0, "orient", 0
        self.stalled, self.last_robot_y = 0, None
        self.last_robot_x = None
        self.pick_y, self.attached, self.release_wait = 0.0, False, 0
        self.grasp_dx = 0.0

    @staticmethod
    def _clip(v, limit):
        return max(-limit, min(limit, v))

    def _action(self, dx=0.0, dy=0.0, dtheta=0.0, darm=0.0, vac=0.0):
        a = np.array([dx, dy, dtheta, darm, vac], dtype=np.float32)
        return np.clip(a, self.action_space.low, self.action_space.high).astype(np.float32)

    def get_action(self, state):
        robot = state.get_objects(self.types["crv_robot"])[0]
        surface = state.get_objects(self.types["target_surface"])[0]
        rx, ry = state.get(robot, "x"), state.get(robot, "y")
        theta = state.get(robot, "theta")
        if self.index >= len(self.todo):
            return self._action()
        obj = state.get_object_from_name(self.todo[self.index])
        is_target = self.index == self.final_index
        ox, oy = state.get(obj, "x"), state.get(obj, "y")
        width = state.get(obj, "width")

        if self.phase == "orient":
            err = (-math.pi / 2 - theta + math.pi) % (2 * math.pi) - math.pi
            if abs(err) < 0.025:
                self.phase = "rise"
            else:
                return self._action(dtheta=self._clip(err, 0.196))
        if self.phase == "rise":
            if ry >= self.safe_y - 0.004:
                self.phase = "align"
            else:
                return self._action(dy=min(0.05, self.safe_y - ry))
        if self.phase == "align":
            offsets = (0.0, -0.22, 0.22, -0.45, 0.45, -0.70, 0.70, -0.90, 0.90)
            tx = ox + offsets[min(self.retry, len(offsets) - 1)] * width
            if abs(tx - rx) < 0.004:
                self.phase, self.stalled = "descend", 0
                self.last_robot_y, self.pick_y = ry, oy
            else:
                if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
                    self.stalled += 1
                else:
                    self.stalled = 0
                self.last_robot_x = rx
                if self.stalled >= 3:
                    self.retry = min(len(offsets) - 1, self.retry + 1)
                    self.stalled = 0
                # Keep suction off in transit: a previously parked object may
                # touch the gripper as it passes underneath.
                return self._action(dx=self._clip(tx - rx, 0.05), vac=0.0)
        if self.phase == "descend":
            # A neighboring floating object can be pushed downward before the
            # vacuum acquires it.  Verify lift relative to the lowest observed
            # height, not merely its height at the start of the approach.
            self.pick_y = min(self.pick_y, oy)
            if self.last_robot_y is not None and abs(ry - self.last_robot_y) < 0.001:
                self.stalled += 1
            else:
                self.stalled = 0
            self.last_robot_y = ry
            if self.stalled >= 2 or ry < 0.18:
                self.phase = "lift"
            else:
                # Fine approach is essential: collision resolution rejects an
                # overshooting move wholesale, leaving the vacuum just off-contact.
                return self._action(dy=-0.01, vac=1.0)
        if self.phase == "lift":
            if oy > self.pick_y + 0.015:
                if not self.attached:
                    self.grasp_dx = ox - rx
                self.attached = True
            # A modest vertical park is enough to clear the ground while still
            # leaving room above it for a later verified re-grasp.
            park_y = 0.45 if (obj.type.name == "target_block" and not is_target) else 0.30
            parked_high_enough = (not is_target and self.attached and oy >= park_y)
            lift_limit = self.safe_y if is_target else 0.74
            if ry < lift_limit and not parked_high_enough:
                return self._action(dy=min(0.05, self.safe_y - ry), vac=1.0)
            if not self.attached:
                self.retry += 1
                if self.retry < 9:
                    self.phase = "align"
                    return self._action()
                if not is_target:
                    self.index += 1
                    self.retry = 0
                    self.phase = "rise"
                    return self._action()
                self.retry, self.phase = 0, "align"
                return self._action()
            self.phase = "carry"
            self.stalled, self.last_robot_x = 0, rx
        if self.phase == "carry":
            if is_target:
                desired_obj_x = state.get(surface, "x") + 0.008
            elif obj.type.name == "target_block":
                desired_obj_x = self.target_park
            else:
                desired_obj_x = self.parking[obj.name]
            tx = desired_obj_x - self.grasp_dx
            if abs(tx - rx) > 0.004:
                if self.last_robot_x is not None and abs(rx - self.last_robot_x) < 0.001:
                    self.stalled += 1
                else:
                    self.stalled = 0
                self.last_robot_x = rx
                if self.stalled >= 3 and not is_target:
                    self.phase = "release"
                else:
                    return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
            else:
                self.phase = "lower" if is_target else "release"
            self.stalled, self.last_robot_y = 0, ry
        if self.phase == "lower":
            if abs(ry - self.last_robot_y) < 0.001:
                self.stalled += 1
            else:
                self.stalled = 0
            self.last_robot_y = ry
            if self.stalled >= 3:
                self.phase = "release"
            else:
                return self._action(dy=-0.01, vac=1.0)
        if self.phase == "release":
            self.release_wait += 1
            if self.release_wait < 2:
                return self._action()
            self.phase = "retreat"
        if self.phase == "retreat":
            if ry < self.safe_y - 0.004:
                return self._action(dy=min(0.05, self.safe_y - ry))
            self.index += 1
            self.retry, self.attached, self.release_wait = 0, False, 0
            self.last_robot_x = None
            self.phase = "align" if self.index < len(self.todo) else "done"
            return self._action()
        return self._action()
