import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach


def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed)
    policy = GeneratedApproach(env.action_space, env.observation_space, {})
    policy.reset(obs, info)
    initial = obs.copy()
    old_mode = policy.mode
    for step in range(env.max_steps):
        obs, reward, term, trunc, info = env.step(policy.get_action(obs))
        if verbose and policy.mode != old_mode:
            print(' transition', step, old_mode, '->', policy.mode,
                  'nav', [np.round(x, 2).tolist() for x in policy.nav])
            old_mode = policy.mode
        if verbose and step % 10 == 0:
            print(' ', step, policy.mode, 'pose', np.round(obs[:3], 3),
                  'robot', np.round(obs[16:18], 3))
        if term or trunc:
            break
    env.close()
    pe = np.linalg.norm(obs[:2] - obs[29:31])
    ae = abs((obs[2] - obs[31] + np.pi) % (2*np.pi) - np.pi)
    print(seed, term, step + 1, 'err', round(float(pe), 3), round(float(ae), 3),
          'init', np.round(initial[[0,1,2,16,17,29,30,31]], 3))
    return term, step + 1


if __name__ == '__main__':
    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
    results = [run(s, verbose=len(seeds) == 1) for s in seeds]
    print('success', sum(x[0] for x in results), '/', len(results))
