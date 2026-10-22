import sys, time
import numpy as np
from env_client import make_env
import os; exec("from " + os.environ.get("APPROACH","approach") + " import GeneratedApproach")
def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
    steps=0; term=False
    while steps < env.max_steps:
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        steps += 1
        if term or trunc: break
    tt=time.time()-t0
    env.close()
    return seed, info.get('object_count') if isinstance(info,dict) else None, term, steps, ap.replans, round(tp,2), round(tt,1)
if __name__ == "__main__":
    seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv)>2 else range(10)
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(run, seeds))
    import json; json.dump(res, open(sys.argv[3] if len(sys.argv)>3 else "last_res.json","w"))
    for r in res: print(r)
    ok=[r for r in res if r[2]]
    print("solved", len(ok), "/", len(res), "mean steps", np.mean([r[3] for r in ok]) if ok else None)
