"""Small black-box probes for the Rovers environment (never imported by approach.py)."""

import argparse
import math

import numpy as np

from env_client import make_env


CENTERS = [-5 / 6, -1 / 2, -1 / 6, 1 / 6, 1 / 2, 5 / 6]


def objects(state, env, type_name):
    return state.get_objects(env.observation_space.get_type(type_name))


def row(state, obj):
    return obj.name, tuple(round(float(x), 3) for x in state.data[obj])


def changed(before, after):
    out = []
    for name in sorted(before.get_object_names()):
        a = before.get_object_from_name(name)
        b = after.get_object_from_name(name)
        if not np.array_equal(before.data[a], after.data[b]):
            out.append((name, row(before, a)[1], row(after, b)[1]))
    return out


def action(r0=(0, 0, 0, 0), r1=(0, 0, 0, 0)):
    return np.asarray((*r0, *r1), dtype=np.float32)


def dump(seed):
    env = make_env()
    state, info = env.reset(seed=seed)
    print("seed", seed, "info", info, "max_steps", env.max_steps)
    for typ in ("rover", "lander", "objective", "sample", "obstacle"):
        print(typ, *[row(state, o) for o in objects(state, env, typ)], sep="\n  ")
    env.close()


def selector(seed):
    for value in CENTERS:
        env = make_env()
        state, _ = env.reset(seed=seed)
        nxt, rew, term, trunc, info = env.step(action((0, 0, 0, value)))
        print(value, "reward", rew, "done", term, trunc, "changed", changed(state, nxt), "info", info)
        env.close()


def drive_and_operate(seed, rover_index, target_name, op_value, stop=0.12):
    """Greedily drive one rover directly to an object, then apply an operator."""
    env = make_env()
    state, _ = env.reset(seed=seed)
    rover_name = f"rover{rover_index}"
    steps = 0
    while steps < 100:
        r = state.get_object_from_name(rover_name)
        t = state.get_object_from_name(target_name)
        dx = state.get(t, "x") - state.get(r, "x")
        dy = state.get(t, "y") - state.get(r, "y")
        dist = math.hypot(dx, dy)
        if dist <= stop:
            break
        scale = min(1.0, max(0.0, (dist - stop) / max(abs(dx), abs(dy), 1e-9)))
        cmd = (max(-.2, min(.2, dx * scale)), max(-.2, min(.2, dy * scale)), 0, CENTERS[3])
        a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
        nxt, _, term, trunc, _ = env.step(a)
        if not changed(state, nxt):
            print("stuck", rover_name, "at", row(state, r), "toward", row(state, t), "dist", dist)
            break
        state = nxt
        steps += 1
    before = state
    cmd = (0, 0, 0, op_value)
    a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
    state, rew, term, trunc, info = env.step(a)
    print("steps", steps, "operator", op_value, "changed", changed(before, state), "done", term, trunc, "info", info)
    env.close()


def move(env, state, rover_index, tx, ty, stop=0.12, limit=100):
    rover_name = f"rover{rover_index}"
    for n in range(limit):
        r = state.get_object_from_name(rover_name)
        dx, dy = tx - state.get(r, "x"), ty - state.get(r, "y")
        dist = math.hypot(dx, dy)
        if dist <= stop:
            return state, n, False
        scale = min(1.0, max(0.0, (dist - stop) / max(abs(dx), abs(dy), 1e-9)))
        cmd = (max(-.2, min(.2, dx * scale)), max(-.2, min(.2, dy * scale)), 0, CENTERS[3])
        a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
        nxt, _, _, _, _ = env.step(a)
        oldr, newr = state.get_object_from_name(rover_name), nxt.get_object_from_name(rover_name)
        stuck = (state.get(oldr, "x") == nxt.get(newr, "x") and state.get(oldr, "y") == nxt.get(newr, "y"))
        state = nxt
        if stuck:
            return state, n + 1, True
    return state, limit, True


def op(env, state, rover_index, op_index, motion=(0, 0, 0)):
    cmd = (*motion, CENTERS[op_index])
    a = action(cmd, (0, 0, 0, CENTERS[3])) if rover_index == 0 else action((0, 0, 0, CENTERS[3]), cmd)
    nxt, rew, term, trunc, info = env.step(a)
    print("op", op_index, "r", rover_index, "motion", motion, "changed", changed(state, nxt), "done", term, trunc)
    return nxt


def scenario(seed):
    env = make_env()
    state, _ = env.reset(seed=seed)
    # Seed 0 has a conveniently accessible soil sample near rover1.
    sample = state.get_object_from_name("sample4")
    state, n, stuck = move(env, state, 1, state.get(sample, "x"), state.get(sample, "y"))
    print("move to sample", n, stuck)
    state = op(env, state, 1, 0)
    state = op(env, state, 1, 4)
    state = op(env, state, 1, 5)
    # Approach an objective until its mound rejects further motion.
    objective = state.get_object_from_name("objective2")
    state, n, stuck = move(env, state, 1, state.get(objective, "x"), state.get(objective, "y"))
    print("move to objective", n, stuck)
    state = op(env, state, 1, 2)  # image without calibration: refused
    state = op(env, state, 1, 1)
    state = op(env, state, 1, 2)
    state = op(env, state, 1, 2)  # calibration was spent: refused
    state = op(env, state, 1, 4)  # expected out of lander range / occluded
    env.close()


def home_probe(seed):
    env = make_env()
    state, _ = env.reset(seed=seed)
    # Walk rover0 away in 0.1m increments, then back, displaying at_home.
    for dx in (0.1, 0.1, 0.1, -0.1, -0.1, -0.1):
        before = state
        state, _, term, trunc, _ = env.step(action((dx, 0, 0, CENTERS[3]), (0, 0, 0, CENTERS[3])))
        r = state.get_object_from_name("rover0")
        print("dx", dx, "xy", state.get(r, "x"), state.get(r, "y"), "home", state.get(r, "at_home"), "done", term, trunc,
              "delta", changed(before, state))
    env.close()


def simultaneous_probe(seed):
    env = make_env()
    state, _ = env.reset(seed=seed)
    # Initial rovers are two metres apart. Drive both toward x=0 concurrently.
    for n in range(6):
        before = state
        state, _, _, _, _ = env.step(action((-.2, 0, 0, CENTERS[3]), (.2, 0, 0, CENTERS[3])))
        print("step", n, changed(before, state))
    env.close()


def count_probe(start, count):
    for seed in range(start, start + count):
        env = make_env()
        _, info = env.reset(seed=seed)
        print(seed, info.get("object_count"))
        env.close()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["dump", "selector", "operate", "scenario", "home", "simultaneous", "counts"])
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--rover", type=int, default=0)
    p.add_argument("--target", default="sample0")
    p.add_argument("--op", type=float, default=CENTERS[0])
    args = p.parse_args()
    if args.mode == "dump":
        dump(args.seed)
    elif args.mode == "selector":
        selector(args.seed)
    elif args.mode == "operate":
        drive_and_operate(args.seed, args.rover, args.target, args.op)
    elif args.mode == "scenario":
        scenario(args.seed)
    elif args.mode == "home":
        home_probe(args.seed)
    elif args.mode == "simultaneous":
        simultaneous_probe(args.seed)
    else:
        count_probe(args.seed, 20)
