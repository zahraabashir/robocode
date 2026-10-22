from env_client import make_env
import numpy as np
env = make_env()
def rob(obs):
    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
def objs(obs):
    return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name!="robot"}
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
obs,_=env.reset(seed=1)
for _ in range(5): obs,*_=env.step(A(i4=.2))
s0=rob(obs); print("j2 now",s0[4])
obs,*_=env.step(A(i4=.2,i3=.1)); print("j2+.2(rej)&j1+.1:",np.round(rob(obs)-s0,4))
obs,*_=env.step(A(i4=.01,i3=.1)); print("j2+.01&j1+.1:",np.round(rob(obs)-s0,4))
# sweeps: for each seed, lower arm, then sweep j1 and base y, record rejections + object moves
for seed in range(6):
    obs,_=env.reset(seed=seed); o0=objs(obs)
    for _ in range(5): obs,*_=env.step(A(i4=.2))
    rej=0; mv=set()
    seq=[A(i3=.05)]*40+[A(i3=-.05)]*80+[A(i1=.05)]*20+[A(i1=-.05)]*40+[A(i0=.02)]*10+[A(i3=.05)]*80
    for a in seq:
        s=rob(obs); obs,*_=env.step(a)
        if np.allclose(rob(obs),s): rej+=1
        o=objs(obs)
        for k in o0:
            if np.abs(o[k]-o0[k]).max()>1e-6: mv.add(k)
    print("seed",seed,"rejected",rej,"/",len(seq),"moved objs",mv, "final j1",round(rob(obs)[3],2))
env.close()
