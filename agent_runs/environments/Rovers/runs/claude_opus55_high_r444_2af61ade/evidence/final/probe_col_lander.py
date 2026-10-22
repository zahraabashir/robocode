from probe_col_lib import R
from probe_col_bounds import approach, rot
import numpy as np, sys
c=np.array([-1.9,-2.0]); RAD=1.0
r=R(4)
print([o for o in r.obst() if o[1]<0 and o[2]<0 and o[3]<0.1])
rot(r,1,float(sys.argv[1]))
r.goto(1,-1.0,-1.2)
for k in range(-30,185,5):
    a=np.deg2rad(k); S=c+RAD*np.array([np.cos(a),np.sin(a)])
    S=np.clip(S,-2.26,-0.24)
    if k>100: r.goto(1,-1.0,-1.2); r.goto(1,-2.0,-1.2)
    if not r.goto(1,-1.0,-1.2) or not r.goto(1,*S): print(k,'nav fail',r.pos(1)); continue
    p=approach(r,1,c,tol=2e-4); rel=p[:2]-c
    print('%4d rel %.4f %.4f  r=%.4f th=%.3f'%(k,rel[0],rel[1],np.hypot(*rel),p[2]))
