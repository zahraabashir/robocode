import time, numpy as np
from env_client import make_env
import approach
env=make_env(); obs,info=env.reset(seed=5)
ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
t=time.time(); b=ap._plan_push(obs); print("plan", time.time()-t)
t=time.time(); a=ap._navigate(obs,b[0][1]); print("nav", time.time()-t, len(a))
t=time.time(); p=ap._astar(obs[16:18], b[0][1], obs[0:2], obs[2], 0.115); print("astar", time.time()-t)
print("ncand", len(ap.c_pts))
