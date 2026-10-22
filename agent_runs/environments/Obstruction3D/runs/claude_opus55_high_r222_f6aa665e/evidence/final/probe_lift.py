import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach, down_R
env = make_env(); obs, info = env.reset(seed=4, options={"object_count":4})
ap = GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(34):
    a = ap.get_action(obs); obs,*_ = env.step(a)
bx = ap._boxes(obs)
for n in ['obstruction0','obstruction1','obstruction2']: print(n, {k: round(v,4) for k,v in bx[n].items()})
R=ap._robot(obs); print("finger", obs.get(R,'finger_state'), np.round(obs.data[R][11:],4))
q=ap._q(obs); base=ap._base(obs); T=ap._ee_world(q,base); print("EE", np.round(T[:3,3],4))
for d in [(0,0,0.002),(0,0.003,0),(0,0.003,0.002),(0.003,0,0),(-0.003,0,0),(0,-0.003,0)]:
    qt,e=ap._ik_world(q, T[:3,3]+np.array(d), T[:3,:3], base)
    a=np.zeros(11,np.float32); a[3:10]=qt-q; o2,*_=env.step(a)
    moved = not np.allclose(ap._q(o2), q)
    print(d, "moved", moved)
    if moved:
        a[3:10]=q-qt; o2,*_=env.step(a)
