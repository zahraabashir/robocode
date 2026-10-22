from env_client import make_env
import numpy as np, math
SEL={'sample':-0.8333,'cal':-0.5,'img':-0.1667,'noop':0.0,'send':0.5,'drop':0.8333}
class E:
    def __init__(s,seed):
        s.env=make_env(); s.obs,_=s.env.reset(seed=seed); s.seed=seed
    def r(s,i): return s.obs.get_object_from_name('rover%d'%i)
    def rs(s,i):
        o=s.r(i); return {f:s.obs.get(o,f) for f in ['x','y','theta','store_full','calibrated','at_home']}
    def objs(s):
        out={}
        for o in s.obs:
            if o.type.name=='objective':
                out[o.name]={f:s.obs.get(o,f) for f in ['x','y','z','have_image_rover0','have_image_rover1','received_image']}
        return out
    def step(s,i,dx=0,dy=0,dth=0,sel='noop',other=None):
        a=np.zeros(8,np.float32)
        a[4*i:4*i+4]=[dx,dy,dth,SEL[sel]]
        if other is not None: a[4*(1-i):4*(1-i)+4]=other
        s.obs,rew,te,tr,inf=s.env.step(a); return rew
    def goto(s,i,x,y,tol=1e-4,maxit=200):
        for _ in range(maxit):
            st=s.rs(i); ex=x-st['x']; ey=y-st['y']
            if abs(ex)<tol and abs(ey)<tol: return True
            dx=float(np.clip(ex,-0.2,0.2)); dy=float(np.clip(ey,-0.2,0.2))
            s.step(i,dx,dy)
            st2=s.rs(i)
            if abs(st2['x']-st['x'])<1e-9 and abs(st2['y']-st['y'])<1e-9:
                return False
        return False
    def path(s,i,pts):
        for p in pts:
            if not s.goto(i,*p): return False
        return True
    def turn(s,i,th,maxit=50):
        for _ in range(maxit):
            e=(th-s.rs(i)['theta']+math.pi)%(2*math.pi)-math.pi
            if abs(e)<1e-5: return
            s.step(i,0,0,float(np.clip(e,-0.4,0.4)))
    def close(s): s.env.close()
