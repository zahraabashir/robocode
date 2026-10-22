"""Black-box validation; this module is not imported by the submitted policy."""
import argparse
import json
import time
from env_client import make_env
from approach import GeneratedApproach

p=argparse.ArgumentParser()
p.add_argument('--start',type=int,default=0)
p.add_argument('--stop',type=int,default=100)
p.add_argument('--count',type=int)
p.add_argument('--out',default='validation.jsonl')
args=p.parse_args()
with open(args.out,'w') as out:
 for seed in range(args.start,args.stop):
  e=make_env()
  try:
   s,info=e.reset(seed=seed,options={'object_count':args.count} if args.count is not None else None)
   a=GeneratedApproach(e.action_space,e.observation_space,{})
   start=time.perf_counter();a.reset(s,info);compute=time.perf_counter()-start
   initial={o.name:a.rect(s,o) for o in s.get_objects(a.types['rectangle'])}
   for n in range(e.max_steps):
    now=time.perf_counter();action=a.get_action(s);compute+=time.perf_counter()-now
    s,reward,term,trunc,info=e.step(action)
    if term or trunc:break
   row={'seed':seed,'count':args.count,'success':term,'steps':n+1,'policy_seconds':round(compute,4),'elapsed':round(time.perf_counter()-start,3)}
   if not term:row.update(phase=a.phase,task=a.task.name,dest=a.dest,robot=[s.get(a.robot,f) for f in ('x','y')],initial=initial,final={o.name:a.rect(s,o) for o in s.get_objects(a.types['rectangle'])})
  except Exception as error:
   row={'seed':seed,'count':args.count,'error':str(error)}
  finally:e.close()
  out.write(json.dumps(row)+'\n');out.flush()
  if not row.get('success',False):print(json.dumps(row),flush=True)
