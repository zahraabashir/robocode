from probe_motion_lib import *
# bounds with rover0 (step 0.2 then 0.01)
for d in [(1,0),(0,1),(0,-1)]:
    obs,_=env.reset(seed=0)
    drive_until_stop(0, .2*d[0], .2*d[1])
    p=drive_until_stop(0, .01*d[0], .01*d[1])
    print('rover0 dir',d,np.round(p,4))
for d in [(-1,0),(0,1),(0,-1)]:
    obs,_=env.reset(seed=0)
    p=drive_until_stop(1, .2*d[0], .2*d[1]); print(' coarse',np.round(p,4))
    p=drive_until_stop(1, .01*d[0], .01*d[1])
    print('rover1 dir',d,np.round(p,4))
