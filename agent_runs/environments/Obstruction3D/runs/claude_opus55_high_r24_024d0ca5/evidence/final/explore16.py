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
bp=np.array([obs.get(B,f) for f in ['pose_x','pose_y','pose_z']]); h=[obs.get(B,f) for f in ['half_extent_x','half_extent_y','half_extent_z']]
print(name,bp,h)
for dz in np.arange(0.05,-0.005,-0.004):
    obs,_=env.reset(seed=seed)
    move(bp+[0,0,h[2]+0.08]); r=move(bp+[0,0,h[2]+dz],n=20)
    tz=tool_fk(q_of(obs),base)[2,3]
    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
    g=[n for n in sorted(obs.get_object_names()) if n!='robot' and obs.get(obs.get_object_from_name(n),'grasp_active')>0]
    print('dz',round(dz,3),'reached',r,'tool-top',round(tz-bp[2]-h[2],4),'grasp',g, round(obs.get(R,'finger_state'),3),flush=True)
env.close()
