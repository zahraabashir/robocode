from probe_vis_lib import *
def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
# mound occlusion test: seed5 rover0 at (1.0,2.0) viewing obj1 on (-0.5,2) through mound (0.5,2)
for th in [math.pi, 0.0, -math.pi/2]:
    e=E(5); ok=e.path(0,[(1.6,-1.75),(1.6,1.0),(1.0,1.5),(1.0,2.0)]); e.turn(0,th)
    st=e.rs(0); out=[]
    for i in range(2):
        e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img'); out.append((c,flags(e)))
    print('mound test th=%.2f'%th, ok, round(st['x'],3), round(st['y'],3), out); e.close()
# image under bypass: seed4 rover1 deep shadow
for th in [math.pi/2, -math.pi/2]:
    e=E(4); e.path(1,[(-1.0,-1.0),(-1.0,0.75),(-1.95,0.75)]); e.turn(1,th)
    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
    print('shadow th=%.2f cal=%d'%(th,c), flags(e)); e.close()
