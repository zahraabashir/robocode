from pB_lib import *
import numpy as np
im=lambda s:[objf(s,k,'have_image_rover0') for k in range(3)]
s=Sim(0); gp(s,0,[(1.964,0.3)],th=np.pi/2)
s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img')); print('1st',im(s),s.r(0)['calibrated'])
s.act(a0=(0,0,0,'cal')); print('cal again',s.r(0)['calibrated']); s.act(a0=(0,0,0,'img')); print('2nd img',im(s),'cal',s.r(0)['calibrated'])
# persistence across moves: calibrate here, move far away then image obj0
s=Sim(0); gp(s,0,[(1.964,0.3)],th=np.pi/2); s.act(a0=(0,0,0,'cal')); print('cal',s.r(0)['calibrated'])
gp(s,0,[(1.964,-1.5),(1.2,-1.5),(1.2,0.9),(0.9,0.9)]); print('after move cal',s.r(0)['calibrated'],s.r(0)); s.act(a0=(0,0,0,'img')); print('img at obj0',im(s))
# motion + op same step: start out of range (y=0.0, th=pi/2 threshold ~0.2), move +0.2 and cal simultaneously
for y0 in [0.05,0.1,0.15]:
    s=Sim(0); gp(s,0,[(1.964,y0)],th=np.pi/2); s.act(a0=(0,0.2,0,'cal')); print('y0',y0,'move+cal ->',s.r(0)['y'],s.r(0)['calibrated'])
# move + send same step 
s=prep0(); s.goto(1,-1,-1); gp(s,0,[(1.2,0.5),(1.2,0.0),(1.75,0.0)],th=0); s.act(a0=(-0.2,0,0,'send')); print('move+send',s.r(0)['x'],objf(s,0,'received_image'))
