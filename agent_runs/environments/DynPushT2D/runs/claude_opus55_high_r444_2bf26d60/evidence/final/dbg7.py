import numpy as np, sys
from env_client import make_env
from approach import *
np.set_printoptions(precision=3, suppress=True)
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
ap=GeneratedApproach(None,None,{}); ap.reset(obs,{})
prev=None
for i in range(1000):
    m0=ap.mode
    a=ap.get_action(obs)
    if ap.mode=="nav" and m0!="nav":
        L=sum(np.linalg.norm(np.diff(np.vstack([obs[16:18]]+ap.path),axis=0),axis=1))
        print(i,"NAV start rob",obs[16:18],"path",np.round(np.array(ap.path),2).tolist(),"len %.2f steps %.0f"%(L,L/0.049), "pose",obs[0:3])
    obs,r,te,tr,_=env.step(a)
    if te: print("done",i); break
