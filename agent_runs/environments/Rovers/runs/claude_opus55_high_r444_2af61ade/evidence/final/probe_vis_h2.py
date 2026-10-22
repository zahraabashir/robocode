import sys, json, math, glob
from probe_vis_model import seg_box_hit
from probe_vis_lib import E
e=E(4); ob=e.objs()['objective2']; obj=(ob['x'],ob['y'],ob['z'])
obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']; e.close()
data=json.load(open('probe_vis_d1.json'))['data']
for f in glob.glob('probe_vis_j_*_0.75.json'): data+=json.load(open(f))
print(len(data))
def vis(x,y,th,a,b,thr,mode,infl=0.0):
    cx=x+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
    for (px,py,pz,hx,hy,hz) in obs:
        if abs(px-obj[0])<=hx and abs(py-obj[1])<=hy: continue
        if seg_box_hit((cx,cy),obj[:2],(px-hx-infl,py-hy-infl),(px+hx+infl,py+hy+infl)):
            if mode=='obj': tx,ty=obj[0],obj[1]
            else: tx,ty=px,py
            rel=math.atan2(ty-cy,tx-cx)-th; rel=(rel+math.pi)%(2*math.pi)-math.pi
            if abs(rel)<thr: return False
    return True
best=[]
for mode in ['obj','pil']:
  for a in [-0.06,-0.087,-0.1,-0.12,-0.15]:
    for b in [-0.0125,0.0]:
      for thr in [1.45,1.5,1.55,1.6,1.65,1.7,1.75]:
        m=sum(vis(x,y,th,a,b,thr,mode)!=bool(c) for x,y,th,c in data)
        best.append((m,mode,a,b,thr))
best.sort(); print(best[:10])
mm=[(round(th,2),round(x,3),round(y,3),c) for x,y,th,c in data if vis(x,y,th,-0.1,0.0,1.6,'obj')!=bool(c)]
mm.sort(); 
for r in mm: print(r)
