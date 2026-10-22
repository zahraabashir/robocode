import sys
from test_approach import *
for seed in map(int, sys.argv[1:]):
    env = make_env(); obs, info = env.reset(seed=seed); env.close()
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    print(seed, 'pred', ap.pred)
    for ri in range(2):
        print(' r%d'%ri, len(ap.actions[ri]), [(i+1,round(x,2),round(y,2),op) for i,(x,y,op,h) in enumerate(ap.actions[ri]) if op])
    for o in obs:
        if o.type.name in ('objective','sample'): print('  ',o.name,[round(float(v),2) for v in obs.data[o]][:4])
