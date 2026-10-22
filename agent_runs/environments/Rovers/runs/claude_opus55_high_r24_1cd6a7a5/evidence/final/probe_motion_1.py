from probe_motion_lib import *
obs,info = env.reset(seed=0)
for n,v in obstacles(obs): print(n,v)
print('max_steps', getattr(env,'max_steps',None))
print(rov(obs,0))
for a in [(0.1,0,0),(0,0.1,0),(0.3,0,0),(0,0,0.3),(0.1,0,0),(0,0,1.0),(0.1,0.0,0)]:
    obs,r,te,tr,inf = step(0,*a); print(a, np.round(rov(obs,0),4), r, te, tr)
