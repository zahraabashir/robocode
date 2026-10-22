import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
from multiprocessing import Pool

def run(seed):
    env = make_env()
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    t0 = time.time()
    steps = 0
    done = False
    for steps in range(1, env.max_steps + 1):
        try:
            a = ap.get_action(obs)
        except Exception as e:
            print("EXC", seed, steps, obs[[0,1,2,16,17]], repr(e)); break
        obs, r, term, trunc, _ = env.step(np.clip(a, -0.05, 0.05))
        if term:
            done = True
            break
        if trunc:
            break
    env.close()
    g = obs[29:32]
    err = (abs(obs[0]-g[0]), abs(obs[1]-g[1]), abs((obs[2]-g[2]+np.pi)%(2*np.pi)-np.pi))
    return seed, done, steps, time.time()-t0, err

if __name__ == "__main__":
    a = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    with Pool(10) as p:
        res = p.map(run, range(a, b))
    for r in res:
        print(r[0], r[1], r[2], "%.1fs" % r[3], np.round(r[4], 3))
    print("solved", sum(r[1] for r in res), "/", len(res), "mean steps", np.mean([r[2] for r in res]))
