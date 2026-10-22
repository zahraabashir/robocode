import concurrent.futures,itertools,numpy as np,sys
from env_client import make_env
seed=int(sys.argv[1]) if len(sys.argv)>1 else 8
name=sys.argv[2] if len(sys.argv)>2 else 'obstruction1'
def run(c):
 e=make_env();s,_=e.reset(seed=seed);q=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2])
 def v(n,f):return s.get(s.get_object_from_name(n),f)
 for t in range(16):
  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
  a[0]=np.clip(-.12-v('robot','pos_base_x'),-.2,.2);a[1]=np.clip(v(name,'pose_y')-.00135-v('robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
  if v(name,'grasp_active')>.5:out=(c,t,v('robot','finger_state'));e.close();return out
 e.close();return(c,None,None)
cs=list(itertools.product([.4,.5,.6,.7],[-2.2,-2.05,-1.9],[-.8,-.6,-.4]))
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
 for x in ex.map(run,cs):
  if x[1] is not None:print(x,flush=True)
