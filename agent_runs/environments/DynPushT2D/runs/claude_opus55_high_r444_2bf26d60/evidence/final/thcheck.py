import numpy as np
from env_client import make_env
import approach
from multiprocessing import Pool
def run(seed):
    env=make_env(); obs,_=env.reset(seed=seed)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
    ths=[obs[2]]; jumps=0
    for i in range(400):
        obs,r,te,tr,_=env.step(np.clip(ap.get_action(obs),-0.049,0.049))
        if abs(obs[2]-ths[-1])>1: jumps+=1
        ths.append(obs[2])
        if te: break
    env.close()
    return seed, round(ths[0],2), round(min(ths),2), round(max(ths),2), jumps, round(obs[31],2)
with Pool(15) as p: res=p.map(run, range(2000,2030))
for r in res: print(r)
