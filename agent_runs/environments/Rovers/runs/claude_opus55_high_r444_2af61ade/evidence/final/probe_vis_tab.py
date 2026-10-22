import sys, json, math
from probe_vis_model import *
from probe_vis_lib import E
d=json.load(open(sys.argv[1])); e=E(d['seed'])
ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']
kw=eval(sys.argv[2]) if len(sys.argv)>2 else dict(dim3=False)
rows={}
for x,y,th,c in d['data']:
    rows.setdefault((round(y,3),round(th,2)),[]).append((x,c,visible(x,y,th,obj,obs,**kw)))
for k in sorted(rows):
    r=sorted(rows[k])
    print(k, 'x0=%.2f'%r[0][0], ''.join(str(c) for _,c,_ in r))
    print(' '*len(str(k)),'model   ',''.join(str(int(p)) for _,_,p in r))
