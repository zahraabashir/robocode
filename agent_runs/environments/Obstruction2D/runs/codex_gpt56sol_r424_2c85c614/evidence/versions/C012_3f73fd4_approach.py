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
        self.todo = ([target_name] if crowded else []) + [o.name for o in obstacles]
        self.todo.append(target_name)  # retrieve it last for the actual placement
        self.final_index = len(self.todo) - 1
        xs = [state.get(state.get_object_from_name(n), "x") for n in state.get_object_names()]
        self.initial_x = {n: state.get(state.get_object_from_name(n), "x")
                          for n in state.get_object_names()}
        self.park_base = max(xs) + 0.45
        robot = state.get_objects(self.types["crv_robot"])[0]
        self.safe_y = state.get(robot, "y")
        self.index, self.phase, self.retry = 0, "orient", 0
        self.stalled, self.last_robot_y = 0, None
        self.pick_y, self.attached, self.release_wait = 0.0, False, 0

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
            offsets = (0.0, -0.22, 0.22, -0.38, 0.38)
            tx = ox + offsets[min(self.retry, 4)] * width
            if abs(tx - rx) < 0.004:
                self.phase, self.stalled = "descend", 0
                self.last_robot_y, self.pick_y = ry, oy
            else:
                # Keep suction off in transit: a previously parked object may
                # touch the gripper as it passes underneath.
                return self._action(dx=self._clip(tx - rx, 0.05), vac=0.0)
        if self.phase == "descend":
            if self.last_robot_y is not None and abs(ry - self.last_robot_y) < 0.001:
                self.stalled += 1
            else:
                self.stalled = 0
            self.last_robot_y = ry
            if self.stalled >= 2 or ry < 0.18:
                self.phase = "lift"
            else:
                return self._action(dy=-0.05, vac=1.0)
        if self.phase == "lift":
            if oy > self.pick_y + 0.015:
                self.attached = True
            # A modest vertical park is enough to clear the ground while still
            # leaving room above it for a later verified re-grasp.
            parked_high_enough = (not is_target and self.attached and oy >= 0.35)
            if ry < 0.79 and not parked_high_enough:
                return self._action(dy=0.05, vac=1.0)
            if not self.attached:
                self.retry += 1
                if self.retry < 5:
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
        if self.phase == "carry":
            if is_target:
                tx = state.get(surface, "x")
            elif obj.type.name == "target_block":
                tx = ox
            else:
                sx = state.get(surface, "x")
                origin_x = self.initial_x[obj.name]
                direction = 1.0 if origin_x >= sx else -1.0
                tx = origin_x + direction * (0.25 + 0.08 * self.index)
                # Empirically the circular base center is constrained here.
                tx = max(0.11, min(1.39, tx))
            if abs(tx - rx) > 0.004:
                return self._action(dx=self._clip(tx - rx, 0.05), vac=1.0)
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
                return self._action(dy=-0.05, vac=1.0)
        if self.phase == "release":
            self.release_wait += 1
            if self.release_wait < 2:
                return self._action()
            self.phase = "retreat"
        if self.phase == "retreat":
            if ry < self.safe_y - 0.004:
                return self._action(dy=0.05)
            self.index += 1
            self.retry, self.attached, self.release_wait = 0, False, 0
            self.phase = "align" if self.index < len(self.todo) else "done"
            return self._action()
        return self._action()
