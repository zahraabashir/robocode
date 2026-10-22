from pB_lib import *
import numpy as np
s=prep0()
pts=[(1.0,y) for y in np.arange(0.5,-2.2,-0.25)]+[(x,-2.1) for x in np.arange(1.0,0.25,-0.1)]+[(0.3,y) for y in np.arange(-2.1,-0.4,0.2)]+[(x,-0.5) for x in np.arange(0.3,2.2,0.2)]
for p in pts:
    ok=s.goto(0,*p); s.act(a0=(0,0,0,'send'))
    print(p, ok, s.r(0)['x'],s.r(0)['y'], objf(s,0,'received_image'))
    if objf(s,0,'received_image'): break
