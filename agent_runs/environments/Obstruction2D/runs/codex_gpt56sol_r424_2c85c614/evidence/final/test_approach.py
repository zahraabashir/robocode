"""Evaluate the current policy against fresh live instances."""

import argparse
import time
from collections import Counter
from env_client import make_env
from approach import GeneratedApproach


def run(seed, verbose=False, object_count=None):
    env = make_env()
    options = {"object_count": object_count} if object_count is not None else None
    state, info = env.reset(seed=seed, options=options)
    approach = GeneratedApproach(env.action_space, env.observation_space, {})
    approach.reset(state, info)
    t0 = time.monotonic()
    term = trunc = False
    steps = 0
    try:
        while not (term or trunc) and steps < env.max_steps:
            action = approach.get_action(state)
            state, reward, term, trunc, info = env.step(action)
            steps += 1
            if verbose and (steps < 10 or steps % 25 == 0 or term):
                r = state.get_objects(env.observation_space.get_type("crv_robot"))[0]
                b = state.get_objects(env.observation_space.get_type("target_block"))[0]
                print(steps, action.round(3), "r", round(state.get(r,"x"),3), round(state.get(r,"y"),3), round(state.get(r,"theta"),3), round(state.get(r,"arm_joint"),3), round(state.get(r,"vacuum"),1), "b", round(state.get(b,"x"),3), round(state.get(b,"y"),3))
    finally:
        env.close()
    return term, steps, info.get("object_count"), time.monotonic() - t0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--count", type=int, default=None)
    args = ap.parse_args()
    results = []
    for seed in range(args.start, args.start + args.n):
        result = run(seed, args.verbose, args.count)
        results.append(result)
        print(seed, result)
    print("success", sum(r[0] for r in results), "/", len(results), "by_count", Counter((r[2], r[0]) for r in results))
