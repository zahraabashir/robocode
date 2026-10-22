import concurrent.futures,numpy as np
from env_client import make_env
base=(.314,-2.227,-.614)
triples=[(base[0]+d2,base[1]+d4,base[2]+d6) for d2,d4,d6 in
         [(0,0,0),(-.1,0,0),(.08,0,0),(0,-.1,-.1),(0,.1,.1),(0,0,-.18),(0,0,.18),(.15,-.15,0),(-.15,.15,0)]]
def run(c):
 e=make_env();s,_=e.reset(seed=1,options={'object_count':0});q=np.array([0,c[0],-np.pi,c[1],0,c[2],np.pi/2])
 def v(n,f):return s.get(s.get_object_from_name(n),f)
 for t in range(25):
  r=s.get_object_from_name('robot');cur=np.array([s.get(r,'joint_%d'%i) for i in range(1,8)]);a=np.zeros(11,np.float32)
  a[0]=np.clip(-.3-v('robot','pos_base_x'),-.2,.2);a[1]=np.clip(v('target_block','pose_y')-.00135-v('robot','pos_base_y'),-.2,.2);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1 if t<16 else -1;s,*_=e.step(a)
  if v('target_block','grasp_active')>.5:
   out=(c,t,round(v('robot','finger_state'),3),round(v('robot','grasp_tf_z'),3));e.close();return out
 e.close();return (c,None,None,None)
with concurrent.futures.ThreadPoolExecutor(max_workers=9) as ex:
 for x in ex.map(run,triples):print(x,flush=True)
