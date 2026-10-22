import concurrent.futures,numpy as np,sys,itertools
from env_client import make_env
def v(s,n,f):return s.get(s.get_object_from_name(n),f)
seed=int(sys.argv[1]) if len(sys.argv)>1 else 3
name=sys.argv[2] if len(sys.argv)>2 else 'obstruction1'
def run(spec):
 off,q7=spec;e=make_env();s,_=e.reset(seed=seed);y=v(s,name,'pose_y')
 tar=np.array([0,.40,-np.pi,-2.22,0,-.61,q7])
 for t in range(15):
  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
  a[0]=np.clip(-.12-v(s,'robot','pos_base_x'),-.2,.2);a[1]=np.clip(y+off-v(s,'robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(tar-cur,-.2,.2);a[10]=1 if t<9 else -1;s,*_=e.step(a)
  if v(s,name,'grasp_active')>.5:
   out=(round(off,3),round(q7,3),round(v(s,'robot','finger_state'),3));e.close();return out
 e.close();return None
specs=[(.00135,q7) for q7 in (0.,np.pi/2,np.pi)]
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
 for out in ex.map(run,specs):
  if out:print(out,flush=True)
