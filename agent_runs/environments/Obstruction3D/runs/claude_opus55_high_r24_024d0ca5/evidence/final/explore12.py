from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
seed=1
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
def goto(qt,g=0):
    global obs
    for _ in range(60):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-5: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
        obs,r,te,tr,info=env.step(a)
        if obs.get(R,'grasp_active')>0: return 'G'
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
bx,by=0.1377,0.1831
z=float(sys.argv[1]); yaw=float(sys.argv[2])
obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
found=False
for dx in np.arange(-0.12,0.121,0.02):
    for dy in np.arange(-0.12,0.121,0.02):
        p=np.array([bx+dx,by+dy,z])
        qt,ok=ik(q_of(obs),p+[0,0,0.05],down_R(yaw),base); goto(qt)
        qt,ok=ik(q_of(obs),p,down_R(yaw),base); r=goto(qt)
        a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
        if obs.get(R,'grasp_active')>0 or r=='G':
            print('GRASP at',dx,dy,z, [round(obs.get(R,f),4) for f in ['finger_state','grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']]); found=True; break
    if found: break
print('done',z,yaw,found)
env.close()
