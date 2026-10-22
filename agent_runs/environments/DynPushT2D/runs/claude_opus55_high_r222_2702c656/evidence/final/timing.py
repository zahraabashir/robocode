import time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); worst=0; tot=0
for seed in [127, 3139, 1077, 5]:
    obs,info=env.reset(seed=seed); ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
    ct=0
    for t in range(1000):
        t0=time.time(); a=ap.get_action(obs); dt=time.time()-t0; ct+=dt; worst=max(worst,dt)
        obs,r,te,tr,_=env.step(a)
        if te: break
    print(seed, t+1, 'compute', round(ct,3))
print('worst step', worst)
