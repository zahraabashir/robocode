import sys, numpy as np, approach
from env_client import make_env
seed=int(sys.argv[1]); N=int(sys.argv[2])
env=make_env(); obs,info=env.reset(seed=seed)
ap=approach.GeneratedApproach(env.action_space, env.observation_space, None); ap.reset(obs,info)
orig=ap._dp_path3
def wrap(x0,y0,arm0,x1,tipy1,obstacles,ctip):
    r=orig(x0,y0,arm0,x1,tipy1,obstacles,ctip)
    if r is None:
        print('DP3 FAIL', x0,y0,arm0,x1,tipy1,ctip, obstacles)
        A=ap.ARMS
        for a in A:
            for yy in np.arange(0.2,0.9,0.05):
                print(a, round(yy,2), ap._free_pts3(np.array([x0]),np.array([yy]),obstacles,ctip,a), ap._free_pts3(np.array([x1]),np.array([yy]),obstacles,ctip,a))
    return r
ap._dp_path3=wrap
for i in range(N):
    a=ap.get_action(obs); obs,*_=env.step(a)
