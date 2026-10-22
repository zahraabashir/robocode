import numpy as np
from env_client import make_env
env=make_env(); obs,_=env.reset(seed=1)
for a in [np.array([0.05,0.0]), np.array([0.049,0.0]), np.array([0.05,0.0],dtype=np.float32)]:
    try: env.step(a); print("ok",a.dtype,a)
    except Exception as e: print("fail",a, e)
print(env.action_space.low, env.action_space.high, env.action_space.dtype)
