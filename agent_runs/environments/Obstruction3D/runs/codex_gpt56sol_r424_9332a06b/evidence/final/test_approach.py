from env_client import make_env
from approach import GeneratedApproach
import sys
for seed in map(int,sys.argv[1:] or [11]):
 e=make_env();s,i=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
 for t in range(e.max_steps):
  s,r,d,tr,i=e.step(p.get_action(s))
  if t%25==0:
   rob=s.get_object_from_name('robot');b=s.get_object_from_name('target_block')
   cur=s.get_object_from_name(p.object_name)
   print(seed,t,p.object_name,p.mode,p.waypoint,'held',s.get(rob,'grasp_active'),
         'finger',round(s.get(rob,'finger_state'),3),
         'obj',[round(s.get(cur,'pose_'+c),3) for c in 'xyz'],
         'b',[round(s.get(b,'pose_'+c),3) for c in 'xyz'])
  if d or tr: break
 print('RESULT',seed,t+1,d,tr,p.mode)
 e.close()
