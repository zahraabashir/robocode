import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach

def run(seed, verbose=False, max_steps=None, count=None):
    env = make_env()
    obs, info = env.reset(seed=seed, options={'object_count': count} if count else None)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    t0 = time.time()
    ap.reset(obs, info)
    ms = max_steps or env.max_steps
    steps = 0
    term = False
    pt = 0.0
    for steps in range(1, ms + 1):
        t1 = time.time()
        a = ap.get_action(obs)
        pt += time.time() - t1
        obs, r, term, trunc, info = env.step(a)
        if term or trunc:
            break
    dt = time.time() - t0
    nobs = len([n for n in obs.get_object_names() if n.startswith('obstruction')])
    env.close()
    return term, steps, dt, nobs, ap.phase, pt

if __name__ == '__main__':
    seeds = range(int(sys.argv[1]), int(sys.argv[2]))
    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
    ok = 0
    for s in seeds:
        term, steps, dt, n, ph, pt = run(s, count=count)
        ok += term
        print(f'seed {s}: success={term} steps={steps} time={dt:.1f}s ptime={pt:.1f}s nobs={n} phase={ph}', flush=True)
    print(f'{ok}/{len(seeds)}')
