from plib import *
np.set_printoptions(precision=5, suppress=True, linewidth=200)
env=make_env(); obs,_=env.reset(seed=0)
pose=obs[0:3].copy()
st=to_world(pose,np.array([0,0.35]))
obs,ok=navigate(env,obs,st); print(ok)
dw=rot(pose[2])@np.array([0,-1.0])
for k in range(12):
    a=dw*M if k<6 else np.zeros(2)
    o2,*_=env.step(a)
    print(k, 'blk d', o2[0:3]-obs[0:3], 'dist', block_dist_many(o2,o2[16:18]), 'vel?',o2[3:6])
    obs=o2
