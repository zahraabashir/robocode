import sys
from test_approach import *
import numpy as np
seed=int(sys.argv[1]); N=int(sys.argv[2])
env = make_env(); obs, info = env.reset(seed=seed)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
def show(o):
    for n in sorted(o.get_object_names()):
        if n.startswith(('rover','lander','sample','objective')):
            ob=o.get_object_from_name(n); print(" ",n, dict(zip(o.type_features[ob.type], np.round(o.data[ob],3))))
for t in range(N):
    a=ap.get_action(obs); obs,r,term,tr,info=env.step(a)
print("t",N); 
try: show(obs)
except Exception as e: print(e); print(obs)
print(info)
