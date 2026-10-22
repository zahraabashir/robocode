from pB_lib import *
import numpy as np, sys, time
x=float(sys.argv[1]); th=float(sys.argv[2])*np.pi
s=Sim(0); s.goto(0,x,-0.1,th); y=-0.1; out=''
t=time.time()
while y<0.3:
    s.goto(0,x,y); s.act(a0=(0,0,0,'cal'))
    c=s.r(0); out+= '1' if c['calibrated'] else '0'
    if c['calibrated']:
        s.act(a0=(0,0,0,'img'))
        if s.r(0)['calibrated']: print('img failed to reset at',y); break
    y+=0.005
print(x,th,out,time.time()-t)
