from env_client import make_env
import numpy as np
env = make_env()
def rob(obs):
    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
def objs(obs):
    return {o.name: np.array(obs.data[o][:3],dtype=float) for o in obs.data if o.name not in ("robot",)}
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
obs,_=env.reset(seed=1)
for _ in range(3): obs,*_=env.step(A(i4=.2))
s0=rob(obs); print("j2 now",s0[4])
obs,*_=env.step(A(i4=.2,i3=.1)); print("j2+.2(rej)&j1+.1:",np.round(rob(obs)-s0,4))
obs,_=env.reset(seed=1); s0=rob(obs)
obs,*_=env.step(A(i3=.7)); print("j1 +0.7 ->",np.round(rob(obs)-s0,4)[3])
obs,_=env.reset(seed=1); s0=rob(obs)
obs,*_=env.step(A(i6=-.1)); print("j4 -0.1 ->",np.round(rob(obs)-s0,4)[6])
obs,*_=env.step(A(i6=-.1)); print("j4 another -0.1 ->",np.round(rob(obs)-s0,4)[6])
# fine j2 limit via 0.01
obs,_=env.reset(seed=1); s=rob(obs)
for i in range(200):
    obs,*_=env.step(A(i4=.01)); m=rob(obs)
    if np.allclose(m,s): break
    s=m
print("j2 fine stop", s[4])
# random exploration for object movement
rng=np.random.default_rng(0)
moved=0; tot=0
for seed in range(4):
    obs,_=env.reset(seed=seed); o0=objs(obs)
    for t in range(300):
        a=rng.uniform(-.2,.2,11).astype(np.float32); a[10]=1.0
        a[0]=abs(a[0])*0.3 if t<100 else a[0]*0.3
        obs,*_=env.step(a); tot+=1
        o=objs(obs)
        for k in o0:
            if np.abs(o[k]-o0[k]).max()>1e-6:
                moved+=1; print("seed",seed,"t",t,k,"moved",np.round(o[k]-o0[k],4)); o0=o; break
print("moves",moved,"of steps",tot)
env.close()
