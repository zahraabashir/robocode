import json, sys
from concurrent.futures import ThreadPoolExecutor
from env_client import make_env
def get(seed):
    env=make_env(); obs,info=env.reset(seed=seed)
    out={'info':info,'objs':{}}
    for n in obs.get_object_names():
        o=obs.get_object_from_name(n)
        feats=env.observation_space.type_features[o.type] if o.type in env.observation_space.type_features else None
        out['objs'][n]={'type':o.type.name,'f':{f:float(obs.get(o,f)) for f in feats}}
    env.close(); return seed,out
with ThreadPoolExecutor(8) as ex:
    res=dict(ex.map(get, range(int(sys.argv[1]), int(sys.argv[2]))))
json.dump(res, open(f'states_{sys.argv[1]}_{sys.argv[2]}.json','w'))
print(len(res))
