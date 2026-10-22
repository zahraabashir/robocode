from probe_vis_lib import *
e=E(1)
e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,1.0)])
o=e.objs()['objective0']
for k in range(16):
    th=-math.pi+k*2*math.pi/16
    e.turn(0,th)
    e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img')
    print('th=%.3f cal=%d'%(e.rs(0)['theta'],c))
