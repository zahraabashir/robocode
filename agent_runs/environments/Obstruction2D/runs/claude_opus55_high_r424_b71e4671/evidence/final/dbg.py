import sys
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); every=int(sys.argv[2]) if len(sys.argv)>2 else 10
env = make_env()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=seed); ap.reset(obs, info)
r = obs.get_object_from_name('robot')
for t in range(env.max_steps):
    a = ap.get_action(obs)
    ph=ap.leg
    obs, rew, te, tr, _ = env.step(a)
    if t%every==0 or te:
        print(t, ph, np.round(a,3), [round(float(obs.get(r,f)),3) for f in ['x','y','theta','arm_joint','vacuum']])
    if te: print("DONE", t+1); break
env.close()
