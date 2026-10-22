from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
r1 = obs.get_object_from_name('rover1')
for k in range(12):
    obs,*_ = env.step(np.array([0,0,0,1/6, 0,0,0.1,1/6],dtype=np.float32))
    print(round(obs.get(r1,'theta'),2), obs.get(r1,'at_home'), end='; ')
print()
obs, info = env.reset(seed=0)
for k in range(12):
    obs,*_ = env.step(np.array([0,0,0,1/6, 0,0,-0.1,1/6],dtype=np.float32))
    print(round(obs.get(r1,'theta'),2), obs.get(r1,'at_home'), end='; ')
