# grasp test in TCP coords: python calib_14.py seed yaw dx dy tcpz
from calib_u import *
import sys
seed=int(sys.argv[1]); yaw=float(sys.argv[2]); dx,dy,zt=[float(v) for v in sys.argv[3:6]]; T=0.12
e=R(); e.reset(seed); b=e.blk(); x,y=b[0]+dx,b[1]+dy; z=0.25
e.go([x,y,z],yaw,tool=T)
while z>zt+1e-9:
    if not e.go([x,y,z-0.0025],yaw,tool=T): break
    z-=0.0025
e.stepq(np.zeros(7),-1.0)
ga=e.rob('grasp_active'); fs=e.rob('finger_state')
e.go([x,y,0.25],yaw,tool=T,grip=-1)
print(f"seed{seed} yaw{yaw:.2f} d=({dx:+.3f},{dy:+.3f}) tcpz={z:.4f} grasp={ga} fs={fs:.3f} blk_after_lift_z={e.blk()[2]:.3f} tf={[round(e.rob('grasp_tf_'+k),4) for k in 'x y z qx qy qz qw'.split()]}")
