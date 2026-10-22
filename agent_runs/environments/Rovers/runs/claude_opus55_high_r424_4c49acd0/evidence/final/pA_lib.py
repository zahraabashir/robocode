from env_client import make_env
import numpy as np
class P:
    def __init__(self,seed=0):
        self.env=make_env(); self.reset(seed)
    def reset(self,seed=0):
        self.obs,_=self.env.reset(seed=seed); return self
    def st(self,name):
        o=self.obs.get_object_from_name(name)
        out={}
        for f in ['x','y','theta','store_full','calibrated','at_home','z','half_x','half_y','half_z']:
            try: out[f]=float(self.obs.get(o,f))
            except Exception: pass
        return out
    def pos(self,i):
        s=self.st('rover%d'%i); return np.array([s['x'],s['y'],s['theta']])
    def step(self,a0=(0,0,0,0),a1=(0,0,0,0)):
        a=np.array(list(a0)+list(a1),dtype=np.float32)
        self.obs,r,te,tr,info=self.env.step(a); return r,te,tr
    def mv(self,i,dx,dy,dth=0,sel=0):
        a=[dx,dy,dth,sel]; z=[0,0,0,0]
        before=self.pos(i)
        self.step(a,z) if i==0 else self.step(z,a)
        after=self.pos(i)
        return after, not np.allclose(before,after,atol=1e-6)
    def goto(self,i,x,y,th=None,maxit=200):
        """greedy; returns final pos; tries axis-sliding if blocked"""
        for _ in range(maxit):
            p=self.pos(i); d=np.array([x,y])-p[:2]
            dth=0 if th is None else ((th-p[2]+np.pi)%(2*np.pi)-np.pi)
            if np.linalg.norm(d)<1e-4 and abs(dth)<1e-4: break
            dd=np.clip(d,-0.2,0.2); dt=np.clip(dth,-0.4,0.4)
            _,ok=self.mv(i,dd[0],dd[1],dt)
            if not ok:
                _,ok=self.mv(i,dd[0],0,0)
                if not ok: _,ok=self.mv(i,0,dd[1],0)
                if not ok: _,ok=self.mv(i,0,0,dt)
                if not ok: break
        return self.pos(i)
    def probe(self,i,dx,dy,dth=0,n=500):
        """step repeatedly until blocked"""
        for k in range(n):
            p,ok=self.mv(i,dx,dy,dth)
            if not ok: return p,k
        return p,n
    def bisect(self,i,ux,uy,lo=0.2):
        """from current pos, coarse probe in unit dir then refine to 1e-4"""
        s=0.2
        while s>1e-4:
            p,k=self.probe(i,ux*s,uy*s)
            s/=2
        return self.pos(i)
