from pE_lib import *
import sys
for seed,i,x,y in eval(sys.argv[1]):
    s=Sim(seed)
    if not drive(s,i,x,y): print(seed,i,'noreach'); continue
    I=info(s,i); seq=[]
    for rep in range(3):
        b=objs(s); act1(s,i,'cal'); c=s.r(i)['calibrated']; act1(s,i,'img'); a=objs(s)
        seq.append((int(c),[k for k in range(len(a)) if a[k][2+i]!=b[k][2+i]]))
    print(seed,i,(x,y),'dists',[(k,d,m) for k,d,m,_ in I if d<2.1],'seq(cal,imaged)',seq,flush=True)
