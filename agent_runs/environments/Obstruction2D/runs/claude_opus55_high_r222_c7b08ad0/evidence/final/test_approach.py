import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor

OC=None
def run(seed):
    env = make_env()
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed, options=({'object_count':OC} if OC is not None else None))
    ap.reset(obs, info)
    tot = 0; t0 = time.time(); ct = 0
    for t in range(env.max_steps):
        tc=time.time(); a = ap.get_action(obs); ct += time.time()-tc
        obs, r, term, trunc, info2 = env.step(a)
        tot += r
        if term or trunc: break
    env.close()
    return seed, info.get('object_count'), term, t+1, round(time.time()-t0,1), round(ct,2)

if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    if len(sys.argv)>3: OC=int(sys.argv[3])
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(run, range(a, b)))
    for r in res:
        if not r[2] or len(res)<20 or r[5] > 6: print(r)
    print('max compute', max(r[5] for r in res)); print('success', sum(r[2] for r in res), '/', len(res), 'mean steps', np.mean([r[3] for r in res]))
