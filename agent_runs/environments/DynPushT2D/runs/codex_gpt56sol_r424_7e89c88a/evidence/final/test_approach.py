import argparse
import numpy as np
from env_client import make_env
from approach import GeneratedApproach


def run(seed, verbose=False, cap=None):
    env = make_env()
    obs, info = env.reset(seed=seed)
    policy = GeneratedApproach(env.action_space, env.observation_space, env.make_primitives())
    policy.reset(obs, info)
    initial = obs.copy()
    terminated = truncated = False
    steps = 0
    while not (terminated or truncated) and (cap is None or steps < cap):
        obs, reward, terminated, truncated, info = env.step(policy.get_action(obs))
        steps += 1
    poserr = float(np.linalg.norm(obs[:2] - obs[29:31]))
    angerr = abs(float((obs[2] - obs[31] + np.pi) % (2*np.pi) - np.pi))
    env.close()
    if verbose:
        print(seed, terminated, steps, "init", np.round(initial[[0,1,2,16,17,29,30,31]],3),
              "finalerr", round(poserr,3), round(angerr,3), flush=True)
    return terminated, steps, poserr, angerr


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("seeds", nargs="*", type=int, default=list(range(10)))
    ap.add_argument("--cap", type=int, default=None)
    args = ap.parse_args()
    results = [run(seed, True, args.cap) for seed in args.seeds]
    print("success", sum(x[0] for x in results), "/", len(results))
