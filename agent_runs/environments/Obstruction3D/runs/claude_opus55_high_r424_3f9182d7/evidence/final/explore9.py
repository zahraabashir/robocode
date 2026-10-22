from env_client import make_env
import numpy as np, kin, sys
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
yaw=float(sys.argv[1]); axis=sys.argv[2]; other=float(sys.argv[3])
rng=np.arange(-0.12,0.121,0.02)
row=[]
for v in rng:
    dx,dy=(v,other) if axis=='x' else (other,v)
    obs, info = env.reset(seed=1)
    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
    getq=lambda o: np.array([o.get(r,f) for f in F])
    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
    q=getq(obs); stop=False
    z=bz+0.22
    while not stop and z>0.22:
        qt,ok=kin.ik(base,q,np.array([bx+dx,by+dy,z]),kin.down_R(yaw))
        if not ok: print("IKFAIL")
        while np.max(np.abs(qt-q))>1e-6:
            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
            obs,_,_,_,_=env.step(a); qn=getq(obs)
            if np.allclose(qn,q): stop=True; break
            q=qn
        z-=0.005
    row.append(kin.fk(base,q)[2,3])
print("yaw=%s axis=%s other=%s: "%(sys.argv[1],axis,other)+" ".join("%.3f"%v for v in row), flush=True)
env.close()
