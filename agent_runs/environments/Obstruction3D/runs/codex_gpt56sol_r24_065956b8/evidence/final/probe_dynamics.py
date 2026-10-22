"""Small black-box probes for Obstruction3DEnv dynamics."""

import numpy as np

from env_client import make_env


ROBOT_FEATURES = (
    "pos_base_x", "pos_base_y", "pos_base_rot",
    "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7",
    "finger_state", "grasp_active",
    "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
    "grasp_tf_qx", "grasp_tf_qy", "grasp_tf_qz", "grasp_tf_qw",
)


def robot_values(state):
    robot = state.get_object_from_name("robot")
    return np.array([state.get(robot, f) for f in ROBOT_FEATURES], dtype=float)


def main():
    env = make_env()
    state, info = env.reset(seed=0)
    print("names", state.get_object_names())
    for name in state.get_object_names():
        obj = state.get_object_from_name(name)
        print("object", name, "type", getattr(obj, "type", None), "repr", repr(obj))
    print("robot baseline", dict(zip(ROBOT_FEATURES, robot_values(state))))
    cuboid_features = (
        "pose_x", "pose_y", "pose_z", "pose_qx", "pose_qy", "pose_qz", "pose_qw",
        "grasp_active", "object_type", "half_extent_x", "half_extent_y", "half_extent_z",
    )
    for name in sorted(n for n in state.get_object_names() if n != "robot"):
        obj = state.get_object_from_name(name)
        print("cuboid", name, {f: state.get(obj, f) for f in cuboid_features})
    env.close()

    # Independent one-step effects from exactly the same initial state.
    for action_i in range(11):
        env = make_env()
        before, _ = env.reset(seed=0)
        b = robot_values(before)
        action = np.zeros(11, dtype=np.float32)
        action[action_i] = 0.2 if action_i < 10 else 1.0
        after, reward, terminated, truncated, _ = env.step(action)
        a = robot_values(after)
        changed = {
            feature: round(float(delta), 7)
            for feature, delta in zip(ROBOT_FEATURES, a - b)
            if abs(delta) > 1e-7
        }
        print("one_step", action_i, "changed", changed,
              "reward/done", reward, terminated, truncated)
        env.close()

    env = make_env()
    for label, action_i, magnitude in (
        ("base_x_negative", 0, -0.2),
        ("base_y_negative", 1, -0.2),
        ("base_rot_negative", 2, -0.2),
        ("close", 10, -1.0),
    ):
        before, _ = env.reset(seed=0)
        b = robot_values(before)
        action = np.zeros(11, dtype=np.float32)
        action[action_i] = magnitude
        after, reward, terminated, truncated, _ = env.step(action)
        a = robot_values(after)
        changed = {
            feature: round(float(delta), 7)
            for feature, delta in zip(ROBOT_FEATURES, a - b)
            if abs(delta) > 1e-7
        }
        print(label, changed, "robot", dict(zip(ROBOT_FEATURES, a)))
        for name in sorted(n for n in after.get_object_names() if n != "robot"):
            obj = after.get_object_from_name(name)
            if after.get(obj, "grasp_active"):
                print("grasped", name)
    env.close()

    # Cumulative response and any action clipping / rate effects.
    for action_i in range(10):
        env = make_env()
        state, _ = env.reset(seed=0)
        b = robot_values(state)
        action = np.zeros(11, dtype=np.float32)
        action[action_i] = 0.2
        for _ in range(5):
            state, _, _, _, _ = env.step(action)
        delta = robot_values(state) - b
        changed = {
            feature: round(float(d), 6)
            for feature, d in zip(ROBOT_FEATURES, delta)
            if abs(d) > 1e-7
        }
        print("five_step", action_i, changed)
        env.close()


if __name__ == "__main__":
    main()
