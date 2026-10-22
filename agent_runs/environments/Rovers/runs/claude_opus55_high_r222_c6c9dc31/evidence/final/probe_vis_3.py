from probe_vis_util import *
r=R(1)
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(-2.1,1.0)])
for k in range(8):
    th=-math.pi+k*math.pi/4
    r.turn(1,th)
    r.act(1,'calibrate'); c=r.rv(1)['calibrated']
    r.act(1,'image'); c2=r.rv(1)['calibrated']
    print('theta %.2f'%r.rv(1)['theta'],'cal',c,'after image',c2,r.objst())
