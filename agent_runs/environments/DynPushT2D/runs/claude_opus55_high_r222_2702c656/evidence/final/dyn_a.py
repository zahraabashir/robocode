import numpy as np
from env_client import make_env
env=make_env()
obs,info=env.reset(seed=0)
np.set_printoptions(precision=3,suppress=True)
print(obs)
print(info)
