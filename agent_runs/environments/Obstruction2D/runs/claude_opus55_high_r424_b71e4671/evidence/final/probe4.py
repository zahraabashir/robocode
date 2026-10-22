from env_client import make_env
import numpy as np
def A(*a): return np.array(a,dtype=np.float32)
def setup(gap, vac_during=False, seed=0):
    env=make_env(); obs,_=env.reset(seed=seed)
    r=obs.get_object_from_name('robot'); b=obs.get_object_from_name('target_block')
    g=lambda o,f: float(obs.get(o,f))
    tx=g(b,'x')+g(b,'width')/2; top=g(b,'y')+g(b,'height')
    # move to x with arm extended
    obs,*_=env.step(A(0,0,0,0.1,0))
    for _ in range(40): obs,*_=env.step(A(np.clip(tx-g(r,'x'),-.05,.05),0,0,0,0))
    ty=top+0.2+0.01+gap
    for _ in range(40): obs,*_=env.step(A(0,np.clip(ty-g(r,'y'),-.05,.05),0,0,1 if vac_during else 0))
    return env,obs,r,b,g
# (b) grasp tolerance
for gap in [0.0005,0.002,0.005,0.01,0.02]:
    env,obs,r,b,g=setup(gap)
    obs,*_=env.step(A(0,0,0,0,1)); by=float(obs.get(b,'y'))
    obs,*_=env.step(A(0,0.05,0,0,1)); print("gap",gap,"lifted", round(float(obs.get(b,'y'))-by,4)); env.close()
# vac on during descent from far: grabbed?
env,obs,r,b,g=setup(0.0005, vac_during=True); by=float(obs.get(b,'y'))
obs,*_=env.step(A(0,0.05,0,0,1)); print("vac-during descent lifted", round(float(obs.get(b,'y'))-by,4))
# (c) release and move same step; gravity
obs,*_=env.step(A(0,0.05,0,0,1)); y1=float(obs.get(b,'y'))
obs,*_=env.step(A(0,0.05,0,0,0)); print("release+move: block dy", round(float(obs.get(b,'y'))-y1,4))
for i in range(3): obs,*_=env.step(A(0,0.0,0,0,0))
print("after release block y", float(obs.get(b,'y')), "(gravity if decreasing)")
env.close()
# move+vac same step: move into contact from gap 0.03 with dy=-0.03 and vac=1
env,obs,r,b,g=setup(0.03); by=float(obs.get(b,'y'))
obs,*_=env.step(A(0,-0.0295,0,0,1)); print("robot y after", g(r,'y'), "vac", g(r,'vacuum'))
obs,*_=env.step(A(0,0.05,0,0,1)); print("move+vac same step lifted", round(float(obs.get(b,'y'))-by,4)); env.close()
