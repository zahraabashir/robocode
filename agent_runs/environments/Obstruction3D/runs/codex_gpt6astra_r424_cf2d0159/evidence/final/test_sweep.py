from env_client import make_env
from approach import GeneratedApproach
import sys,time,json
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
end=int(sys.argv[2]) if len(sys.argv)>2 else 20
count=int(sys.argv[3]) if len(sys.argv)>3 else None
for seed in range(start,end):
 e=make_env();s,info=e.reset(seed=seed,options={} if count is None else {'object_count':count});p=GeneratedApproach(e.action_space,e.observation_space,{});t0=time.time();p.reset(s,info)
 last=None;stuck=0
 for k in range(1000):
  a=p.get_action(s);s,r,t,tr,info=e.step(a)
  ro=next(iter(s.get_objects(p.robot_type)))
  now=(p.phase,p.goal,tuple(s.get(ro,'joint_'+str(i)) for i in range(1,8)),s.get(ro,'pos_base_x'),s.get(ro,'pos_base_y'),s.get(ro,'grasp_active'))
  stuck=stuck+1 if now==last else 0;last=now
  if t or tr or stuck>45 or time.time()-t0>55:break
 print(json.dumps({'seed':seed,'count':count,'success':bool(t),'steps':k+1,'phase':p.phase,'goal':p.goal,'seconds':round(time.time()-t0,2),'grasp':s.get(ro,'grasp_active')}),flush=True)
 e.close()
