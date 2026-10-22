import numpy as np
from env_client import make_env
np.set_printoptions(precision=5, suppress=True, linewidth=200)
def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
class E:
    def __init__(s): s.env=make_env()
    def reset(s,seed):
        s.obs,_=s.env.reset(seed=seed); return s.obs
    def step(s,a):
        a=np.clip(np.asarray(a,float),-0.049,0.049)
        s.obs,r,t,tr,info=s.env.step(a); return s.obs
    def goto(s,p,maxstep=0.049,tol=1e-9):
        for _ in range(2000):
            d=np.asarray(p)-s.obs[16:18]
            if np.linalg.norm(d)<tol: break
            n=np.abs(d).max()
            a=d if n<=maxstep else d*maxstep/n
            s.step(a)
        return s.obs
    def path(s,pts):
        b0=s.obs[0:3].copy()
        for p in pts: s.goto(p)
        return np.abs(s.obs[0:3]-b0).max()

def safe_goto_local(e, pl, rad=1.7):
    """navigate robot to local point pl (block frame) by going around at radius rad"""
    o=e.obs; c=o[0:2]; th=o[2]
    target=c+R(th)@np.asarray(pl)
    b0=o[0:3].copy()
    rp=o[16:18]-c
    a0=np.arctan2(rp[1],rp[0]); tp=target-c; a1=np.arctan2(tp[1],tp[0])
    pts=[c+rad*np.array([np.cos(a0),np.sin(a0)])]
    da=(a1-a0+np.pi)%(2*np.pi)-np.pi
    for k in range(1,13): a=a0+da*k/12; pts.append(c+rad*np.array([np.cos(a),np.sin(a)]))
    pts.append(target)
    mv=e.path(pts)
    return mv

def probe(e, seed, pl, dl, step=0.001, n=600):
    e.reset(seed); mv=safe_goto_local(e,pl)
    o=e.obs; b0=o[0:3].copy(); th=b0[2]; c=b0[0:2]
    dw=R(th)@np.asarray(dl,float); dw/=np.linalg.norm(dw)
    prev=R(th).T@(o[16:18]-c)
    for i in range(n):
        o=e.step(dw*step)
        if np.abs(o[0:3]-b0).max()>1e-9:
            return mv, prev, R(th).T@(o[16:18]-c), o[0:3]-b0
        prev=R(th).T@(o[16:18]-c)
    return mv,None,None,None

def run_push(e, seed, pl, dl, step, n, pre_contact=True):
    """go to local pl, then move along local dir dl (fixed world dir) with given step for n steps. returns list of obs"""
    e.reset(seed); mv=safe_goto_local(e,pl)
    o=e.obs; th=o[2]
    dw=R(th)@np.asarray(dl,float); dw/=np.linalg.norm(dw)
    obs=[o.copy()]
    for i in range(n):
        obs.append(e.step(dw*step).copy())
    return mv,np.array(obs),dw*step
