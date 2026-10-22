from probe_vis_util import *
r=R(4)
O=np.array([0.683,1.874]); A=np.array([-0.25,0.4])
print(path(r,1,[(-0.5,-1.0),(-0.4,0.0),tuple(A)]))
u=(O-A)/np.linalg.norm(O-A)
B=A+u*1.1
print(path(r,0,[(1.0,0.5),tuple(B)]), r.rv(0))
for th in [0,math.pi/2,math.pi,-math.pi/2]:
    r.turn(1,th); r.act(1,'calibrate'); c=r.rv(1)['calibrated']
    if c: r.act(1,'image')
    print('blocked by rover0? th',th,'cal',c, r.objst())
r.goto(0,1.0,0.5)
r.act(1,'calibrate'); print('rover0 moved: cal',r.rv(1)['calibrated'])
