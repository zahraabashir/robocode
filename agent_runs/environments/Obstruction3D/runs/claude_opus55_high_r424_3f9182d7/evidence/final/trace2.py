import sys, numpy as np
from env_client import make_env
import approach, kin
seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 300; CNT=int(sys.argv[3]) if len(sys.argv)>3 else None
env=make_env(); obs,info=env.reset(seed=seed, options=({"object_count":CNT} if CNT else None))
ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
last=None; rej=0
for t in range(N):
    a=ap.get_action(obs)
    r=obs.get_object_from_name('robot')
    q=np.array([obs.get(r,f) for f in approach.JF]); base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    tcp=kin.fk(base,q,0.12)[:3,3]
    cmd=ap.queue[0] if ap.queue else None
    key=(cmd[0], str(cmd[1])) if cmd else None
    if key!=last:
        print(t, cmd[0], round(cmd[2],2) if len(cmd)>2 and isinstance(cmd[2],float) else "", round(obs.get(r,"finger_state"),2), np.round(cmd[1],3) if not isinstance(cmd[1],(str,float)) else cmd[1], "tcp",np.round(tcp,3),"g",obs.get(r,'grasp_active'))
        last=key
    obs2,rew,term,trunc,info=env.step(a)
    q2=np.array([obs2.get(r,f) for f in approach.JF])
    if np.allclose(q,q2) and np.any(a[3:10]!=0): print("   rejected at",t)
    obs=obs2
    if term: print("TERM",t); break
