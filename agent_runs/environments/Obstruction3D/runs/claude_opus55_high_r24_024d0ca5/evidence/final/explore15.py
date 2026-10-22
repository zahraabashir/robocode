from env_client import make_env
import numpy as np, sys
from kin import tool_fk, tool_ik, down_R
env = make_env()
seed=0; name=sys.argv[1]; dz=float(sys.argv[2]); yaw=float(sys.argv[3])
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
rows=[]
for dy in np.arange(-0.07,0.071,0.01):
    row=''
    for dx in np.arange(-0.07,0.071,0.01):
        obs,_=env.reset(seed=seed)
        move(bp+[dx,dy,0.12]); r=move(bp+[dx,dy,h[2]+dz])
        a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
        g=[n for n in sorted(obs.get_object_names()) if n!='robot' and obs.get(obs.get_object_from_name(n),'grasp_active')>0]
        row+=('.' if not g else ('G' if g[0]==name else g[0][0]))+('' if r else '!')+' '
    print(round(dy,2),row,flush=True)
env.close()
