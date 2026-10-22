import time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); ap=GeneratedApproach(None,None,{})
for seed in range(5):
    obs,info=env.reset(seed=seed); ap.reset(obs,info)
    t0=time.time(); ap.plan_push(obs); print(time.time()-t0)
