from env_client import make_env
from kin import *
import numpy as np, sys
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); x=float(sys.argv[3])
ys=np.round(np.arange(-0.6,0.6001,0.05),3)
if len(sys.argv)>4: ys=np.round(np.arange(float(sys.argv[4]),float(sys.argv[5])+1e-6,float(sys.argv[6])),3)
env = make_env()
B=(0,0,0); Rd=down_R(yaw)
def reset():
    o,_=env.reset(seed=seed); return o
obs=reset(); R=obs.get_object_from_name("robot")
objs=[]
for n in ['target_block','target_region','obstruction0','obstruction1','obstruction2','obstruction3']:
    try:
        o=obs.get_object_from_name(n); objs.append((obs.get(o,'pose_x'),obs.get(o,'pose_y')))
    except Exception: pass
def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
def goto(obs, qt, maxn=40):
    for _ in range(maxn):
        q=q_of(obs); d=qt-q
        if np.max(np.abs(d))<1e-4: break
        a=np.zeros(11,np.float32); a[3:10]=np.clip(d,-.2,.2)
        obs2,r,te,tr,_=env.step(a)
        if np.allclose(q_of(obs2),q): return obs2,False
        obs=obs2
    return obs,True
def moveto(obs,p):
    q=q_of(obs); qt,e=ik(q,np.array(p),Rd,B)
    if e>1e-3: return obs,False,e
    obs,ok=goto(obs,qt); return obs,ok,e
res=[]
for y in ys:
    if any(np.hypot(x-ox,y-oy)<0.09 for ox,oy in objs): res.append('O'); continue
    q=q_of(obs)
    _,e1=ik(q,np.array([x,y,0.36]),Rd,B); _,e2=ik(q,np.array([x,y,0.23]),Rd,B)
    if e1>1e-3 and e2>1e-3: res.append('N'); continue
    # up then across
    p=ee_pose(q,B)[:3,3]
    obs,ok,_=moveto(obs,[p[0],p[1],0.36])
    good=True
    for t in np.linspace(0,1,6)[1:]:
        obs,ok,e=moveto(obs,[p[0]+t*(x-p[0]),p[1]+t*(y-p[1]),0.36])
        if not ok: good=False; break
    if not good:
        obs=reset(); obs,ok,e=moveto(obs,[x,y,0.36])
        if not ok: res.append('T'); obs=reset(); continue
    stop=None; last=0.36
    for z in np.round(np.arange(0.35,0.0999,-0.01),3):
        obs,ok,e=moveto(obs,[x,y,z])
        if e>1e-3: stop='n%d'%round(z*100); break
        if not ok: stop='%d'%round(z*100); break
    res.append(stop if stop else 'F')
    for z in np.arange(ee_pose(q_of(obs),B)[2,3],0.37,0.02): obs,ok,e=moveto(obs,[x,y,min(z,0.36)])
print("%+.3f "%x+" ".join("%4s"%r for r in res), flush=True)
env.close()
