from probe_vis_util import *
r=R(0)
path(r,0,[(1.2,0.0),(1.2,1.6)])
for k in range(2): r.act(0,'calibrate'); r.act(0,'image')
print(path(r,0,[(1.2,0.0),(0.5,-1.0)]), r.rv(0))
r.act(0,'send'); print('send w/ rover1 at start',r.objst())
r.goto(1,-1.0,-1.3); r.act(0,'send'); print('rover1 moved to (-1,-1.3)',r.objst())
