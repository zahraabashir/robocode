from env_client import make_env
import numpy as np, kin, sys
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
for yaw in [0, 1.5708]:
  for dx,dy in [(0,0),(-0.02,0),(0.02,0),(0,0.02),(0,-0.02),(-0.035,0),(0,-0.04)]:
    obs, info = env.reset(seed=1)
    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
    getq=lambda o: np.array([o.get(r,f) for f in F])
    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
    q=getq(obs); stop=False
    z=bz+0.3
    while not stop and z>0.2:
        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
        while np.max(np.abs(qt-q))>1e-6:
            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
            obs,_,_,_,_=env.step(a); qn=getq(obs)
            if np.allclose(qn,q): stop=True; break
            q=qn
        z-= 0.01 if z>bz+0.2 else 0.002
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,_,_,_,_=env.step(a)
    print(yaw,dx,dy,"ee",np.round(kin.fk(base,q)[:3,3],3),"grasp",obs.get(r,'grasp_active'),obs.get(tb,'grasp_active'))
env.close()
