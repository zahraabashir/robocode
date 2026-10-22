from env_client import make_env
from approach import GeneratedApproach
import time,json,sys
seeds=list(map(int,sys.argv[1:])) or list(range(20))
for seed in seeds:
 e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info);start=time.monotonic();term=False
 for t in range(400):
  s,r,term,trunc,_=e.step(p.get_action(s))
  if term or trunc:break
 print(json.dumps(dict(seed=seed,count=info['object_count'],success=term,steps=t+1,seconds=round(time.monotonic()-start,2),phase=p.phase,obj=str(p.obj),stall=p.stall,attempt=p.attempt)),flush=True);e.close()
