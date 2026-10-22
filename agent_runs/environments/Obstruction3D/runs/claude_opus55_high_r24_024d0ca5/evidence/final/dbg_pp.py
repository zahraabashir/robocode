import sys, numpy as np
from env_client import make_env
import approach
from approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]))
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
for t in range(int(sys.argv[2])):
    a=ap.get_action(obs); obs,*_=env.step(a)
orig=ap._set_path
def sp(state,wps,yaw,final_grip=0.0,res=0.01):
    print('wps',[np.round(w,3) for w in wps],'yaw',round(float(yaw),3))
    orig(state,wps,yaw,final_grip,res); print('len',len(ap.qpath))
ap._set_path=sp
ap._plan_place(obs)
for n in ap.names: print(n,np.round(ap._pose(obs,n)[0],3),np.round(ap._pose(obs,n)[2],3))
from kin import tool_fk
for qp in ap.qpath[:4]: T=tool_fk(qp,ap._base(obs)); print(np.round(T[:3,3],3), round(float(np.arctan2(T[1,0],T[0,0])),3), np.round(qp-ap._q(obs),3))
