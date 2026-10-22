from calib_u import *
import sys, shutil
e=R(); e.reset(int(sys.argv[1])); yaw=float(sys.argv[2]); b=e.blk()
dx,dy,z=[float(v) for v in sys.argv[3:6]]
qt,ok=kin.ik(e.base(),e.q(),np.array([b[0]+dx,b[1]+dy,z]),kin.down_R(yaw))
o=e.obs.copy()
for i,f in enumerate(F): o.set(e.r,f,qt[i])
pth=e.env.render_state(state=o); shutil.copy(pth,'dbg/r_'+sys.argv[6]+'.png'); print(ok,np.round(qt,3))
