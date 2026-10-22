from env_client import make_env
import numpy as np
class R:
    def __init__(self, seed=0):
        self.env=make_env(); self.obs,_=self.env.reset(seed=seed)
    def pos(self,i):
        o=self.obs.get_object_from_name(f'rover{i}')
        return np.array([self.obs.get(o,'x'),self.obs.get(o,'y'),self.obs.get(o,'theta')],float)
    def step(self,i,dx=0,dy=0,dth=0):
        a=np.zeros(8,np.float32); a[4*i:4*i+3]=[dx,dy,dth]
        self.obs,*_=self.env.step(a)
        return self.pos(i)
    def goto(self,i,x,y,maxit=200):
        for _ in range(maxit):
            p=self.pos(i); d=np.array([x,y])-p[:2]
            if np.linalg.norm(d)<1e-6: return True
            d=np.clip(d,-0.2,0.2)
            q=self.step(i,*d)
            if np.allclose(q[:2],p[:2]): return False
        return False
    def path(self,i,pts):
        for (x,y) in pts:
            if not self.goto(i,x,y): print('blocked going to',(x,y),'at',self.pos(i)); return False
        return True
    def push(self,i,ux,uy,step=0.005,maxit=2000):
        """move in direction (ux,uy) with given step until blocked; return last pos"""
        u=np.array([ux,uy],float); u/=np.linalg.norm(u)
        # coarse
        for s in [0.05,step]:
            for _ in range(maxit):
                p=self.pos(i); q=self.step(i,*(u*s))
                if np.allclose(q[:2],p[:2],atol=1e-9): break
        # finer
        for s in [0.001]:
            for _ in range(maxit):
                p=self.pos(i); q=self.step(i,*(u*s))
                if np.allclose(q[:2],p[:2],atol=1e-9): break
        return self.pos(i)
    def obst(self):
        out=[]
        for o in self.obs:
            if o.type.name=='obstacle':
                out.append((o.name,self.obs.get(o,'x'),self.obs.get(o,'y'),self.obs.get(o,'half_x')))
        return out
