from probe_col_lib import R
from probe_col_bounds import approach, rot
import numpy as np, sys
c=np.array([0.654,-0.199]); RAD=0.42
th=float(sys.argv[1]); k0=int(sys.argv[2])
r=R(0); r.path(0,[(1.0,-1.0),(c[0]+RAD,c[1])]); rot(r,0,th)
for kk in range(0,k0+1,10):
    r.goto(0,*(c+RAD*np.array([np.cos(np.deg2rad(kk)),np.sin(np.deg2rad(kk))])))
for k in range(k0,k0+90,2):
    a=np.deg2rad(k); S=c+RAD*np.array([np.cos(a),np.sin(a)])
    if not r.goto(0,*S): print('navfail',k); break
    p=approach(r,0,c,tol=1e-4); rel=p[:2]-c
    cx,cy=np.clip(rel,-.05,.05); print(k,'%.4f'%np.hypot(rel[0]-cx,rel[1]-cy)); r.goto(0,*S)
