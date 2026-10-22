from probe_send_lib import *
import numpy as np, probe_ops_lib as L
def scan(x,y0,y1,dy=-0.004):
    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
    goto(0,x,y0+0.05)
    prev=None
    for y in np.arange(y0,y1,dy):
        goto(0,x,y,tol=0.001)
        step(0,op='send')
        if dump('sample')['sample3'][-1]>0:
            p=pos(0)[:2]; 
            yc=p[1]+(-2-p[1])*p[0]/(p[0]+1.9)
            return prev, [round(v,4) for v in p], 'cross0', round(yc,4)
        prev=[round(v,4) for v in pos(0)[:2]]
for x in [0.24,0.4,0.7,1.2,1.8,2.0]:
    print(x, scan(x,-1.6,-2.2))
