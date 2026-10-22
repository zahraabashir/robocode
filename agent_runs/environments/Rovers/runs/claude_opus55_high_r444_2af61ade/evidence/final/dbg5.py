import sys
from test_approach import *
seed=int(sys.argv[1])
env = make_env(); obs, info = env.reset(seed=seed)
for o in obs:
    print(o.name, [round(float(v),2) for v in obs.data[o]])
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
print([len(a) for a in ap.actions], getattr(ap,'pred',None))
