from pm_util import *
e=E()
seed=12
o=e.reset(seed); w,L,V=o[12:15]
for name,p,d in [("top x=0",[0,0.12],[0,-1]),("top x=.3",[0.3,0.12],[0,-1]),("stem side y=-.6",[0.08,-0.6],[-1,0]),("stem side y=-1.1",[0.08,-1.1],[-1,0]),("stem bottom",[0,-1.3],[0,1])]:
    mv,obs,a=run_push(e,seed,p,d,0.01,12)
    print(name,"navmv",mv)
    for i in range(1,len(obs)):
        b0=obs[i-1][0:3]; b1=obs[i][0:3]
        dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
        rl=R(b0[2]).T@(obs[i][16:18]-b0[0:2])
        print(f"  {i:2d} dloc={dl} dth={dth:+.5f} robot_loc_after={rl}")
