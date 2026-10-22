from env_client import make_env
import numpy as np
e=make_env();s,_=e.reset(seed=0);o=s.get_object_from_name('rover0')
def step(dx=0,dy=0,op=0):
 global s
 a=np.zeros(8);a[:4]=dx,dy,0,op;s,*_=e.step(a)
def p():return np.array([s.get(o,'x'),s.get(o,'y')])
def go(t):
 for k in range(30):
  q=p();d=np.clip(np.array(t)-q,-.2,.2)
  if max(abs(d))<1e-5:break
  step(*d)
  if np.linalg.norm(p()-q)<1e-7:break

def flags():return [(ob.name,s.get(ob,'have_image_rover0'),s.get(ob,'received_image')) for ob in s.get_objects(e.observation_space.get_type('objective'))]
go((1,.9));step(op=-.5);step(op=-1/6);print('camera',p(),flags())
for y in [.7,.5,.3,.1,-.1,-.3,-.5,-.7,-.9,-1.1,-1.3,-1.5,-1.75]:
 go((1,y));step(op=.5);print('send',p(),flags())
e.close()
