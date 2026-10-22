import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from kin import tool_fk, tool_ik, down_R
seed=int(sys.argv[1]); T=int(sys.argv[2])
def replay():
    env=make_env(); obs,info=env.reset(seed=seed)
    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    for t in range(T):
        a=ap.get_action(obs); obs,*_=env.step(a)
    return env,obs,ap
env,obs,ap=replay()
q=ap._q(obs); base=ap._base(obs); Tt=tool_fk(q,base); yaw=np.arctan2(Tt[1,0],Tt[0,0])
print('tool',np.round(Tt[:3,3],3),'yaw',yaw,'finger',obs.get(ap.robot,'finger_state'))
tests={'up1cm':(0,0,0.01),'up3mm':(0,0,0.003),'-x':(-0.005,0,0.002),'+x':(0.005,0,0.002),'-y':(0,-0.005,0.002),'+y':(0,0.005,0.002)}
for k,d in tests.items():
    env.close(); env,obs,ap=replay()
    qn,ok=tool_ik(q,Tt[:3,3]+np.array(d),down_R(yaw),base)
    a=np.zeros(11,dtype=np.float32); a[3:10]=np.clip(qn-q,-0.2,0.2)
    obs2,*_=env.step(a)
    print(k,'moved',not np.allclose(ap._q(obs2),q))
a=np.zeros(11,dtype=np.float32); a[1]=0.01
env.close(); env,obs,ap=replay(); obs2,*_=env.step(a); print('base dy moved', not np.allclose(ap._base(obs2),base))
