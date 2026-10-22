from env_client import make_env
import numpy as np, kin, sys
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); obj=sys.argv[3] if len(sys.argv)>3 else 'target_block'
out=[]
for ang in [0,90,180,270]:
    d=np.array([np.cos(np.radians(ang)),np.sin(np.radians(ang))])
    obs, info = env.reset(seed=seed)
    r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name(obj)
    getq=lambda o: np.array([o.get(r,f) for f in F])
    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
    q=getq(obs)
    def go(p):
        global q,obs
        qt,ok=kin.ik(base,q,np.array(p),kin.down_R(yaw))
        while np.max(np.abs(qt-q))>1e-6:
            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
            obs,_,_,_,_=env.step(a); qn=getq(obs)
            if np.allclose(qn,q): return False
            q=qn
        return True
    s=0.2
    go([bx-d[0]*s,by-d[1]*s,bz+0.3]); ok=go([bx-d[0]*s,by-d[1]*s,bz+0.165])
    if not ok: out.append((ang,'startblocked')); continue
    while s>-0.2:
        s-=0.002
        if not go([bx-d[0]*s,by-d[1]*s,bz+0.165]): break
    out.append((ang, round(-s,3)))
print("seed",seed,"yaw",yaw,obj,"block",round(bx,3),round(by,3),"contact offsets (EE - block along -d):",out)
env.close()
