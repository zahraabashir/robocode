import json, math, glob
import numpy as np
from probe_vis_model import seg_box_hit
from probe_vis_lib import E
e=E(4); ob=e.objs()['objective2']; obj=(ob['x'],ob['y'])
obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']; e.close()
data=json.load(open('probe_vis_d1.json'))['data']
for f in glob.glob('probe_vis_j_*_0.75.json')+glob.glob('probe_vis_n_*.json'): data+=json.load(open(f))
HOLES=[(73.5,80),(52.5,58),(-53.5,-48),(-77.5,-70)]
def rel(x,y,th):
    r=math.degrees(math.atan2(obj[1]-y,obj[0]-x)-th); return (r+180)%360-180
def vis(x,y,th,a,b,infl,thr=97.5,holes=True):
    r=rel(x,y,th)
    if abs(r)>thr: return True
    if holes and any(lo<=r<=hi for lo,hi in HOLES): return True
    cx=x+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
    for (px,py,pz,hx,hy,hz) in obs:
        if abs(px-obj[0])<=hx and abs(py-obj[1])<=hy: continue
        if seg_box_hit((cx,cy),obj,(px-hx-infl,py-hy-infl),(px+hx+infl,py+hy+infl)): return False
    return True
print(len(data))
res=[]
for a in np.arange(-0.16,0.061,0.02):
    for b in np.arange(-0.06,0.061,0.02):
        for infl in [0,0.01,0.02,0.03]:
            res.append((sum(vis(x,y,th,a,b,infl)!=bool(c) for x,y,th,c in data),round(a,3),round(b,3),infl))
res.sort(); print(res[:8])
m,a,b,infl=res[0]
mm=[(round(math.degrees(th)),round(x,3),round(y,3),round(rel(x,y,th),1),c) for x,y,th,c in data if vis(x,y,th,a,b,infl)!=bool(c)]
print(mm[:60])
