from probe_col_lib import R
from probe_col_bounds import approach, rot
import numpy as np, sys
c=np.array([float(sys.argv[2]),2.0]); RAD=0.75
r=R(2)
r.goto(0,1.0,-1.0); r.goto(0,1.2,1.0)
rot(r,0,float(sys.argv[1]))
for k in range(180,365,10):
    a=np.deg2rad(k); S=c+RAD*np.array([np.cos(a),np.sin(a)])
    S=np.clip(S,0.24,2.26)
    if not r.goto(0,1.2,1.0) or not r.goto(0,*S): print(k,'nav fail',r.pos(0)); continue
    p=approach(r,0,c,tol=2e-4); rel=p[:2]-c
    cx,cy=np.clip(rel,-0.25,0.25)
    print('%4d rel %.4f %.4f  dbox=%.4f'%(k,rel[0],rel[1],np.hypot(rel[0]-cx,rel[1]-cy)))
