import sys, time, math
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor

def run(seed):
    env = make_env()
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    import os, json
    for k_,v_ in json.loads(os.environ.get('PARAMS','{}')).items(): setattr(ap,k_,v_)
    ap.reset(obs, info)
    t0=time.time()
    for t in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        if term:
            env.close(); return seed, True, t+1, time.time()-t0, None
    e = (obs[29]-obs[0], obs[30]-obs[1], math.degrees((obs[31]-obs[2]+math.pi)%(2*math.pi)-math.pi), obs[2], obs[31])
    env.close()
    return seed, False, env.max_steps, time.time()-t0, e

seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else range(20)
with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(run, seeds))
for r in res:
    print(r if not r[1] else r[:4])
print('success', sum(r[1] for r in res), '/', len(res), 'mean steps', np.mean([r[2] for r in res]))
