from env_client import make_env
import numpy as np
env = make_env()
def rob(obs):
    R = obs.get_object_from_name("robot"); return np.array(obs.data[R][:10], dtype=float)
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
def push(seed, idx, d, n=80, pre=()):
    obs,_=env.reset(seed=seed)
    for p in pre: obs,*_=env.step(p)
    s=rob(obs); k=0
    for i in range(n):
        obs,*_=env.step(A(**{f"i{idx}":d})); m=rob(obs)
        if np.allclose(m,s): break
        s=m; k+=1
    return s, k
# x+ at y=2 (off table?)
s,k=push(1,0,.01,pre=[A(i1=.2)]*10); print("x+ at y=2 stops at x",s[0],k)
s,k=push(1,0,.01,pre=[A(i2=.2)]*16); print("x+ at rot=pi stops at x",s[0],k)
for j in range(1,8):
    idx=2+j
    for d in (.2,-.2):
        s,k=push(1,idx,d,n=40)
        # find fine limit with 0.01
        obs,_=env.reset(seed=1)
        s2,k2=None,None
        print(f"j{j} d{d:+}: stops at {s[idx]:.4f} after {k} steps")
env.close()
