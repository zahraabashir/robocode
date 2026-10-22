from env_client import make_env
from kin import *
from scipy.spatial.transform import Rotation as R
E=make_env();s,_=E.reset(seed=0);r=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
fs=['joint_'+str(i) for i in range(1,8)]
def vec(s):return np.array([s.get(r,f) for f in fs])
def pose(s,o):return np.array([s.get(o,'pose_'+f) for f in ['x','y','z']]),R.from_quat([s.get(o,'pose_'+f) for f in ['qx','qy','qz','qw']]).as_matrix()
x,y,z=pose(s,b)[0]
for zt in [.32]*15+list(np.arange(.32,.14,-.005)):
 q=ik(x,zt);a=np.zeros(11,dtype=np.float32);a[3:10]=np.clip(q-vec(s),-.12,.12);a[1]=np.clip(y-.001-s.get(r,'pos_base_y'),-.12,.12);a[10]=-1;s,*_=E.step(a)
 if s.get(r,'grasp_active'):break
print('grabbed',s.get(r,'grasp_active'),flush=True)
def report(s):
 p,rr=pose(s,b);tf=np.array([s.get(r,'grasp_tf_'+f) for f in ['x','y','z']]);rt=R.from_quat([s.get(r,'grasp_tf_'+f) for f in ['qx','qy','qz','qw']]).as_matrix();eeR=rr@rt.T;ee=p-eeR@tf; pred,pr=fk(vec(s));pred+=np.array([s.get(r,'pos_base_x'),s.get(r,'pos_base_y'),0]);print('CAL',vec(s).round(6).tolist(),'actual',ee.round(8).tolist(),'delta',(ee-pred).round(8).tolist(),'localdelta',(pr.T@(ee-pred-np.array([.12,0,0]))).round(8).tolist(),'rerr',(eeR-pr).round(4).tolist(),flush=True)
report(s)
for j,d in [(4,-.1),(4,-.1),(8,.15),(3,.1),(6,.1)]:
 a=np.zeros(11,dtype=np.float32);a[j]=d;s,*_=E.step(a);report(s)
a=np.zeros(11,dtype=np.float32);a[10]=1;before=pose(s,b)[0];s,reward,done,tr,info=E.step(a);print('RELEASE',before,pose(s,b)[0],s.get(r,'grasp_active'),done,flush=True)
a[:]=0;s,*_=E.step(a);print('AFTERWAIT',pose(s,b)[0],flush=True)
E.close()
