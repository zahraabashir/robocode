import sys, time
from env_client import make_env
from approach import GeneratedApproach
env = make_env()
for seed in range(int(sys.argv[1]), int(sys.argv[2])):
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed)
    t0=time.time(); ap.reset(obs, info); tr=time.time()-t0
    ta=0; tenv=0; n=0
    for _ in range(1000):
        t0=time.time(); a=ap.get_action(obs); ta+=time.time()-t0
        t0=time.time(); obs,r,te,trr,_=env.step(a); tenv+=time.time()-t0; n+=1
        if te: break
    print(seed, info['object_count'], "reset %.3f act %.3f (%.4f/step) env %.2f steps %d"%(tr,ta,ta/n,tenv,n), flush=True)
