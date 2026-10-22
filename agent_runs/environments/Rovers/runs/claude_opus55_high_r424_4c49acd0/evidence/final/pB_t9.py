from pB_lib import *
import numpy as np
s=Sim(0); ok=gp(s,1,[(-1.08,-1.75),(-1.08,1.5),(-1.2,1.5),(-1.2,1.95)],th=np.pi); print('r1',ok,s.r(1))
for k in range(3):
    s.act(a1=(0,0,0,'cal')); c=s.r(1)['calibrated']; s.act(a1=(0,0,0,'img'))
    print('cal',c,'imgs r1', [objf(s,k,'have_image_rover1') for k in range(3)])
# wall gap scan with rover0
s=Sim(0); gp(s,0,[(1.2,-1.75),(1.2,0.6)])
for y in np.arange(-0.4,2.31,0.15):
    gp(s,0,[(1.2,y)]); ok=s.goto(0,-0.6,y); c=s.r(0); print(round(y,2),ok,c['x'],c['y']); gp(s,0,[(1.2,c['y'])])
