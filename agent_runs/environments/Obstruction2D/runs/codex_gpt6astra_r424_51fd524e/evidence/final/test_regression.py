"""Reproduce the edge cases discovered during black-box exploration."""
import hashlib
import json
import time
from env_client import make_env
from approach import GeneratedApproach

cases=[(21,None),(31,None),(74,None),(151,None),(489,None),(627,None),(42,3),(154,3),(0,4),(1,4),(2,4),(3,4),(4,4),(5,4)]
policy_hash=hashlib.sha256(open('approach.py','rb').read()).hexdigest()
results=[]
e=make_env()
for seed,count in cases:
    s,info=e.reset(seed=seed,options={'object_count':count} if count is not None else None)
    policy=GeneratedApproach(e.action_space,e.observation_space,{})
    tick=time.perf_counter();policy.reset(s,info);cpu=time.perf_counter()-tick
    for step in range(e.max_steps):
        tick=time.perf_counter();action=policy.get_action(s);cpu+=time.perf_counter()-tick
        s,reward,done,truncated,info=e.step(action)
        if done or truncated:break
    result=dict(seed=seed,count=count,done=done,steps=step+1,policy_seconds=cpu,policy_hash=policy_hash)
    results.append(result);print(result,flush=True)
    json.dump(results,open('regression_results.json','w'),indent=2)
e.close()
assert all(r['done'] for r in results)
