import numpy as np
from env_client import make_env
env=make_env()
obs,_=env.reset(seed=3)
for i in range(5000):
    obs,r,te,tr,info=env.step(np.array([0.0,0.0]))
    if te or tr: print("done at",i+1,te,tr,r,info); break
else: print("no termination in 5000")
