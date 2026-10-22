from pB_lib import *
import numpy as np
for block in [True]:
    s=Sim(0)
    if block: print('r0',gp(s,0,[(1.2,-1.75),(1.2,1.45),(0.6,1.45),(0.45,1.45)]),s.r(0))
    print('r1',gp(s,1,[(-1.08,-1.75),(-1.08,0.9),(-0.4,0.9)],th=-0.72),s.r(1))
    s.act(a1=(0,0,0,'cal')); c=s.r(1)['calibrated']; s.act(a1=(0,0,0,'img'))
    print('block',block,'cal',c,'after img cal',s.r(1)['calibrated'],'imgs r1', [objf(s,k,'have_image_rover1') for k in range(3)])
