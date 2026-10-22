from dyn_push import *
import sys
sys.path.insert(0,'.')
from dyn_fit2 import pred
P=[0,-0.375,0.2129]
for a in [0,5,10,15,20,25,30,40]:
    ar=np.radians(a); d=np.array([np.sin(ar),-np.cos(ar)])
    out,e=push(0,[-0.2*np.sin(ar)/np.cos(ar)*0,0.6],d,0.005,6)
    for k in [1,3]:
        cb,tw=out[k]; cb2=out[k+1][0]
        cp=cb-[0,0.1]; u=d*0.005
        print(f'a={a} k={k} cp={cp.round(4)} slip_x/step={cb2[0]-cb[0]:.5f} ut={u[0]:.5f} twist={tw} stickpred={pred(P,cp,u).round(5)}')
