from env_client import make_env
import numpy as np, sys
from kin import fk, ik, down_R
env = make_env()
seed=1
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
def goto(qt):
    global obs
    for _ in range(60):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-5: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2)
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
bx,by=0.1377,0.1831
yaw=float(sys.argv[1])
for dirn in [(1,0),(-1,0),(0,1),(0,-1)]:
  for z in [0.24,0.28,0.32,0.36]:
    obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot')
    base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
    start=np.array([bx-0.15*dirn[0],by-0.15*dirn[1],z])
    qt,ok=ik(q_of(obs),start+[0,0,0.1],down_R(yaw),base); goto(qt)
    qt,ok=ik(q_of(obs),start,down_R(yaw),base); r=goto(qt)
    if not r: print('start blocked'); continue
    s=0
    while s<0.3:
        p=start+np.array([dirn[0],dirn[1],0])*(s+0.002)
        qt,ok=ik(q_of(obs),p,down_R(yaw),base)
        if not goto(qt): break
        s+=0.002
    pos=start+np.array([dirn[0],dirn[1],0])*s
    print('dir',dirn,'z',z,'stopped at',np.round(pos,3),'offset from block ctr',np.round(pos[:2]-[bx,by],3) if s<0.3 else 'passed')
env.close()
