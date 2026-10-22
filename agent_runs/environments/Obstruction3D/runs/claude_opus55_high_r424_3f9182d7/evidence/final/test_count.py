import sys, time, numpy as np
from concurrent.futures import ProcessPoolExecutor
def run(args):
    seed, cnt = args
    from env_client import make_env
    import approach
    env = make_env()
    obs, info = env.reset(seed=seed, options={"object_count": cnt})
    ap = approach.GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    t0=time.time(); tc=0; term=False
    n=len([x for x in obs.get_object_names() if x.startswith('obstruction')])
    for steps in range(1, env.max_steps+1):
        t1=time.time(); a = ap.get_action(obs); tc+=time.time()-t1
        obs, rew, term, trunc, info = env.step(a)
        if term or trunc: break
    env.close()
    return seed, n, bool(term), steps, round(tc,1)
if __name__ == "__main__":
    cnt=int(sys.argv[1]); a=int(sys.argv[2]); b=int(sys.argv[3])
    with ProcessPoolExecutor(8) as ex:
        res=list(ex.map(run, [(s,cnt) for s in range(a,b)]))
    for r in res:
        if not r[2]: print(r)
    print("count",cnt,"success", sum(r[2] for r in res), "/", len(res), "mean steps", np.mean([r[3] for r in res]), "max compute", max(r[4] for r in res))
