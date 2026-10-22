from env_client import make_env
from candidate_strategy import CandidateStrategy
import numpy as np
import sys


def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed)
    policy = CandidateStrategy(env.action_space, env.observation_space, env.make_primitives())
    policy.reset(obs, info)
    initial = obs.copy()
    for step in range(env.max_steps):
        action = policy.get_action(obs)
        try:
            obs, reward, term, trunc, info = env.step(action)
        except Exception:
            print("BAD ACTION", seed, step, action, action.dtype, policy.mode, policy.phase)
            raise
        if verbose and (step % 100 == 99 or term or trunc):
            ae = (obs[31] - obs[2] + np.pi) % (2*np.pi) - np.pi
            print(seed, step + 1, policy.mode, policy.phase, "block", np.round(obs[0:3], 2),
                  "robot", np.round(obs[16:18], 2), "poserr", round(float(np.linalg.norm(obs[29:31]-obs[0:2])), 3),
                  "angerr", round(float(ae), 3))
        if term or trunc:
            break
    env.close()
    ae = (obs[31] - obs[2] + np.pi) % (2*np.pi) - np.pi
    return term, step + 1, float(np.linalg.norm(obs[29:31]-obs[0:2])), abs(float(ae)), initial, obs


if __name__ == "__main__":
    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
    results = []
    for seed in seeds:
        result = run(seed, verbose=True)
        results.append(result)
        print("RESULT", seed, result[:4])
    print("SUMMARY", sum(r[0] for r in results), "/", len(results), "mean_steps", np.mean([r[1] for r in results]))
