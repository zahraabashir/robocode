import sys
from env_client import make_env
import numpy as np, kin
from common import *
env = make_env()
obs, info = env.reset(seed=0)
base = getbase(obs)
for (x,y) in [(0.2,-0.1),(0.3,-0.2),(0.15,0.0)]:
    p = np.array([x,y,0.40])
    for z in np.arange(0.40, -0.2, -0.005):
        p[2]=z
        qt, ok = kin.ik(base, getq(obs), p, kin.topdown_R(0))
        obs, blocked = move_to(env, obs, qt)
        if blocked or not ok: print(x,y,'blocked at', round(z,3), ok); break
    p[2]=0.4; qt, ok = kin.ik(base, getq(obs), p, kin.topdown_R(0)); obs,_=move_to(env,obs,qt)
