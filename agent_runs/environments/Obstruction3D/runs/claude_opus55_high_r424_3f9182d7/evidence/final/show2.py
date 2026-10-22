import sys
from env_client import make_env
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]), options={"object_count":int(sys.argv[2])})
for n in sorted(obs.get_object_names()):
    if n=='robot': continue
    o=obs.get_object_from_name(n)
    print(n,[round(obs.get(o,f),4) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','pose_qz']])
