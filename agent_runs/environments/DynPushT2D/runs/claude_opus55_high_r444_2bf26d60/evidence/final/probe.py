from env_client import make_env
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=200)
env = make_env()
for s in range(5):
    obs,_ = env.reset(seed=s)
    print(s, obs[[0,1,2,16,17,29,30,31]], obs[12:16], obs[28], obs[41:45])
env.close()
