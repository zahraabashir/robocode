from pE_lib import *
import time
def pose(s,i):
    o=s.obs.get_object_from_name('rover%d'%i); v=s.obs.vec([o]); return np.array([float(v[0]),float(v[1]),float(v[2])])
def step(s,i,dx,dy,dth=0.0):
    a=(dx,dy,dth,'noop')
    if i==0: s.act(a0=a)
    else: s.act(a1=a)
    return pose(s,i)
def go(s,i,x,y,th=None,maxit=60):
    for _ in range(maxit):
        p=pose(s,i); dx=np.clip(x-p[0],-.2,.2); dy=np.clip(y-p[1],-.2,.2)
        dth=0 if th is None else np.clip((th-p[2]+np.pi)%(2*np.pi)-np.pi,-.4,.4)
        if abs(dx)<1e-6 and abs(dy)<1e-6 and abs(dth)<1e-6: return True
        q=step(s,i,dx,dy,dth)
        if np.allclose(q,p,atol=1e-7): return False
    return False
def approach(s,i,px,py,ux,uy,d0=0.5):
    """start at pillar + d0*u, move along -u, return min centre distance reached (projected along u)."""
    if not go(s,i,px+d0*ux,py+d0*uy): return None
    for h in (0.04,0.02,0.01,0.005,0.0025,0.00125):
        for _ in range(40):
            p=pose(s,i); q=step(s,i,-h*ux,-h*uy)
            if np.allclose(q,p,atol=1e-7): break
    p=pose(s,i); return float(np.hypot(p[0]-px,p[1]-py)), p
