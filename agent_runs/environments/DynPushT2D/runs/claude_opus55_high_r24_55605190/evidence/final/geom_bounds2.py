from env_client import make_env
import numpy as np
env=make_env()
obs,_=env.reset(seed=0)
for d in [(1,0),(-1,0),(0,1),(0,-1)]:
    obs,_=env.reset(seed=0)
    for t in range(200):
        obs,*_=env.step(np.array(d)*0.0499)
    p=obs[16:18].copy()
    # now fine steps
    seq=[]
    for t in range(10):
        obs,*_=env.step(np.array(d)*0.001); seq.append(obs[16:18].copy())
    print(d,'after coarse',p,'after fine',seq[-1], 'fine deltas', np.round(np.diff([p]+seq,axis=0)[:,0 if d[0] else 1],5))
