import sys, time
from env_client import make_env
import numpy as np
import os, importlib as _il
GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
OC=None
def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0=time.time(); ap.reset(obs, info)
    n = len(obs.get_object_names())-3
    for t in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        if term: env.close(); return True, t+1, n, time.time()-t0
        if trunc: break
    env.close(); return False, t+1, n, time.time()-t0
if __name__ == '__main__':
    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
    if len(sys.argv) > 3:
        OC = int(sys.argv[3])
    from concurrent.futures import ProcessPoolExecutor as ThreadPoolExecutor
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(run, seeds))
    for s, r in zip(seeds, res):
        if not r[0] or r[3] > 20: print(s, r)
    print('success', sum(r[0] for r in res), '/', len(res), 'mean steps', np.mean([r[1] for r in res if r[0]]), 'max time', max(r[3] for r in res))
