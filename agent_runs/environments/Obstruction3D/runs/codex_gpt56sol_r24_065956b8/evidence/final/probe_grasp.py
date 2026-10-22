"""Focused black-box probes for Obstruction3D grasp mechanics."""

import numpy as np

from env_client import make_env


def read(state, obj, names):
    return {name: float(state.get(obj, name)) for name in names}


def snapshot(state):
    out = {}
    for name in state.get_object_names():
        obj = state.get_object_from_name(name)
        try:
            out[name] = read(state, obj, ["pose_x", "pose_y", "pose_z", "grasp_active"])
        except Exception:
            out[name] = read(state, obj, [
                "pos_base_x", "pos_base_y", "pos_base_rot",
                "joint_1", "joint_2", "joint_3", "joint_4", "joint_5",
                "joint_6", "joint_7", "finger_state", "grasp_active",
                "grasp_tf_x", "grasp_tf_y", "grasp_tf_z",
            ])
    return out


def main():
    env = make_env()
    state, info = env.reset(seed=0)
    print("max_steps", env.max_steps, "info", info)
    print(snapshot(state))
    for label, action in [
        ("close", [0] * 10 + [-1]),
        ("open", [0] * 10 + [1]),
        ("all_joint_plus", [0, 0, 0] + [0.2] * 7 + [0]),
        ("all_joint_minus", [0, 0, 0] + [-0.2] * 7 + [0]),
        ("base_plus", [0.2, 0.2, 0.2] + [0] * 8),
    ]:
        state, reward, term, trunc, info = env.step(np.asarray(action, dtype=np.float32))
        print(label, reward, term, trunc, info, snapshot(state))
    env.close()


def random_search(seed=0, steps=1000):
    """Look for any attachment while broadly random-walking configuration."""
    rng = np.random.default_rng(seed + 991)
    env = make_env()
    state, _ = env.reset(seed=seed)
    initial = snapshot(state)
    print("seed", seed, "objects", initial)
    last_positions = {k: (v.get("pose_x"), v.get("pose_y"), v.get("pose_z"))
                      for k, v in initial.items() if "pose_x" in v}
    for t in range(steps):
        action = np.zeros(11, dtype=np.float32)
        # Persistent random motion explores configurations better than white noise.
        action[:10] = rng.choice([-0.2, 0.0, 0.2], size=10, p=[0.3, 0.4, 0.3])
        action[10] = -1.0
        state, reward, term, trunc, info = env.step(action)
        snap = snapshot(state)
        moved = []
        for k, old in last_positions.items():
            new = tuple(snap[k].get(x) for x in ("pose_x", "pose_y", "pose_z"))
            if max(abs(a - b) for a, b in zip(old, new)) > 1e-5:
                moved.append((k, old, new))
            last_positions[k] = new
        if moved or snap["robot"]["grasp_active"]:
            print("EVENT", t, "a", action.tolist(), "moved", moved,
                  "robot", snap["robot"])
        if snap["robot"]["grasp_active"] or term or trunc:
            print("END", t, reward, term, trunc, snap)
            break
    env.close()


def joint_grid(seed=0):
    """Sweep the main pitch joints with the base y-aligned to the target."""
    env = make_env()
    state, _ = env.reset(seed=seed)
    snap = snapshot(state)
    target_y = snap["target_block"]["pose_y"]
    action = np.zeros(11, dtype=np.float32)
    action[1] = np.clip(target_y - snap["robot"]["pos_base_y"], -0.2, 0.2)
    state, *_ = env.step(action)
    base_j2 = snapshot(state)["robot"]["joint_2"]
    base_j4 = snapshot(state)["robot"]["joint_4"]
    old_xyz = tuple(snapshot(state)["target_block"]["pose_" + c] for c in "xyz")
    j2s = [base_j2 + 0.2 * k for k in range(-6, 7)]
    j4s = [base_j4 + 0.2 * k for k in range(-6, 7)]
    for row, wanted_j2 in enumerate(j2s):
        for wanted_j4 in (j4s if row % 2 == 0 else list(reversed(j4s))):
            now = snapshot(state)["robot"]
            action = np.zeros(11, dtype=np.float32)
            action[4] = np.clip(wanted_j2 - now["joint_2"], -0.2, 0.2)
            action[6] = np.clip(wanted_j4 - now["joint_4"], -0.2, 0.2)
            action[10] = 1.0
            state, *_ = env.step(action)
            close = np.zeros(11, dtype=np.float32)
            close[10] = -1.0
            state, reward, term, trunc, _ = env.step(close)
            ss = snapshot(state)
            xyz = tuple(ss["target_block"]["pose_" + c] for c in "xyz")
            moved = max(abs(a - b) for a, b in zip(xyz, old_xyz))
            if moved > 1e-6 or ss["robot"]["grasp_active"]:
                print("EVENT", wanted_j2, wanted_j4, "xyz", xyz, "moved", moved,
                      "robot", ss["robot"], "done", term, trunc)
            old_xyz = xyz
            if ss["robot"]["grasp_active"] or term or trunc:
                env.close()
                return
    print("grid found no grasp")
    env.close()


