from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV=sys.argv[1]; seed=int(sys.argv[2]); name=sys.argv[3]; pill=np.array(eval(sys.argv[4])); rs=eval(sys.argv[5]); threl=float(sys.argv[6]); via=eval(sys.argv[7]); lats=eval(sys.argv[8])
reset(seed); o=objpos(name)[:2]
u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
goto(via); ox,oy=-0.087,-0.0125
th=np.arctan2(-u[1],-u[0])-np.deg2rad(threl); turn(th); th=pos()[2]
for r in rs:
    line=''
    for lat in lats:
        ct=o+r*u+lat*n
        b=ct-np.array([ox*np.cos(th)-oy*np.sin(th), ox*np.sin(th)+oy*np.cos(th)])
        q=goto([tuple(b)])
        if np.linalg.norm(q[:2]-b)>1e-4: line+='X'; continue
        c=cal(); line+=str(int(c))
        if c>0.5: step(op=-1/6)
    print(r,line,flush=True)
