import sys, time
from env_client import make_env
import numpy as np
import approach
from approach import GeneratedApproach
seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
env = make_env()
obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {})
ap.reset(obs, info)
for n,o in ap.objs.items(): print(n, np.round(o.p,3), np.round(o.h,3))
orig = ap._next_task
def nt(state):
    orig(state); print('step', ap.steps, 'task', ap.current, 'grasp', state.get(ap.robot,'grasp_active'), 'plan len', len(ap.plan), 'fails', ap.fail_count)
ap._next_task = nt
for t in range(N):
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    if term: print('SOLVED', t+1); break
