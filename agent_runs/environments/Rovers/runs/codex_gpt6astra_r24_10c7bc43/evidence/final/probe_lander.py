from env_client import make_env
import numpy as np
e=make_env();s,_=e.reset(seed=2);o=s.get_object_from_name('rover1')
for ob in s.get_objects(e.observation_space.get_type('obstacle')):
 x,y=s.get(ob,'x'),s.get(ob,'y')
 if x<0 and y<-1: print('near',ob.name,x,y)
def go(t):
 global s
 for k in range(30):
  p=np.array([s.get(o,'x'),s.get(o,'y')]);d=np.clip(np.array(t)-p,-.2,.2)
  if max(abs(d))<1e-6:break
  a=np.zeros(8);a[4:6]=d;s,*_=e.step(a)
  q=np.array([s.get(o,'x'),s.get(o,'y')])
  if np.linalg.norm(q-p)<1e-7:break
 print(t,s.get(o,'x'),s.get(o,'y'))
for t in [(-1.,-1.1),(-1.9,-1.1),(-1.9,-1.49),(-1.9,-1.495),(-1.9,-1.499),(-1.9,-1.5)]:go(t)
e.close()
