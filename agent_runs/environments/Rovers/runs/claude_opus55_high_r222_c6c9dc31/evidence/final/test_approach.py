import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seeds = [int(s) for s in sys.argv[1:]] or list(range(10))
env = make_env()
tot=[]
for seed in seeds:
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
    plen = {r: len(p) for r,p in ap.plans.items()}
    done=False; steps=0
    while not done and steps < 1000:
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        steps += 1; done = term or trunc
    print(f"seed {seed} n={info.get('object_count')} steps={steps} term={term} plan={plen} replans={ap.nreplan} tplan={tp:.2f}s total={time.time()-t0:.1f}s", flush=True)
    tot.append(steps)
print("mean", np.mean(tot))
