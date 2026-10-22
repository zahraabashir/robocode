from env_client import make_env
import math
env=make_env(); T=lambda n: env.observation_space.get_type(n)
for seed in range(40):
    obs,_=env.reset(seed=seed)
    obst=list(obs.get_objects(T('obstacle')))
    for o in obst:
        if obs.get(o,'half_x')>0.1: continue
        x,y=obs.get(o,'x'),obs.get(o,'y')
        dmin=min(math.hypot(x-obs.get(p,'x'),y-obs.get(p,'y'))-obs.get(p,'half_x') for p in obst if p is not o)
        if dmin>1.0 and 0.75<abs(x)<1.7 and abs(y)<1.7 and math.hypot(x+1.9,y+2)>1.5:
            print(seed,o.name,round(x,2),round(y,2),round(dmin,2))
