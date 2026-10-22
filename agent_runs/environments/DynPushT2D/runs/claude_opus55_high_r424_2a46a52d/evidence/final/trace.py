import sys, numpy as np
from env_client import make_env
import approach
seed=int(sys.argv[1])
params = eval(sys.argv[2]) if len(sys.argv)>2 else {}
for k,v in params.items(): setattr(approach.GeneratedApproach,k,v)
env=make_env(); obs,info=env.reset(seed=seed)
ap=approach.GeneratedApproach(None,None,{}); ap.reset(obs,info)
orig=ap._plan_push
def pp(o):
    b,c0=orig(o)
    g=ap.goal; print(f"t={ap.nsteps} blk=({o[0]-g[0]:+.3f},{o[1]-g[1]:+.3f},{approach._wrap(o[2]-g[2]):+.3f}) cost={c0:.3f} -> pred {b[4]:.3f} k={b[3]} step={np.linalg.norm(b[2]):.3f} navdist={np.linalg.norm(b[1]-o[16:18]):.2f}")
    return b,c0
ap._plan_push=pp
for t in range(1000):
    a=ap.get_action(obs); obs,r,term,trunc,_=env.step(a)
    if term: print("done",t+1); break
