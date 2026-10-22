import sys, time
from env_client import make_env
from approach import GeneratedApproach
seeds = [int(s) for s in sys.argv[1].split(',')] if len(sys.argv)>1 else list(range(10))
env = make_env()
tot=0; fails=[]
for seed in seeds:
    obs, info = env.reset(seed=seed)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0=time.time(); ap.reset(obs, info); tp=time.time()-t0
    steps=0; done=False
    while steps < env.max_steps:
        a = ap.get_action(obs)
        obs, r, term, trunc, info = env.step(a)
        steps += 1
        if term or trunc:
            done = term; break
    tt=time.time()-t0
    print(f"seed {seed} n={len(ap.objectives)} steps={steps} done={done} plan={getattr(ap,'plan_score',None)} tplan={tp:.1f}s ttot={tt:.1f}s plan={ap.plan}", flush=True)
    tot+=steps
    if not done: fails.append(seed)
print("total", tot, "fails", fails)
