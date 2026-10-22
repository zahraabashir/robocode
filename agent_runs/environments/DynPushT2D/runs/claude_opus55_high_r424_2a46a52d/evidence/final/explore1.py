import numpy as np
from env_client import make_env
env = make_env()
np.set_printoptions(precision=3, suppress=True, linewidth=200)
for s in range(5):
    obs,_ = env.reset(seed=s)
    print(s, obs[0:3], obs[12:16], "robot", obs[16:18], obs[28], "goal", obs[29:32])
obs,_ = env.reset(seed=0)
print(obs)
for i in range(5):
    obs,r,t,tr,info = env.step(np.array([0.049,0.0]))
    print(obs[16:21], r, t, tr, info)
env.close()
