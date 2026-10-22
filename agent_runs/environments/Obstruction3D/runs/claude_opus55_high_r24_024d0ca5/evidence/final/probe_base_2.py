import numpy as np
from env_client import make_env
from kin import tool_fk
env = make_env()
def base(o):
    r=o.get_object_from_name('robot'); return np.array([float(o.get(r,k)) for k in ['pos_base_x','pos_base_y','pos_base_rot']])
def q(o):
    r=o.get_object_from_name('robot'); return np.array([float(o.get(r,f'joint_{i}')) for i in range(1,8)])
def A(i,v):
    a=np.zeros(11,dtype=np.float32); a[i]=v; return a
for seed in [0,1,2]:
    res=[]
    for i,s in [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1)]:
        obs,_=env.reset(seed=seed); b0=base(obs)
        n=0
        for step_sz in [0.05,0.01,0.002]:
            for k in range(400):
                o,*_=env.step(A(i,s*step_sz)); b=base(o)
                if np.allclose(b,base(obs)): break
                obs=o
        res.append(round(float(base(obs)[i]),3))
    print('seed',seed,'+x,-x,+y,-y,+rot,-rot limits:',res)
# FK check
obs,_=env.reset(seed=0)
T0=tool_fk(q(obs),base=tuple(base(obs)))
o,*_=env.step(A(0,-0.2)); o,*_=env.step(A(1,0.15))
T1=tool_fk(q(o),base=tuple(base(o)))
print('base delta',base(o)-np.array([-0.12,0,0]),'tool delta',np.round(T1[:3,3]-T0[:3,3],4), 'Rsame',np.allclose(T0[:3,:3],T1[:3,:3]))
o,*_=env.step(A(2,0.2)); b=base(o); T2=tool_fk(q(o),base=tuple(b))
c,s=np.cos(0.2),np.sin(0.2); Rz=np.array([[c,-s,0],[s,c,0],[0,0,1]])
p=T1[:3,3]-np.array([b[0],b[1],0]); print('rot pred',np.round(Rz@p+np.array([b[0],b[1],0]),4),'fk',np.round(T2[:3,3],4))
env.close()
