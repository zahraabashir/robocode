import sys
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]), options={"object_count":int(sys.argv[2])})
ap=GeneratedApproach(env.action_space, env.observation_space, None); ap.reset(obs,info)
for t in range(int(sys.argv[3])):
    obs,r,term,trunc,info=env.step(ap.get_action(obs))
print('queue', ap.queue[:2])
for n in sorted(obs.get_object_names()):
    o=obs.get_object_from_name(n)
    if n=='robot':
        print(n,[round(obs.get(o,f),4) for f in ['finger_state','grasp_active']]); continue
    print(n,[round(obs.get(o,f),4) for f in ['pose_x','pose_y','pose_z','half_extent_x','half_extent_y','half_extent_z','pose_qz','pose_qw']])
