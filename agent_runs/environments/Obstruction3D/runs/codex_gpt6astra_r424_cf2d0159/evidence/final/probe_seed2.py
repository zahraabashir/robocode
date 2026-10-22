from env_client import make_env
e=make_env();s,_=e.reset(seed=2)
for t in e.observation_space.types:
 if t.name=='Kinematic3DCuboid':
  for o in s.get_objects(t):print(o.name,[s.get(o,'pose_'+a) for a in 'xyz'],[s.get(o,'half_extent_'+a) for a in 'xyz'])
e.close()
