from env_client import make_env
from approach import GeneratedApproach
import time,json,sys,numpy as np
for count in map(int,sys.argv[1:] or ['5','10']):
 for seed in range(4):
  E=make_env();s,info=E.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info);start=time.monotonic();term=False
  for t in range(min(1000,100+60*count)):
   s,rew,term,trunc,info=E.step(p.get_action(s))
   if term or trunc:break
  print(json.dumps(dict(seed=seed,count=count,success=term,steps=t+1,seconds=round(time.monotonic()-start,2),phase=p.phase,obj=str(p.obj),index=p.index,todo=len(p.todo),stall=p.stall,attempt=p.attempt,pos=p.pos(s,p.obj).tolist(),dest=p.destination.tolist())),flush=True)
  E.close()
