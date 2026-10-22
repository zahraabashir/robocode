from env_client import make_env
import numpy as np, kin, sys
F=['joint_%d'%i for i in range(1,8)]
seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
env=make_env()
res=[]
for dz in [0.0,0.01,0.02,0.03,0.04,0.05]:
    obs,_=env.reset(seed=seed)
    r=obs.get_object_from_name('robot'); o=obs.get_object_from_name(name)
    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    p=np.array([obs.get(o,f) for f in ['pose_x','pose_y','pose_z']])
    q=np.array([obs.get(r,f) for f in F])
    blocked=False
    for z in list(np.arange(0.3,p[2]+dz,-0.01))+[p[2]+dz]:
        qt,ok=kin.ik(base,q,np.array([p[0],p[1],z]),kin.down_R(yaw),tool=0.12)
        while np.max(np.abs(qt-q))>1e-6:
            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
            obs,_,_,_,_=env.step(a); qn=np.array([obs.get(r,f) for f in F])
            if np.allclose(qn,q): blocked=True; break
            q=qn
        if blocked: break
    a=np.zeros(11,dtype=np.float32); a[10]=-1
    obs,_,_,_,_=env.step(a)
    res.append((dz, 'B' if blocked else '', round(kin.fk(base,q,0.12)[2,3]-p[2],3), obs.get(r,'grasp_active'), round(obs.get(r,'finger_state'),3)))
print(seed,name,yaw,res)
