import sys
from env_client import make_env
from approach import GeneratedApproach
env = make_env(); ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=1029, options={"object_count":4}); ap.reset(obs, info)
for i in range(10):
    a=ap.get_action(obs); obs,*_=env.step(a)
    print(i, ap.mode, ap.cur, ap.place_c, ap.block_g, ap.blockers, ap.drop, getattr(ap,'drop_y',None))
env.close()
