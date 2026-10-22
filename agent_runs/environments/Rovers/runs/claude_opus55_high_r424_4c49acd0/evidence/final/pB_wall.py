from pB_lib import *
import numpy as np
s=Sim(0)
for y in np.arange(-2.3,2.31,0.25):
    s.goto(0,0.7,-1.75); s.goto(0,0.7,y)
    ok=s.goto(0,-0.7,y); c=s.r(0)
    print(round(y,2), 'reached' if ok else 'stopped', c['x'],c['y'])
    if ok: s.goto(0,0.7,y)
