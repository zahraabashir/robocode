import sys, time, numpy as np
from concurrent.futures import ProcessPoolExecutor
def run(seed):
    from env_client import make_env
    import approach
    env = make_env()
    obs, info = env.reset(seed=seed)
    ap = approach.GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    t0=time.time(); steps=0; term=False
    n=len([x for x in obs.get_object_names() if x.startswith('obstruction')])
    for steps in range(1, env.max_steps+1):
        a = ap.get_action(obs)
        obs, rew, term, trunc, info = env.step(a)
        if term or trunc: break
    env.close()
    return seed, n, bool(term), steps, round(time.time()-t0,1)
if __name__ == "__main__":
    a=int(sys.argv[1]) if len(sys.argv)>1 else 0; b=int(sys.argv[2]) if len(sys.argv)>2 else 10
    with ProcessPoolExecutor(8) as ex:
        res=list(ex.map(run, range(a,b)))
    for r in res: print(r)
    print("success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]))
