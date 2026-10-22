from env_client import make_env
import numpy as np

e=make_env()
def act(s,j,v):
 a=np.zeros(11,dtype=np.float32);a[j]=v
 return e.step(a)[0]
def pos(s):
 r=s.get_object_from_name('robot');return [round(s.get(r,f),4) for f in ['pos_base_x','pos_base_y','joint_2','joint_4','joint_6','finger_state']]
for y in [-.8,-.6,-.4,-.2,0,.2,.4,.6,.8]:
 s,_=e.reset(seed=0)
 for _ in range(round(abs(y)/.2)):s=act(s,1,np.sign(y)*.2)
 for _ in range(5):s=act(s,0,.1)
 print('BASETEST',y,pos(s),flush=True)
for j in [4,6,8]:
 for delta in [-1,-.6,-.2,0,.2,.6,1]:
  s,_=e.reset(seed=0)
  for _ in range(round(abs(delta)/.2)):s=act(s,j,np.sign(delta)*.2)
  before=pos(s)
  for _ in range(3):s=act(s,0,.1)
  print('JOINTTEST',j,delta,before,pos(s),flush=True)
e.close()
