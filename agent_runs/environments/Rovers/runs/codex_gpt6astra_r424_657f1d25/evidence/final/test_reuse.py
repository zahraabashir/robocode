"""Check repeated resets, variable object counts, and the action contract."""
import numpy as np
from env_client import make_env
from approach import GeneratedApproach

env=make_env()
policy=GeneratedApproach(env.action_space,env.observation_space,{})
for seed,count in ((0,1),(89,3),(1212,4),(349,2)):
 state,info=env.reset(seed=seed,options={'object_count':count})
 policy.reset(state,info)
 for step in range(200):
  action=policy.get_action(state)
  assert action.shape==(8,) and action.dtype==np.float32
  assert np.isfinite(action).all()
  assert (action>=env.action_space.low).all() and (action<=env.action_space.high).all()
  state,_,terminated,truncated,_=env.step(action)
  if terminated or truncated:break
 assert terminated,(seed,count)
 print('PASS',seed,count,step+1,flush=True)
env.close()
