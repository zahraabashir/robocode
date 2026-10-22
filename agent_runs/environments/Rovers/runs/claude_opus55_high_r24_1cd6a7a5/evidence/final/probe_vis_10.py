from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV=sys.argv[1]; seed=int(sys.argv[2]); name=sys.argv[3]; ang=float(sys.argv[4]); via=eval(sys.argv[5]); ths=eval(sys.argv[6])
lo=float(sys.argv[7]) if len(sys.argv)>7 else 1.3
for thd in ths:
    th=np.deg2rad(thd); b=bis(seed,name,np.deg2rad(ang),th,lo=lo,via=via)
    if b and not isinstance(b[0],str):
        reset(seed); o=objpos(name); print(thd,b,'camdist',round(model(b[2],th,o),4))
    else: print(thd,b)
