import sys, time, numpy as np
from multiprocessing import Pool
from env_client import make_env

def run(seed):
    from approach import GeneratedApproach
    env = make_env()
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0 = time.time()
    ap.reset(obs, info)
    steps = 0; term = False
    for t in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        steps += 1
        if term or trunc: break
    g = obs[29:32]
    err = (abs(obs[0]-g[0]), abs(obs[1]-g[1]), abs((obs[2]-g[2]+np.pi)%(2*np.pi)-np.pi))
    env.close()
    return seed, bool(term), steps, time.time()-t0, err

if __name__ == "__main__":
    a, b = int(sys.argv[1]), int(sys.argv[2])
    with Pool(8) as p:
        res = p.map(run, range(a, b))
    for s, ok, st, tt, err in res:
        print(s, ok, st, f"{tt:.1f}s", np.round(err, 3))
    print("success", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]), "max time", max(r[3] for r in res))
