import numpy as np, sys
from env_client import make_env
from approach import *
np.set_printoptions(precision=4, suppress=True)
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
for i in range(1000):
    a=ap.get_action(obs)
    obs,r,te,tr,_=env.step(a)
    if i>int(sys.argv[2]): print(i, ap.mode, obs[[0,1,2,16,17]]-np.r_[obs[29:32],0,0], te)
    if te: break
