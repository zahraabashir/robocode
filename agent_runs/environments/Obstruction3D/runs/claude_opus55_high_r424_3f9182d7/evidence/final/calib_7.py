# collect grasped samples: python calib_7.py seed out.npy
from calib_u import *
import sys
seed=int(sys.argv[1]); e=R(); e.reset(seed); b=e.blk(); yaw=0.0
x,y=b[0]-0.10,b[1]-0.01; z=0.40
e.go([x,y,z],yaw)
while z>0.25+1e-9:
    if not e.go([x,y,z-0.005],yaw): break
    z-=0.005
for i in range(2): e.stepq(np.zeros(7),-1.0)
print('grasp',e.rob('grasp_active'))
e.go([x,y,0.40],yaw,grip=-1)
rng=np.random.default_rng(seed); D=[]
def rec():
    D.append(np.concatenate([e.base(),e.q(),[e.g('target_block',k) for k in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']],[e.rob('grasp_tf_'+k) for k in ['x','y','z','qx','qy','qz','qw']],[e.rob('grasp_active')]]))
rec(); q0=e.q()
for t in range(120):
    a=np.zeros(11,np.float32); a[10]=-1
    if t%4==3: a[:3]=rng.uniform(-0.1,0.1,3)
    else:
        a[3:10]=np.clip(rng.uniform(-0.15,0.15,7)+0.3*(q0-e.q()),-0.2,0.2)
    e.step(a); rec()
D=np.array(D); np.save(sys.argv[2],D); print(D.shape, 'grasp_active all', D[:,-1].min(), 'tf std', D[:,17:24].std(0).round(5))
