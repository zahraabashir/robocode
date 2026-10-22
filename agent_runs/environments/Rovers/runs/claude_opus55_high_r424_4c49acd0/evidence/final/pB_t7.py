from pB_lib import *
import numpy as np
for p in [(1,-1.75),(0.35,-0.9),(1.8,-1.2)]:
    s=prep0(); s.goto(1,-1.0,-1.0); ok=gp(s,0,[(1.2,0.5),(1.2,p[1]),p]); s.act(a0=(0,0,0,'send'))
    print('r1 moved; send from',p,ok,'recv',objf(s,0,'received_image'))
s=Sim(0); ok=gp(s,1,[(-1.0,-0.5),(-0.4,-0.5),(-0.4,1.2),(-0.35,1.2)]); print('r1',ok,s.r(1))
s.act(a1=(0,0,0,'cal')); print('cal',s.r(1)['calibrated']); s.act(a1=(0,0,0,'img'))
print('imgs r1', [objf(s,k,'have_image_rover1') for k in range(3)], 'cal after', s.r(1)['calibrated'])
