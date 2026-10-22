import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from kin import tool_fk
seed=int(sys.argv[1]); ms=int(sys.argv[2]) if len(sys.argv)>2 else 300
env=make_env(); cnt=int(sys.argv[3]) if len(sys.argv)>3 else None
obs,info=env.reset(seed=seed,options={'object_count':cnt} if cnt else None)
for n in sorted(obs.get_object_names()):
    if n=='robot': continue
    o=obs.get_object_from_name(n); print(n,[round(obs.get(o,f),3) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z']])
ap=GeneratedApproach(env.action_space,env.observation_space,{}); ap.reset(obs,info)
print('tasks',ap.tasks)
prev=None
for t in range(ms):
    a=ap.get_action(obs)
    q0=ap._q(obs)
    obs,r,term,trunc,info=env.step(a)
    moved=not np.allclose(ap._q(obs),q0,atol=1e-7)
    tool=ap._tool(obs)[:3,3]
    key=(ap.phase, moved)
    if key!=prev or t%25==0:
        print(t,ap.phase,'moved',moved,'tool',np.round(tool,3),'grip',a[10],'held',ap._grasped_name(obs),'nwp',len(ap.waypoints),'task',ap.tasks[0] if ap.tasks else None)
    prev=key
    if term: print('SUCCESS',t); break
