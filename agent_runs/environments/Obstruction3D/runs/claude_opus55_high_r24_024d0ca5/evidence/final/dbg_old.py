import numpy as np
from env_client import make_env
from old_approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=0)
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
for t in range(80):
    a=ap.get_action(obs)
    if a[10]<-0.5:
        print(t,'close q',np.round(ap._q(obs),4),'tool',np.round(ap._tool(obs)[:3,:],3).tolist())
    obs,*_=env.step(a)
    if a[10]<-0.5: print(' grasped',ap._grasped_name(obs)); 
