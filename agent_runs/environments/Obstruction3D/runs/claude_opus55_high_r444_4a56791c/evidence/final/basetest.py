import numpy as np
from env_client import make_env
from common import *
env=make_env(); obs,_=env.reset(seed=312, options={'object_count':15})
print(env.action_space)
for d in [(-0.05,0,0),(-0.1,0,0),(0,0.05,0)]:
    a=np.zeros(11,dtype=np.float32); a[0:3]=d
    obs,*_=env.step(a); print(d, getbase(obs))
