import sys, time
import numpy as np
from env_client import make_env
import os, importlib
GeneratedApproach = importlib.import_module(os.environ.get("APPROACH", "approach")).GeneratedApproach
def run(seed, verbose=False, count=None):
    env = make_env()
    obs, info = env.reset(seed=seed, options=({'object_count': count} if count is not None else None))
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    n_obs = len(obs.get_object_names()) - 3
    t0=time.time()
    for t in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        if term or trunc: break
    env.close()
    return term, t+1, n_obs, time.time()-t0
if __name__ == "__main__":
    s0, s1 = int(sys.argv[1]), int(sys.argv[2])
    cnt = int(sys.argv[3]) if len(sys.argv) > 3 else None
    succ=0
    for s in range(s0, s1):
        term, steps, n, dt = run(s, count=cnt)
        succ += term
        print(f"seed {s} nobs {n} success {term} steps {steps} time {dt:.1f}", flush=True)
    print("success", succ, "/", s1-s0)
