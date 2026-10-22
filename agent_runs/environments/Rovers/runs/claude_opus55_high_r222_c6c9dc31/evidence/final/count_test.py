import sys, time
from env_client import make_env
from approach import GeneratedApproach
env=make_env()
n=int(sys.argv[1])
for seed in range(int(sys.argv[2]),int(sys.argv[3])):
    obs,info=env.reset(seed=seed, options={"object_count":n})
    T=env.observation_space.get_type
    t0=time.time(); ap=GeneratedApproach(env.action_space, env.observation_space,{}); ap.reset(obs,info)
    steps=0; term=False
    while not term and steps<300:
        obs,r,term,tr,info=env.step(ap.get_action(obs)); steps+=1
    print(seed, len(list(obs.get_objects(T('objective')))), len(list(obs.get_objects(T('sample')))), steps, term, round(time.time()-t0,1), flush=True)
