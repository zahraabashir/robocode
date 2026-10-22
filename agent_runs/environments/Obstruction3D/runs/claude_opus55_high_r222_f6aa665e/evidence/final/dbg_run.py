import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach, fk
import approach as AP
seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 1000; OC=int(sys.argv[3]) if len(sys.argv)>3 else None
env = make_env(); obs, info = env.reset(seed=seed, options=({"object_count":OC} if OC else None))
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
bx = ap._boxes(obs)
for n,b in sorted(bx.items()): print(n, {k: round(v,3) for k,v in b.items()})
lastseg=None
for t in range(N):
    a = ap.get_action(obs)
    seg = ap.cur
    key = None if seg is None else tuple((tuple(np.round(v,3)) if isinstance(v,np.ndarray) else (round(v,2) if isinstance(v,float) else v)) for v in seg)
    obs, r, term, trunc, info = env.step(a)
    q = ap._q(obs); T = ap._ee_world(q, ap._base(obs))
    rob = ap._robot(obs)
    if key != lastseg or np.allclose(q, ap.last_q):
        print(t, key, "ee", np.round(T[:3,3],3), "grasp", obs.get(rob,'grasp_active'), "REJ" if np.allclose(q, ap.last_q) and np.any(a[3:10]!=0) else "")
        lastseg = key
    if term: print("DONE", t); break
