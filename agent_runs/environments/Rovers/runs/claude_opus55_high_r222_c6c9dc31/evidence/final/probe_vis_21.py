from probe_vis_util import *
r=R(0)
path(r,0,[(1.2,0.0),(1.2,1.6)])
r.act(0,'calibrate'); r.act(0,'image')
print(path(r,0,[(1.2,0.0),(1.9,-1.0),(1.95,-1.95)]), r.rv(0), 'dist',math.hypot(r.rv(0)['x']+1.9,r.rv(0)['y']+2))
r.goto(1,-1.0,-1.0)
r.turn(0,0); r.act(0,'send'); print('send from far right low',r.objst())
