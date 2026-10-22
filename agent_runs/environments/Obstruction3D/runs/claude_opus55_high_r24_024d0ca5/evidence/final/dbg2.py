import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from kin import tool_fk, tool_ik, down_R
seed=int(sys.argv[1]); T=int(sys.argv[2])
env=make_env(); obs,info=env.reset(seed=seed)
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
for t in range(T):
    a=ap.get_action(obs); obs,*_=env.step(a)
q=ap._q(obs); base=ap._base(obs)
print('q',np.round(q,3)); print('wp',ap.waypoints[:2], 'yaw',ap.wp_yaw)
a=ap.get_action(obs); print('a',np.round(a,3))
qt,ok=tool_ik(q,ap.waypoints[0],down_R(ap.wp_yaw),base,iters=100); print('ik ok',ok,np.round(qt,3))
print('tool now',np.round(tool_fk(q,base),3))
# try smaller steps
for s in [0.5,0.25,0.1]:
    a2=a.copy(); a2[3:10]*=s; o2,*_=env.step(a2); print('scale',s,'moved',not np.allclose(ap._q(o2),q,atol=1e-7))
