from probe_vis_lib import *
from probe_vis_geo import *
e=E(1)
ob=e.objs()['objective1']; o=(ob['x'],ob['y'])
pil=(-1.002,0.435)
for o_ in e.obs:
    if o_.name=='obstacle8': pil=(e.obs.get(o_,'x'),e.obs.get(o_,'y'))
print('pillar',pil)
print(e.path(1,[(-1.0,-1.0),(-1.9,-1.0),(-1.9,0.3),(-1.25,0.6)]))
e.turn(1,0.0)
t=1.75
for k in range(41):
    ang=-58+k*0.15
    u=(math.cos(math.radians(ang)),math.sin(math.radians(ang)))
    p=(o[0]+t*u[0],o[1]+t*u[1])
    ok=e.goto(1,*p,tol=1e-7)
    st=e.rs(1)
    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
    C=cam(st['x'],st['y'],st['theta'])
    print('ang=%.2f ok=%d vis=%d boxdist=%.4f ctrdist=%.4f ctrdist_center=%.4f'%(ang,ok,c,seg_box_dist(C,o,pil,(0.05,0.05)),seg_pt_dist(C,o,pil),seg_pt_dist((st['x'],st['y']),o,pil)))
