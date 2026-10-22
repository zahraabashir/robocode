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
print('phase',ap.phase,'q',np.round(q,3),'tool',np.round(tool_fk(q,base)[:3,3],3),'yaw',ap.wp_yaw)
print('finger',obs.get(ap.robot,'finger_state'),'grasp',obs.get(ap.robot,'grasp_active'))
for n in ap.names:
    p,_,h=ap._pose(obs,n); print(n,np.round(p,3),np.round(h,3))
for j in range(7):
    for s in [0.01,-0.01]:
        a=np.zeros(11,dtype=np.float32); a[3+j]=s; o2,*_=env.step(a)
        mv=not np.allclose(ap._q(o2),q,atol=1e-7)
        if mv:
            a[3+j]=-s; obs,*_=env.step(a)
        print(j,s,mv,end=' | ')
print()
for g in [1,-1,0]:
    a=np.zeros(11,dtype=np.float32); a[3]=0.01; a[10]=g; o2,*_=env.step(a); print('grip',g,'moved',not np.allclose(ap._q(o2),q,atol=1e-7))
