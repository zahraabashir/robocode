from env_client import make_env
from approach import GeneratedApproach as Baseline
from candidate_angles import GeneratedApproach as Candidate
import time,json,sys
seeds=list(map(int,sys.argv[1:])) or list(range(30))
results=[]
for seed in seeds:
 row={'seed':seed}
 for name, cls in [('baseline',Baseline),('angles',Candidate)]:
  env=make_env();s,info=env.reset(seed=seed);p=cls(env.action_space,env.observation_space,{});p.reset(s,info);start=time.monotonic()
  for t in range(env.max_steps):
   s,r,done,trunc,info=env.step(p.get_action(s))
   if done or trunc:break
  row[name]=[bool(done),t+1,round(time.monotonic()-start,3)];env.close()
 print(row,flush=True);results.append(row)
with open('angles_results.json','w') as f:json.dump(results,f)
