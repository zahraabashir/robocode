import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from kin import tool_fk
cnt=int(sys.argv[3]) if len(sys.argv)>3 else None
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={'object_count':cnt} if cnt else None)
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
for t in range(int(sys.argv[2])):
    a=ap.get_action(obs); obs,*_=env.step(a)
q=ap._x(obs); print('q',np.round(q,2))
for i,qp in enumerate(ap.qpath[:30]):
    from kin import wb_fk; T=wb_fk(qp); print(i,np.round(T[:3,3],3),round(float(np.arctan2(T[1,0],T[0,0])),2),np.round(qp-q,2)); q=qp
