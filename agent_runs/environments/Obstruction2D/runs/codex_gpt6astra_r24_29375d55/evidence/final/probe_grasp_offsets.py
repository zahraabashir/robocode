from env_client import make_env
import numpy as np
for off in [-.022,-.03,-.035,-.04,-.043,-.045]:
 e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
 def step(a):
  global s
  s,*_=e.step(np.array(a,dtype=np.float32))
 def move(x,y,v=0):
  for _ in range(30):
   rx,ry=s.get(r,'x'),s.get(r,'y')
   if abs(rx-x)<1e-5 and abs(ry-y)<1e-5:break
   step([np.clip(x-rx,-.05,.05),np.clip(y-ry,-.05,.05),0,.1,v])
 x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
 move(x+w/2,.8);move(x+w/2,y+h+.215);step([0,0,0,0,1]);move(x+w/2,.65,1);step([0,0,0,0,0])
 x,y,w,h=[s.get(b,f) for f in ['x','y','width','height']]
 move(x+w/2,.85);move(x+off,.85);move(x+off,y+h+.215);step([0,0,0,0,1]);old=s.get(b,'y');step([0,.05,0,0,1]);dy=s.get(b,'y')-old
 print('offset',off,'grasp_delta_y',round(dy,6),'robot_x_error',round(s.get(r,'x')-x-off,6),flush=True);e.close()
