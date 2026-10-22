import numpy as np
from multiprocessing import Pool
from env_client import make_env
import approach
def run(seed):
    env=make_env(); obs,info=env.reset(seed=seed)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    nav=0; push={}; plans=0; orig=ap._plan_push
    def pp(o):
        nonlocal plans; plans+=1; return orig(o)
    ap._plan_push=pp
    for t in range(1000):
        navmode = ap.nav_len>0 if hasattr(ap,'nav_len') and ap.plan else None
        a=ap.get_action(obs)
        if ap.nav_len>0 or (len(ap.plan)>0 and False): pass
        obs2,r,term,trunc,_=env.step(a)
        moved = np.abs(obs2[0:3]-obs[0:3]).max()>1e-6
        if moved: 
            k=round(float(np.abs(a).max()),3); push[k]=push.get(k,0)+1
        else: nav+=1
        obs=obs2
        if term: break
    return t+1, nav, push, plans
with Pool(10) as p: res=p.map(run, range(200,240))
print("mean steps", np.mean([r[0] for r in res]), "nav(no block motion)", np.mean([r[1] for r in res]), "plans", np.mean([r[3] for r in res]))
tot={}
for r in res:
    for k,v in r[2].items(): tot[k]=tot.get(k,0)+v/len(res)
print(sorted(tot.items(), key=lambda x:-x[1])[:10])
