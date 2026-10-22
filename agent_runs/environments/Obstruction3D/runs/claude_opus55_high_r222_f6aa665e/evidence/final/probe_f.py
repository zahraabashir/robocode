import numpy as np
from env_client import make_env
env = make_env(); obs, info = env.reset(seed=0)
r = obs.get_object_from_name("robot"); print("init", obs.get(r,"finger_state"))
a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); print("closed", obs.get(r,"finger_state"))
a[10]=1; obs,*_=env.step(a); print("open", obs.get(r,"finger_state"))
