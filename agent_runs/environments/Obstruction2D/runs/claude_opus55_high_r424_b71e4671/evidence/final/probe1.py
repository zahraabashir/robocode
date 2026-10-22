from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
r = obs.get_object_from_name('robot')
def R(o): return {f: round(float(o_.get(r,f)),4) for f in ["x","y","theta","arm_joint","vacuum"] for o_ in [o]}
print(R(obs))
for a in [[0.05,0,0,0,0],[0,-0.05,0,0,0],[0,0,0,0.1,0],[0,0,0,0.1,0],[0,0,0,0.1,0],[0,0,0.19,0,0],[-0.07,0,0,0,0],[0,0,0,0,1],[0,0,-0.19,0,0]]:
    obs,rew,te,tr,_=env.step(np.array(a,dtype=np.float32)); print(a, R(obs), rew, te)
# move down until blocked
for i in range(30):
    obs,rew,te,tr,_=env.step(np.array([0,-0.05,0,0,0],dtype=np.float32))
print("after down", R(obs))
env.close()
