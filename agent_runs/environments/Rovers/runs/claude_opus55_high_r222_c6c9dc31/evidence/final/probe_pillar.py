import sys, math
import numpy as np
from env_client import make_env
env=make_env()
T=lambda n: env.observation_space.get_type(n)
seed=int(sys.argv[1]); pname=sys.argv[2]; rname=sys.argv[3] if len(sys.argv)>3 else 'rover1'
obs,_=env.reset(seed=seed)
rv=[o for o in obs.get_objects(T('rover')) if o.name==rname][0]
k=0 if rname=='rover0' else 4
pl=[o for o in obs.get_objects(T('obstacle')) if o.name==pname][0]
px,py=obs.get(pl,'x'),obs.get(pl,'y')
def pos(): return obs.get(rv,'x'),obs.get(rv,'y')
def mv(dx,dy):
    global obs
    a=np.zeros(8,np.float32); a[k]=dx; a[k+1]=dy; a[k+3]=1/6
    obs,*_=env.step(a)
def goto(tx,ty,n=60):
    for _ in range(n):
        x,y=pos()
        if abs(tx-x)<1e-4 and abs(ty-y)<1e-4: return True
        mv(np.clip(tx-x,-.2,.2),np.clip(ty-y,-.2,.2))
    return False
res=[]
for ang in range(0,360,30):
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a)
    R=0.45
    sx,sy=px+R*ux,py+R*uy
    # route: go via waypoint far out
    ok=goto(sx,sy)
    if not ok: res.append((ang,'unreach')); continue
    d=R
    while d>0.05:
        x,y=pos(); mv(-0.005*ux,-0.005*uy); x2,y2=pos()
        if abs(x2-x)<1e-6 and abs(y2-y)<1e-6: break
        d-=0.005
    x,y=pos()
    res.append((ang, round(x-px,3), round(y-py,3), round(math.hypot(x-px,y-py),3)))
    goto(sx,sy)
print('pillar',px,py)
for r in res: print(r)
