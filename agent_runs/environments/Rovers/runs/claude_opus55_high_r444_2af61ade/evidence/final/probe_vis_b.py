from probe_vis_lib import *
e=E(1)
e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,0.2)])
o=e.objs()['objective0']
y=0.2
while y>-0.3:
    e.goto(0,2.118,y)
    e.step(0,0,0,0,'cal'); c=e.rs(0)['calibrated']
    e.step(0,0,0,0,'img'); c2=e.rs(0)['calibrated']; hi=e.objs()['objective0']['have_image_rover0']
    st=e.rs(0); d=math.hypot(o['x']-st['x'],o['y']-st['y'])
    print('y=%.3f d2=%.4f d3=%.4f cal=%d after_img=%d img=%d'%(st['y'],d,math.sqrt(d*d+o['z']**2),c,c2,hi))
    y-=0.02
