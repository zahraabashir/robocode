from env_client import make_env
from approach import GeneratedApproach
import sys,time,json
seeds=[int(x) for x in sys.argv[1:]] or list(range(10))
e=make_env()
for seed in seeds:
 s,i=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i);start=time.time()
 trace=[]
 for t in range(e.max_steps):
  a=p.get_action(s); s,re,done,trunc,info=e.step(a)
  if t%20==0:trace.append([t,p.phase,p.obj.name if p.obj else '',*[round(s.get(p.robot,f),3) for f in ['x','y']],*[round(s.get(p.obj,f),3) for f in ['x','y']]])
  if done or trunc:break
 print(seed,'OK' if done else 'FAIL',t+1,'time',round(time.time()-start,2),flush=True)
 if not done:print(trace[-15:],flush=True)
e.close()
