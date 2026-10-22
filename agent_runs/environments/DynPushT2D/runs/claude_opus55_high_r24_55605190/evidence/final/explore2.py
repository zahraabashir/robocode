from env_client import make_env
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=200)
env = make_env()
obs,_=env.reset(seed=0)
# block at (1.05,3.44). robot at (1.637,1.27). move robot to (1.05, 2.3) then push up
def goto(obs, tgt, n=200):
    for _ in range(n):
        d = np.array(tgt)-obs[16:18]
        if np.linalg.norm(d)<1e-4: break
        a = np.clip(d, -0.049, 0.049)
        obs,r,te,tr,_=env.step(a)
    return obs
obs = goto(obs,[1.05,2.3])
print(obs[16:18], obs[0:6])
for t in range(40):
    obs,r,te,tr,_=env.step(np.array([0,0.04]))
    if t%4==0: print(t, obs[16:18], obs[0:6])
for t in range(20):
    obs,r,te,tr,_=env.step(np.array([0,0.0]))
    if t%2==0: print('stop',t, obs[16:18], obs[0:6])
env.close()
