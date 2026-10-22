from env_client import make_env
from approach import GeneratedApproach
import numpy as np,time,json
seeds=np.random.RandomState(74027).choice(np.arange(10000,1000000),100,replace=False)
rows=[]
for count,seed in enumerate(seeds):
 seed=int(seed);env=make_env();s,info=env.reset(seed=seed);p=GeneratedApproach(env.action_space,env.observation_space,{});p.reset(s,info);trace=[s.tolist()];start=time.monotonic()
 for t in range(env.max_steps):
  s,r,done,trunc,info=env.step(p.get_action(s));trace.append(s.tolist())
  if done or trunc:break
 env.close();elapsed=time.monotonic()-start;row={'seed':seed,'success':bool(done),'steps':t+1,'seconds':elapsed};rows.append(row)
 if not done:
  print('FAIL',row,flush=True)
  with open('holdout_trace_%d.json'%seed,'w') as f:json.dump(trace,f)
 if count%10==9:print('PROGRESS',count+1,'success',sum(x['success'] for x in rows),'mean',np.mean([x['steps'] for x in rows]),flush=True)
 with open('holdout_results.json','w') as f:json.dump(rows,f)
print('SUMMARY',len(rows),'success',sum(x['success'] for x in rows),'mean',np.mean([x['steps'] for x in rows]),'max',max(x['steps'] for x in rows),'maxseconds',max(x['seconds'] for x in rows),flush=True)
