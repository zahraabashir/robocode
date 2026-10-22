from probe_vis_util import *
r=R(0)
print(path(r,1,[(-0.5,-1.0),(-0.4,0.0),(-0.3,0.6)]), r.rv(1))
for th in [0, math.pi]:
    r.turn(1,th)
    r.act(1,'calibrate'); print('th',th,'cal',r.rv(1)['calibrated'])
    r.act(1,'image'); print(r.objst())
