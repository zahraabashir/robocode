"""Approximate quasi-static push model for the T block (fitted to env).
Body frame: origin = obs[0:2]; bar: x in [-L/2,L/2], y in [-w,0]; stem: x in [-w/2,w/2], y in [-w-Lv,-w].
Motion: sticking/sliding point contact (mu=1), ellipsoidal limit surface == free body impulse model about CoM,
c^2 = I/m of uniform-density T."""
import numpy as np
MU=1.0; RP=0.1
def Rm(t): c,s=np.cos(t),np.sin(t); return np.array([[c,-s],[s,c]])
def geom(w,L,Lv):
    a1,a2=w*L,w*Lv; y1,y2=-w/2,-w-Lv/2
    yc=(a1*y1+a2*y2)/(a1+a2)
    I=a1*((L*L+w*w)/12+(y1-yc)**2)+a2*((w*w+Lv*Lv)/12+(y2-yc)**2)
    return dict(w=w,L=L,Lv=Lv,C=np.array([0.0,yc]),c2=I/(a1+a2),
                rects=[(-L/2,L/2,-w,0.0),(-w/2,w/2,-w-Lv,-w)])
def closest(g,p):
    """closest point on T boundary to p (body frame), signed distance, outward normal"""
    best=None
    for (x0,x1,y0,y1) in g['rects']:
        q=np.array([min(max(p[0],x0),x1),min(max(p[1],y0),y1)])
        d=np.linalg.norm(p-q)
        if d>1e-12: n=(p-q)/d; sd=d
        else:  # inside rect
            ds=[p[0]-x0,x1-p[0],p[1]-y0,y1-p[1]]; k=int(np.argmin(ds)); sd=-ds[k]
            n=[np.array([-1,0.]),np.array([1,0.]),np.array([0,-1.]),np.array([0,1.])][k]
            q=p-n*sd
        if best is None or sd<best[0]: best=(sd,q,n)
    return best
def twist_from_force(g,cp,f):
    r=cp-g['C']; w=(r[0]*f[1]-r[1]*f[0])/g['c2']
    return np.array([f[0],f[1]]),w   # velocity of C, omega
def contact_vel(v,w,r): return v+w*np.array([-r[1],r[0]])
def sim_substep(g,pose,pb_world,dp_world,rp=RP):
    """pose=(x,y,th). pusher moves by dp. returns new pose"""
    x,y,th=pose; Rt=Rm(th)
    p_new=Rt.T@(pb_world+dp_world-np.array([x,y]))
    sd,q,n=closest(g,p_new)
    pen=rp-sd
    if pen<=0: return np.array(pose,float)
    u=Rt.T@dp_world  # pusher velocity body
    r=q-g['C']; c2=g['c2']
    # sticking
    A=np.array([[1+r[1]**2/c2,-r[0]*r[1]/c2],[-r[0]*r[1]/c2,1+r[0]**2/c2]])
    un=np.dot(u,n)
    # required contact displacement: normal component = penetration removal
    t=np.array([-n[1],n[0]])
    utan=np.dot(u,t)
    dcont=-pen*n + utan*t   # want contact pt to move by this (normal: remove penetration)
    f=np.linalg.solve(A,dcont)
    fn=-np.dot(f,n); ft=np.dot(f,t)
    if fn<=0: return np.array(pose,float)
    if abs(ft)>MU*fn:
        fdir=-n+MU*np.sign(ft)*t
        v1,w1=twist_from_force(g,q,fdir); cv=contact_vel(v1,w1,r)
        lam=pen/(-np.dot(cv,n)); f=lam*fdir
    v,w=twist_from_force(g,q,f)
    # displacement of origin in body frame: v_C + w x (0-C)
    vo=v+w*np.array([g['C'][1],-g['C'][0]])
    # integrate exactly as rotation about ICR-ish (small): use midpoint rotation
    dpos=Rm(th+w/2)@vo
    return np.array([x+dpos[0],y+dpos[1],th+w])
KAPPA=0.265  # block ends each step separated by extra KAPPA*normal pusher step (velocity-dependent gap)
def sim_step(g,pose,pb_world,action,nsub=10,kappa=KAPPA):
    pose=np.array(pose,float); pb=np.array(pb_world,float); a=np.asarray(action,float); d=a/nsub
    sd,q,n=closest(g,Rm(pose[2]).T@(pb+a-pose[0:2]))
    un=max(0.0,-np.dot(Rm(pose[2]).T@a,n))
    rp=RP+kappa*un
    for _ in range(nsub):
        pose=sim_substep(g,pose,pb,d,rp); pb=pb+d
    return pose,pb
