from env_client import make_env
import numpy as np

def experiment(joint,epsilon,release=False):
 e=make_env();s,i=e.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
 def step(a):
  nonlocal s
  s,re,t,tr,i=e.step(np.array(a,dtype=np.float32));return t
 x=s.get(b,'x')+s.get(b,'width')/2;top=s.get(b,'y')+s.get(b,'height'); y=top+joint+epsilon
 for k in range(30):
  step([np.clip(x-s.get(r,'x'),-.05,.05),np.clip(y-s.get(r,'y'),-.05,.05),0,np.clip(joint-s.get(r,'arm_joint'),-.1,.1),1])
 by=s.get(b,'y');ry=s.get(r,'y');step([0,.05,0,0,1]);dy=s.get(b,'y')-by
 print('joint eps',joint,epsilon,'base_y',round(ry,5),'offset',round(ry-top,5),'grasp',round(dy,5))
 if release:
  for k in range(5):step([0,.05,0,0,1])
  print('lift',s.get(b,'y'));step([0,0,0,0,0]);print('release',s.get(b,'y'))
  for k in range(5):step([0,0,0,0,0])
  print('after5',s.get(b,'y'))
 e.close()
for joint in [.1,.2]:
 for epsilon in [0,.005,.009,.01,.011,.015,.02,.03]:experiment(joint,epsilon)
experiment(.2,.01,True)
