import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from kin import tool_fk, tool_ik, down_R, wb_ik2, wb_fk
seed=int(sys.argv[1]); T=int(sys.argv[2]); cnt=int(sys.argv[3])
def replay():
    env=make_env(); obs,info=env.reset(seed=seed,options={'object_count':cnt})
    ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
    for t in range(T):
        a=ap.get_action(obs); obs,*_=env.step(a)
    return env,obs,ap
env,obs,ap=replay()
x=ap._x(obs); Tt=wb_fk(x); yaw=np.arctan2(Tt[1,0],Tt[0,0])
print('x',np.round(x,3),'tool',np.round(Tt[:3,3],3),'yaw',round(yaw,2), 'held', ap._grasped_name(obs))
for n in ap.names:
    c,hh,b,t=ap._box(obs,n); print(' ',n,np.round(c,3),np.round(hh,3),round(b,3),round(t,3))
tests=[('arm up 5mm',None,(0,0,0.005)),('wb up 5mm','wb',(0,0,0.005)),('base -x 1cm','bx',None),('base -y 1cm','by-',None),('base +y 1cm','by+',None),('arm +x5mm',None,(0.005,0,0)),('arm -x5mm',None,(-0.005,0,0)),('arm +y5mm',None,(0,0.005,0)),('arm -y5mm',None,(0,-0.005,0))]
for name,mode,d in tests:
    env.close(); env,obs,ap=replay()
    a=np.zeros(11,dtype=np.float32)
    if mode=='bx': a[0]=-0.01
    elif mode=='by-': a[1]=-0.01
    elif mode=='by+': a[1]=0.01
    elif mode=='wb':
        xn,ok=wb_ik2(x,Tt[:3,3]+np.array(d),down_R(yaw),k_null=0.05,bx_max=-0.09); a[0:10]=np.clip(xn-x,-0.2,0.2)
    else:
        q,ok=tool_ik(x[3:],Tt[:3,3]+np.array(d),down_R(yaw),tuple(x[:3])); a[3:10]=np.clip(q-x[3:],-0.2,0.2)
    obs2,*_=env.step(a); print(name,'moved',not np.allclose(ap._x(obs2),x))
