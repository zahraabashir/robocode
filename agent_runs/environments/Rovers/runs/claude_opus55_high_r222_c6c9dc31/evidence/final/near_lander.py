import sys, math
from env_client import make_env
env=make_env()
for s in range(int(sys.argv[1]),int(sys.argv[2])):
    obs,_=env.reset(seed=s)
    for o in obs.get_objects(env.observation_space.get_type('sample')):
        x,y=float(obs.get(o,'x')),float(obs.get(o,'y'))
        d=math.hypot(x+1.9,y+2.0)
        if d<float(sys.argv[3]): print(s,o.name,round(x,3),round(y,3),round(d,3),round(float(obs.get(o,"z")),3),flush=True)
