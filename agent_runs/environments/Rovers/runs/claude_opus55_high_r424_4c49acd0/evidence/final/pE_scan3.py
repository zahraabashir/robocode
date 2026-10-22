from pE_lib import *
import sys
seed,i,y,xw,st,k=eval(sys.argv[1])
s0=Sim(seed); O=objs(s0); o=np.array(O[k][:2]); P=pillars(s0)
out=[]
for x in np.arange(xw[0],xw[1]+1e-9,st):
    s=Sim(seed)
    if not drive(s,i,x,y): out.append((round(x,3),'NR')); continue
    sp=np.array(sense(s,i)); I=info(s,i); act1(s,i,'cal')
    u=(o-sp)/np.linalg.norm(o-sp); perps=[round(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]),3) for p in P if abs(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]))<0.2 and (p-sp)@u>0]
    out.append((round(x,3),int(s.r(i)['calibrated']),perps, [d for kk,d,m,_ in I if d<2.0]))
for z in out: print(z)
