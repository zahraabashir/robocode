from env_client import make_env
import numpy as np, kin
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
obs, info = env.reset(seed=1)
r = obs.get_object_from_name('robot')
def getq(o): return np.array([o.get(r,f) for f in F])
base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
q=getq(obs)
M=kin.fk(base,q); print("init ee",M[:3,3], M[:3,2])
yaw=np.arctan2(M[1,0],M[0,0])
def goto(pos, yaw):
    global obs,q
    qt,ok=kin.ik(base,q,np.array(pos),kin.down_R(yaw))
    if not ok: print("ik fail",pos); return False
    while True:
        d=qt-q; 
        if np.max(np.abs(d))<1e-6: return True
        d=np.clip(d,-0.19,0.19)
        a=np.zeros(11,dtype=np.float32); a[3:10]=d
        obs,_,_,_,_=env.step(a); qn=getq(obs)
        if np.allclose(qn,q): print("rejected at", kin.fk(base,q)[:3,3]); return False
        q=qn
x,y=0.25,-0.2
z=0.34
goto([x,y,z],yaw)
print("at",kin.fk(base,q)[:3,3])
while z>-0.1:
    z-=0.005
    if not goto([x,y,z],yaw): break
print("final ee", kin.fk(base,q)[:3,3])
env.close()
