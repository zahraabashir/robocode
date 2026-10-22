from env_client import make_env
import numpy as np
env=make_env(); obs,_=env.reset(seed=38); print(obs[29:32])
