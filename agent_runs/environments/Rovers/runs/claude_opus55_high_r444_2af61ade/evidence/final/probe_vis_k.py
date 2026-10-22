from probe_vis_lib import *
def flags(e): return {k:(int(v['have_image_rover0']),int(v['have_image_rover1'])) for k,v in e.objs().items()}
e=E(0)
print(e.path(0,[(1.0,0.0),(1.3,1.4)]), e.rs(0)['x'],e.rs(0)['y'])
for k,v in e.objs().items(): print(k, round(math.hypot(v['x']-1.3,v['y']-1.4),3))
print('img w/o cal:', e.step(0,0,0,0,'img'), e.rs(0)['calibrated'], flags(e))
e.step(0,0,0,0,'cal'); print('cal',e.rs(0)['calibrated'])
for i in range(3): e.step(0,0,0,0,'noop')
print('after 3 noops cal=',e.rs(0)['calibrated'])
e.step(0,0.2,0,0,'noop'); e.step(0,-0.2,0,0,'noop'); e.step(0,0,0,0.4,'noop')
print('after moves cal=',e.rs(0)['calibrated'])
r=e.step(0,0,0,0,'img'); print('img rew',r,flags(e),'cal',e.rs(0)['calibrated'])
r=e.step(0,0.1,0,0,'cal'); print('cal+move: pos',round(e.rs(0)['x'],3),'cal',e.rs(0)['calibrated'])
r=e.step(0,-0.1,0,0,'img'); print('img+move: pos',round(e.rs(0)['x'],3),'cal',e.rs(0)['calibrated'],flags(e),r)
r=e.step(0,0,0,0,'cal'); print('cal when all imaged by r0: cal',e.rs(0)['calibrated'])
r=e.step(0,0,0,0,'img'); print('img again',flags(e),'cal',e.rs(0)['calibrated'],r)
# rover1 calibrate while rover0 acts
