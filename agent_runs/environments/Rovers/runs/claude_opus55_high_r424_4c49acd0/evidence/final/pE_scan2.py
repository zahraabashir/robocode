from pE_lib import *
import sys
seed,i,ys,xw,st,k=eval(sys.argv[1])
for y in ys:
    s0=Sim(seed); O=objs(s0); o=np.array(O[k][:2]); P=pillars(s0)
    blocked=[]
    for x in np.arange(xw[0],xw[1]+1e-9,st):
        s=Sim(seed)
        if not drive(s,i,x,y): continue
        sp=np.array(sense(s,i)); act1(s,i,'cal')
        if s.r(i)['calibrated']<0.5:
            u=(o-sp)/np.linalg.norm(o-sp); perps=[round(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]),3) for p in P if abs(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]))<0.15]
            blocked.append((round(x,3),perps))
    print('y',y,'blocked',blocked[:1],blocked[-1:],len(blocked),flush=True)
