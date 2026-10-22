from env_client import make_env
import numpy as np, sys
from kin import tool_fk, tool_ik, down_R
env = make_env()
seed=int(sys.argv[1]); name=sys.argv[2]; yaw=float(sys.argv[3])
jn=[f'joint_{i}' for i in range(1,8)]
def q_of(o): return np.array([o.get(R,f) for f in jn])
def goto(qt,g=0):
    global obs
    for _ in range(60):
        q=q_of(obs); d=qt-q
        d=(d+np.pi)%(2*np.pi)-np.pi
        if np.max(np.abs(d))<1e-5: return True
        a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(d,-0.2,0.2); a[10]=g
        obs,r,te,tr,info=env.step(a)
        if np.allclose(q_of(obs),q,atol=1e-7): return False
    return False
def move(p, n=6):
    cur=tool_fk(q_of(obs),base)[:3,3]
    for k in range(1,n+1):
        qt,ok=tool_ik(q_of(obs),cur+(p-cur)*k/n,down_R(yaw),base)
        if not goto(qt): return False
    return True
obs,_=env.reset(seed=seed); R=obs.get_object_from_name('robot'); B=obs.get_object_from_name(name)
base=(obs.get(R,'pos_base_x'), obs.get(R,'pos_base_y'), obs.get(R,'pos_base_rot'))
bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); h=np.array([obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']])
print(name,bp,h)
for dz in [0.02, 0.0]:
  for dirn in [(0,1),(0,-1),(1,0),(-1,0)]:
    dv=np.array([dirn[0],dirn[1],0.0])
    obs,_=env.reset(seed=seed)
    start=bp+dv*0.14+[0,0,h[2]+dz]
    move(start+[0,0,0.08]); r=move(start)
    s=0.14
    while s>-0.14 and r:
        qt,ok=tool_ik(q_of(obs),bp+dv*(s-0.002)+[0,0,h[2]+dz],down_R(yaw),base)
        if not goto(qt): break
        s-=0.002
    # contact offset in direction; subtract object half extent
    he=h[0] if dirn[0] else h[1]
    print('dz',dz,'dir',dirn,'start ok',r,'blocked at offset',round(s,3),'gap from face',round(s-he,3))
env.close()
