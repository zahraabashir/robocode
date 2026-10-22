from env_client import make_env
import numpy as np
env = make_env()
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
def objs(obs): return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
# j2 limit off-table
obs,_=env.reset(seed=1); R=obs.get_object_from_name("robot")
for _ in range(10): obs,*_=env.step(A(i1=.2))
for _ in range(50):
    j=obs.get(R,"joint_2"); obs,*_=env.step(A(i4=.05))
    if abs(obs.get(R,"joint_2")-j)<1e-6: break
print("off-table (y=2) j2 stops at", obs.get(R,"joint_2"))
rng=np.random.default_rng(1)
tot=rej=0; moves=[]
for seed in range(5):
    obs,_=env.reset(seed=seed); o0=objs(obs)
    obs,*_=env.step(A(i0=.05))
    for t in range(400):
        a=np.zeros(11,np.float32); a[3:10]=rng.uniform(-.2,.2,7); a[10]=1
        a[4]+=0.03  # bias downward
        s=np.array(obs.data[R][:10]); obs,*_=env.step(a); tot+=1
        if np.allclose(np.array(obs.data[R][:10]),s): rej+=1
        o=objs(obs)
        for k in o0:
            if np.abs(o[k]-o0[k]).max()>1e-6: moves.append((seed,t,k,np.round(o[k]-o0[k],3)))
        o0=o
print("steps",tot,"rejected",rej,"object moves",len(moves)); print(moves[:10])
env.close()
