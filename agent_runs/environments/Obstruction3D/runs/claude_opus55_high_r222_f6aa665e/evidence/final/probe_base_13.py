from env_client import make_env
import numpy as np
env=make_env(); obs,_=env.reset(seed=1); R=obs.get_object_from_name("robot")
for g in [-1,-1,-1,1,1,0,-0.3,-0.6]:
    a=np.zeros(11,np.float32); a[10]=g; obs,r,te,tr,info=env.step(a)
    print(g, obs.get(R,"finger_state"), obs.get(R,"grasp_active"), r, te, info)
env.close()
