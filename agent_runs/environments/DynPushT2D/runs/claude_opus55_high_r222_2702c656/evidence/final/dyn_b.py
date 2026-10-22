import numpy as np, sys
from env_client import make_env
np.set_printoptions(precision=4,suppress=True)
env=make_env()
def goto(env,obs,tx,ty,speed=0.0499):
    n=0
    while True:
        r=obs[16:18]; d=np.array([tx,ty])-r
        if np.linalg.norm(d)<1e-4: return obs,n
        step=np.clip(d,-speed,speed)
        obs,rew,te,tr,info=env.step(step); n+=1
def run(seed,speed,pushsteps):
    obs,_=env.reset(seed=seed)
    b0=obs[0:3].copy()
    print("seed",seed,"block",b0,"robot",obs[16:18])
    obs,n=goto(env,obs,b0[0],b0[1]-1.5)
    print("after approach block",obs[0:3],"robot",obs[16:18],"steps",n)
    hist=[]
    for t in range(pushsteps):
        prev=obs[0:3].copy()
        obs,rew,te,tr,info=env.step(np.array([0,speed]))
        hist.append((t,obs[1]-prev[1],obs[4],obs[0:3].copy(),obs[3:6].copy(),obs[17],rew))
    for h in hist[::5]: print("push",h[0],"dy %.4f vy %.4f"%(h[1],h[2]),h[3],h[4],"ry %.3f"%h[5],h[6])
    # stop
    for t in range(15):
        prev=obs[0:3].copy()
        obs,rew,te,tr,info=env.step(np.array([0,0]))
        print("stop",t,"d",obs[0:3]-prev,"v",obs[3:6])
    for t in range(5):
        prev=obs[0:3].copy()
        obs,rew,te,tr,info=env.step(np.array([0,-0.0499]))
        print("back",t,"d",obs[0:3]-prev,"v",obs[3:6])
run(int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]))
