import sys
import numpy as np
from env_client import make_env
import approach
from approach import GeneratedApproach
seed=int(sys.argv[1]); upto=int(sys.argv[2])
env = make_env()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=seed); ap.reset(obs, info)
print(ap.legs)
orig=ap._control
def wrap(x,y,a,tx,tg,G,B,obs_):
    out=orig(x,y,a,tx,tg,G,B,obs_)
    if wrap.on: print("CTRL",round(x,3),round(y,3),round(a,3),"t",round(tx,3),round(tg,3),"G",np.round(G,3).tolist(),"obs",np.round(obs_,3).tolist(),"->",np.round(out[:3],3))
    return out
wrap.on=False
ap._control=wrap
for t in range(upto):
    wrap.on = t>=upto-3
    a = ap.get_action(obs)
    obs, rew, te, tr, _ = env.step(a)
    if te: break
env.close()
