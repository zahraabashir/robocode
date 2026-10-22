from probe_vis_lib import *
for k in range(8):
    th=-math.pi+k*math.pi/4
    e=E(1)
    e.path(0,[(1.0,0.0),(2.118,0.0)])
    e.turn(0,th)
    o=e.objs()['objective0']
    lo,hi=0.2,-0.3
    for it in range(16):
        y=(lo+hi)/2
        e.goto(0,2.118,y,tol=1e-7)
        e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']; e.step(0,0,0,0,'img')
        if c: lo=y
        else: hi=y
    st=e.rs(0)
    print('theta=%.3f y*=%.5f d2=%.5f'%(st['theta'],lo,math.hypot(o['x']-st['x'],o['y']-lo)))
    e.close()
