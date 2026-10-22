from env_client import make_env
import numpy as np

def vals(s, o):
    feats = ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z',
             'object_type','grasp_active','pos_base_x','pos_base_y','pos_base_rot',
             'joint_1','joint_2','joint_3','joint_4','joint_5','joint_6','joint_7',
             'finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z']
    out={}
    for f in feats:
        try: out[f]=float(s.get(o,f))
        except Exception: pass
    return out

e=make_env(); s,info=e.reset(seed=0)
print('info', info, 'max', e.max_steps, 'names', s.get_object_names())
for n in s.get_object_names(): print(n, vals(s,s.get_object_from_name(n)))
for ix in range(11):
    e2=make_env(); q,_=e2.reset(seed=0); a=np.zeros(11,np.float32); a[ix]=e2.action_space.high[ix]
    q,r,t,tr,inf=e2.step(a)
    rob=q.get_object_from_name('robot')
    print('ACT',ix,'rtt',r,t,tr,'robot',vals(q,rob))
    for n in q.get_object_names():
        if n!='robot': print(' ',n,vals(q,q.get_object_from_name(n)))
    e2.close()
e.close()
