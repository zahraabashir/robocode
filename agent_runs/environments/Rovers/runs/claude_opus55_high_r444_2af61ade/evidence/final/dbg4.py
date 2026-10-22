import sys
from test_approach import *
seed=int(sys.argv[1])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for o in obs:
    if o.type.name=='obstacle' and obs.get(o,'half_x')<0.1: print(o.name, round(obs.get(o,'x'),2), round(obs.get(o,'y'),2))
steps=0
while True:
    n=len(ap.log)
    a=ap.get_action(obs)
    if len(ap.log)>n:
        r1=obs.get_object_from_name('rover1'); print('step',steps,'rover1 at', obs.get(r1,'x'), obs.get(r1,'y'), ap.log[-1]); break
    obs,r,term,tr,info=env.step(a); steps+=1
    if term: break
