import sys, json, time
import numpy as np
from env_client import make_env
import approach
from multiprocessing import Pool
OV = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
def run(seed):
    env = make_env()
    obs, info = env.reset(seed=seed)
    ap = approach.GeneratedApproach(env.action_space, env.observation_space, {})
    for k,v in OV.items():
        if k.startswith("G_"): setattr(approach, k[2:], v)
        else: setattr(ap, k, v)
    ap.reset(obs, info)
    t0=time.time()
    for steps in range(1, env.max_steps + 1):
        obs, r, term, trunc, _ = env.step(np.clip(ap.get_action(obs), -0.049, 0.049))
        if term or trunc: break
    env.close()
    if time.time()-t0 > 10: print("SLOW", seed, steps, time.time()-t0, flush=True)
    if not term: print("FAIL", seed, obs[0:3]-obs[29:32], flush=True)
    return term, steps, time.time()-t0
if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    with Pool(15) as p:
        res = p.map(run, range(a, b))
    print(OV, "solved %d/%d mean %.1f maxt %.1f" % (sum(r[0] for r in res), len(res), np.mean([r[1] for r in res]), max(r[2] for r in res)))
