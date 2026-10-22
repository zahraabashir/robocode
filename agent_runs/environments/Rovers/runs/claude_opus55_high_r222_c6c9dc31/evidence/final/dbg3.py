import sys, math
from env_client import make_env
env=make_env(); obs,_=env.reset(seed=int(sys.argv[1]))
T=lambda n: env.observation_space.get_type(n)
cx,cy=float(sys.argv[2]),float(sys.argv[3])
for o in obs.get_objects(T('objective')):
    x,y=obs.get(o,'x'),obs.get(o,'y'); print(o.name, round(x,3),round(y,3), 'dist',round(math.hypot(x-cx,y-cy),3))
