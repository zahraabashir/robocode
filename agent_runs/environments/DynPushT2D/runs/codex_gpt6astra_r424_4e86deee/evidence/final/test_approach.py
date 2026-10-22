from env_client import make_env
from approach import GeneratedApproach
import numpy as np
import sys, time, json
seeds=[int(x) for x in sys.argv[1:]] or list(range(10))
for seed in seeds:
 e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,info)
 start=time.time();trace=[s.tolist()];ok=False
 for t in range(e.max_steps):
  a=p.get_action(s);s,r,done,trunc,info=e.step(a);trace.append(s.tolist())
  if done or trunc:ok=done;break
 err=s[29:32]-s[:3];err[2]=(err[2]+np.pi)%(2*np.pi)-np.pi
 print(seed,ok,t+1,'err',np.round(err,4),'secs',round(time.time()-start,2),flush=True)
 with open('trace_%s.json'%seed,'w') as f:json.dump(trace,f)
 e.close()
