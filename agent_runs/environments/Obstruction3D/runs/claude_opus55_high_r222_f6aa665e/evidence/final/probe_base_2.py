from env_client import make_env
import numpy as np
env = make_env()
def rob(obs):
    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
for seed in [0,1]:
    obs,_ = env.reset(seed=seed); s=rob(obs)
    for i in range(30):
        obs,*_ = env.step(A(i0=.01)); n=rob(obs)
        if np.allclose(n,s): print("seed",seed,"x+ stops at base_x",n[0]); break
        s=n
    # exactness
    obs,_=env.reset(seed=seed); s0=rob(obs)
    obs,*_=env.step(A(i1=0.0123456,i2=-0.0333,i3=0.0777)); s1=rob(obs)
    print("exact diff", (s1-s0)[:4]-np.array([0,0.0123456,-0.0333,0.0777],dtype=np.float32))
# rejection whole action: x+.1 (rejected) combined with y+.1 and j1+.1
for name,a in [("x+.1 & y+.1",A(i0=.1,i1=.1)),("x+.1 & j1+.1",A(i0=.1,i3=.1)),("x+.1 & rot.1",A(i0=.1,i2=.1))]:
    obs,_=env.reset(seed=1); s0=rob(obs); obs,*_=env.step(a); print(name, np.round(rob(obs)-s0,4))
# base x limit when moving away / y wide range
obs,_=env.reset(seed=1); s=rob(obs)
for i in range(60):
    obs,*_=env.step(A(i0=-.2)); n=rob(obs)
    if np.allclose(n,s): break
    s=n
print("x- stops at", n[0], "after", i)
obs,_=env.reset(seed=1); s=rob(obs)
for i in range(60):
    obs,*_=env.step(A(i1=.2)); n=rob(obs)
    if np.allclose(n,s): break
    s=n
print("y+ stops at", n[1], "after", i)
obs,_=env.reset(seed=1); 
for i in range(40): obs,*_=env.step(A(i2=.2))
print("rot after 40*0.2 =", rob(obs)[2], "(8.0 raw)")
env.close()
