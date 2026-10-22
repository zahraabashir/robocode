import sys, time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
OC=None
def run(seed, verbose=False):
    env = make_env()
    obs, info = env.reset(seed=seed, options=({'object_count': OC} if OC else None))
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t = time.time(); ap.reset(obs, info)
    ret = 0; steps = 0; term = False; tot_a = 0.0; max_a = 0.0
    for steps in range(1, env.max_steps + 1):
        t1 = time.time(); a = ap.get_action(obs); ta = time.time() - t1
        tot_a += ta; max_a = max(max_a, ta)
        obs, r, term, trunc, info = env.step(a)
        ret += r
        if term or trunc: break
    dt = time.time() - t
    env.close()
    return seed, info.get('object_count'), term, steps, round(dt, 1), round(tot_a, 2), round(max_a, 3)
if __name__ == "__main__":
    from concurrent.futures import ThreadPoolExecutor
    seeds = list(range(int(sys.argv[1]), int(sys.argv[2])))
    if len(sys.argv) > 3: OC = int(sys.argv[3])
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(run, seeds))
    for r in res: print(r)
    print("success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]))
