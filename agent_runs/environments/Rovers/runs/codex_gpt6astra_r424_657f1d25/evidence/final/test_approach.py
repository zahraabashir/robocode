import time
import argparse
import json
from env_client import make_env
from approach import GeneratedApproach
p=argparse.ArgumentParser();p.add_argument('--start',type=int,default=0);p.add_argument('--n',type=int,default=10);p.add_argument('--count',type=int);p.add_argument('--limit',type=int,default=250);p.add_argument('--verbose',action='store_true');args=p.parse_args()
for seed in range(args.start,args.start+args.n):
 e=make_env();s,info=e.reset(seed=seed,options={'object_count':args.count} if args.count is not None else None);a=GeneratedApproach(e.action_space,e.observation_space,{})
 t=time.time();a.reset(s,info);success=False
 for k in range(args.limit):
  ac=a.get_action(s);s,r,term,trunc,i=e.step(ac)
  if args.verbose and (k%10==0 or term):
   print(seed,k,'pos',[a.xy(s,ro).round(3).tolist() for ro in a.rovers],'task',a.tasks,'ops',ac[[3,7]].round(2),'images',[(o.name,int(s.get(o,'received_image'))) for o in a.objectives],flush=True)
  if term or trunc:success=term;break
 print('RESULT',seed,info,success,k+1,round(time.time()-t,3),flush=True)
 if not success:
  print('FAILED',a.tasks,[(o.name,{f:s.get(o,f) for f in e.observation_space.type_features[o.type]}) for o in a.rovers+a.objectives+a.samples],flush=True)
 e.close()
