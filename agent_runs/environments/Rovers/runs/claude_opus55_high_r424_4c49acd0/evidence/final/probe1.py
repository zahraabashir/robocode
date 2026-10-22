from env_client import make_env
from util import R
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
def step(a):
    global obs
    obs,r,te,tr,inf=env.step(np.array(a,dtype=np.float32))
    return r,te,tr
print(R(obs,'rover0'),R(obs,'rover1'))
print(step([0.2,0,0,0, 0.2,0,0,0]), R(obs,'rover0'),R(obs,'rover1'))
print(step([0,0.2,0,0, 0,0.2,0,0]), R(obs,'rover0'),R(obs,'rover1'))
print(step([0,0,0.4,0, 0,0,0.4,0]), R(obs,'rover0'),R(obs,'rover1'))
print(step([0.2,0,0,0, 0.2,0,0,0]), R(obs,'rover0'),R(obs,'rover1'))
print(step([0.5,0,0,0, 0.3,0,0,0]), R(obs,'rover0'),R(obs,'rover1'))
# rover1 move right toward wall
for i in range(10):
    step([0,0,0,0, 0.1,0,0,0]); print(R(obs,'rover1'))
