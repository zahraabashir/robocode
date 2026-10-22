import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from kin import tool_fk, tool_ik, down_R, wb_ik, wb_fk
seed=int(sys.argv[1]); T=int(sys.argv[2])
def replay():
    env=make_env(); obs,info=env.reset(seed=seed)
    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    for t in range(T):
        a=ap.get_action(obs); obs,*_=env.step(a)
    return env,obs,ap
env,obs,ap=replay()
x=ap._x(obs); Tt=wb_fk(x); yaw=np.arctan2(Tt[1,0],Tt[0,0])
print('x',np.round(x,3),'tool',np.round(Tt[:3,3],3),'yaw',round(yaw,2))
for mode in ['arm','wb']:
  for dz in [0.005,0.02]:
    env.close(); env,obs,ap=replay()
    tgt=Tt[:3,3]+np.array([0,0,dz])
    if mode=='arm':
        q,ok=tool_ik(x[3:],tgt,down_R(yaw),tuple(x[:3])); xn=np.concatenate([x[:3],q])
    else:
        xn,ok=wb_ik(x,tgt,down_R(yaw))
    a=np.zeros(11,dtype=np.float32); a[0:10]=np.clip(xn-x,-0.2,0.2)
    obs2,*_=env.step(a); print(mode,dz,'moved',not np.allclose(ap._x(obs2),x),np.round(xn-x,3))
