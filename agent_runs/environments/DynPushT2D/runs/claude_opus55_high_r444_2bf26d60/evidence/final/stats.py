import sys, numpy as np
from env_client import make_env
import approach
from multiprocessing import Pool
def run(seed):
    env=make_env(); obs,_=env.reset(seed=seed)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
    cnt={"nav":0,"push":0}; plans=0
    for i in range(1000):
        m0=ap.mode
        a=ap.get_action(obs)
        cnt[ap.mode if ap.mode in cnt else "nav"]+=1
        obs,r,te,tr,_=env.step(np.clip(a,-0.049,0.049))
        if te: break
    env.close()
    return i+1, cnt["nav"], cnt["push"]
with Pool(15) as p: res=p.map(run, range(1000,1030))
r=np.array(res); print(r.mean(0)); print(r[:10])
