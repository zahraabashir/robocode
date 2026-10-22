import math, json, numpy as np
def seg_box_hit(p,q,lo,hi):
    # slab test for 3D segment p->q vs box [lo,hi]
    t0,t1=0.0,1.0
    for k in range(len(p)):
        d=q[k]-p[k]
        if abs(d)<1e-12:
            if p[k]<lo[k] or p[k]>hi[k]: return False
        else:
            a=(lo[k]-p[k])/d; b=(hi[k]-p[k])/d
            if a>b: a,b=b,a
            t0=max(t0,a); t1=min(t1,b)
            if t0>t1: return False
    return True
def visible(rx,ry,th,obj,obstacles,a=-0.087,b=-0.0125,zc=None,D=1.99758,infl=0.0,dim3=True,ozoff=0.0,skip_own=True):
    cx=rx+a*math.cos(th)-b*math.sin(th); cy=ry+a*math.sin(th)+b*math.cos(th)
    ox,oy,oz=obj
    if math.hypot(ox-cx,oy-cy)>D: return False
    for (x,y,z,hx,hy,hz) in obstacles:
        if skip_own and abs(x-ox)<=hx and abs(y-oy)<=hy: continue
        if dim3:
            if seg_box_hit((cx,cy,zc),(ox,oy,oz+ozoff),(x-hx-infl,y-hy-infl,z-hz),(x+hx+infl,y+hy+infl,z+hz)): return False
        else:
            if seg_box_hit((cx,cy),(ox,oy),(x-hx-infl,y-hy-infl),(x+hx+infl,y+hy+infl)): return False
    return True
