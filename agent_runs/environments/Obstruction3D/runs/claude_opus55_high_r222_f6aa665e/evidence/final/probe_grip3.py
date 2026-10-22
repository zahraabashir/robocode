from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=3)
R = obs.get_object_from_name("robot")
for g in [1,1,-1,-1,-0.7,-1,1,0,-1]:
    a=np.zeros(11,np.float32); a[10]=g; a[3]=0.01
    obs,r,te,tr,info=env.step(a); print(g, np.round(obs.data[R][3:12],3))
print(env.action_space.low, env.action_space.high)
env.close()
