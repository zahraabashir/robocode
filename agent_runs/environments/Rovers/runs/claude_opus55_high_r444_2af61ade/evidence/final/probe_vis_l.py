from probe_vis_lib import *
def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
# pre/post motion evaluation at range boundary (seed1, theta=pi, y*=-0.0852)
for sel,y0,dy in [('cal',-0.05,-0.1),('cal',-0.15,0.1)]:
    e=E(1); e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,y0)])
    e.step(0,0,0,0,sel if False else 'noop')
    e.step(0,0,dy,0,sel); print(sel,'from y',y0,'to',round(e.rs(0)['y'],3),'cal=',e.rs(0)['calibrated']); e.close()
# image: calibrate at visible spot then move out of range then image
e=E(1); e.path(0,[(1.0,0.0),(2.118,0.0)]); e.step(0,0,0,0,'cal'); print('cal at y=0:',e.rs(0)['calibrated'])
e.goto(0,2.118,-0.3); r=e.step(0,0,0,0,'img'); print('img out of range',flags(e),e.rs(0)['calibrated'],r); e.close()
# image with move crossing boundary
for y0,dy in [(-0.05,-0.1),(-0.15,0.1)]:
    e=E(1); e.path(0,[(1.0,0.0),(2.118,0.0)]); e.step(0,0,0,0,'cal'); e.goto(0,2.118,y0)
    e.step(0,0,dy,0,'img'); print('img move from',y0,'to',round(e.rs(0)['y'],3),flags(e),e.rs(0)['calibrated']); e.close()
# nearest choice
e=E(0); e.path(0,[(1.0,0.0),(1.9,0.0),(1.9,1.5)])
for k,v in e.objs().items(): print(k, round(math.hypot(v['x']-1.9,v['y']-1.5),3))
e.step(0,0,0,0,'cal'); e.step(0,0,0,0,'img'); print('nearest test',flags(e))
