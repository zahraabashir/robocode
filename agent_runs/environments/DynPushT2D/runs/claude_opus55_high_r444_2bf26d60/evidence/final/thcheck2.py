import numpy as np
from env_client import make_env
import approach
env=make_env(); obs,_=env.reset(seed=2006)
ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,{})
ap.goal=np.array([obs[0],obs[1],obs[2]+0.8])
ths=[]
for i in range(300):
    obs,r,te,tr,_=env.step(np.clip(ap.get_action(obs),-0.049,0.049))
    ths.append(obs[2])
print(np.round(ths[::10],3))
