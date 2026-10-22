from pB_lib import *
import numpy as np
def run(th,x=-1.866,y0=0.0):
    s=Sim(0); gp(s,1,[(-1.0,-0.3),(x,-0.3),(x,y0)],th=th); y=y0
    while y<0.4:
        s.goto(1,x,y); s.act(a1=(0,0,0,'cal'))
        if s.r(1)['calibrated']: return s.r(1)['y']
        y+=0.002
for th in [np.pi/2,-np.pi/2]: print(th, run(th))
