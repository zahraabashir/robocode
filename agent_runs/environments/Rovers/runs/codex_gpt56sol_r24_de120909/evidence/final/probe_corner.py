import numpy as np
from env_client import make_env
e=make_env();s,_=e.reset(seed=13)
def go(x,y):
 global s
 for _ in range(30):
  r=s.get_object_from_name('rover1'); px,py=s.get(r,'x'),s.get(r,'y')
  a=np.zeros(8,np.float32);a[4]=max(-.2,min(.2,x-px));a[5]=max(-.2,min(.2,y-py))
  old=(px,py);s,*_=e.step(a)
  r=s.get_object_from_name('rover1');new=(s.get(r,'x'),s.get(r,'y'))
  print('go',x,y,'old',old,'new',new)
  if abs(new[0]-x)<.03 and abs(new[1]-y)<.03:return
  if new==old:return
go(-1,-1.4);go(-2.25,-1.4);go(-2.25,-2.05)
a=np.zeros(8,np.float32);a[7]=-5/6;s,*_=e.step(a)
r=s.get_object_from_name('rover1');print('FINAL',s.get(r,'x'),s.get(r,'y'),s.get(r,'store_full'))
e.close()
