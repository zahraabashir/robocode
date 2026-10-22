from probe_vis_util import *
r=R(1)
o=r.obs.get_object_from_name('objective1'); ox,oy=float(r.obs.get(o,'x')),float(r.obs.get(o,'y'))
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(ox,0.3)])
r.goto(1,ox,oy-2.0,tol=1e-6)
for k in range(16):
    r.turn(1,-math.pi+k*math.pi/8); q=r.rv(1)
    print(k,'%.4f %.4f %.4f'%(q['x'],q['y'],q['theta']))
