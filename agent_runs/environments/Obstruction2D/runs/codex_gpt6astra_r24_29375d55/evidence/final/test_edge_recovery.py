"""Exercise the tilted-gripper recovery even on ordinary reachable blocks."""
import json
import math
from env_client import make_env
from approach import GeneratedApproach

for seed, offset in [(0,None),(1,None),(2,None),(7,None),(0,-.05),(0,-.055),(0,-.06)]:
    env=make_env()
    state,info=env.reset(seed=seed)
    policy=GeneratedApproach(env.action_space,env.observation_space,{})
    policy.reset(state,info)
    policy.edge_task(state,policy.block)
    if offset is not None:
        policy.pickx=state.get(policy.block,'x')+offset
        policy.task_theta=-math.pi/2+.22
    for step in range(env.max_steps):
        state,reward,terminated,truncated,info=env.step(policy.get_action(state))
        if terminated or truncated:
            break
    print(json.dumps({'seed':seed,'offset':offset,'success':terminated,'steps':step+1}),flush=True)
    env.close()
    assert terminated
