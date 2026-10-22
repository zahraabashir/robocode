import sys, json, math, itertools
import numpy as np
from probe_vis_model import *
from probe_vis_lib import E
sets=[]
for f in sys.argv[1:]:
    d=json.load(open(f)); e=E(d['seed'])
    ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
    obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']
    e.close(); sets.append((obj,obs,d['data']))
def score(**kw):
    m=0
    for obj,obs,data in sets:
        for x,y,th,c in data:
            m+= (visible(x,y,th,obj,obs,D=9,**kw)!=bool(c))
    return m
res=[]
for a in np.arange(-0.4,0.41,0.05):
    for b in np.arange(-0.2,0.21,0.05):
        for zc in list(np.arange(0.25,1.01,0.05)):
            res.append((score(a=a,b=b,zc=zc),round(a,3),round(b,3),round(zc,3)))
res.sort(); print(res[:15])
