# grasp attempt: python calib_6.py seed yaw ox oy zfinal
from calib_u import *
import sys
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); ox,oy,zf=[float(v) for v in sys.argv[3:6]]
e=R(); e.reset(seed); b=e.blk()
x,y=b[0]-ox,b[1]-oy; z=0.40
e.go([x,y,z],yaw)
while z>zf+1e-9:
    if not e.go([x,y,z-0.005],yaw): break
    z-=0.005
print('stopped z',round(z,3))
for i in range(6):
    e.stepq(np.zeros(7),-1.0); print('close',i,e.rob('finger_state'),e.rob('grasp_active'),e.g('target_block','grasp_active'))
for i in range(5):
    r=e.go([x,y,z+0.02*(i+1)],yaw); print('lift',r,np.round(e.blk()[:3],4),'ee',np.round(e.ee()[:3,3],4))
print('tf',[round(e.rob('grasp_tf_'+k),4) for k in ['x','y','z','qx','qy','qz','qw']])
from scipy.spatial.transform import Rotation as Rot
Rb=Rot.from_quat([e.g('target_block',k) for k in ['pose_qx','pose_qy','pose_qz','pose_qw']]).as_matrix()
M=e.ee(); print('EE R\n',np.round(M[:3,:3],3),'\nblock R\n',np.round(Rb,3))
