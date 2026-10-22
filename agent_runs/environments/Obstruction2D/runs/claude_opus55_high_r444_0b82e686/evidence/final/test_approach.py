import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor

OC=None
def run(seed):
    try:
        return run_(seed)
    except Exception as e:
        return seed, None, 0, str(e)[:80]

def run_(seed):
    env = make_env()
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
    ap.reset(obs, info)
    t0 = time.time()
    for step in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        if term:
            env.close(); return seed, True, step + 1, time.time() - t0
        if trunc:
            break
    env.close()
    return seed, False, env.max_steps, time.time() - t0

if __name__ == "__main__":
    global_oc = None
    s0 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    globals()["OC"] = int(sys.argv[3]) if len(sys.argv) > 3 else None
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(run, range(s0, s0 + n)))
    for r in res:
        if r[1] is False: print("FAIL", r)
    ok = [r for r in res if r[1]]
    print("errors", [r[0] for r in res if r[1] is None]); print(f"success {len(ok)}/{len(res)}, mean steps (succ) {np.mean([r[2] for r in ok]) if ok else 0:.1f}")
