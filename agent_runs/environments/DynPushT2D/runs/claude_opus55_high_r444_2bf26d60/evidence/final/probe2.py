from env_client import make_env
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=200)
env = make_env()
obs,_ = env.reset(seed=1)
print(obs[[0,1,2,16,17]])
# move robot in straight line towards the block origin and keep going 
t=0
for i in range(80):
    d = obs[0:2]-obs[16:18]
    a = np.clip(d/np.linalg.norm(d)*0.05, -0.05,0.05) if i<40 else np.zeros(2)
    obs,r,te,tr,_ = env.step(a)
    print(i, a, obs[[0,1,2,3,4,5,16,17,19,20]], r)
env.close()
