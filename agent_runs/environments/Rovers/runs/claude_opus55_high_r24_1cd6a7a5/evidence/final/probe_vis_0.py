from env_client import make_env
import sys
env=make_env()
for seed in [int(s) for s in sys.argv[1:]]:
    obs,info=env.reset(seed=seed)
    print('SEED',seed)
    for o in obs:
        f=obs.type_features[o.type]
        print(o.type.name,o.name,{k:round(float(v),3) for k,v in zip(f,obs.data[o]) if not k.startswith('have_') and k not in('r','g','b')})
