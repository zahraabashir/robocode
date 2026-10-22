from env_client import make_env
import numpy as np
np.set_printoptions(precision=5, suppress=True, linewidth=200)
env = make_env()
M=0.0499
obs,_ = env.reset(seed=3)
for i in range(6):
    a=np.array([0.0,-M]) if i<3 else np.array([0.02,0.0])
    p=obs[16:18].copy(); obs,*_=env.step(a); print('d-a', obs[16:18]-p-a, obs[18:21])
for d,a in [('down',[0,-M]),('left',[-M,0])]:
    for i in range(40):
        obs,*_=env.step(np.array(a))
    print(d, obs[16:18], obs[18:21])
for i in range(90):
    obs,*_=env.step(np.array([0,M]))
print('up', obs[16:18], obs[[0,1,2]])
env.close()
