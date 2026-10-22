from env_client import make_env
import numpy as np, json
env = make_env()
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
obs,_=env.reset(seed=1)
for _ in range(5): obs,*_=env.step(A(i4=.2))
for _ in range(3): obs,*_=env.step(A(i4=.02))
print(type(obs), [m for m in dir(obs) if not m.startswith('_')][:30])
env.close()
