import numpy as np
from env_client import make_env


def vals(s, name):
    o = s.get_object_from_name(name)
    out = {}
    for f in [
        "pos_base_x", "pos_base_y", "pos_base_rot",
        "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6", "joint_7",
        "finger_state", "grasp_active", "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
        "pose_x", "pose_y", "pose_z", "grasp_active", "half_extent_x", "half_extent_y", "half_extent_z",
    ]:
        try:
            out[f] = float(s.get(o, f))
        except Exception:
            pass
    return out


def diff(a, b):
    return {k: round(b[k] - v, 6) for k, v in a.items() if k in b and abs(b[k] - v) > 1e-8}


env = make_env()
print("spaces", env.action_space.shape, env.action_space.low, env.action_space.high, "max", env.max_steps)
for seed in [0, 1, 2]:
    s, info = env.reset(seed=seed)
    print("RESET", seed, s.get_object_names(), info)
    for n in s.get_object_names():
        print(n, vals(s, n))
env.close()

for idx in range(11):
    for mag in [-1.0, 1.0]:
        env = make_env()
        s, _ = env.reset(seed=0)
        before = {n: vals(s, n) for n in s.get_object_names()}
        a = np.zeros(11, dtype=np.float32); a[idx] = mag
        s, r, term, trunc, info = env.step(a)
        after = {n: vals(s, n) for n in s.get_object_names()}
        print("ACT", idx, mag, "rtt", r, term, trunc, "robot", diff(before["robot"], after["robot"]))
        moved = {n: diff(before[n], after[n]) for n in before if n != "robot"}
        print(" moved", {k:v for k,v in moved.items() if v})
        env.close()
