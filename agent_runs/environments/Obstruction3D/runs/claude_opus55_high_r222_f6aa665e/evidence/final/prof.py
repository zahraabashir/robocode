import time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
env = make_env(); obs, info = env.reset(seed=7)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
ta=te=0
for i in range(60):
    t=time.time(); a=ap.get_action(obs); ta+=time.time()-t
    t=time.time(); obs,r,term,tr,info=env.step(a); te+=time.time()-t
    if term: break
print(i, "approach", ta, "env", te)
