from env_client import make_env
from approach import GeneratedApproach
import sys,time,json,numpy as np
seed=int(sys.argv[1]);count=int(sys.argv[2])
e=make_env();s,info=e.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info);start=time.monotonic();compute=0;term=False
for t in range(e.max_steps):
 st=time.monotonic();a=p.get_action(s);compute+=time.monotonic()-st
 s,r,term,trunc,info=e.step(a)
 if t%50==0:print('progress',t,p.phase,str(p.obj),p.index,len(p.todo),p.stall,p.attempt,round(time.monotonic()-start,2),flush=True)
 if term or trunc or time.monotonic()-start>58:break
print(json.dumps(dict(seed=seed,count=count,success=term,steps=t+1,seconds=round(time.monotonic()-start,2),compute=round(compute,3),phase=p.phase,obj=str(p.obj),stall=p.stall,attempt=p.attempt)),flush=True)
e.close()
