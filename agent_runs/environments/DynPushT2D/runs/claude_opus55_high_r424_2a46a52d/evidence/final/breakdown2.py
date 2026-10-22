import numpy as np, sys, json
from multiprocessing import Pool
from env_client import make_env
import approach
params=json.loads(sys.argv[1]) if len(sys.argv)>1 else {}
def run(seed):
    for k,v in params.items(): setattr(approach.GeneratedApproach,k,v)
    env=make_env(); obs,info=env.reset(seed=seed)
    ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
    first=None; nav=0; push=0; small=0
    for t in range(1000):
        a=ap.get_action(obs)
        obs2,r,term,trunc,_=env.step(a)
        moved = np.abs(obs2[0:3]-obs[0:3]).max()>1e-6
        if moved and first is None: first=t
        if moved:
            push+=1; small += np.abs(a).max()<0.03
        else: nav+=1
        obs=obs2
        if term: break
    return t+1, first, nav-first, push, small
with Pool(10) as p: res=np.array(p.map(run, range(200,260)))
print(params, "steps %.1f initial_nav %.1f later_nav %.1f push %.1f smallpush %.1f"%tuple(res.mean(0)))
