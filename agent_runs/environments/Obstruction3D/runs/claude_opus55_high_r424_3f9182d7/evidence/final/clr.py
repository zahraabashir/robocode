import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=int(sys.argv[1]), options={"object_count":int(sys.argv[2])})
ap=GeneratedApproach(env.action_space, env.observation_space, None); ap.reset(obs,info)
cubes=[obs.get_object_from_name(n) for n in sorted(obs.get_object_names()) if n.startswith('obs')]
tb=obs.get_object_from_name('target_block')
for c in cubes:
    oth=[d for d in cubes if d.name!=c.name]+[tb]
    print(c.name, [round(ap._finger_clearance(obs,c,k*np.pi/2,oth),4) for k in range(4)])
