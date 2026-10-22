from pC_lib import *
import time
reset(11)
sx,sy=g('sample3','x'),g('sample3','y'); goto(0,1.0,sy); goto(0,sx,sy); step(s0='sample')
s=g('sample3','analyzed_rover0'); step(s0='drop'); step(s0='sample'); print('resample same', R(0), SM(3))
t=time.time()
while True:
    r=step()
    if r[1] or r[2]: break
print('end at',S.n,r,time.time()-t)
