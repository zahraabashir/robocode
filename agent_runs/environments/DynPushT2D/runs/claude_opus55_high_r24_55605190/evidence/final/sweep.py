import sys, json, numpy as np
from env_client import make_env
import approach
from concurrent.futures import ThreadPoolExecutor
cfg=json.loads(sys.argv[1]); a,b=int(sys.argv[2]),int(sys.argv[3])
for k,v in cfg.items(): setattr(approach.GeneratedApproach,k,v)
def run(seed):
    env=make_env(); ap=approach.GeneratedApproach(None,None,{})
    obs,info=env.reset(seed=seed); ap.reset(obs,info)
    for t in range(1000):
        obs,r,te,tr,_=env.step(ap.get_action(obs))
        if te: break
    env.close(); return t+1, te
with ThreadPoolExecutor(6) as ex: res=list(ex.map(run, range(a,b)))
print(sys.argv[1], 'mean', np.mean([r[0] for r in res]), 'succ', sum(r[1] for r in res), '/', len(res))
