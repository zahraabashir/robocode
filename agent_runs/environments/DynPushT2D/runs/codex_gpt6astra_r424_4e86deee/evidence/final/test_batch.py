"""Independent live rollouts; save diagnostic traces only for failures."""
from env_client import make_env
from approach import GeneratedApproach
import numpy as np
import sys, time, json
start_seed=int(sys.argv[1]) if len(sys.argv)>1 else 300
count=int(sys.argv[2]) if len(sys.argv)>2 else 100
prefix=sys.argv[3] if len(sys.argv)>3 else 'batch'
results=[]
for seed in range(start_seed,start_seed+count):
 env=make_env();state,info=env.reset(seed=seed)
 policy=GeneratedApproach(env.action_space,env.observation_space,{})
 policy.reset(state,info);trace=[state.tolist()];actions=[];tic=time.monotonic();success=False
 for step in range(env.max_steps):
  a=policy.get_action(state)
  assert np.all(np.isfinite(a)) and np.max(np.abs(a))<=.050000001
  state,reward,terminated,truncated,info=env.step(a)
  trace.append(state.tolist());actions.append(a.tolist())
  if terminated or truncated:success=terminated;break
 elapsed=time.monotonic()-tic
 error=state[29:32]-state[:3];error[2]=(error[2]+np.pi)%(2*np.pi)-np.pi
 row=dict(seed=seed,success=bool(success),steps=step+1,seconds=elapsed,error=error.tolist(),reward=float(reward))
 results.append(row)
 if not success:
  with open('%s_fail_%s.json'%(prefix,seed),'w') as f:json.dump(dict(states=trace,actions=actions),f)
  print('FAIL',row,flush=True)
 if (seed-start_seed+1)%25==0:print('progress',seed,'passed',sum(x['success'] for x in results),'/',len(results),flush=True)
 env.close()
with open('%s_summary.json'%prefix,'w') as f:json.dump(results,f)
print('SUMMARY',sum(x['success'] for x in results),'/',len(results),'mean_steps',np.mean([x['steps'] for x in results]),'max_steps',max(x['steps'] for x in results),'max_seconds',max(x['seconds'] for x in results),flush=True)
