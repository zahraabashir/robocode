from env_client import make_env
import numpy as np, kin, sys
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
res=[]
for (x,y,yaw) in [(0.25,-0.2,0),(0.3,0.0,0),(0.1,-0.25,0.7),(0.35,0.3,0),(0.2,0.1,1.5)]:
    obs, info = env.reset(seed=1)
    r = obs.get_object_from_name('robot')
    getq=lambda o: np.array([o.get(r,f) for f in F])
    base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    q=getq(obs)
    z=0.34; stop=None
    while z>0.1 and stop is None:
        qt,ok=kin.ik(base,q,np.array([x,y,z]),kin.down_R(yaw))
        while np.max(np.abs(qt-q))>1e-6:
            a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qt-q,-0.19,0.19)
            obs,_,_,_,_=env.step(a); qn=getq(obs)
            if np.allclose(qn,q): stop=kin.fk(base,q)[:3,3]; break
            q=qn
        z-=0.004
    print(x,y,yaw,"stop",stop)
env.close()
