from env_client import make_env
import numpy as np
R=1.6
def rot(th): c,s=np.cos(th),np.sin(th); return np.array([[c,-s],[s,c]])
class Prober:
    def __init__(s): s.env=make_env()
    def reset(s,seed):
        s.seed=seed; s.obs,_=s.env.reset(seed=seed); s.b0=s.obs[0:3].copy(); return s.obs
    def moved(s): return np.max(np.abs(s.obs[0:3]-s.b0))>1e-7
    def step(s,a):
        s.obs,*_=s.env.step(np.clip(np.asarray(a,float),-0.0499,0.0499))
    def goto(s,p,maxstep=0.04):
        for _ in range(2000):
            d=p-s.obs[16:18]; n=np.linalg.norm(d)
            if n<1e-9: return
            a=d if n<=maxstep else d/n*maxstep
            s.step(a)
            if n<=maxstep: return
    def nav(s,world_pt):
        c=s.b0[:2]; r=s.obs[16:18]-c; ang=np.arctan2(r[1],r[0])
        s.goto(c+R*np.array([np.cos(ang),np.sin(ang)]))
        v=world_pt-c; tang=np.arctan2(v[1],v[0])
        da=(tang-ang+np.pi)%(2*np.pi)-np.pi
        n=int(abs(da)/0.02)+1
        for k in range(1,n+1):
            a=ang+da*k/n; s.goto(c+R*np.array([np.cos(a),np.sin(a)]))
        s.goto(world_pt)
    def probe(s,seed,start_b,dir_b,maxdist=2.0,fine=0.0002):
        """start_b, dir_b in body frame. returns distance travelled at contact (bounds)."""
        th=s.b0[2]; M=rot(th)
        s.reset(seed); c=s.b0[:2]; start_w=c+M@start_b; d=M@(dir_b/np.linalg.norm(dir_b))
        s.nav(start_w)
        if s.moved(): return None,'moved during nav'
        p0=s.obs[16:18].copy(); t=0
        while t<maxdist:
            prev=s.obs[16:18].copy(); s.step(d*0.005); t+=0.005
            if s.moved(): break
        else: return None,'no contact'
        coarse=np.dot(prev-p0,d)
        s.reset(seed); s.nav(start_w); p0=s.obs[16:18].copy()
        s.goto(p0+d*(coarse-0.006),0.005)
        while True:
            prev=s.obs[16:18].copy(); s.step(d*fine)
            if s.moved(): break
        dprev=np.dot(prev-p0,d); dnow=np.dot(s.obs[16:18]-p0,d)
        # contact point robot center in body frame
        pb_prev=M.T@(prev-c); pb_now=M.T@(s.obs[16:18]-c)
        return (pb_prev,pb_now),'ok'
