import sys, time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
seeds = range(int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else range(10)
env = make_env()
res = []
for sd in seeds:
    obs, info = env.reset(seed=sd)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0 = time.time()
    ap.reset(obs, info)
    ok = False
    for t in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        if term:
            ok = True; break
        if trunc: break
    dt = time.time() - t0
    g = obs[29:32]
    err = (obs[0]-g[0], obs[1]-g[1], (obs[2]-g[2]+np.pi)%(2*np.pi)-np.pi)
    res.append(ok)
    print(f"seed {sd} ok={ok} steps={t+1} time={dt:.1f}s err={np.round(err,3)}", flush=True)
print('success', np.mean(res), sum(res), len(res))
