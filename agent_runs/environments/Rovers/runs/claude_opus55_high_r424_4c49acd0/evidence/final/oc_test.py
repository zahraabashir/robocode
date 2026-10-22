import sys, time
from multiprocessing import Pool
from env_client import make_env
from approach import GeneratedApproach
def run(args):
    seed, oc = args
    env = make_env()
    obs, info = env.reset(seed=seed, options={"object_count": oc})
    t0=time.time()
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    tplan=time.time()-t0
    steps=0; te=False
    for k in range(env.max_steps):
        a = ap.get_action(obs)
        obs, r, te, tr, info = env.step(a)
        steps+=1
        if te or tr: break
    env.close()
    nobj=sum(1 for n in obs.get_object_names() if obs.get_object_from_name(n).type.name=='objective')
    return (seed, oc, nobj, steps, te, ap.plan_cost, round(tplan,2), round(time.time()-t0,1))
if __name__=='__main__':
    ocs=[int(x) for x in sys.argv[1].split(',')]; seeds=range(int(sys.argv[2]))
    with Pool(8) as p:
        for r in p.imap_unordered(run, [(s,o) for o in ocs for s in seeds]): print(*r, flush=True)
