from env_client import make_env
from approach import GeneratedApproach
import numpy as np
E=make_env();s,inf=E.reset(seed=8,options={'object_count':10});p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,inf);print('TASKS',[p.goal]+p.tasks,flush=True)
for o in s.get_objects(p.cube_type):print(o.name,'pos',[s.get(o,'pose_'+v) for v in 'xyz'],'half',[s.get(o,'half_extent_'+v) for v in 'xyz'],flush=True)
E.close()
