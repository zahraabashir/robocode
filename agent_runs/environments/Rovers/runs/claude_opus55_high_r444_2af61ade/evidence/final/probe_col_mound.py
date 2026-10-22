from probe_col_lib import R
from probe_col_bounds import approach
import numpy as np
for seed in [1,2]:
    r=R(seed)
    print('seed',seed,[o for o in r.obst() if o[3]<0.1 and o[1]>0])
    r.goto(0,1.0,-1.5); r.goto(0,1.2,1.2)
    p=approach(r,0,(1.2,2.5)); print('r0 at x=1.2 up to', p)
    r.goto(0,1.2,1.2); r.goto(0,2.0,1.2)
    p=approach(r,0,(2.0,2.5)); print('r0 toward mound (2,2) from below', p)
    r.goto(0,2.0,1.2); r.goto(0,1.0,1.2); r.goto(0,0.5,1.2)
    p=approach(r,0,(0.5,2.5)); print('r0 toward mound (0.5,2) from below', p)
    # clamp vs reject test
    r.goto(0,1.0,1.2); r.goto(0,1.0,-1.5); r.goto(0,2.2,-1.5); print('at',r.pos(0)); print('step +0.2 ->',r.step(0,0.2,0))
    r.env.close()
