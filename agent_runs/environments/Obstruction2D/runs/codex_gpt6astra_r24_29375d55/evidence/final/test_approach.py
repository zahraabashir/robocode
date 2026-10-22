from env_client import make_env
from approach import GeneratedApproach
import sys,time,json
seeds=[int(x) for x in sys.argv[1:]] or list(range(20))
for seed in seeds:
 e=make_env();s,i=e.reset(seed=seed);a=GeneratedApproach(e.action_space,e.observation_space,{ });a.reset(s,i);start=time.time()
 last=None;stuck=0
 for n in range(e.max_steps):
  act=a.get_action(s);s,r,t,tr,info=e.step(act)
  sig=(a.phase,tuple(s.get(a.robot,f) for f in ('x','y')),tuple(s.get(a.task,f) for f in ('x','y')))
  stuck=stuck+1 if sig==last else 0;last=sig
  if t or tr or stuck>35:break
 print(json.dumps({'seed':seed,'success':t,'steps':n+1,'seconds':round(time.time()-start,2),'phase':a.phase,'task':a.task.name,'robot':[s.get(a.robot,f) for f in ('x','y')],'taskxy':[s.get(a.task,f) for f in ('x','y')],'dest':a.dest}),flush=True)
 e.close()
