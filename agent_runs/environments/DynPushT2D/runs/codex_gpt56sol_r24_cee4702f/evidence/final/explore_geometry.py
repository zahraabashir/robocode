"""Small black-box probes for DynPushT2D reset and contact dynamics."""
import argparse
import math

import numpy as np

from env_client import make_env


def resets(count):
    env = make_env()
    try:
        for seed in range(count):
            s, _ = env.reset(seed=seed)
            print(
                seed,
                "block", np.round(s[[0, 1, 2]], 4).tolist(),
                "robot", np.round(s[[16, 17]], 4).tolist(),
                "goal", np.round(s[[29, 30, 31]], 4).tolist(),
                "dims", np.round(s[[12, 13, 14, 28]], 4).tolist(),
            )
    finally:
        env.close()


def drive_to(env, state, target, max_steps=100):
    """Move robot toward a world point, stopping once close."""
    for _ in range(max_steps):
        delta = np.asarray(target) - state[16:18]
        if np.linalg.norm(delta) < 0.006:
            break
        # The server additionally enforces a Euclidean speed cap near 0.05.
        norm = np.linalg.norm(delta)
        action = delta * min(1.0, 0.049 / max(norm, 1e-12))
        state, _, done, trunc, _ = env.step(action)
        if done or trunc:
            break
    return state


def contact(seed, offset, push, push_steps=8):
    env = make_env()
    try:
        s, _ = env.reset(seed=seed)
        start = s.copy()
        target = s[0:2] + np.asarray(offset)
        s = drive_to(env, s, target)
        pre = s.copy()
        rows = []
        for k in range(push_steps):
            s, _, done, trunc, _ = env.step(np.asarray(push, dtype=float))
            rows.append((k + 1, *(s[0:3] - start[0:3]), *s[0:3], *s[16:18]))
            if done or trunc:
                break
        print("seed", seed, "offset", offset, "push", push)
        print("start", np.round(start[[0, 1, 2, 16, 17]], 4).tolist())
        print("pre", np.round(pre[[0, 1, 2, 16, 17]], 4).tolist())
        for row in rows:
            print(np.round(row, 5).tolist())
    finally:
        env.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("resets", "contact"))
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--offset", nargs=2, type=float, default=(-0.15, 0))
    parser.add_argument("--push", nargs=2, type=float, default=(0.05, 0))
    parser.add_argument("--steps", type=int, default=8)
    args = parser.parse_args()
    if args.mode == "resets":
        resets(args.count)
    else:
        contact(args.seed, args.offset, args.push, args.steps)
