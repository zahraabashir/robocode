import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor
def run(seed):
    env=make_env(); ap=GeneratedApproach(None,None,{})
    obs,info=env.reset(seed=seed); ap.reset(obs,info)
    nav=push=npl=0
    for t in range(1000):
        if not ap.plan: npl+=1
        a=ap.get_action(obs)
        kind = ap._lastkind if hasattr(ap,'_lastkind') else None
        obs,r,te,tr,_=env.step(a)
        if te: break
    env.close()
    return seed,t+1,npl
with ThreadPoolExecutor(8) as ex: res=list(ex.map(run, range(int(sys.argv[1]),int(sys.argv[2]))))
for r in res: print(*r)
print(np.mean([r[1] for r in res]), np.mean([r[2] for r in res]))
