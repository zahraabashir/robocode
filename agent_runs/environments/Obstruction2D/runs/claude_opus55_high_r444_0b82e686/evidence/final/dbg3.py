import sys
from env_client import make_env
from approach import GeneratedApproach
seed=int(sys.argv[1]); T=int(sys.argv[2])
env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=seed); ap.reset(obs, info)
for i in range(T):
    a=ap.get_action(obs); obs,*_=env.step(a)
r,objs,s=ap._parse(obs)
print(r); [print({k:(round(v,3) if isinstance(v,float) else v) for k,v in o.items()}) for o in objs.values()]
print(ap.mode, ap.cur, ap.place_c, ap.block_g, ap.blockers, ap.drop)
env.close()
