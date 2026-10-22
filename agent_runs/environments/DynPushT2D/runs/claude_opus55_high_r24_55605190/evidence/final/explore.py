from env_client import make_env
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=200)
env = make_env()
for s in range(5):
    obs,_ = env.reset(seed=s)
    print(s, obs)
print(env.max_steps)
obs,_=env.reset(seed=0)
for t in range(10):
    obs,r,te,tr,_=env.step(np.array([0.049,0.0]))
    print(t, obs[16:22], obs[0:6], r, te)
env.close()
