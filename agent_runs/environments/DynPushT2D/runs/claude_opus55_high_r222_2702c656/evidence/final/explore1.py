from env_client import make_env
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=200)
env = make_env()
obs,_ = env.reset(seed=0)
M=0.0499
for d in [(1,0),(0,1),(-1,0),(0,-1)]:
    for i in range(150):
        obs,r,te,tr,_ = env.step(np.array(d)*M)
    print(d, obs[16:19], obs[0:6])
obs,_=env.reset(seed=1)
p=obs[16:18].copy()
obs,*_=env.step(np.array([0.0499,0.03])); print(obs[16:18]-p)
