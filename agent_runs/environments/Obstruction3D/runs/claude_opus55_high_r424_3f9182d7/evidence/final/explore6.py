from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=1)
r = obs.get_object_from_name('robot')
F=env.observation_space.type_features[r.type]
prev=np.array([obs.get(r,f) for f in F])
for g in [-1,-1,-1,1,1,1,-0.7,0.7]:
    a=np.zeros(11,dtype=np.float32); a[10]=g
    obs,rew,te,tr,info=env.step(a)
    cur=np.array([obs.get(r,f) for f in F])
    print(g, {f:(round(p,4),round(c,4)) for f,p,c in zip(F,prev,cur) if abs(p-c)>1e-9})
    prev=cur
env.close()
