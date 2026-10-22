import sys
import numpy as np
from test_approach import *
seed=int(sys.argv[1])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
r0=obs.get_object_from_name('rover0'); r1=obs.get_object_from_name('rover1')
hist=[]
while True:
    n=len(ap.log)
    a=ap.get_action(obs)
    if len(ap.log)>n: break
    hist.append((round(obs.get(r1,'x'),2), round(obs.get(r1,'y'),2)))
    obs,r,term,tr,info=env.step(a)
print(hist[-4:])
