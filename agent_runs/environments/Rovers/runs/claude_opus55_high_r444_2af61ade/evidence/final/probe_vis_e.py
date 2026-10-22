from probe_vis_lib import *
A,B,D=-0.087,-0.0125,1.99758
def pred_t(o,u,th):
    # find t s.t. camera at o + t*u (rover center) dist = D
    lo,hi=0.5,3.0
    for _ in range(60):
        t=(lo+hi)/2; cx=o[0]+t*u[0]+A*math.cos(th)-B*math.sin(th); cy=o[1]+t*u[1]+A*math.sin(th)+B*math.cos(th)
        if math.hypot(cx-o[0],cy-o[1])<=D: lo=t
        else: hi=t
    return lo
for ang,th in [(-90,0.3),(-75,1.2),(-55,-2.0),(-62,2.8)]:
    e=E(1)
    ob=e.objs()['objective1']; o=(ob['x'],ob['y'])
    u=(math.cos(math.radians(ang)),math.sin(math.radians(ang)))
    p0=(o[0]+2.3*u[0],o[1]+2.3*u[1])
    ok=e.path(1,[(-1.0,-1.0),(p0[0],-1.0),p0]); 
    e.turn(1,th); th=e.rs(1)['theta']
    lo,hi=1.8,2.3
    for it in range(16):
        t=(lo+hi)/2
        e.goto(1,o[0]+t*u[0],o[1]+t*u[1],tol=1e-7)
        e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
        if c: lo=t
        else: hi=t
    # note: here lo= fails side? visible when t small
    print('ang',ang,'th=%.3f ok=%s measured t*=%.5f predicted %.5f pos=%s'%(th,ok,lo,pred_t(o,u,th),(round(e.rs(1)['x'],3),round(e.rs(1)['y'],3))))
    e.close()
