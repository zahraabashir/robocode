from pB_lib import *
import numpy as np
im=lambda s:[(objf(s,k,'have_image_rover0'),objf(s,k,'received_image')) for k in range(3)]
s=Sim(0); s.goto(1,-1,-1); gp(s,0,[(1.0,0.5)])
for i in range(3):
    s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img')); print('img',i,im(s),'cal',s.r(0)['calibrated'])
s.act(a0=(0,0,0,'send')); print('after send',im(s))
s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img')); print('img after send',im(s),'cal',s.r(0)['calibrated'])
s=Sim(0); gp(s,0,[(1.0,0.5)]); s.act(a0=(0,0,0,'cal')); gp(s,0,[(1.0,-1.5)]); s.act(a0=(0,0,0,'img')); print('img with nothing visible: cal',s.r(0)['calibrated'],im(s))
# send with nothing held: anything?
s.act(a0=(0,0,0,'send')); print(s.r(0))
