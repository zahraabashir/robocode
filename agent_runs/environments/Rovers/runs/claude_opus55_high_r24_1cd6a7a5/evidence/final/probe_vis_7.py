from probe_vis_lib import *
import probe_vis_lib as L, sys
seed=int(sys.argv[1]); p=eval(sys.argv[2]); thd=float(sys.argv[3]); via=eval(sys.argv[4]) if len(sys.argv)>4 else [(-1.0,-1.75),(-1.0,p[1])]
reset(seed); q=goto(via+[p]); turn(np.deg2rad(thd)); q=pos()
out=[]
for k in range(3):
    c=cal(); step(op=-1/6); out.append((c,imaged()))
print(p,thd,q.round(4),out)
