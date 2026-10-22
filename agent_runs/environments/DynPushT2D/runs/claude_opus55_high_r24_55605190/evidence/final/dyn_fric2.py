from dyn_push import *
from dyn_fit2 import pred
P=[0,-0.375,0.2129]
for a in [40,50,55,60,65,70,75]:
    ar=np.radians(a); d=np.array([np.sin(ar),-np.cos(ar)])
    out,e=push(0,[-np.tan(ar)*0.5,0.6],d,0.005,8)
    for k in [0,1,3,6]:
        cb,tw=out[k]
        cp=cb-[0,0.1]; u=d*0.005
        rx,ry=cp[0],cp[1]+0.375; c2=0.2129
        A=np.array([[1+ry**2/c2,-rx*ry/c2],[-rx*ry/c2,1+rx**2/c2]]); f=np.linalg.solve(A,u)
        print(f'a={a} k={k} cp={cp.round(4)} twist={tw} stickpred={pred(P,cp,u).round(5)} |ft/fn|={abs(f[0]/f[1]):.3f}')
