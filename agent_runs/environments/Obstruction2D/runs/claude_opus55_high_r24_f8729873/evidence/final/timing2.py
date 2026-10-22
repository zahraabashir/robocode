import sys, time
from env_client import make_env
from approach import GeneratedApproach
for seed,cnt in [(411,4),(403,4),(329,3),(182,None)]:
    env=make_env(); obs,info=env.reset(seed=seed, options={'object_count':cnt} if cnt else None)
    ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
    tc=0; mx=0
    for t in range(1000):
        t0=time.time(); a=ap.get_action(obs); dt=time.time()-t0; tc+=dt; mx=max(mx,dt)
        obs,r,term,tr,_=env.step(a)
        if term: break
    print(seed, cnt, "steps", t+1, "compute %.2fs maxstep %.3fs"%(tc,mx))
    env.close()
