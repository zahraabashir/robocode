from env_client import make_env
from candidate_balanced import GeneratedApproach as Candidate
from assignment_baseline import GeneratedApproach as Baseline
import json,time
for seed in range(10):
 record={'seed':seed}
 for label,cls in [('candidate',Candidate)]:
  e=make_env();s,info=e.reset(seed=seed);p=cls(e.action_space,e.observation_space,{})
  start=time.time();p.reset(s,info)
  for step in range(160):
   s,r,term,trunc,inf=e.step(p.get_action(s))
   if term or trunc:break
  record[label]={'steps':step+1,'success':term,'seconds':round(time.time()-start,3)}
  e.close()
 print(json.dumps(record),flush=True)
