from probe_vis_lib import *
import probe_vis_lib as L, sys
seed=int(sys.argv[1]); L.RV=sys.argv[2]; name=sys.argv[3]; ang=float(sys.argv[4])
via=eval(sys.argv[5]) if len(sys.argv)>5 else None
for thd in [0,90,180,-90]:
    th=np.deg2rad(thd)
    b=bis(seed,name,np.deg2rad(ang),th,via=via)
    if b and not isinstance(b[0],str):
        reset(seed); o=objpos(name)
        print(thd,b,'model',round(model(b[2],th,o),4))
    else: print(thd,b)
