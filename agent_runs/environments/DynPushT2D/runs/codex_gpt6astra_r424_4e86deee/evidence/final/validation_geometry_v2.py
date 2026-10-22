from env_client import make_env
from approach import GeneratedApproach
import numpy as np
import time,json
out=[]
for seed in range(100,200):
 e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
 start=time.time();trace=[s.tolist()];ok=False
 for t in range(e.max_steps):
  s,r,done,trunc,info=e.step(p.get_action(s));trace.append(s.tolist())
  if done or trunc:ok=done;break
 err=s[29:32]-s[:3];err[2]=(err[2]+np.pi)%(2*np.pi)-np.pi
 out.append((seed,bool(ok),t+1,time.time()-start))
 if not ok:
  print('FAIL',seed,t+1,'err',np.round(err,4),flush=True)
  with open('geometry_v2_fail_%s.json'%seed,'w') as f:json.dump(trace,f)
 if seed%10==9:print('PROGRESS',seed,'success',sum(o[1] for o in out),'/',len(out),flush=True)
 e.close()
print('RESULT',out,flush=True)
with open('validation_geometry_v2_results.json','w') as f:json.dump(out,f)
