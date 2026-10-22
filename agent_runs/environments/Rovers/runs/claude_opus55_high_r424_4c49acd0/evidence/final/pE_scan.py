from pE_lib import *
import sys
seed,i,y,x0,x1,st=eval(sys.argv[1])
for x in np.arange(x0,x1+1e-9,st):
    s=Sim(seed)
    if not drive(s,i,x,y): print(round(x,3),'noreach'); continue
    I=info(s,i); act1(s,i,'cal'); print(round(x,3),s.r(i)['calibrated'],[(k,d,m) for k,d,m,_ in I if d<2.1],flush=True)
