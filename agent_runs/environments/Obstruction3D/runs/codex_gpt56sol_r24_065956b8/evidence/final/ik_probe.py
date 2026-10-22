from env_client import make_env
import numpy as np
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation

ORIGINS=[([0,0,.15643],[np.pi,0,0]),([0,.005375,-.12838],[np.pi/2,0,0]),([0,-.21038,-.006375],[-np.pi/2,0,0]),([0,.006375,-.21038],[np.pi/2,0,0]),([0,-.20843,-.006375],[-np.pi/2,0,0]),([0,.00017505,-.10593],[np.pi/2,0,0]),([0,-.10593,-.00017505],[-np.pi/2,0,0])]
Q0=np.array([0,-.35,-np.pi,-2.5,0,-.87,np.pi/2])
def fk(q):
 T=np.eye(4)
 for qi,(xyz,rpy) in zip(q,ORIGINS):
  A=np.eye(4);A[:3,:3]=Rotation.from_euler('xyz',rpy).as_matrix();A[:3,3]=xyz
  Z=np.eye(4);Z[:3,:3]=Rotation.from_euler('z',qi).as_matrix();T=T@A@Z
 A=np.eye(4);A[:3,:3]=Rotation.from_euler('x',np.pi).as_matrix();A[:3,3]=[0,0,-.061525]
 return T@A
def ik(xyz,off):
 def fun(q):
  T=fk(q); grasp=T[:3,3]+off*T[:3,2]
  return np.r_[5*(grasp-xyz), T[:2,2], .15*(q-Q0)]
 return least_squares(fun,Q0,max_nfev=300).x
def val(s,n,f): return float(s.get(s.get_object_from_name(n),f))

for off in [.04,.08,.12,.16]:
 e=make_env();s,_=e.reset(seed=0);xyz=np.array([val(s,'target_block',f) for f in ['pose_x','pose_y','pose_z']])
 q=ik(xyz-np.array([-.12,0,0]),off) # base frame target
 print('OFF',off,'q',q,'fk',fk(q)[:3,3], 'gp',fk(q)[:3,3]+off*fk(q)[:3,2])
 for k in range(40):
  rob=s.get_object_from_name('robot'); cur=np.array([float(s.get(rob,'joint_'+str(i))) for i in range(1,8)])
  a=np.zeros(11,np.float32);a[3:10]=np.clip(q-cur,-.2,.2);a[10]=1
  s,r,t,tr,info=e.step(a)
  if np.max(np.abs(q-cur))<.01:break
 a=np.zeros(11,np.float32);a[10]=-1;s,r,t,tr,info=e.step(a)
 print(' grasp',val(s,'robot','grasp_active'),val(s,'target_block','grasp_active'),'obj',[val(s,'target_block',f) for f in ['pose_x','pose_y','pose_z']], 'tf',[val(s,'robot',f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
 e.close()
