from probe_vis_util import *
r=R(4)
O=np.array([-1.803,1.925]); P=np.array([-1.921,1.281]); u=(P-O)/np.linalg.norm(P-O)
q=O+u*(0.654+0.4)
print(path(r,1,[(-1.0,0.0),(-1.5,0.75),tuple(q)]))
r.act(1,'calibrate'); r.act(1,'image'); print('behind pillar image',r.objst())
# send with lander behind pillar? seed 4 pillar4 (-1.859,0.445) not near lander; just send from here dist
r.act(1,'send'); print('send',r.objst(), 'dist to lander', math.hypot(q[0]+1.9,q[1]+2))
r=R(0)
L=np.array([-1.9,-2.0]); P=np.array([-1.808,-1.549]); u=(P-L)/np.linalg.norm(P-L)
path(r,1,[(-0.5,-1.0),(-0.4,0.0),(-0.3,0.6)]); r.act(1,'calibrate'); r.act(1,'image'); print(r.objst())
q=L+u*1.2
print(path(r,1,[(-0.4,0.0),(-1.0,-0.6),tuple(q)]), r.rv(1))
for th in [0,math.pi/2]:
    r.turn(1,th)
r.act(1,'send'); print('send behind pillar',r.objst())
