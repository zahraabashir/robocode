from probe_vis_lib import *
from probe_vis_geo import *
import sys
seed=int(sys.argv[1]); ri=int(sys.argv[2]); objn=sys.argv[3]; piln=sys.argv[4]; yrow=float(sys.argv[5]); x0,x1,dxs=map(float,sys.argv[6:9]); th=float(sys.argv[9])
path=eval(sys.argv[10])
e=E(seed)
ob=e.objs()[objn]; o=(ob['x'],ob['y'])
for o_ in e.obs:
    if o_.name==piln: pil=(e.obs.get(o_,'x'),e.obs.get(o_,'y')); h=(e.obs.get(o_,'half_x'),e.obs.get(o_,'half_y'))
print('obj',o,'pil',pil,h,'path ok',e.path(ri,path))
e.turn(ri,th)
x=x0; prev=None
while (x<=x1+1e-9):
    ok=e.goto(ri,x,yrow,tol=1e-7); st=e.rs(ri)
    e.step(ri,0,0,0,'cal'); c=e.rs(ri)['calibrated']; e.step(ri,0,0,0,'img')
    C=cam(st['x'],st['y'],st['theta'])
    bd=seg_box_dist(C,o,pil,h); bd0=seg_box_dist((st['x'],st['y']),o,pil,h)
    line='x=%.4f ok=%d vis=%d camboxdist=%.4f ctrboxdist=%.4f d=%.3f'%(st['x'],ok,c,bd,bd0,math.hypot(C[0]-o[0],C[1]-o[1]))
    if c!=prev or abs(bd)<0.1: print(line)
    prev=c; x+=dxs
