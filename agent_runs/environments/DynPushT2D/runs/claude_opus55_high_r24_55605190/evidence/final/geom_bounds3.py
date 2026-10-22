from env_client import make_env
import numpy as np
env=make_env()
obs,_=env.reset(seed=0)
for t in range(64): obs,*_=env.step(np.array([0.0499,0]))
print('x',obs[16])
for a in [0.01,0.005,0.003,0.002,0.001,0.0005,0.0002,0.0001]:
    for k in range(40):
        x0=obs[16]; obs,*_=env.step(np.array([a,0])); 
        if abs(obs[16]-x0)<1e-6: print('a',a,'rejected at x0',x0,'x0+a',x0+a); break
    else: print('a',a,'no reject x',obs[16])
# go to left via y bottom
obs,_=env.reset(seed=0)
for t in range(31): obs,*_=env.step(np.array([-0.0499,0]))
print('x',obs[16])
for a in [0.01,0.005,0.002,0.001,0.0005,0.0002,0.0001]:
    for k in range(40):
        x0=obs[16]; obs,*_=env.step(np.array([-a,0]))
        if abs(obs[16]-x0)<1e-6: print('a',a,'rejected at x0',x0,'x0-a',x0-a); break
        print('  moved',x0,'->',obs[16]) if k<3 else None
    else: print('a',a,'no reject x',obs[16])
