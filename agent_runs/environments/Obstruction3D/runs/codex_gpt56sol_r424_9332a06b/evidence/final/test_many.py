import concurrent.futures,sys
from env_client import make_env
from approach import GeneratedApproach
count=int(sys.argv[1]) if len(sys.argv)>1 else 0
seeds=list(map(int,sys.argv[2:])) if len(sys.argv)>2 else list(range(20))
def run(seed):
 e=make_env();s,i=e.reset(seed=seed,options={'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
 prior_task=-1
 for t in range(e.max_steps):
  if p.task_i!=prior_task:
   print('ENTER',seed,t,p.task_i,p.object_name,flush=True);prior_task=p.task_i
  if p.mode=='pick' and p._held(s):
   print('GRASP',seed,t,p.task_i,p.object_name,p.pick_i,flush=True)
  s,_,d,tr,_=e.step(p.get_action(s))
  if d or tr:break
 cur=s.get_object_from_name(p.object_name)
 detail=(p.object_name,p.task_i,p.pick_i,len(p.pick_poses),
         tuple(round(s.get(cur,'pose_'+c),3) for c in 'xyz'))
 e.close();return seed,t+1,d,p.mode,detail
with concurrent.futures.ThreadPoolExecutor(max_workers=min(4,len(seeds))) as ex:
 for x in ex.map(run,seeds):print('COUNT',count,*x,flush=True)
