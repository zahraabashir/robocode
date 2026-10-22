from env_client import make_env
from kin import *
E=make_env()
for dx,dy,zz in [(v,0,.155) for v in [0,.005,.01,.02,.03,-.01,-.02]]+[(0,v,.155) for v in [.005,.01,.02,.03,-.01,-.02]]+[(0,0,v) for v in [.17,.165,.16,.15,.14,.13,.12]]:
 s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block');fs=['joint_'+str(i) for i in range(1,8)]
 def vec(s):return np.array([s.get(r,f) for f in fs])
 x,y,z=[s.get(b,'pose_'+f) for f in 'xyz']
 for zt in [.3]*15+list(np.arange(.3,zz,-.005))+[zz]:
  q=ik(x+dx,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[1]=np.clip(y+dy-.001-s.get(r,'pos_base_y'),-.12,.12);s,*_=E.step(a)
 a[:]=0;a[10]=-1;s,*_=E.step(a)
 print('GRASPTEST',dx,dy,zz,s.get(r,'grasp_active'),'fkz',fk(vec(s))[0][2],flush=True)
E.close()
