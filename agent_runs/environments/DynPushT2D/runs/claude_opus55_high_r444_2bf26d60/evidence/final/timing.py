import numpy as np, time
from env_client import make_env
from approach import *
env=make_env(); obs,_=env.reset(seed=1003)
ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
t=time.time()
for _ in range(5): r=ap.plan_push(obs[0:3],obs[16:18])
print((time.time()-t)/5)
sw,dw=ap.candidates(obs[0:3]); print(len(sw))
