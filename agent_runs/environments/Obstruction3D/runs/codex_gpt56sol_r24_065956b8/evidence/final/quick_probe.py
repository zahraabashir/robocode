from env_client import make_env
import numpy as np

def get(s,n,f): return float(s.get(s.get_object_from_name(n),f))
def snap(s):
    names=sorted(s.get_object_names())
    rob=[get(s,'robot',f) for f in ['pos_base_x','pos_base_y','pos_base_rot','joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_7','finger_state','grasp_active','grasp_tf_x','grasp_tf_y','grasp_tf_z']]
    objs={n:[get(s,n,f) for f in ['pose_x','pose_y','pose_z','grasp_active']] for n in names if n!='robot'}
    return rob,objs

e=make_env(); s,_=e.reset(seed=0); print('start',snap(s))
seq=[]
a=np.zeros(11,np.float32); a[10]=-1; seq.append(a)
for idx in range(10):
    a=np.zeros(11,np.float32); a[idx]=.2; seq.append(a)
for k,a in enumerate(seq):
    s,r,t,tr,i=e.step(a); print(k, snap(s), r,t,tr)
e.close()
