from env_client import make_env
from collections import Counter
env = make_env()
cnt=Counter(); mounds=Counter()
for seed in range(40):
    obs, info = env.reset(seed=seed)
    objs=[o for o in obs if o.type.name=='objective']
    cnt[len(objs)]+=1
    for o in objs: mounds[(round(obs.get(o,'x'),1))]+=1
    smp=[(round(obs.get(o,'x'),2),round(obs.get(o,'y'),2),int(obs.get(o,'is_soil'))) for o in obs if o.type.name=='sample']
    if seed<8: print(seed,len(objs),[(round(obs.get(o,'x'),2),round(obs.get(o,'y'),2)) for o in objs],smp)
print(cnt, sorted(mounds.items()))
env.close()
