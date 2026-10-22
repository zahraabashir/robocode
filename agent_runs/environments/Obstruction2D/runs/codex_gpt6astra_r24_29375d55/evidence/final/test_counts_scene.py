from env_client import make_env
from approach import GeneratedApproach
import json,time
f=open('test_counts_scene_v3.jsonl','w')
for count in [4,5]:
 for seed in range(100 if count==4 else 2):
  e=make_env();start=time.time()
  try:
   s,i=e.reset(seed=seed,options={'object_count':count});a=GeneratedApproach(e.action_space,e.observation_space,{})
   a.reset(s,i);init={str(o.name):a.rect(s,o) for o in s.get_objects(a.types['rectangle'])}
   term=False
   for k in range(e.max_steps):
    s,r,term,trunc,i=e.step(a.get_action(s))
    if term or trunc:break
   row={'count':count,'seed':seed,'steps':k+1,'success':term,'seconds':round(time.time()-start,2)}
   if not term:row.update(phase=a.phase,task=str(a.task.name),dest=a.dest,robot=[s.get(a.robot,z) for z in ['x','y']],init=init,final={str(o.name):a.rect(s,o) for o in s.get_objects(a.types['rectangle'])})
  except Exception as exc: row={'count':count,'seed':seed,'error':str(exc)}
  finally:e.close()
  f.write(json.dumps(row)+'\n');f.flush();print(json.dumps(row),flush=True)
