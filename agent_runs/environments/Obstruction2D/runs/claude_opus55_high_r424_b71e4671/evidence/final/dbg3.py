import sys, numpy as np
from env_client import make_env
import approach as A
seed=int(sys.argv[1]); upto=int(sys.argv[2])
env=make_env(); obs,info=env.reset(seed=seed)
ap=A.GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(upto):
    obs,*_=env.step(ap.get_action(obs))
robot, block, surface, obst = ap._parse(obs)
rx,ry=A._g(obs,robot,'x'),A._g(obs,robot,'y')
print("robot",rx,ry,"leg",ap.leg, ap.legs[ap.leg])
for o in obst+[block]: print(o.name, np.round(A._rect(obs,o),4))
leg=ap.legs[ap.leg]; name=leg[1]
allr={o.name:A._rect(obs,o) for o in obst+[block]}
r=allr[name]; held=(r[0]-rx,r[1]-rx,r[2]-ry)
obstacles=[(q[0],q[1],q[3]) for n,q in allr.items() if n!=name]
boxes=ap._assembly(held)
X=np.linspace(rx-0.2,rx+0.3,11)
print("held",np.round(held,4)); print("S",np.round(ap._safe(X,boxes,obstacles),3), "X", np.round(X,3))
tx,ty=leg[2]; print("control", ap._control(rx,ry,tx,ty,boxes,obstacles))
