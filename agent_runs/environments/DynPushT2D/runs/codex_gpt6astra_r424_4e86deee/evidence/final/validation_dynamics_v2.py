from env_client import make_env
from approach import GeneratedApproach
import numpy as np
import time,json
summary=[]
for seed in range(200,300):
 e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
 start=time.time();trace=[dict(s=s.tolist())];ok=False
 for t in range(e.max_steps):
  a=p.get_action(s);s,r,done,trunc,info=e.step(a);trace.append(dict(s=s.tolist(),a=np.asarray(a).tolist(),phase=p.phase,contact=None if p.contact is None else np.asarray(p.contact,dtype=object).tolist()))
  if done or trunc:ok=done;break
 err=s[29:32]-s[:3];err[2]=(err[2]+np.pi)%(2*np.pi)-np.pi
 result=dict(seed=seed,success=bool(ok),steps=t+1,error=err.tolist(),seconds=time.time()-start)
 summary.append(result)
 if not ok: print(seed,ok,t+1,'err',np.round(err,4),'secs',round(time.time()-start,2),flush=True)
 if not ok:
  # Keep JSON-safe state/action traces; contact structure may contain nested arrays.
  for entry in trace:entry.pop('contact',None)
  with open('dynamics_v2_fail_%s.json'%seed,'w') as f:json.dump(trace,f)
 e.close()
open('validation_dynamics_v2_summary.json','w').write(json.dumps(summary))

print('TOTAL',len(summary),'SUCCESS',sum(z['success'] for z in summary),'MEAN_STEPS',sum(z['steps'] for z in summary)/len(summary),'MAX_SECONDS',max(z['seconds'] for z in summary),flush=True)
