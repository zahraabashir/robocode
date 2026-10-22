import sys
from env_client import make_env
import numpy as np, kin
import approach
from approach import GeneratedApproach
seed=int(sys.argv[1]); N=int(sys.argv[2])
env = make_env()
obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {})
ap.reset(obs, info)
for t in range(N):
    q0=ap._q(obs)
    head = ap.plan[0] if ap.plan else None
    a = ap.get_action(obs)
    head = ap.plan[0] if ap.plan else None
    obs, r, term, trunc, info = env.step(a)
    q1=ap._q(obs)
    T=kin.fk(ap.base,q1)
    tgt = kin.fk(ap.base, head[1])[:3,3] if head and head[0]=='move' else None
    print(t, ap.current, head[0] if head else None, 'moved', round(float(np.max(np.abs(q1-q0))),3), 'tool', np.round(T[:3,3],3), 'tgt', None if tgt is None else np.round(tgt,3), 'grip', a[10], 'g', obs.get(ap.robot,'grasp_active'))
