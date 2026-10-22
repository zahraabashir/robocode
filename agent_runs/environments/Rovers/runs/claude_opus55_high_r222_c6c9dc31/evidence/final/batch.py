import sys, time, subprocess
from concurrent.futures import ProcessPoolExecutor
def run(seed):
    import numpy as np
    from env_client import make_env
    from approach import GeneratedApproach
    env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":int(sys.argv[3])} if len(sys.argv)>3 else None))
    t0=time.time()
    ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
    steps=0; term=False
    while not term and steps < 300:
        a = ap.get_action(obs); obs, r, term, trunc, info = env.step(a); steps += 1
    env.close()
    return ap.log, seed, info.get('object_count'), steps, term, ap.nreplan, time.time()-t0
if __name__=='__main__':
    a,b=int(sys.argv[1]),int(sys.argv[2])
    with ProcessPoolExecutor(8) as ex:
        res=list(ex.map(run, range(a,b)))
    import numpy as np
    for r in res:
        if not r[4] or r[5]>0 or r[6]>10: print(r)
    print('solved',sum(r[4] for r in res),'/',len(res),'mean steps',np.mean([r[3] for r in res]), 'max time', max(r[6] for r in res))
