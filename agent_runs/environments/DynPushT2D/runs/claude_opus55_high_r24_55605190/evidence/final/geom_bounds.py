from env_client import make_env
import numpy as np
env=make_env()
for s in [0,1]:
  for d in [(1,0),(-1,0),(0,1),(0,-1)]:
    obs,_=env.reset(seed=s)
    prev=obs[16:18].copy(); stuck=0
    for t in range(300):
        obs,*_=env.step(np.array(d)*0.0499)
        if np.linalg.norm(obs[16:18]-prev)<1e-4: stuck+=1
        else: stuck=0
        prev=obs[16:18].copy()
        if stuck>5: break
    print(s,d,'t',t,'robot',obs[16:18],'block',obs[0:3])
