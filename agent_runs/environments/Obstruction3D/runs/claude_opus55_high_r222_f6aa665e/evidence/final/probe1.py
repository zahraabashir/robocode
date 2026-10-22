from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name("robot")
F = obs.type_features[R.type]
def rv(o): return np.round(o.data[R],4)
print(F)
print(rv(obs))
a = np.zeros(11, dtype=np.float32)
a[3]=0.1; a[4]=0.3
obs,r,te,tr,_ = env.step(a); print("j1+.1 j2+.3(clipped?)", rv(obs), r)
a = np.zeros(11, dtype=np.float32); a[0]=0.1; a[2]=0.1
obs,r,te,tr,_ = env.step(a); print("base", rv(obs))
a = np.zeros(11, dtype=np.float32); a[10]=-1
obs,r,te,tr,_ = env.step(a); print("close", rv(obs))
a = np.zeros(11, dtype=np.float32); a[10]=1
obs,r,te,tr,_ = env.step(a); print("open", rv(obs))
a = np.zeros(11, dtype=np.float32); a[4]=0.2
for i in range(15):
    obs,r,te,tr,_ = env.step(a)
    print(i, rv(obs)[:10])
print(env.max_steps)
env.close()
