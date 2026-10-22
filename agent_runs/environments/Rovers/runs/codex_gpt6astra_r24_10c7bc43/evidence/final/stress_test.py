from env_client import make_env
from approach import GeneratedApproach
import time,sys,json
start_seed=int(sys.argv[1]);end_seed=int(sys.argv[2]);count=int(sys.argv[3]) if len(sys.argv)>3 else None
for seed in range(start_seed,end_seed):
 e=make_env();s,info=e.reset(seed=seed,options={'object_count':count} if count else None);p=GeneratedApproach(e.action_space,e.observation_space,{})
 start=time.time();p.reset(s,info);hist=[]
 for t in range(200):
  a=p.get_action(s);s,r,done,trunc,inf=e.step(a)
  hist.append({'t':t,'rover':[[s.get(ro,k) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers], 'images':[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs], 'samples':[[s.get(o,k) for k in ['received_analysis','analyzed_rover0','analyzed_rover1']] for o in p.samples], 'action':a.tolist()})
  if done or trunc:break
 result={'seed':seed,'n':len(p.objs),'steps':t+1,'success':done,'sec':round(time.time()-start,3)}
 if not done:
  with open('failure_%s_%s.json'%(seed,count),'w') as f:json.dump(hist,f)
 print(json.dumps(result),flush=True);e.close()
