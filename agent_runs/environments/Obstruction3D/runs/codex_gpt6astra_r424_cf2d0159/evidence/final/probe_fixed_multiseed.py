from env_client import make_env
import numpy as np
Q=np.array([0,.44754084944725037,-np.pi,-2.120941162109375,0,.009999980218708515,.6907963752746582])
e=make_env();results=[]
for seed in range(20):
 s,inf=e.reset(seed=seed);ro=s.get_object_from_name('robot');ob=s.get_object_from_name('target_block');base=np.array([s.get(ob,'pose_x')-.64,s.get(ob,'pose_y')-.001])
 for k in range(30):
  a=np.zeros(11);a[:2]=np.clip(base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')],-.1,.1);a[-1]=1;s,*_=e.step(a)
  if np.max(abs(a[:2]))<1e-5:break
 for k in range(70):
  a=np.zeros(11);a[3:10]=np.clip(Q-[s.get(ro,'joint_'+str(j)) for j in range(1,8)],-.08,.08);a[-1]=1;s,*_=e.step(a)
  if np.max(abs(a[3:10]))<1e-5:break
 a=np.zeros(11);a[-1]=-1;s,*_=e.step(a)
 cq=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)]);success=s.get(ob,'grasp_active');results.append(bool(success))
 print(seed,inf,'SUCCESS' if success else 'FAIL','gap',np.max(abs(cq-Q)),'q',cq.tolist() if not success else '',flush=True)
print('TOTAL',sum(results),len(results),flush=True);e.close()
