import sys, numpy as np
from env_client import make_env
import approach
from approach import GeneratedApproach
Y=float(sys.argv[2])
def cy(self,state,name,kind,attempt):
    p,q,h=self._pose(state,name); self.grasp_z=self._grasp_z(p,h); return approach._yaw_of_quat(q)+Y
GeneratedApproach._choose_yaw=cy
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
for t in range(40):
    a=ap.get_action(obs); obs,*_=env.step(a)
    if ap.phase=='close':
        T=ap._tool(obs); print(t,'close at',np.round(T[:3,3],3),ap.cur_obj,np.round(ap._pose(obs,ap.cur_obj)[2],3))
    if ap.phase=='to_place': print('grasped',ap._grasped_name(obs)); break
