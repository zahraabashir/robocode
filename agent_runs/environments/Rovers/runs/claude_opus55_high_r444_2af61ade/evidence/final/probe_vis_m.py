from probe_vis_lib import *
def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
for th in [2.3,-0.84,0.0,math.pi]:
  for pos in [(0.25,1.2),(0.25,1.45)]:
    e=E(5); ok=e.path(0,[(0.25,-1.75),pos]); e.turn(0,th)
    ds={k:round(math.hypot(v['x']-pos[0],v['y']-pos[1]),2) for k,v in e.objs().items()}
    e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img')
    print('th',th,'pos',pos,ok,'cal',c,flags(e),ds); e.close()
