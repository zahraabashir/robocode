import sys, time
from env_client import make_env
import numpy as np
import os, importlib as _il
GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
tot=[]; 
for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    env = make_env(); obs, info = env.reset(seed=seed, options=({'object_count': int(sys.argv[3])} if len(sys.argv)>3 else None))
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0=time.time(); ap.reset(obs, info); ct=time.time()-t0; mx=0
    for t in range(1000):
        t1=time.time(); a = ap.get_action(obs); dt=time.time()-t1; ct+=dt; mx=max(mx,dt)
        obs, r, term, trunc, info = env.step(a)
        if term: break
    print(seed, term, t+1, 'compute', round(ct,2), 'max step', round(mx,2)); env.close()
