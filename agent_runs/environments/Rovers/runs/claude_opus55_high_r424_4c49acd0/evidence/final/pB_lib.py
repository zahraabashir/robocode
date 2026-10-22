import numpy as np
from env_client import make_env
SEL=dict(sample=-0.8333,cal=-0.5,img=-0.1667,noop=0,send=0.5,drop=0.8333)
def R(s,n):
    o=s.get_object_from_name(n); return {f:round(float(s.get(o,f)),3) for f in ['x','y','theta','store_full','calibrated','at_home']}
def F(s,n):
    o=s.get_object_from_name(n); return {f:round(float(s.get(o,f)),3) for f in o.type.__dict__.get('features',[])} 
def dump(s):
    for n in sorted(s.get_object_names()):
        o=s.get_object_from_name(n)
        print(n, o.type.name, s.vec([o]).round(3).tolist())
class Sim:
    def __init__(s,seed=0):
        s.env=make_env(); s.obs,_=s.env.reset(seed=seed)
    def act(s,a0=(0,0,0,'noop'),a1=(0,0,0,'noop')):
        a=[a0[0],a0[1],a0[2],SEL[a0[3]],a1[0],a1[1],a1[2],SEL[a1[3]]]
        s.obs,r,te,tr,info=s.env.step(np.array(a,dtype=np.float32)); return r,te
    def r(s,i): return R(s.obs,'rover%d'%i)
    def goto(s,i,x,y,th=None,maxit=200):
        for _ in range(maxit):
            c=s.r(i); dx=np.clip(x-c['x'],-.2,.2); dy=np.clip(y-c['y'],-.2,.2)
            dth=0 if th is None else np.clip((th-c['theta']+np.pi)%(2*np.pi)-np.pi,-.4,.4)
            if abs(dx)<1e-3 and abs(dy)<1e-3 and abs(dth)<1e-3: return True
            a=(dx,dy,dth,'noop'); 
            p=s.r(i)
            if i==0: s.act(a0=a)
            else: s.act(a1=a)
            if s.r(i)==p: return False
        return False
def gp(s,i,pts,th=None):
    for p in pts:
        if not s.goto(i,p[0],p[1],th): return False
    return True
def objf(s,k,f): return float(s.obs.get(s.obs.get_object_from_name('objective%d'%k),f))
def prep0(seed=0):
    s=Sim(seed); s.goto(0,1.0,0.5); s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img'))
    assert objf(s,0,'have_image_rover0')==1
    return s
