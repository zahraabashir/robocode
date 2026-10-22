from pB_lib import *
import numpy as np, sys
def run(th,x=1.964,y0=-0.1):
    s=Sim(0); ok=s.goto(0,x,y0,th); y=y0
    while y<0.4:
        ok=s.goto(0,x,y); s.act(a0=(0,0,0,'cal'))
        o=s.obs.get_object_from_name('rover0')
        if s.obs.get(o,'calibrated'): return float(s.obs.get(o,'x')),float(s.obs.get(o,'y')), float(s.obs.get(o,'theta'))
        y+=0.002
    return s.r(0)
for th in [np.pi/2,-np.pi/2,np.pi/4,3*np.pi/4]:
    print(th, run(th))
