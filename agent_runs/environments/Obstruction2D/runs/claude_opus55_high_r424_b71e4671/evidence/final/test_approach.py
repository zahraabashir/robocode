import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
OC=None
def run_once(seed):
    env = make_env()
    try:
        ap = GeneratedApproach(env.action_space, env.observation_space, {})
        obs, info = env.reset(seed=seed, options={'object_count':OC} if OC is not None else None)
        t0=time.time(); ap.reset(obs, info)
        te=False
        for t_ in range(env.max_steps):
            a = ap.get_action(obs)
            obs, r, te, tr, _ = env.step(a)
            if te or tr: break
        return te, t_+1, info.get('object_count'), getattr(ap,'leg',None), time.time()-t0
    finally:
        try: env.close()
        except Exception: pass
def run(seed):
    for k in range(3):
        try: return run_once(seed)
        except Exception as e:
            err=e; time.sleep(2)
    return None, 0, None, repr(err)[:80], 0
if __name__ == "__main__":
    if len(sys.argv)>3: OC=int(sys.argv[3])
    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(run, seeds))
    ok = 0
    for s, (te, n, c, ph, dt) in zip(seeds, res):
        ok += bool(te)
        if not te: print("FAIL seed", s, "n_obj", c, "leg", ph, flush=True)
    slow=sorted([(r[4],seeds[i]) for i,r in enumerate(res)])[-3:]; print("slowest idx",slow)
    print(f"solved {ok}/{len(res)}  mean steps {np.mean([r[1] for r in res if r[0]]) if ok else 0:.1f} max time {max(r[4] for r in res):.1f}s")
