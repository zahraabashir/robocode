# measure blocking height at many xy
from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
seed=int(sys.argv[1])
obs0, info = env.reset(seed=seed)
R = obs0.get_object_from_name('robot')
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
base=(obs0.get(R,'pos_base_x'), obs0.get(R,'pos_base_y'), obs0.get(R,'pos_base_rot'))
for n in sorted(obs0.get_object_names()):
    if n=='robot': continue
    o=obs0.get_object_from_name(n); print(n,[round(obs0.get(o,f),3) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
def goto(qt):
    global obs
    for _ in range(40):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-5: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
pts=[tuple(map(float,s.split(','))) for s in sys.argv[2:]]
for (x,y) in pts:
    obs,_=env.reset(seed=seed)
    qt,ok=ik(q_of(obs),np.array([x,y,0.32]),down_R(0),base); goto(qt)
    z=0.32
    while z>0.0:
        qt,ok=ik(q_of(obs),np.array([x,y,z-0.002]),down_R(0),base)
        if not goto(qt): break
        z-=0.002
    print((x,y),'lowest flange z',round(z,4))
env.close()
