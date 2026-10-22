from probe_col_lib import R
from probe_col_bounds import approach
import numpy as np, sys
seed=int(sys.argv[1]); i=int(sys.argv[2]); sg=1 if i==0 else -1
r=R(seed)
X=0.30*sg; FAR=1.0*sg
r.goto(i,sg*1.0,-1.2) if i==0 else r.goto(i,-1.0,-1.2)
r.goto(i,FAR,-2.2); r.goto(i,X,-2.2)
res=[]
for y in np.arange(-2.27,1.56,0.05):
    if not r.goto(i,X,y):
        # detour
        r.goto(i,FAR,r.pos(i)[1]); r.goto(i,FAR,y)
        if not r.goto(i,X,y): res.append((round(y,2),'blk')); continue
    p=approach(r,i,(-sg*1.0,y),tol=5e-4)
    res.append((round(y,2),round(p[0],4)))
    r.goto(i,X,y)
bad=[t for t in res if t[1]=='blk' or abs(t[1]-sg*0.2271)>0.002]
print('seed',seed,'rover',i,'n',len(res),'non-standard:',bad)
