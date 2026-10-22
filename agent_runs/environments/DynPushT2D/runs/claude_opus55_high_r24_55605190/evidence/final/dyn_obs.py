from env_client import make_env
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=200)
env=make_env()
for s in range(3):
    o,_=env.reset(seed=s); print(s,o)
