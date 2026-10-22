from probe_send_lib import *
import numpy as np
L=np.array([-1.9,-2.0])
def segd(p,a,b):
    a,b,p=map(np.array,(a,b,p)); t=np.clip(np.dot(p-a,b-a)/np.dot(b-a,b-a),0,1); return float(np.linalg.norm(a+t*(b-a)-p))
def scan(blk, pts, setup=None):
    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
    if setup: setup()
    goto(0,*pts[0]); prev=None
    for p in pts:
        goto(0,*p,tol=0.001); step(0,op='send')
        q=pos(0)[:2]
        if dump('sample')['sample3'][-1]>0:
            return prev, round(segd(blk,q,L),4)
        prev=round(segd(blk,q,L),4)
    return 'nosuccess',prev
# rover1 blocker at home, scan rover0 at x=1.0 and x=0.4 and x=2.0 downward
r1=(-1.0,-1.75)
for x in [0.4,1.0,1.6]:
    print('rover1', x, scan(r1,[(x,y) for y in np.arange(-1.6,-2.1,-0.003)]))
# rover1 rotated 90deg
def rot(): 
    for _ in range(4): step(1,dth=0.4)
    print(' r1 theta', pos(1)[2])
print('rover1 rot', scan(r1,[(1.0,y) for y in np.arange(-1.6,-2.1,-0.003)],rot))
# pillar obstacle10 (-0.47,-1.23): rover1 moved away
P=np.array([-0.47,-1.23]); d=(P-L)/np.linalg.norm(P-L); n=np.array([-d[1],d[0]])
def away(): goto(1,-1.0,0.3)
base=L+d*((0.6-L[0])/d[0])
print('pillar', scan(P,[tuple(base+n*s) for s in np.arange(0.4,-0.4,-0.004)],away))
print('pillar rev', scan(P,[tuple(base+n*s) for s in np.arange(-0.4,0.4,0.004)],away))