def triple_grid(seed=0):
    """Sweep shoulder, elbow, and wrist pitch at target-aligned base y."""
    env = make_env()
    state, _ = env.reset(seed=seed)
    initial = snapshot(state)
    action = np.zeros(11, dtype=np.float32)
    action[1] = np.clip(initial["target_block"]["pose_y"], -0.2, 0.2)
    state, *_ = env.step(action)
    home = snapshot(state)["robot"]
    vals2 = [home["joint_2"] + 0.2 * k for k in range(-6, 7)]
    vals4 = [home["joint_4"] + 0.2 * k for k in range(-6, 7)]
    vals6 = [home["joint_6"] + 0.2 * k for k in range(-6, 7)]
    # First walk to the low corner (joint deltas are capped at 0.2).
    for _ in range(6):
        action = np.zeros(11, dtype=np.float32)
        action[[4, 6, 8]] = -0.2
        action[10] = -1.0
        state, *_ = env.step(action)
    for i, wanted2 in enumerate(vals2):
        order4 = vals4 if i % 2 == 0 else list(reversed(vals4))
        for j, wanted4 in enumerate(order4):
            order6 = vals6 if (i + j) % 2 == 0 else list(reversed(vals6))
            for wanted6 in order6:
                now = snapshot(state)["robot"]
                action = np.zeros(11, dtype=np.float32)
                action[4] = np.clip(wanted2 - now["joint_2"], -0.2, 0.2)
                action[6] = np.clip(wanted4 - now["joint_4"], -0.2, 0.2)
                action[8] = np.clip(wanted6 - now["joint_6"], -0.2, 0.2)
                action[10] = -1.0
                state, reward, term, trunc, _ = env.step(action)
                ss = snapshot(state)
                moved = []
                for name, old in initial.items():
                    if "pose_x" not in old:
                        continue
                    d = max(abs(ss[name]["pose_" + c] - old["pose_" + c]) for c in "xyz")
                    if d > 1e-5:
                        moved.append((name, d, tuple(ss[name]["pose_" + c] for c in "xyz")))
                if moved or ss["robot"]["grasp_active"]:
                    print("TRIPLE EVENT", wanted2, wanted4, wanted6,
                          "moved", moved, "robot", ss["robot"], "done", term, trunc)
                if ss["robot"]["grasp_active"] or term or trunc:
                    env.close()
                    return
    print("triple grid found no grasp")
    env.close()


def exact_sequence(seed=0):
    """Reproduce the discovered grasp, translate it, and test release."""
    env = make_env()
    state, _ = env.reset(seed=seed)
    ss = snapshot(state)
    block0 = tuple(ss["target_block"]["pose_" + c] for c in "xyz")
    region = tuple(ss["target_region"]["pose_" + c] for c in "xyz")
    print("INITIAL block", block0, "region", region)
    # Exact relative sequence from home: y-align and open while moving to the
    # successful q2/q4/q6 configuration, respecting +/-0.2 action limits.
    actions = []
    for k in range(3):
        a = np.zeros(11, dtype=np.float32)
        # Predicted current values are enough while constructing this fixed
        # sequence: x needs at most one move, y may need two bounded moves.
        if k == 0:
            a[0] = np.clip(block0[0] - 0.33598166704177856, -0.2, 0.0)
        if k < 2:
            a[1] = np.clip(block0[1] - (0.0 if k == 0 else np.clip(block0[1], -0.2, 0.2)), -0.2, 0.2)
        a[4] = 0.2
        a[6] = 0.2 if k == 0 else 0.0
        a[8] = 0.2 if k < 2 else 0.0
        a[10] = 1.0
        actions.append(("pose_open", a))
    far_extra = np.clip(
        (block0[0] - 0.33598166704177856) /
        (0.4644085764884949 - 0.33598166704177856) * 0.2,
        0.0, 0.2)
    if far_extra > 1e-6:
        a = np.zeros(11, dtype=np.float32)
        a[[4, 6, 8]] = far_extra
        a[10] = 1.0
        actions.append(("far_reach", a))
    close = np.zeros(11, dtype=np.float32)
    close[10] = -1.0
    actions.append(("close", close))
    for _ in range(4):
        lift = np.zeros(11, dtype=np.float32)
        lift[4] = -0.1
        actions.append(("lift_q2", lift))
    carry = np.zeros(11, dtype=np.float32)
    carry[0] = np.clip(region[0] - block0[0], -0.2, 0.2)
    carry[1] = np.clip(region[1] - block0[1], -0.2, 0.2)
    actions.append(("carry", carry))
    for _ in range(4):
        lower = np.zeros(11, dtype=np.float32)
        lower[4] = 0.1
        actions.append(("lower_q2", lower))
    release = np.zeros(11, dtype=np.float32)
    release[10] = 1.0
    actions.append(("release", release))
    for k, (label, action) in enumerate(actions, 1):
        state, reward, term, trunc, _ = env.step(action)
        ss = snapshot(state)
        held = [name for name, data in ss.items()
                if name != "robot" and data.get("grasp_active", 0) > 0.5]
        print(k, label, "a", action.tolist(), "robot", ss["robot"],
              "block", ss["target_block"], "held", held,
              "reward/done", reward, term, trunc)
        if term or trunc:
            break
    env.close()


