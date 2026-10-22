from env_client import make_env
import numpy as np, sys
from kin import tool_fk, tool_ik, down_R
env = make_env()
seed=int(sys.argv[1]); dz=float(sys.argv[2])
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
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
def move(p, n=10):
    cur=tool_fk(q_of(obs),base)[:3,3]
    for k in range(1,n+1):
        qt,ok=tool_ik(q_of(obs),cur+(p-cur)*k/n,down_R(0),base)
        if not goto(qt): return False
    return True
obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_object_from_name('target_block')
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); hz=obs.get(B,'half_extent_z')
print('block',bp)
print(move(bp+[0,0,0.15]), move(bp+[0,0,hz+dz]))
print('tool',np.round(tool_fk(q_of(obs),base)[:3,3],4))
a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
print('grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'),np.round([obs.get(R,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qw']],4))
print('lift',move(bp+[0,0,0.2]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
print('move',move(bp+[0,-0.1,0.2]))
print('down',move(bp+[0,-0.1,hz+dz+0.05]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
for k in range(3):
    a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
    print('open: grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'))
print('down2',move(bp+[0,-0.1,hz+dz+float(sys.argv[3])]), 'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
for k in range(3):
    a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
    print('open: grasp',obs.get(R,'grasp_active'),obs.get(R,'finger_state'))
print('open: grasp',obs.get(R,'grasp_active'),'block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
obs,*_=env.step(np.zeros(11,dtype=np.float32))
print('block', np.round([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']],4))
env.close()
