import numpy as np
from env_client import make_env
from approach import *
np.set_printoptions(precision=3, suppress=True)
env=make_env(); obs,_=env.reset(seed=1)
m=TModel(obs[12],obs[13],obs[14])
pose=obs[0:3].copy(); rob=obs[16:18].copy()
for i in range(40):
    a=np.array([0.049,0.0])
    p2,r2=m.step(pose,rob,a)
    obs,*_=env.step(a)
    if i>=33: print(i, obs[[0,1,2,16,17]], p2[0], r2[0])
    pose=obs[0:3].copy(); rob=obs[16:18].copy()
