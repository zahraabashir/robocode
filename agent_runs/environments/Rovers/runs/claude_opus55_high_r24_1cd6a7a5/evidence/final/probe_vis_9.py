from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV=sys.argv[1]; seed=int(sys.argv[2]); p=eval(sys.argv[3]); via=eval(sys.argv[4]); dth=float(sys.argv[5]) if len(sys.argv)>5 else 15
reset(seed); q=goto(via+[p]); print('at',q.round(4))
res=[]
for thd in np.arange(-180,180,dth):
    turn(np.deg2rad(thd)); c=cal()
    got=''
    if c>0.5:
        before=set(imaged()); step(op=-1/6); got=','.join(n[-1] for n in set(imaged())-before) or '='
    res.append(f"{int(thd)}:{int(c)}{got}")
print(' '.join(res))
