import sys
import numpy as np
from test_approach import *
seed=int(sys.argv[1]); dy=float(sys.argv[2]) if len(sys.argv)>2 else 0.05
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
steps=0
while True:
    n=len(ap.log)
    a=ap.get_action(obs)
    if len(ap.log)>n: break
    obs,r,term,tr,info=env.step(a); steps+=1
r0=obs.get_object_from_name('rover0'); r1=obs.get_object_from_name('rover1')
objs=[o for o in obs if o.type.name=='objective']
print('fail at', obs.get(r0,'x'), obs.get(r0,'y'), obs.get(r0,'theta'))
for k in range(12):
    obs,*_=env.step(np.array([0,0,0,0.5, 0,dy,0,0],dtype=np.float32))
    print(k, round(obs.get(r1,'x'),3), round(obs.get(r1,'y'),3), [obs.get(o,'received_image') for o in objs])
