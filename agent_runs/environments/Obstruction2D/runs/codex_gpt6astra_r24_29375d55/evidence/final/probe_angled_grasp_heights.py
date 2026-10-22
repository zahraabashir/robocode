from env_client import make_env
import numpy as np
import math
for sign,heightoff in [(1,.216),(1,.213),(1,.210),(1,.207),(1,.204),(-1,.213),(-1,.207)]:
 e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
 theta=-math.pi/2+sign*.22
 def step(a):
  global s
  s,*_=e.step(np.array(a,dtype=np.float32))
 def move(x,y,v=0):
  for _ in range(40):
   rx,ry,rt=[s.get(r,f) for f in ['x','y','theta']]
   if abs(rx-x)<1e-5 and abs(ry-y)<1e-5 and abs(rt-theta)<1e-5:break
   step([np.clip(x-rx,-.05,.05),np.clip(y-ry,-.05,.05),np.clip(theta-rt,-.196,.196),np.clip(.2-s.get(r,'arm_joint'),-.1,.1),v])
 x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
 gx=x-.045 if sign==1 else x+w+.045; gy=y+h+heightoff
 move(gx,.8);move(gx,gy);step([0,0,0,0,1]);before=[s.get(b,f) for f in ['x','y','theta']];robotbefore=[s.get(r,f) for f in ['x','y','theta']]
 step([0,.05,0,0,1]);after=[s.get(b,f) for f in ['x','y','theta']]
 step([.05,0,0,0,1]);horizontal=[s.get(b,f) for f in ['x','y','theta']]
 print({'sign':sign,'requested_base':[gx,gy,theta],'actual_base':robotbefore,'before':before,'lifted':after,'translated':horizontal},flush=True);e.close()
