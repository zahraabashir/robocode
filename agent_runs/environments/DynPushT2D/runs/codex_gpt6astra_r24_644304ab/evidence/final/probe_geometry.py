import numpy as np
from env_client import make_env
for xx in [0,.3,-.3]:
 e=make_env();o,_=e.reset(seed=0);p=o[:2].copy();a=o[2];R=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
 def go(t):
  global o
  for _ in range(150):
   d=t-o[16:18]
   if np.linalg.norm(d)<1e-5:break
   o,*_=e.step(np.clip(d,-.049,.049).astype(np.float32))
 go(p+R@np.array([xx,.8]));print('start',xx,(R.T@(o[16:18]-p)).tolist(),o[:3].tolist())
 for i in range(100):
  bef=o.copy();o,*_=e.step((R@np.array([0.,-.01])).astype(np.float32))
  if np.linalg.norm(o[:2]-p)>1e-5 or abs(o[2]-a)>1e-5:
   print('contact',xx,'robot before',(R.T@(bef[16:18]-p)).tolist(),'after',(R.T@(o[16:18]-p)).tolist(),'object',o[:3].tolist());break
 e.close()
