import numpy as np
from env_client import make_env
import approach, kin
env=make_env(); obs,info=env.reset(seed=2)
ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
r=obs.get_object_from_name('robot')
for t in range(40):
    if obs.get(r,'grasp_active')>0.5: break
    obs,*_=env.step(ap.get_action(obs))
print("grasped at", t)
F=approach.JF
def state():
    q=np.array([obs.get(r,f) for f in F]); base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    return q,base
for d in []:
    q,base=state(); M=kin.fk(base,q,0.12)
    qt,ok=kin.ik(base,q,M[:3,3]+np.array(d),M[:3,:3],tool=0.12)
    a=np.zeros(11,dtype=np.float32); a[3:10]=qt-q; a[10]=-1
    obs,*_=env.step(a); q2,_=state()
    print(d, "moved" if not np.allclose(q,q2) else "REJECTED")
print("---- 3mm steps")
o1=obs.get_object_from_name('obstruction1')
for i in range(30):
    q,base=state(); M=kin.fk(base,q,0.12)
    qt,ok=kin.ik(base,q,M[:3,3]+np.array([0,0,0.003]),M[:3,:3],tool=0.12)
    a=np.zeros(11,dtype=np.float32); a[3:10]=qt-q; a[10]=-1
    obs,*_=env.step(a); q2,_=state()
    print(i, round(M[2,3],3), "moved" if not np.allclose(q,q2) else "REJECTED", [round(obs.get(o1,f),3) for f in ['pose_x','pose_y','pose_z']], np.round(qt-q,3))
