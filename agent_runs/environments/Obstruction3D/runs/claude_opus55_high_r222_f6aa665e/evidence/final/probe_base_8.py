from env_client import make_env
import numpy as np, json
env = make_env()
def A(**kw):
    a = np.zeros(11, dtype=np.float32)
    for k,v in kw.items(): a[int(k[1:])] = v
    return a
obs,_=env.reset(seed=1)
for _ in range(5): obs,*_=env.step(A(i4=.2))
for _ in range(6): obs,*_=env.step(A(i4=.01))
print([o.name for o in obs.data])
try: v=env.observation_space.vectorize(obs); print("vec ok")
except Exception as e: v=obs.vec(list(obs.data)); print("fallback",e)
json.dump([float(x) for x in v], open("probe_base_vec.json","w"))
print(len(v))
env.close()
