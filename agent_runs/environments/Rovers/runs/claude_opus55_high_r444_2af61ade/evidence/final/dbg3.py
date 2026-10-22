import sys
from test_approach import *
seed=int(sys.argv[1])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for ri in range(2):
    print(ri, [(round(x,2),round(y,2),op) for x,y,op in ap.actions[ri]])
env.close()
