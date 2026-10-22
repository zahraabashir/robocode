import time
from pB_lib import *
t=time.time(); s=Sim(44); print('reset',time.time()-t); t=time.time()
n=0
_a=s.act
def act(*a,**k):
    global n; n+=1; return _a(*a,**k)
s.act=act
s.goto(0,1.0,0.7); print('goto',n,time.time()-t)
