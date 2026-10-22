import sys
from test_approach import *
import approach
seed=int(sys.argv[1])
env = make_env(); obs, info = env.reset(seed=seed); env.close()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
orig=ap._rover_tables
def wrap(*a, **k):
    P,t=orig(*a,**k)
    print('rover',a[0], sorted([(tuple(sorted(map(str,key))),v[0]) for key,v in t.items()], key=lambda z:z[1])[:40])
    return P,t
ap._rover_tables=wrap
ap.reset(obs, info)
