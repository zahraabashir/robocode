from env_client import make_env
import numpy as np, kin, sys
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
yaw=float(sys.argv[1])
for dz in [0.13,0.15,0.17,0.19,0.21]:
  for dx,dy in [(0,0),(0.02,0),(-0.02,0),(0,0.02),(0,-0.02)]:
    obs, info = env.reset(seed=1)
    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
    getq=lambda o: np.array([o.get(r,f) for f in F])
    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
    q=getq(obs); stop=False
    for z in list(np.arange(bz+0.3,bz+dz,-0.01))+[bz+dz]:
        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
        while np.max(np.abs(qt-q))>1e-6:
            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
            obs,_,_,_,_=env.step(a); qn=getq(obs)
            if np.allclose(qn,q): stop=True; break
            q=qn
        if stop: break
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,_,_,_,_=env.step(a)
    print(dz,dx,dy,"blocked" if stop else "", "ee",np.round(kin.fk(base,q)[:3,3],3),"finger",obs.get(r,'finger_state'),"grasp",obs.get(r,'grasp_active'))
env.close()
