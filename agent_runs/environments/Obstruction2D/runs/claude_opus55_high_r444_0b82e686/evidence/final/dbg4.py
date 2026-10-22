import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); T0=int(sys.argv[2]); T1=int(sys.argv[3]); name=sys.argv[4]
env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=seed); ap.reset(obs, info)
for i in range(T1):
    a=ap.get_action(obs)
    if i>=T0:
        r,objs,s=ap._parse(obs); o=objs[name]
        print(i, ap.mode, ap.cur, "robot",round(r['x'],4),round(r['y'],4),r['vac'], name, round(o['x'],4), round(o['y'],4), "act",np.round(a,4), "drop",ap.drop)
    obs,*_=env.step(a)
env.close()
