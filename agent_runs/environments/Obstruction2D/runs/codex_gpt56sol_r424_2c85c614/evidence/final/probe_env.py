"""Small black-box probes; never imported by approach.py."""

import argparse
import numpy as np
from env_client import make_env


def dump(state):
    for name in sorted(state.get_object_names()):
        obj = state.get_object_from_name(name)
        fs = state.type_features[obj.type]
        vals = [state.get(obj, f) for f in fs]
        print(name, obj.type.name, dict(zip(fs, np.round(vals, 4))))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--steps", type=int, default=0)
    args = ap.parse_args()
    env = make_env()
    obs, info = env.reset(seed=args.seed)
    print("max_steps", env.max_steps, "info", info)
    dump(obs)
    for i in range(args.steps):
        obs, rew, term, trunc, info = env.step(np.array([0, 0, 0, 0, 1], np.float32))
        print("step", i + 1, rew, term, trunc)
        dump(obs)
    env.close()
