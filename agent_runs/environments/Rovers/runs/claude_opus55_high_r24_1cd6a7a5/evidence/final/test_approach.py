import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
seeds = [int(s) for s in sys.argv[1].split(',')] if len(sys.argv) > 1 else list(range(10))
env = make_env()
res = []
for seed in seeds:
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0 = time.time()
    ap.reset(obs, info)
    tp = time.time() - t0
    steps = 0; term = False
    while steps < 400:
        obs, r, term, trunc, info = env.step(ap.get_action(obs))
        steps += 1
        if term or trunc: break
    nobj = len(ap.sc.objectives)
    print(f"seed {seed} nobj {nobj} steps {steps} term {term} plan {tp:.2f}s", flush=True)
    res.append(steps if term else 9999)
print("mean", np.mean(res), "fails", sum(r == 9999 for r in res))
