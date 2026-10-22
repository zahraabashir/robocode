from probe_vis_util import *
r=R(1)
ox,oy=-2.114,2.096
path(r,1,[(-0.9,-0.5),(-1.6,0.0),(ox,0.3)])
prev=None
for k in range(120):
    y=0.13-k*0.0005
    r.goto(1,ox,y,tol=1e-6)
    r.act(1,'calibrate'); c=r.rv(1)['calibrated']
    if c: r.act(1,'image')
    if c!=prev: print('y %.5f d2=%.5f cal %s'%(r.rv(1)['y'],oy-r.rv(1)['y'],c), r.rv(1)['x'])
    prev=c
