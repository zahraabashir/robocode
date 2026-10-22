from env_client import make_env
from approach import GeneratedApproach
import numpy as np
import time
import sys
import json
seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
for seed in seeds:
    env=make_env(); s,info=env.reset(seed=seed)
    policy=GeneratedApproach(env.action_space,env.observation_space,{})
    policy.reset(s,info); trace=[s.tolist()]; start=time.monotonic()
    for t in range(env.max_steps):
        a=policy.get_action(s); s,r,done,trunc,info=env.step(a); trace.append(s.tolist())
        if done or trunc: break
    err=s[29:32]-s[:3]; err[2]=(err[2]+np.pi)%(2*np.pi)-np.pi
    print(seed,'success',done,'steps',t+1,'err',np.round(err,4).tolist(),'time',round(time.monotonic()-start,3),flush=True)
    if not done:
        with open('trace_%s.json'%seed,'w') as f: json.dump(trace,f)
    env.close()
