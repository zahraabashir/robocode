from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
seed=int(sys.argv[1]); yaw=float(sys.argv[2])
obs, info = env.reset(seed=seed)
R = obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
bx,by,bz=[obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]
print('block',bx,by,bz,[obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']])
def goto(qt, grip=0):
    global obs
    for _ in range(40):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-4: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=grip
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q): return False
    return False
for z in np.arange(0.35,0.1,-0.005):
    qt,ok=ik(q_of(obs),np.array([bx,by,z]),down_R(yaw),base)
    if not goto(qt): print('blocked at',z); break
ee=fk(q_of(obs),base)[:3,3]; print('ee',ee)
a=np.zeros(11,dtype=np.float32); a[10]=-1
obs,*_=env.step(a)
print('grasp', obs.get(R,'grasp_active'), obs.get(R,'finger_state'), obs.get(B,'grasp_active'))
print('tf',[round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
# lift
for z in np.arange(ee[2],0.35,0.01):
    qt,ok=ik(q_of(obs),np.array([bx,by,z]),down_R(yaw),base)
    goto(qt)
print('block after lift',[round(obs.get(B,f),4) for f in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']], 'ee',fk(q_of(obs),base)[:3,3])
env.close()
