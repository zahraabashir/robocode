import sys, time
import numpy as np
from env_client import make_env
from approach import GeneratedApproach
TMAX=0
AT=[0]
def run(seed, count=None, verbose=False):
    env = make_env()
    kw = {}
    if count is not None: kw['options'] = {'object_count': count}
    obs, info = env.reset(seed=seed, **kw)
    ap = GeneratedApproach(env.action_space, env.observation_space, {})
    ap.reset(obs, info)
    n_obj = info.get('object_count')
    global TMAX
    AT[0]=0
    t0=time.time()
    for t in range(env.max_steps):
        tt=time.time(); a = ap.get_action(obs); AT[0]+=time.time()-tt
        obs, r, term, trunc, info = env.step(a)
        if term: env.close(); TMAX=max(TMAX, AT[0]); return True, t+1, n_obj
        if trunc: break
    env.close(); return False, env.max_steps, n_obj
if __name__ == '__main__':
    s0, s1 = int(sys.argv[1]), int(sys.argv[2])
    count = int(sys.argv[3]) if len(sys.argv) > 3 else None
    ok = 0; steps=[]
    for s in range(s0, s1):
        succ, n, c = run(s, count)
        ok += succ; steps.append(n)
        if not succ: print('FAIL seed', s, 'count', c)
    print(f'success {ok}/{s1-s0}, mean steps {np.mean(steps):.1f} max approach time {TMAX:.1f}s')
