from env_client import make_env
from approach import GeneratedApproach
import time,json
import sys
args=sys.argv[1:]
count=None
if args and args[0]=="--count":count=int(args[1]);args=args[2:]
seeds=list(range(20,40)) if not args else [int(x) for x in args]
for seed in seeds:
 e=make_env();s,i=e.reset(seed=seed,options={} if count is None else {"object_count":count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i);started=time.monotonic();done=False
 for step in range(300):
  s,r,done,tr,i=e.step(p.get_action(s))
  if done or tr or time.monotonic()-started>50:break
 report={'seed':seed,'count':i.get('object_count'),'success':done,'steps':step+1,'sec':round(time.monotonic()-started,2)}
 if not done:
  report.update(phase=p.phase,obj=p.obj.name,stall=p.stall,base=[s.get(p.robot,f) for f in ['pos_base_x','pos_base_y']],held=s.get(p.robot,'grasp_active'),pos=p.pos(s,p.obj).tolist(),dest=p.destination.tolist())
 print(json.dumps(report),flush=True);e.close()
