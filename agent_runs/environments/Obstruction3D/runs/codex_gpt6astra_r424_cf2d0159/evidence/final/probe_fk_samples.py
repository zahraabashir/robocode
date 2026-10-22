from env_client import make_env
import numpy as np,json
q=np.array([0,.44754084944725037,-np.pi,-2.120941162109375,0,.009999980218708515,.6907963752746582]);base=np.array([-.4509332478046417,-.3362736999988556])
e=make_env();s,_=e.reset(seed=2,options={'object_count':0});ro=s.get_object_from_name('robot');ob=s.get_object_from_name('target_block')
for k in range(70):
 a=np.zeros(11);a[:2]=np.clip(base-[s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y')],-.1,.1);a[3:10]=np.clip(q-[s.get(ro,'joint_'+str(j)) for j in range(1,8)],-.08,.08);a[-1]=1;s,*_=e.step(a)
a=np.zeros(11);a[-1]=-1;s,*_=e.step(a)
rng=np.random.default_rng(390);samples=[];lastq=np.zeros(7)
for k in range(240):
 cq=np.array([s.get(ro,'joint_'+str(j)) for j in range(1,8)])
 if np.max(abs(cq-lastq))>1e-5:
  samples.append({'q':cq.tolist(),'base':[s.get(ro,f) for f in ['pos_base_x','pos_base_y','pos_base_rot']],'obj':[s.get(ob,'pose_'+f) for f in ['x','y','z','qx','qy','qz','qw']],'tf':[s.get(ro,'grasp_tf_'+f) for f in ['x','y','z','qx','qy','qz','qw']]})
  with open('fk_samples.json','w') as f:json.dump(samples,f)
  print('sample',len(samples),'object z',s.get(ob,'pose_z'),flush=True);lastq=cq.copy()
 if len(samples)>=60:break
 a=np.zeros(11);a[3:10]=rng.uniform(-.10,.10,7);s,*_=e.step(a)
e.close()
