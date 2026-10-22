import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed)
    t0=time.time()
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    tplan=time.time()-t0
    steps=0
    for k in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, te, tr, info = env.step(a)
        steps+=1
        if te or tr: break
    env.close()
    return dict(seed=seed, n=info.get('object_count'), steps=steps, term=te, plan=round(ap.plan_cost,1), tplan=round(tplan,2), ttot=round(time.time()-t0,1))
if __name__=='__main__':
    seeds = [int(x) for x in sys.argv[1:]] or list(range(5))
    for s in seeds:
        print(run(s), flush=True)
