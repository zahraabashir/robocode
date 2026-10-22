from env_client import make_env
import numpy as np, time
env=make_env()
RV='rover1'
def reset(seed):
    global obs, r1, T
    obs,info=env.reset(seed=seed)
    T={t.name:t for t in env.observation_space.types}
    r1=obs.get_object_from_name(RV)
    return obs
def pos(): return np.array([obs.get(r1,'x'),obs.get(r1,'y'),obs.get(r1,'theta')])
def step(dx=0,dy=0,dth=0,op=1/6):
    global obs
    a=[0,0,0,1/6]; b=[dx,dy,dth,op]
    act=a+b if RV=='rover1' else b+a
    obs,*_=env.step(np.array(act,dtype=np.float32))
    return obs
def goto(wps):
    for wp in wps:
        for _ in range(60):
            d=np.clip(np.array(wp[:2])-pos()[:2],-0.2,0.2)
            if np.abs(d).max()<1e-7: break
            step(d[0],d[1])
    return pos()
def turn(th):
    for _ in range(40):
        e=(th-pos()[2]+np.pi)%(2*np.pi)-np.pi
        if abs(e)<1e-7: break
        step(0,0,float(np.clip(e,-0.4,0.4)))
    return pos()
def cal():
    step(op=-0.5); return obs.get(r1,'calibrated')
def objpos(name):
    o=obs.get_object_from_name(name); return np.array([obs.get(o,'x'),obs.get(o,'y'),obs.get(o,'z')])
def imaged():
    return [o.name for o in obs.get_objects(T['objective']) if obs.get(o,'have_image_'+RV)>0.5]
def scan(seed,name,ang,r0,r1_,dr,th=0.0,via=None,mode='cal',pre=None):
    """walk along ray at angle ang from objective, radius r0 -> r1_. mode 'cal': first calibrate success.
    mode 'img': at each point cal+img, stop when `name` imaged. pre: point to go first and image there."""
    reset(seed); c=objpos(name)[:2]; u=np.array([np.cos(ang),np.sin(ang)])
    start=c+r0*u
    if pre is not None:
        goto(pre); cal(); step(op=-1/6)
    p=goto((via or [])+[tuple(start)])
    if np.linalg.norm(p[:2]-start)>1e-4: return ('unreach',p.round(3))
    turn(th)
    r=r0; n=int(round(abs(r0-r1_)/dr))+1
    for i in range(n):
        r=r0+(r1_-r0)*i/max(n-1,1)
        q=goto([tuple(c+r*u)])
        if np.linalg.norm(q[:2]-(c+r*u))>1e-4: return ('blocked',r,q.round(3))
        ok=cal()>0.5
        if mode=='cal' and ok:
            step(op=-1/6); return (round(r,4), imaged(), pos().round(4))
        if mode=='img':
            step(op=-1/6)
            if name in imaged(): return (round(r,4), pos().round(4))
    return None
def bis(seed,name,ang,th,lo=1.5,hi=2.3,via=None,mode='cal',pre=None):
    a=scan(seed,name,ang,hi,lo,0.01,th=th,via=via,mode=mode,pre=pre)
    if not a or isinstance(a[0],str): return a
    b=scan(seed,name,ang,a[0]+0.01,a[0]-0.001,0.0005,th=th,via=via,mode=mode,pre=pre)
    return b
def model(base,th,obj,ox=-0.087,oy=-0.0125):
    cam=np.array([base[0]+ox*np.cos(th)-oy*np.sin(th), base[1]+ox*np.sin(th)+oy*np.cos(th)])
    return np.linalg.norm(np.array(obj[:2])-cam)
