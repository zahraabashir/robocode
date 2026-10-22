from env_client import make_env
from approach import ik, fk, down_R
import numpy as np, sys
env = make_env()
dbx, dby, drot = [float(v) for v in sys.argv[1:4]]; hyp = sys.argv[4]
obs, info = env.reset(seed=0)
R = obs.get_object_from_name("robot"); B = obs.get_object_from_name("target_block")
def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
# move base away first: -x then y/rot
for i in range(20):
    rem = np.array([dbx - (obs.get(R,'pos_base_x')+0.12), dby - obs.get(R,'pos_base_y'), drot - obs.get(R,'pos_base_rot')])
    if np.max(np.abs(rem))<1e-6: break
    a=np.zeros(11,np.float32); a[0:3]=np.clip(rem,-.2,.2); obs,*_=env.step(a)
bxw,byw,rot = obs.get(R,'pos_base_x'),obs.get(R,'pos_base_y'),obs.get(R,'pos_base_rot')
print("base", bxw, byw, rot)
if hyp=='A': mount=np.array([bxw+0.12*np.cos(rot), byw+0.12*np.sin(rot)])
else: mount=np.array([bxw+0.12, byw])
c,s=np.cos(rot),np.sin(rot); Rz=np.array([[c,-s,0],[s,c,0],[0,0,1]])
def to_local(p): 
    d=np.array(p)-np.array([mount[0],mount[1],0]); return Rz.T@d
bx,by=obs.get(B,'pose_x'),obs.get(B,'pose_y')
q=q_of(obs)
def goto(obs, qt, maxn=40):
    for _ in range(maxn):
        q = q_of(obs); d = qt - q
        if np.max(np.abs(d)) < 1e-4: break
        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2)
        obs2, *_ = env.step(a)
        if np.allclose(q_of(obs2), q): return obs2, False
        obs = obs2
    return obs, True
for z in [0.36,0.30,0.265]:
    p=to_local([bx,by,z]); Rl=Rz.T@down_R(np.pi/2)
    qt,e=ik(q,p,Rl); obs,ok=goto(obs,qt); q=q_of(obs); print(z, ok, e)
a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a); print("grasp", obs.get(R,'grasp_active'))
