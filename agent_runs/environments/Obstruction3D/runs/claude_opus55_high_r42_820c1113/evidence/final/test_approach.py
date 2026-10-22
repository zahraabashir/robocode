import sys, time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
import os
OC=os.environ.get('OC')
def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed, options={'object_count': int(OC)} if OC else None)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0 = time.time(); ap.reset(obs, info); tc = 0
    for t in range(env.max_steps):
        t1 = time.time(); a = ap.get_action(obs); tc += time.time() - t1
        obs, r, te, tr, info = env.step(a)
        if verbose: print(t, ap.phase, ap.task['name'] if ap.task else None)
        if te: env.close(); return True, t + 1, tc, ap
        if tr: break
    env.close(); return False, env.max_steps, tc, ap
if __name__ == '__main__':
    seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
    for s in seeds:
        ok, n, tc, ap = run(s)
        print(f'seed {s}: success={ok} steps={n} compute={tc:.1f}s phase={ap.phase} task={ap.task["name"] if ap.task else None}', flush=True)
