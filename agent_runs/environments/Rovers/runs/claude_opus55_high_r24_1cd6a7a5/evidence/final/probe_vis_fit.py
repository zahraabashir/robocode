import numpy as np
from probe_vis_geo import cam, segd
exec(open('probe_vis_geo2.py').read().split('for th')[0].split('\n',2)[2])
b=(-1.5267,0.3485)
best=[]
for ox in np.arange(-0.25,0.2501,0.0025):
  for oy in np.arange(-0.25,0.2501,0.0025):
    sc=0
    for v,o,p in [(v1,(-2.176,1.837),(-1.717,0.906)),(v2,(-0.4922,1.8822),(-0.907,1.268))]:
        offs=np.array([segd(cam(b,np.deg2rad(t),ox,oy),o,p)[1] for t in sorted(v)]); vis=np.array([v[t] for t in sorted(v)])
        # best interval [lo,hi] of invisibles: count errors
        bi=offs[vis==0]; lo,hi=bi.min(),bi.max()
        err=np.sum((offs>=lo)&(offs<=hi)&(vis==1))
        sc+=err
    best.append((sc,round(ox,4),round(oy,4)))
best.sort(); print(best[:15])
