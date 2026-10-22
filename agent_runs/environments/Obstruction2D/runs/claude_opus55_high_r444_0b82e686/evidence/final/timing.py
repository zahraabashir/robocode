import sys, time
from env_client import make_env
from approach import GeneratedApproach
oc=int(sys.argv[1]); worst=0; tot=0
env = make_env()
for seed in range(int(sys.argv[2]), int(sys.argv[3])):
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed, options={"object_count":oc}); ap.reset(obs, info)
    t_ep=0
    for i in range(300):
        t=time.time(); a=ap.get_action(obs); dt=time.time()-t; t_ep+=dt; worst=max(worst,dt)
        obs,r,term,*_=env.step(a)
        if term: break
    print(seed, i+1, round(t_ep,2))
print("worst call", worst)
