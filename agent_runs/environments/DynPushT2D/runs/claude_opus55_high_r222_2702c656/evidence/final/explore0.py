from env_client import make_env
import numpy as np
np.set_printoptions(precision=3, suppress=True, linewidth=200)
env = make_env()
for s in range(5):
    obs,_ = env.reset(seed=s)
    print(s, obs)
print(env.max_steps)
