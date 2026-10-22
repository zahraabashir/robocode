from pB_lib import *
import numpy as np, json
def run(th,x,y0,step):
    s=Sim(0); s.goto(0,x,y0,th); y=y0
    while y<y0+0.6:
        s.goto(0,x,y); s.act(a0=(0,0,0,'cal'))
        o=s.obs.get_object_from_name('rover0')
        if s.obs.get(o,'calibrated'): return float(s.obs.get(o,'x')),float(s.obs.get(o,'y')), float(s.obs.get(o,'theta'))
        y+=step
res=[]
for x in [1.564]:
  for k in [0,2,4,6]:
    th=-np.pi+k*np.pi/4
    c=run(th,x,-0.15,0.01); fine=run(th,x,c[1]-0.012,0.0005)
    res.append(fine); print(fine,flush=True)
json.dump(res,open('pB_t4.json','w'))
