from probe_send_lib import E, SEL
import numpy as np, math, time
def setup(seed, P0, th0, Q, h1, wp1=()):
    e=E(seed)
    # rover1 to Q via waypoints
    for w in list(wp1)+[Q]:
        if not e.goto(1,*w,tol=1e-4,maxit=100): return e,'r1 blocked at %s'%(e.pose(1),)
    e.turn(1,h1)
    # rover0 sample
    if not e.goto(0,1.28,-0.95+0.0,tol=1e-3): return e,'r0 blocked to sample'
    e.act(0,(0,0,0),SEL['sample'])
    if e.g('rover0','store_full')<0.5: return e,'sample failed'
    if not e.goto(0,*P0,tol=1e-4): return e,'r0 blocked to P0 %s'%(e.pose(0),)
    e.turn(0,th0)
    return e,None
def sweep(seed,P0,th0,Q,h1,d,step=0.004,n=60,wp1=()):
    e,err=setup(seed,P0,th0,Q,h1,wp1)
    if err: return dict(err=err)
    p0=e.pose(0); hist=[]
    for i in range(n):
        before=e.pose(1)
        mv=(d[0]*step,d[1]*step,0) if i>0 else (0,0,0)
        e.step((0,0,0,SEL['send']),mv+(0,))
        p1=e.pose(1)
        if i>0 and (d[0] or d[1]) and abs(p1[0]-before[0])+abs(p1[1]-before[1])<1e-7: return dict(err='r1 stuck',p0=p0,p1=p1)
        if e.feats('sample5')[6]>0.5:
            return dict(i=i,p0=p0,p1=p1,prev=before if i>0 else None)
    return dict(i=None,p0=p0,p1=e.pose(1))
