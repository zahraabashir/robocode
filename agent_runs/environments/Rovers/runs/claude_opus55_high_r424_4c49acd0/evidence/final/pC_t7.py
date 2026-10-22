from pC_lib import *
import numpy as np
reset(11)
goto(1,-1.5,-1.0); goto(1,-2.0,1.0,np.pi/2); step(s1='calibrate'); step(s1='image'); step(s1='send')
sx,sy=g('sample0','x'),g('sample0','y'); goto(1,sx,sy); step(s1='sample'); step(s1='send')
goto(1,-1.5,-1.0); goto(1,-1.0,-1.75,0.0); print('r1 home',R(1),S.te,S.n)
sx,sy=g('sample3','x'),g('sample3','y'); goto(0,1.0,sy); goto(0,sx,sy); step(s0='sample'); r=step(s0='send'); print('soil sent',r,SM(3),S.n)
for k in range(300):
    p=R(0)
    goal=(1.0,-1.75,np.pi)
    dx,dy=goal[0]-p[0],goal[1]-p[1]; dt=(goal[2]-p[2]+np.pi)%(2*np.pi)-np.pi
    r=step((np.clip(dx,-.2,.2),np.clip(dy,-.2,.2),np.clip(dt,-.2,.2)))
    if r[1] or r[2] or (abs(dx)+abs(dy)+abs(dt)<1e-3): break
print('end',r,R(0),R(1),S.n)
r=step(); print(r)
goto(0,1.0,-0.9); r=step(s0='send'); print('resend',r,SM(3))
goto(0,1.0,-1.75,np.pi); print(R(0),S.te,S.tr,S.n)
r=step(); print(r)
goto(1,-1.0,-1.0); r=step(s0='send'); print('resend r1 moved',r,SM(3))
goto(1,-1.0,-1.75,0.0); print(R(0),R(1),S.te,S.tr,S.n)
r=step(); print(r)
r=step(s0='drop'); print('drop0',r)
r=step(s1='drop'); print('drop1',r,R(0),R(1),S.n)
