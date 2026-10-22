from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
print(type(obs), info)
for n in sorted(obs.get_object_names()):
    o = obs.get_object_from_name(n)
    print(n, o.type.name if hasattr(o,'type') else '', )
for t in ['Kinematic3DCuboid','Kinematic3DRobot','Kinematic3DFixture','Kinematic3DPoint']:
    try:
        ty = env.observation_space.get_type(t)
    except Exception as e:
        print(t, e); continue
    for o in obs.get_objects(ty):
        feats = env.observation_space.type_features[ty] if hasattr(env.observation_space,'type_features') else None
        print(o.name, {f: round(float(obs.get(o,f)),4) for f in feats})
print(env.max_steps)
