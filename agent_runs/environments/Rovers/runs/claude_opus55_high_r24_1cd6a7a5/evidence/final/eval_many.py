import sys, time
import numpy as np
from multiprocessing import Pool
def run(seed):
    from env_client import make_env
    import os, importlib; GeneratedApproach = importlib.import_module(os.environ.get("APP", "approach")).GeneratedApproach
    env = make_env()
    oc = os.environ.get("OC"); obs, info = env.reset(seed=seed, options=({"object_count": int(oc)} if oc else None))
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0 = time.time(); ap.reset(obs, info); tp = time.time()-t0
    pl = [len(p.get('path', p.get('steps', [])))-('path' in p) for p in ap.plans]
    steps=0; term=False
    while steps < 300:
        obs, r, term, trunc, info = env.step(ap.get_action(obs)); steps+=1
        if term or trunc: break
    env.close()
    return seed, len(ap.sc.objectives), steps if term else 9999, max(pl), tp
if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    with Pool(8) as p:
        res = p.map(run, range(a, b))
    for r in res:
        if r[2] == 9999 or r[2] - r[3] > 2: print("seed %d nobj %d steps %d plan %d t %.2f" % r)
    st = [r[2] for r in res]
    print("mean", np.mean([s for s in st if s < 9999]), "fails", sum(s == 9999 for s in st), "maxplan", max(r[4] for r in res))
    import json, os
    json.dump({r[0]: r[2] for r in res}, open('res_%s_%s.json' % (os.environ.get('APP','approach'), os.environ.get('TAG','x')), 'w'))
