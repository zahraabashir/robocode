import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
cnt=int(sys.argv[3]) if len(sys.argv)>3 else None
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={'object_count':cnt} if cnt else None)
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
print('tasks',ap.tasks)
last=None
for t in range(int(sys.argv[2])):
    a=ap.get_action(obs)
    obs,r,term,tr,_=env.step(a)
    key=(ap.phase, ap._grasped_name(obs), ap.tasks[0] if ap.tasks else None)
    if key!=last or ap.blocked or len(sys.argv)>4:
        print(t,ap.phase,len(ap.qpath),np.round(ap._tool(obs)[:3,3],3),'blk',ap.blocked,'grip',a[10],key[1],key[2]); last=key
    if term: print('DONE',t+1);break
