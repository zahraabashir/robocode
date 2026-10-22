from env_client import make_env
from approach import GeneratedApproach
import time,json
for seed in range(20,30):
 e=make_env();s,info=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{})
 start=time.time();p.reset(s,info);trace=[];same=0;old=None
 for step in range(300):
  a=p.get_action(s);s,r,term,trunc,inf=e.step(a)
  sig=repr([[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers])+repr([[s.get(ob,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for ob in p.objs])
  same=same+1 if sig==old else 0;old=sig
  if step%10==0 or same>15:trace.append((step,[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers],[[s.get(ob,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for ob in p.objs],a.tolist()))
  if term or trunc or same>15:break
 print(json.dumps({'seed':seed,'n':info.get('object_count'),'steps':step+1,'success':term,'seconds':round(time.time()-start,2),'trace':trace if not term else []}),flush=True)
 e.close()
