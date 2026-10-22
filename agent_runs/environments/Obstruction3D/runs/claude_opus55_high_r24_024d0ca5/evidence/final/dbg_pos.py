import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach, _yaw_of_quat as yq
cnt=int(sys.argv[2]) if len(sys.argv)>2 else None
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]),options={"object_count":cnt} if cnt else None)
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
for n in ap.names: print(n,np.round(ap._pose(obs,n)[0],3),np.round(ap._pose(obs,n)[2],3), round(float(np.degrees(yq(ap._pose(obs,n)[1]))),1))
print('yaw',ap.grasp_yaw,'q0',np.round(ap._q(obs),2))
for qp in ap.qpath[::3]: print(np.round(qp,2))
