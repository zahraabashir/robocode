from env_client import make_env
from approach import GeneratedApproach
import numpy as np

e=make_env();s,i=e.reset(seed=5828);a=GeneratedApproach(e.action_space,e.observation_space,{});a.reset(s,i);r=s.get_object_from_name('rover1')
def p(): return np.array([s.get(r,'x'),s.get(r,'y')])
def st(d=(0,0),theta=0,op=0):
 global s
 act=np.zeros(8);act[4:6]=d;act[6:8]=[theta,op];s,*_=e.step(act)
def go(target):
 for _ in range(50):
  d=np.clip(np.array(target)-p(),-.1,.1)
  if np.linalg.norm(d)<1e-5:break
  old=p();st(d)
  if np.linalg.norm(old-p())<1e-5:print('stuck',p(),target,flush=True);break
print('samples',[(str(o),a.xy(s,o).tolist()) for o in a.samples],flush=True)
go([-1,-1.3]);go([-2.25,-1.3])
for k in range(18):
 go([-2.0,-1.1]);st(theta=.4);go([-2.25,-1.1])
 for _ in range(80):
  old=p();st((0,-.005),op=-.833333)
  if np.linalg.norm(old-p())<1e-5:break
 print('angle',s.get(r,'theta'),'pos',p(),'sampled',[s.get(o,'analyzed_rover1') for o in a.samples],flush=True)

e.close()
