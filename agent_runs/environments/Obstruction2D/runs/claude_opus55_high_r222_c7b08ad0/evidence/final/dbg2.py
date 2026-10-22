import numpy as np, sys
from env_client import make_env
from approach import GeneratedApproach
import approach
env = make_env()
ap = GeneratedApproach(env.action_space, env.observation_space, {})
obs, info = env.reset(seed=3, options={'object_count':4})
ap.reset(obs, info)
r, rects = ap._parse(obs); ap.r = r
o = rects['obstruction1']; surf=rects['target_surface']; blk=rects['target_block']
xs=ap.xs
gx = ap._grasp_x(o, rects); gy = o['y1']+0.2+r['gw']+ap.grasp_eps
held = ap._mk_held(o,gx,gy)
others = {k:v for k,v in rects.items() if k!=o['name']}
cands, held_b, gxb, gyb = ap._place_candidates_target(blk, surf, others)
print('gx',gx,'gy',gy,'target', cands[0][:4], gxb, gyb)
P1 = ap._profile(xs, others, held); P2 = ap._profile(xs, others, None)
P3 = ap._profile(xs, {k: v for k, v in others.items() if k != blk['name']}, held_b)
_,_,rxt,ryt,_ = cands[0]
for rx in [0.36, 1.45, 1.47, 1.5]:
    ry = max(gy+0.003, P1[ap._xi(rx)]+0.004)
    x0,x1 = rx+held['dx0'], rx+held['dx1']
    box=(x0,x1,ry+held['dy1'])
    c1=ap._est(gx,gy,rx,ry,P1); c2=ap._est(rx,ry,gxb,gyb,np.maximum(P2,ap._colprof(xs,box,None))); c3=ap._est(gxb,gyb,rxt,ryt,np.maximum(P3,ap._colprof(xs,box,held_b)))
    print(rx, ry, c1,c2,c3)
print(ap._drop_spot(o, rects, surf, blk))
