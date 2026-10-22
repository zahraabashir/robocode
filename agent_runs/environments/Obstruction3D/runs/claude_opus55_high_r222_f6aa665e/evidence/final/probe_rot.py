import numpy as np
from env_client import make_env
from approach import GeneratedApproach
env = make_env(); obs, info = env.reset(seed=2)
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
def show(tag):
    q=ap._q(obs); b=ap._base(obs); T=ap._ee_world(q,b)
    print(tag, "base", np.round(b,4), "ee", np.round(T[:3,3],4), "q0", round(q[0],4))
show("init")
for a3 in ([0,0,0.1],[0,0,0.2],[0.0,0.05,0],[0.0,0,-0.3]):
    a=np.zeros(11,dtype=np.float32); a[0:3]=a3
    obs,*_=env.step(a); show(str(a3))
a=np.zeros(11,dtype=np.float32); a[0:3]=[0.012,-0.02,0.15]; a[3]=0.1
obs,*_=env.step(a); show("combo")
