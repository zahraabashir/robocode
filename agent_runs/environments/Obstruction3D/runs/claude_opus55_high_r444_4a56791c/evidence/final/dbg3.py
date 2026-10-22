import sys, time
from env_client import make_env
import numpy as np, kin
import os, importlib as _il
GeneratedApproach = _il.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
seed=int(sys.argv[1]); N=int(sys.argv[2])
env = make_env()
obs, info = env.reset(seed=seed, options=({'object_count': int(sys.argv[3])} if len(sys.argv)>3 else None))
ap = GeneratedApproach(env.action_space, env.observation_space, {})
t0=time.time()
ap.reset(obs, info)
for n,o in ap.objs.items(): print(n, np.round(o.p,3), np.round(o.h,3))
orig = ap._next_task
def nt(state):
    orig(state); T=kin.fk(ap.base, ap._q(state)); print('step', ap.steps, 'task', ap.current, 'grasp', state.get(ap.robot,'grasp_active'), 'plan', len(ap.plan), 'fails', ap.fail_count, 'tool', np.round(T[:3,3],3), 'end', np.round(kin.fk(ap.base, ap.plan[-3][1])[:3,3],3) if len(ap.plan)>3 else '')
ap._next_task = nt
oa=ap._abort
def ab(state):
    T=kin.fk(ap.base, ap._q(state)); print('ABORT step', ap.steps, 'tool', np.round(T[:3,3],3), 'q', np.round(ap._q(state),3), 'target', np.round(ap.plan[0][1],3), 'tgt tool', np.round(kin.fk(ap.base, ap.plan[0][1])[:3,3],3)); oa(state)
ap._abort=ab
for t in range(N):
    pass
    a = ap.get_action(obs)
    obs, r, term, trunc, info = env.step(a)
    if term: print('SOLVED', t+1); break
print('time', time.time()-t0)
