import sys, time
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); seed=int(sys.argv[1])
opts={"object_count":int(sys.argv[2])} if len(sys.argv)>2 else None
obs,info=env.reset(seed=seed, options=opts)
ap=GeneratedApproach(env.action_space, env.observation_space, None)
t0=time.time(); ap.reset(obs,info); tc=time.time()-t0; te=0
for t in range(1000):
    t0=time.time(); a=ap.get_action(obs); tc+=time.time()-t0
    t0=time.time(); obs,r,term,trunc,info=env.step(a); te+=time.time()-t0
    if term or trunc: break
print('steps',t+1,'term',term,'policy s',round(tc,2),'env s',round(te,2))
