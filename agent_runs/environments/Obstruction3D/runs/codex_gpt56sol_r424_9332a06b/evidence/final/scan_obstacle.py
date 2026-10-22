import concurrent.futures,itertools,numpy as np
from env_client import make_env
def v(s,n,f):return s.get(s.get_object_from_name(n),f)
def trial(c):
 e=make_env();s,_=e.reset(seed=0);name='obstruction0';tar=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2]);y=v(s,name,'pose_y')
 for t in range(12):
  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
  a[1]=np.clip(y-.00135-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<7 else -1
  s,*_=e.step(a)
  if v(s,'robot','grasp_active')>.5:e.close();return c,True
 e.close();return c,False
cs=list(itertools.product([.05,.12,.19,.26,.33],[-2.55,-2.4,-2.25,-2.1],[-1.05,-.85,-.65,-.45]))
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
 for c,o in ex.map(trial,cs):
  if o:print('SUCCESS',c,flush=True)
