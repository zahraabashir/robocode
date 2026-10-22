from env_client import make_env
from kin import *
import numpy as np, sys
env = make_env()
obs, info = env.reset(seed=0)
R = obs.get_object_from_name("robot")
def q_of(o): return np.array([o.get(R,f'joint_{i}') for i in range(1,8)])
def goto(obs, qt, grip=0.0, maxn=40):
    for _ in range(maxn):
        q = q_of(obs); d = qt - q
        if np.max(np.abs(d)) < 1e-4: break
        a = np.zeros(11, np.float32); a[3:10] = np.clip(d,-.2,.2); a[10] = grip
        obs2, r, te, tr, _ = env.step(a)
        if np.allclose(q_of(obs2), q): return obs2, False
        obs = obs2
    return obs, True
base=(-0.12,0,0); q=q_of(obs)
x,y = float(sys.argv[1]), float(sys.argv[2])
for z in np.arange(0.40,0.10,-0.005):
    qt,e = ik(q, np.array([x,y,z]), down_R(0), base)
    obs, ok = goto(obs, qt); q=q_of(obs)
    if not ok or e>1e-3: print("stop at", round(z,3), ok, e); break
print("EE z", ee_pose(q,base)[2,3])
env.close()
