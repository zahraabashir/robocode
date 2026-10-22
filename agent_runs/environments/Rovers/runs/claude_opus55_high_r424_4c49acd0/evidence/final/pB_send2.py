from pB_lib import *
import numpy as np
def scan(th,y=0.0,x0=1.45,x1=1.8,st=0.0025):
    s=prep0(); s.goto(0,1.2,0.5,th); s.goto(0,1.2,y)
    x=x1
    while x>x0:
        s.goto(0,x,y); s.act(a0=(0,0,0,'send'))
        if objf(s,0,'received_image'): return s.r(0)
        x-=st
for th in [0,0.5,1,-0.5]:
    c=scan(th*np.pi); print(th,c, np.hypot(c['x']+1.9,c['y']+2))
