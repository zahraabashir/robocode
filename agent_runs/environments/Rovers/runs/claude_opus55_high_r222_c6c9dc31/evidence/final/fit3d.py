import json, glob, math
import numpy as np
exec(open('fit_vis.py').read().split("print('total'")[0])
def exit_frac(ax,ay,bx,by,cx,cy,hx,hy):
    dx,dy=bx-ax,by-ay; t0,t1=0.0,1.0
    for d,a,c,h in ((dx,ax,cx,hx),(dy,ay,cy,hy)):
        if abs(d)<1e-12:
            if abs(a-c)>h: return None
            continue
        u=(c-h-a)/d; v=(c+h-a)/d
        t0=max(t0,min(u,v)); t1=min(t1,max(u,v))
    return (t0,t1) if t0<=t1 else None
data=[]
for r in rows:
    if r['d']>=1.99: continue
    hits=[]
    for px,py,hx,hy,hz in obst[r['seed']]:
        if hx>0.1: continue
        e=exit_frac(r['cx'],r['cy'],r['ox'],r['oy'],px,py,hx,hy)
        if e: hits.append(e)
    data.append((hits,int(r['vis'])))
print(len(data))
best=[]
for h in np.arange(0.3,1.6,0.02):
    for zt in np.arange(-0.1,0.41,0.02):
        err=0
        for hits,vis in data:
            blocked=any(h+(zt-h)*t1<0.401 for t0,t1 in hits)
            err+= (blocked and vis==1) or ((not blocked) and vis==0)
        best.append((err,round(h,2),round(zt,2)))
best.sort(); print(best[:10])
k=0
for r in rows:
    if r['d']>=1.99 or r['vis']>0.5: continue
    hits=[]
    for px,py,hx,hy,hz in obst[r['seed']]:
        if hx>0.1: continue
        e=exit_frac(r['cx'],r['cy'],r['ox'],r['oy'],px,py,hx+0.01,hy+0.01)
        if e: hits.append(e)
    if not hits:
        k+=1
        if k<25: print('nohit invisible', r['seed'], r['r'], round(r['x'],2), round(r['y'],2), 'obj', round(r['ox'],2), round(r['oy'],2), 'd', round(r['d'],3), 'other rover', obst[r['seed']+1000])
print('count',k)
