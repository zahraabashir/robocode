from env_client import make_env
import numpy as np

def run(release):
 e=make_env();s,_=e.reset(seed=0);r=s.get_object_from_name('robot');o=s.get_object_from_name('obstruction1')
 def step(a):
  nonlocal s
  s,_,_,_,_=e.step(np.array(a,dtype=np.float32))
 def pos(): return [round(s.get(z,f),4) for z in [r,o] for f in ['x','y']]
 def move(x,y,v=1):
  for _ in range(100):
   dx=x-s.get(r,'x');dy=y-s.get(r,'y')
   if max(abs(dx),abs(dy))<1e-5:break
   old=pos();step([np.clip(dx,-.05,.05),np.clip(dy,-.05,.05),0,0,v])
   if pos()==old:break
 x=s.get(o,'x')+s.get(o,'width')/2
 step([0,0,0,.1,0])
 move(x,s.get(r,'y'),0)
 move(x,s.get(o,'y')+s.get(o,'height')+.205)
 print('CONTACT',pos(),'arm',s.get(r,'arm_joint'))
 move(x,s.get(r,'y')+.2)
 print('LIFT',pos())
 if release:
  step([0,0,0,0,0]); print('RELEASE',pos())
  for i in range(4):step([-.05,0,0,0,0]);print('AFTER',i,pos())
 else:
  move(.85,s.get(r,'y')); move(.85,.4963); print('LOWER_ON_OBSTACLE',pos()); move(.85,.6963); move(1.8,s.get(r,'y'));print('RIGHT_BOUND',pos())
  for i in range(5):step([.05,0,0,0,1]);print('RIGHT_MORE',pos())
 e.close()
run(True);run(False)
