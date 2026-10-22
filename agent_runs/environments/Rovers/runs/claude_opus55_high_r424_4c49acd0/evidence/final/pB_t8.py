from pB_lib import *
import numpy as np
L=np.array([-1.9,-2.0]); P=np.array([-0.135,-0.64]); d=(P-L)/np.linalg.norm(P-L); perp=np.array([-d[1],d[0]])
print('tpillar',np.linalg.norm(P-L))
def first(ss):
    s=prep0(); 
    for k,sv in enumerate(ss):
        q=L+3.5*d+sv*perp
        ok=gp(s,0,[(1.2,0.5),tuple(q)]) if k==0 else s.goto(0,*q)
        s.act(a0=(0,0,0,'send'))
        if objf(s,0,'received_image'): return sv,ok,s.r(0)
print(first(np.arange(-0.3,0.3,0.01)))
print(first(np.arange(0.3,-0.3,-0.01)))
