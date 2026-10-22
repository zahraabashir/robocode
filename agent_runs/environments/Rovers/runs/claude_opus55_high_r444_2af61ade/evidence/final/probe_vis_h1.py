import sys, json, math
from probe_vis_model import seg_box_hit
from probe_vis_lib import E
sets=[]
for f in sys.argv[1:]:
    d=json.load(open(f)); e=E(d['seed'])
    ob=e.objs()[d['obj']]; obj=(ob['x'],ob['y'],ob['z'])
    obs=[tuple(e.obs.get(o,k) for k in ['x','y','z','half_x','half_y','half_z']) for o in e.obs if o.type.name=='obstacle']
    e.close(); sets.append((obj,obs,d['data']))
def vis(x,y,th,obj,obs,a,b,thr,origin_cam):
    cx=x+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
    for (px,py,pz,hx,hy,hz) in obs:
        if abs(px-obj[0])<=hx and abs(py-obj[1])<=hy: continue
        if seg_box_hit((cx,cy),obj[:2],(px-hx,py-hy),(px+hx,py+hy)):
            ox,oy=(cx,cy) if origin_cam else (x,y)
            rel=math.atan2(py-oy,px-ox)-th; rel=(rel+math.pi)%(2*math.pi)-math.pi
            if abs(rel)<thr: return False
    return True
for oc in [True,False]:
  for a,b in [(-0.087,-0.0125),(0,0)]:
    for thr in [1.2,1.4,1.5,1.571,1.65,1.75,1.9,2.2,3.2]:
        m=sum(vis(x,y,th,obj,obs,a,b,thr,oc)!=bool(c) for obj,obs,data in sets for x,y,th,c in data)
        print(oc,a,b,thr,m)
