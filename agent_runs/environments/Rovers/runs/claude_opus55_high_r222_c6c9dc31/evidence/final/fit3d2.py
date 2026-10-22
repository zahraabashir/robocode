import math
import numpy as np
exec(open('fit3d.py').read().split("data=[]")[0])
def circ_frac(ax,ay,bx,by,cx,cy,R):
    dx,dy=bx-ax,by-ay; fx,fy=ax-cx,ay-cy
    a=dx*dx+dy*dy; b=2*(fx*dx+fy*dy); c=fx*fx+fy*fy-R*R
    disc=b*b-4*a*c
    if disc<0: return None
    sq=math.sqrt(disc); t0=(-b-sq)/(2*a); t1=(-b+sq)/(2*a)
    if t1<0 or t0>1: return None
    return max(t0,0),min(t1,1)
import itertools
for shape in ('box','cyl'):
  for R in (0.04,0.05,0.06,0.07):
    data=[]
    for r in rows:
        if r['d']>=1.99: continue
        hits=[]
        for px,py,hx,hy,hz in obst[r['seed']]:
            if hx>0.1: continue
            e=exit_frac(r['cx'],r['cy'],r['ox'],r['oy'],px,py,R,R) if shape=='box' else circ_frac(r['cx'],r['cy'],r['ox'],r['oy'],px,py,R)
            if e: hits.append(e)
        data.append((hits,int(r['vis'])))
    best=[]
    for h in np.arange(0.3,1.6,0.04):
        for zt in np.arange(-0.2,0.45,0.04):
          for top in (0.401,):
            err=0
            for hits,vis in data:
                blocked=any(h+(zt-h)*t1<top for t0,t1 in hits)
                err+= (blocked and vis==1) or ((not blocked) and vis==0)
            best.append((err,round(h,2),round(zt,2)))
    best.sort(); print(shape,R,best[:3], 'pure2d', sum((len(hh)>0)!=(v==0) for hh,v in data))
print('--- errors cyl .05 h=.66 zt=.08')
for r in rows:
    if r['d']>=1.99: continue
    for px,py,hx,hy,hz in obst[r['seed']]:
        if hx>0.1: continue
        e=circ_frac(r['cx'],r['cy'],r['ox'],r['oy'],px,py,0.075)
        if not e: continue
        L=r['d']; perp=float(seg_point_dist(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py))
        e5=circ_frac(r['cx'],r['cy'],r['ox'],r['oy'],px,py,0.05)
        blocked = e5 is not None and 0.66+(0.08-0.66)*e5[1]<0.401
        if blocked != (r['vis']<0.5):
            print(r['seed'],r['r'],round(r['x'],2),round(r['y'],2),'L',round(L,3),'perp',round(perp,3),'dcam',round(L*(e[0]+e[1])/2,3),'dobj',round(L*(1-(e[0]+e[1])/2),3),'vis',int(r['vis']))
