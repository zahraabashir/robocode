import sys, math
import numpy as np
from env_client import make_env
env=make_env()
T=lambda n: env.observation_space.get_type(n)
seed=int(sys.argv[1]); pname=sys.argv[2]; rname=sys.argv[3]; dth=float(sys.argv[4]) if len(sys.argv)>4 else 0.0
obs,_=env.reset(seed=seed)
rv=[o for o in obs.get_objects(T('rover')) if o.name==rname][0]
k=0 if rname=='rover0' else 4
pl=[o for o in obs.get_objects(T('obstacle')) if o.name==pname][0]
px,py=obs.get(pl,'x'),obs.get(pl,'y')
def pos(): return obs.get(rv,'x'),obs.get(rv,'y')
def mv(dx,dy,th=0.0):
    global obs
    a=np.zeros(8,np.float32); a[k]=dx; a[k+1]=dy; a[k+2]=th; a[k+3]=1/6
    obs,*_=env.step(a)
def goto(tx,ty,n=80):
    for _ in range(n):
        x,y=pos()
        if abs(tx-x)<1e-4 and abs(ty-y)<1e-4: return True
        mv(np.clip(tx-x,-.2,.2),np.clip(ty-y,-.2,.2))
    return False
R=0.55
goto(px+R,py)
# rotate
th0=obs.get(rv,'theta'); target=th0+dth
for _ in range(10):
    th=obs.get(rv,'theta'); d=(target-th+math.pi)%(2*math.pi)-math.pi
    if abs(d)<1e-4: break
    mv(0,0,float(np.clip(d,-.4,.4)))
print('theta',obs.get(rv,'theta'))
res=[]
for ang in range(0,360,10):
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a)
    if not goto(px+R*ux,py+R*uy): print(ang,'unreach'); continue
    lo=0.0
    # coarse then fine
    for step in (0.02,0.0025):
        while True:
            x,y=pos(); mv(-step*ux,-step*uy); x2,y2=pos()
            if abs(x2-x)<1e-7 and abs(y2-y)<1e-7: break
    x,y=pos()
    print(ang, round(x-px,4), round(y-py,4), 'r=',round(math.hypot(x-px,y-py),4), flush=True)
    goto(px+R*ux,py+R*uy)
