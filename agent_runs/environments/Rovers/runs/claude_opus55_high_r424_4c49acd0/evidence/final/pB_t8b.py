from pB_lib import *
import numpy as np
L=np.array([-1.9,-2.0]); P=np.array([-0.135,-0.64]); d=(P-L)/np.linalg.norm(P-L); perp=np.array([-d[1],d[0]])
s=None; out=''
for sv in np.arange(-0.2,0.2,0.02):
    q=L+3.5*d+sv*perp
    if s is None: s=prep0(); gp(s,0,[(1.2,0.5)])
    ok=s.goto(0,*q); assert ok
    s.act(a0=(0,0,0,'send')); r=objf(s,0,'received_image'); out+=str(int(r))
    if r: s=None
print(out)
