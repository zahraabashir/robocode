"""Probe the suspected 0.12 m arm mount offset using Kinova FK/IK."""

import numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation
from env_client import make_env

ORIGINS = [
    ([0, 0, .15643], [np.pi, 0, 0]), ([0, .005375, -.12838], [np.pi / 2, 0, 0]),
    ([0, -.21038, -.006375], [-np.pi / 2, 0, 0]), ([0, .006375, -.21038], [np.pi / 2, 0, 0]),
    ([0, -.20843, -.006375], [-np.pi / 2, 0, 0]), ([0, .00017505, -.10593], [np.pi / 2, 0, 0]),
    ([0, -.10593, -.00017505], [-np.pi / 2, 0, 0]),
]
Q0 = np.array([0, -.35, -np.pi, -2.5, 0, -.87, np.pi / 2])


def fk(q):
    transform = np.eye(4)
    for qi, (xyz, rpy) in zip(q, ORIGINS):
        fixed = np.eye(4)
        fixed[:3, :3] = Rotation.from_euler("xyz", rpy).as_matrix()
        fixed[:3, 3] = xyz
        joint = np.eye(4)
        joint[:3, :3] = Rotation.from_euler("z", qi).as_matrix()
        transform = transform @ fixed @ joint
    tool = np.eye(4)
    tool[:3, :3] = Rotation.from_euler("x", np.pi).as_matrix()
    tool[:3, 3] = [0, 0, -.061525]
    return transform @ tool


def get(state, obj, feature):
    return float(state.get(state.get_object_from_name(obj), feature))


def main():
    env = make_env()
    for mount_x in (0.12, 0.10, 0.14):
        for height in (.10, .125, .15):
            for offset in (.04, .08, .12):
                state, _ = env.reset(seed=0)
                target = np.array([get(state, "target_block", "pose_" + axis) for axis in "xyz"])
                target[2] = height
                desired = target - np.array([-0.12 + mount_x, 0, 0])
                def residual(q):
                    pose = fk(q)
                    grasp = pose[:3, 3] + offset * pose[:3, 2]
                    return np.r_[8 * (grasp - desired), pose[:2, 2], .08 * (q - Q0)]
                q = least_squares(residual, Q0, max_nfev=250).x
                for _ in range(20):
                    robot = state.get_object_from_name("robot")
                    cur = np.array([state.get(robot, "joint_" + str(i)) for i in range(1, 8)])
                    action = np.zeros(11, np.float32)
                    action[3:10] = np.clip(q - cur, -.2, .2)
                    action[10] = 1
                    state, _, _, _, _ = env.step(action)
                    if np.max(np.abs(q - cur)) < .01:
                        break
                action = np.zeros(11, np.float32); action[10] = -1
                state, _, _, _, _ = env.step(action)
                if get(state, "robot", "grasp_active"):
                    print("SUCCESS", mount_x, height, offset, q,
                          "held", [name for name in state.get_object_names()
                                   if name != "robot" and get(state, name, "grasp_active")],
                          "tf", [get(state, "robot", "grasp_tf_" + a) for a in "xyz"],
                          [get(state, "robot", "grasp_tf_q" + a) for a in "xyzw"],
                          "finger", get(state, "robot", "finger_state"))
                    env.close(); return
                print("miss", mount_x, height, offset)
    env.close()


if __name__ == "__main__":
    main()
