from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV=sys.argv[1]; seed=int(sys.argv[2]); name=sys.argv[3]; pill=np.array(eval(sys.argv[4])); r=float(sys.argv[5]); ths=eval(sys.argv[6]); via=eval(sys.argv[7])
lat=float(sys.argv[8]) if len(sys.argv)>8 else 0.0
reset(seed); o=objpos(name)[:2]
u=(pill-o)/np.linalg.norm(pill-o); n=np.array([-u[1],u[0]])
ct=o+r*u+lat*n; goto(via)
ox,oy=-0.087,-0.0125; out=[]
brg=np.degrees(np.arctan2(*(o-ct)[::-1]))
for thd in ths:
    th=np.deg2rad(thd)
    b=ct-np.array([ox*np.cos(th)-oy*np.sin(th), ox*np.sin(th)+oy*np.cos(th)])
    turn(th); q=goto([tuple(b)])
    if np.linalg.norm(q[:2]-b)>1e-4: out.append(f"{thd}:X"); continue
    c=cal()
    if c>0.5: step(op=-1/6)
    out.append(f"{thd}({(brg-thd+180)%360-180:.0f}):{int(c)}")
print('bearing',round(brg,1)); print(' '.join(out))
