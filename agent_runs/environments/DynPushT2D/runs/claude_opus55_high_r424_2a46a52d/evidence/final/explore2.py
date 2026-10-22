import numpy as np
from env_client import make_env
env = make_env()
np.set_printoptions(precision=3, suppress=True, linewidth=200)
obs,_ = env.reset(seed=0)
def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
def goto(obs, p, tol=1e-3):
    for _ in range(200):
        d = p - obs[16:18]
        if np.linalg.norm(d)<tol: break
        a = np.clip(d,-0.049,0.049)
        obs,*_ = env.step(a)
    return obs
ref=obs[0:2]; th=obs[2]
start = ref + R(th)@np.array([-0.5,-0.5])
print("block",obs[0:6],"start",start)
obs=goto(obs,start)
print("after goto block",obs[0:6], "robot", obs[16:18])
dirn = R(th)@np.array([1.0,0])
for i in range(20):
    obs,*_=env.step(dirn*0.03)
    print(i,"blk",obs[0:6],"rob",obs[16:18])
for i in range(30):
    obs,*_=env.step(-dirn*0.0)
    print("coast",i,"blk",obs[0:6])
env.close()
