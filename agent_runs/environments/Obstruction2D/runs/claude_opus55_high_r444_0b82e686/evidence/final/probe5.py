import numpy as np, math
from env_client import make_env
env = make_env()
def R(o):
    r=o.get_object_from_name('robot'); return {f:float(o.get(r,f)) for f in ["x","y","theta","arm_joint","vacuum"]}
def B(o,n):
    b=o.get_object_from_name(n); return {f:round(float(o.get(b,f)),4) for f in ["x","y","theta"]}
def go(env,obs,tx,ty,tth,vac=0.0,n=60):
    for _ in range(n):
        r=R(obs)
        a=[np.clip(tx-r['x'],-.05,.05),np.clip(ty-r['y'],-.05,.05),np.clip(tth-r['theta'],-.19,.19),np.clip(0.2-r['arm_joint'],-.1,.1),vac]
        if max(abs(a[0]),abs(a[1]),abs(a[2]),abs(a[3]))<1e-7: break
        obs,*_=env.step(np.array(a,dtype=np.float32))
    return obs
for mode in ["tilt","side"]:
    obs,_=env.reset(seed=6016, options={"object_count":3})
    from approach import GeneratedApproach
    ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,None)
    for _ in range(17): obs,*_=env.step(ap.get_action(obs))
    print("obs1", B(obs,'obstruction1'))
    # first move obstruction1 away: skip — go high first
    obs=go(env,obs,1.2,0.8,-math.pi/2)
    if mode=="tilt":
        a=0.45
        obs=go(env,obs,1.517,0.6,-math.pi/2+a)
        # descend until blocked
        for _ in range(80):
            y0=R(obs)['y']; obs,*_=env.step(np.array([0,-0.005,0,0,0],dtype=np.float32))
            if abs(R(obs)['y']-y0)<1e-7: break
        print("tilt stopped", R(obs), B(obs,'obstruction0'))
    else:
        obs=go(env,obs,1.2,0.8,0.0)
        obs=go(env,obs,1.5604-0.21-0.0003,0.2+0.001,0.0)
        print("side at", R(obs), B(obs,'obstruction0'))
    obs,*_=env.step(np.array([0,0,0,0,1.0],dtype=np.float32))
    obs,*_=env.step(np.array([-0.05,0.05,0,0,1.0],dtype=np.float32))
    print(mode,"after", R(obs), B(obs,'obstruction0'))
env.close()
