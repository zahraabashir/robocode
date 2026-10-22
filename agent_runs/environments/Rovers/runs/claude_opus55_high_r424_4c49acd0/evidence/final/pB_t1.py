from pB_lib import *
import numpy as np
s=Sim(0)
s.act(a0=(0,0,0,'cal')); print('cal at start',s.r(0))
print(s.goto(0,1.0,0.5), s.r(0))
for th in np.linspace(-np.pi,np.pi,9)[:-1]:
    s.goto(0,1.0,0.5,th); s.act(a0=(0,0,0,'cal')); c=s.r(0)
    print('th',round(th,2),c['theta'],'cal',c['calibrated'])
    if c['calibrated']: break
