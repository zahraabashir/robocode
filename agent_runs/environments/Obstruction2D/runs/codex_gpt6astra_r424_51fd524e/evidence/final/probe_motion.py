from env_client import make_env
import numpy as np

def vals(s,n,fs):
 o=s.get_object_from_name(n);return [round(float(s.get(o,f)),7) for f in fs.split()]
def run():
 e=make_env();s,_=e.reset(seed=0)
 def step(a):
  nonlocal s
  s,*_=e.step(np.array(a,dtype=np.float32))
 def show(t):print(t,vals(s,'robot','x y theta arm_joint'),vals(s,'target_block','x y'))
 for label,a,n in [('retract',[0,0,0,-.1,0],5),('left',[-.05,0,0,0,0],20),('up',[0,.05,0,0,0],20),('right',[.05,0,0,0,0],60),('down',[0,-.05,0,0,0],30),('extend',[0,0,0,.1,0],5)]:
  for _ in range(n):step(a)
  show(label)
 e.close()
 e=make_env();s,_=e.reset(seed=0)
 bx,by,bw,bh=vals(s,'target_block','x y width height');cx=bx+bw/2
 for _ in range(20):
  rx,ry,arm=vals(s,'robot','x y arm_joint')
  step([np.clip(cx-rx,-.05,.05),np.clip(.4-ry,-.05,.05),0,.1,0])
 for _ in range(40):step([0,-.001,0,0,0])
 show('precise contact no vac')
 step([0,0,0,0,1]);step([0,.05,0,0,1]);show('lift')
 # Rotate grabbed object to inspect origin convention
 for _ in range(4):step([0,0,.196,0,1])
 show('rotated');print('blocktheta',vals(s,'target_block','theta'))
 e.close()
run()
e=make_env();s,_=e.reset(seed=0)
r=s.get_object_from_name('robot')
for axis,sign in [(0,-1),(1,1),(0,1)]:
 for size in [.05,.005,.0005,.00005]:
  for _ in range(60 if size==.05 else 120):
   a=np.zeros(5,dtype=np.float32);a[axis]=sign*size
   s,*_=e.step(a)
 print('BOUND',axis,sign,vals(s,'robot','x y'))
e.close()
