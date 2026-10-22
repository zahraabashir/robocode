from env_client import make_env
import numpy as np, sys, json
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
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
bx,by=0.1377,0.1831
obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
p=np.array([bx-0.1,by-0.04,0.235])
qt,ok=ik(q_of(obs),p+[0,0,0.05],down_R(0),base); goto(qt)
qt,ok=ik(q_of(obs),p,down_R(0),base); goto(qt)
a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
for n in sorted(obs.get_object_names()):
    o=obs.get_object_from_name(n)
    print(n, 'grasp_active', obs.get(o,'grasp_active'))
recs=[]
def rec():
    d={'q':q_of(obs).tolist(),'base':[obs.get(R,f) for f in ['pos_base_x','pos_base_y','pos_base_rot']],
       'tf':[obs.get(R,f) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']],
       'fs':obs.get(R,'finger_state')}
    for n in ['target_block']:
        o=obs.get_object_from_name(n); d[n]=[obs.get(o,f) for f in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']]
    recs.append(d)
rec()
qt,ok=ik(q_of(obs),p+[0,0,0.08],down_R(0),base); print('lift',goto(qt)); rec()
rng=np.random.default_rng(0)
for i in range(15):
    a=np.zeros(11,dtype=np.float32); a[3:10]=rng.uniform(-0.1,0.1,7); a[1]=rng.uniform(-0.05,0.05); a[2]=rng.uniform(-0.1,0.1)
    obs,*_=env.step(a); rec()
json.dump(recs,open('grasp_recs.json','w'))
for d in recs: print(np.round(d['target_block'],4), np.round(d['tf'],4), d['fs'])
env.close()