def perturb_grasp(seed=0):
    """Measure one-step carried-object deltas about the successful grasp."""
    for index in range(10):
        for amount in (-0.1, 0.1):
            env = make_env()
            state, _ = env.reset(seed=seed)
            ss = snapshot(state)
            block0 = tuple(ss["target_block"]["pose_" + c] for c in "xyz")
            # Reach exact successful pose in three bounded moves.
            for k in range(3):
                a = np.zeros(11, dtype=np.float32)
                if k == 0:
                    a[1] = np.clip(block0[1], -0.2, 0.2)
                a[4] = 0.2
                a[6] = 0.2 if k == 0 else 0.0
                a[8] = 0.2 if k < 2 else 0.0
                state, *_ = env.step(a)
            a = np.zeros(11, dtype=np.float32)
            a[10] = -1.0
            state, *_ = env.step(a)
            before = snapshot(state)
            a = np.zeros(11, dtype=np.float32)
            a[index] = amount
            state, reward, term, trunc, _ = env.step(a)
            after = snapshot(state)
            delta = tuple(after["target_block"]["pose_" + c] -
                          before["target_block"]["pose_" + c] for c in "xyz")
            print("PERTURB", index, amount, "delta", delta,
                  "still_held", after["robot"]["grasp_active"],
                  "robot", after["robot"], "done", term, trunc)
            env.close()


def grasp_named(seed=0, name="obstruction0"):
    """Try the calibrated table-height grasp on an arbitrary cuboid."""
    env = make_env()
    state, _ = env.reset(seed=seed)
    ss = snapshot(state)
    xyz = tuple(ss[name]["pose_" + c] for c in "xyz")
    desired_bx = xyz[0] - 0.45598166435956955
    for k in range(3):
        now = snapshot(state)["robot"]
        a = np.zeros(11, dtype=np.float32)
        a[0] = np.clip(desired_bx - now["pos_base_x"], -0.2, 0.0)
        a[1] = np.clip(xyz[1] - now["pos_base_y"], -0.2, 0.2)
        a[4] = 0.2
        a[6] = 0.2 if k == 0 else 0.0
        a[8] = 0.2 if k < 2 else 0.0
        a[10] = 1.0
        state, *_ = env.step(a)
    a = np.zeros(11, dtype=np.float32)
    a[10] = -1.0
    state, reward, term, trunc, _ = env.step(a)
    ss = snapshot(state)
    print("NAMED", seed, name, "xyz", xyz, "robot", ss["robot"],
          "held", [n for n, d in ss.items() if n != "robot" and d.get("grasp_active", 0) > .5],
          "done", reward, term, trunc)
    env.close()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", action="store_true")
    parser.add_argument("--grid", action="store_true")
    parser.add_argument("--triple", action="store_true")
    parser.add_argument("--exact", action="store_true")
    parser.add_argument("--perturb", action="store_true")
    parser.add_argument("--object", default="obstruction0")
    parser.add_argument("--named", action="store_true")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    grasp_named(args.seed, args.object) if args.named else (perturb_grasp(args.seed) if args.perturb else (exact_sequence(args.seed) if args.exact else (triple_grid(args.seed) if args.triple else (joint_grid(args.seed) if args.grid else (random_search(args.seed) if args.random else main())))))
