from probe_vis_util import *
r=R(0)
path(r,0,[(1.2,0.0),(1.2,1.6)])
r.act(0,'calibrate'); r.act(0,'image'); print(r.objst())
for p in [(0.3,-1.9),(0.3,-1.0),(0.3,0.0),(0.3,1.0),(0.3,1.5)]:
    print(path(r,0,[p]))
    for th in [0,math.pi/2,math.pi,-math.pi/2]:
        r.turn(0,th); r.act(0,'send')
        if r.objst()['objective0'][2]: print('sent at',p,th); break
    else: print('no send at',p)
