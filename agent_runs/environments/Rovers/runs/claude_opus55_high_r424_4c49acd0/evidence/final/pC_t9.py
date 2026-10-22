from pC_lib import *
import numpy as np
reset(11)
goto(1,-1.5,-1.0); goto(1,-2.0,1.0,np.pi/2); step(s1='calibrate'); step(s1='image'); step(s1='send')
goto(1,-1.0,-1.0)
sx,sy=g('sample3','x'),g('sample3','y'); goto(0,1.0,sy); goto(0,sx,sy); step(s0='sample'); step(s0='send'); step(s0='drop'); print('soil',SM(3))
for p in [(1.0,0.4),(1.65,0.4),(1.65,1.0)]: goto(0,*p)
step(s0='sample');
for p in [(1.65,0.4),(1.0,0.4),(1.0,-0.9)]:
    goto(0,*p); step(s0='send'); print('rock2',p,SM(2))
step(s0='drop'); goto(0,1.0,-1.75,np.pi)
goto(1,-1.5,-1.0); goto(1,-1.0,-1.75,0.0); step(); print('term?',S.te,S.n)
for dx,dth in [(0.22,0),(0.24,0),(0.26,0),(0.28,0),(0,0.4),(0,0.45)]:
    goto(1,-1.0+dx,-1.75,dth); print(dx,dth,R(1)[5],end='; ')
goto(1,-1.0,-1.75+0.24,0); print('y.24',R(1)[5])
