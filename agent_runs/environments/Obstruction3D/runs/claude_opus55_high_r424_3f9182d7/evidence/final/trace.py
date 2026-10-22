import sys, time, numpy as np
from env_client import make_env
import approach, kin
seed=int(sys.argv[1]); N=int(sys.argv[2]) if len(sys.argv)>2 else 200
env=make_env(); obs,info=env.reset(seed=seed)
ap=approach.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
tc=0
for t in range(N):
    t0=time.time(); a=ap.get_action(obs); tc+=time.time()-t0
    r=obs.get_object_from_name('robot')
    q=np.array([obs.get(r,f) for f in approach.JF]); base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
    tcp=kin.fk(base,q,0.12)[:3,3]
    cmd=ap.queue[0] if ap.queue else None
    print(t, cmd[0] if cmd else None, np.round(cmd[1],3) if cmd is not None and not isinstance(cmd[1],str) else (cmd[1] if cmd else ''), "tcp",np.round(tcp,3),"g",obs.get(r,'grasp_active'), "a",np.round(a[3:10],2).tolist(), a[10])
    obs,rew,term,trunc,info=env.step(a)
    if term: print("TERM"); break
print("compute time",tc)
