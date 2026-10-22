# release test: python calib_15.py seed relx rely relz(tcp)
from calib_u import *
import sys
seed=int(sys.argv[1]); T=0.12; e=R(); e.reset(seed); b=e.blk(); yaw=0.0 if b[3]<b[4] else np.pi/2
x,y=b[0],b[1]; z=0.25; e.go([x,y,z],yaw,tool=T)
while z>b[2]+b[5]+0.005: 
    e.go([x,y,z-0.005],yaw,tool=T); z-=0.005
e.stepq(np.zeros(7),-1.0); print('grasp',e.rob('grasp_active'))
tx,ty,tz=[float(v) for v in sys.argv[2:5]]
e.go([x,y,0.25],yaw,tool=T,grip=-1); print('go target',e.go([tx,ty,0.25],yaw,tool=T,grip=-1))
zz=0.25
while zz>tz+1e-9:
    if not e.go([tx,ty,zz-0.0025],yaw,tool=T,grip=-1): print('lower blocked at tcp z',round(zz,4),'blk',np.round(e.blk()[:3],4)); break
    zz-=0.0025
print('before open blk',np.round(e.blk()[:3],4))
for i in range(3):
    ok=e.stepq(np.zeros(7),1.0); print('open',i,'grasp',e.rob('grasp_active'),'fs',e.rob('finger_state'),'blk',np.round(e.blk()[:3],4),'blk_ga',e.g('target_block','grasp_active'))
e.go([tx,ty,0.3],yaw,tool=T,grip=0); print('after retreat blk',np.round(e.blk()[:3],4))
for n in e.obs.get_object_names():
    if n!='robot': print(n,np.round(e.blk(n),3))
