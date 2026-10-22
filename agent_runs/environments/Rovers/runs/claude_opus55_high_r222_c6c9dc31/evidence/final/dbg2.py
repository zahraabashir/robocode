import sys
from env_client import make_env
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
px,py=float(sys.argv[2]),float(sys.argv[3])
for o in obs.get_objects(env.observation_space.get_type('obstacle')):
    x,y=obs.get(o,'x'),obs.get(o,'y')
    if abs(x-px)<0.8 and abs(y-py)<0.8: print(o.name,x,y,obs.get(o,'half_x'),obs.get(o,'half_y'),obs.get(o,'half_z'))
for o in obs.get_objects(env.observation_space.get_type('sample')):
    print(o.name, obs.get(o,'x'), obs.get(o,'y'))
