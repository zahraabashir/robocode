import sys, json, math
from probe_vis_model import *
from probe_vis_lib import E
files=sys.argv[1:]
sets=[]
for f in files:
    d=json.load(open(f)); e=E(d['seed'])
    ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
    obs=[]
    for o in e.obs:
        if o.type.name=='obstacle': obs.append(tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']))
    e.close(); sets.append((obj,obs,d['data']))
def score(**kw):
    m=0;n=0
    for obj,obs,data in sets:
        for x,y,th,c in data:
            n+=1; m+= (visible(x,y,th,obj,obs,**kw)!=bool(c))
    return m,n
print('2D cam',score(dim3=False))
print('2D center',score(dim3=False,a=0,b=0))
for zc in [0.2,0.3,0.4,0.45,0.5,0.52,0.53,0.54,0.55,0.56,0.58,0.6,0.7]:
    print('3D zc',zc,score(zc=zc), 'center', score(zc=zc,a=0,b=0))
