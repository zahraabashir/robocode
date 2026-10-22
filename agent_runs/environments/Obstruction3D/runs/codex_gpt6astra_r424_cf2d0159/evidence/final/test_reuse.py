from env_client import make_env
from approach import GeneratedApproach
import time
E=make_env(); policy=GeneratedApproach(E.action_space,E.observation_space,{})
for seed,count in [(2,2),(22,1)]:
 state,info=E.reset(seed=seed,options={'object_count':count})
 begin=time.monotonic();policy.reset(state,info)
 for step in range(E.max_steps):
  state,reward,done,truncated,info=E.step(policy.get_action(state))
  if done or truncated:break
 print(seed,count,done,step+1,round(time.monotonic()-begin,3),flush=True)
E.close()
