import sys, numpy as np
from env_client import make_env
import approach
from multiprocessing import Pool
def run(seed):
    env=make_env(); obs,_=env.reset(seed=seed)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
    p0=obs[0:3].copy(); first=None; nplans=0; segs=[]; cur=None
    for i in range(1000):
        a=ap.get_action(obs)
        m=ap.mode
        if m!=cur: segs.append([m,0]); cur=m
        segs[-1][1]+=1
        obs,r,te,tr,_=env.step(np.clip(a,-0.049,0.049))
        if first is None and np.any(np.abs(obs[0:3]-p0)>1e-6): first=i
        if te: break
    env.close()
    return i+1, first, segs
with Pool(15) as p: res=p.map(run, range(1000,1030))
print(np.mean([r[0] for r in res]), np.mean([r[1] for r in res]))
for r in res[:8]: print(r[0], r[1], " ".join("%s%d"%(m[0][0],m[1]) for m in r[2]))
