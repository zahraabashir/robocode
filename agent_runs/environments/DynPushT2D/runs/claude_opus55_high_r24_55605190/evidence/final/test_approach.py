import sys, time, numpy as np
from env_client import make_env
from approach import GeneratedApproach
from concurrent.futures import ThreadPoolExecutor
def run(seed):
    env = make_env()
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    obs, info = env.reset(seed=seed)
    ap.reset(obs, info)
    t0 = time.time(); ok=False
    for t in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        if term: ok=True; break
        if trunc: break
    dt=time.time()-t0
    e = (obs[0]-obs[29], obs[1]-obs[30], (obs[2]-obs[31]+np.pi)%(2*np.pi)-np.pi)
    env.close()
    return seed, ok, t+1, dt, e
if __name__=='__main__':
    a,b = int(sys.argv[1]), int(sys.argv[2])
    with ThreadPoolExecutor(8) as ex:
        res = list(ex.map(run, range(a,b)))
    for s,ok,n,dt,e in res:
        print(s, ok, n, f'{dt:.1f}s', np.round(e,3))
    print('success', sum(r[1] for r in res), '/', len(res), 'mean steps', np.mean([r[2] for r in res]))
