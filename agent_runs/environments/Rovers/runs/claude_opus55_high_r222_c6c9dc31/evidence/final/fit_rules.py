import math
import numpy as np
exec(open('fit_vis.py').read().split("print('total'")[0])
for strictR in (0.06,0.07,0.075,0.08):
    miss=0; lost=0
    for r in rows:
        if r['d']>=1.99: continue
        b=any(seg_point_dist(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py)<strictR for px,py,hx,hy,hz in obst[r['seed']] if hx<0.1)
        if not b and r['vis']<0.5: miss+=1
        if b and r['vis']>0.5: lost+=1
    print('strict',strictR,'missed',miss,'lost-visible',lost)
for libR in (0.01,0.02,0.03,0.04):
  for dmax in (0.8,0.9,1.0,9):
    wb=0; mb=0
    for r in rows:
        if r['d']>=1.99: continue
        b=False
        for px,py,hx,hy,hz in obst[r['seed']]:
            if hx>0.1: continue
            if seg_point_dist(np.array(r['cx']),np.array(r['cy']),r['ox'],r['oy'],px,py)<libR and math.hypot(px-r['ox'],py-r['oy'])<dmax: b=True
        if b and r['vis']>0.5: wb+=1
        if not b and r['vis']<0.5: mb+=1
    print('lib',libR,dmax,'wrongly-blocked',wb,'missed',mb)
