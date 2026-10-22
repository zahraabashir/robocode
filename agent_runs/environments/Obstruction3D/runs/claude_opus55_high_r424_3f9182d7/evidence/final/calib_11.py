# per-joint axis identification from grasped block
from calib_u import *
from scipy.spatial.transform import Rotation as Rot
import sys
seed=int(sys.argv[1]); e=R(); e.reset(seed); b=e.blk()
x,y=b[0]-0.10,b[1]-0.01; z=0.40
e.go([x,y,z],0.0)
while z>0.25+1e-9:
    if not e.go([x,y,z-0.005],0.0): break
    z-=0.005
for i in range(2): e.stepq(np.zeros(7),-1.0)
e.go([x,y,0.42],0.0,grip=-1)
def bp():
    return np.array([e.g('target_block',k) for k in ['pose_x','pose_y','pose_z']]), Rot.from_quat([e.g('target_block',k) for k in ['pose_qx','pose_qy','pose_qz','pose_qw']]).as_matrix()
def jframes(base,q):
    bx,by,br=base; M=kin._T((bx,by,0),kin._rz(br)); out=[]
    for Jt,qi in zip(kin._JT,q):
        M=M@Jt; out.append(M.copy()); M=M@kin._T((0,0,0),kin._rz(qi))
    return out
np.set_printoptions(precision=3,suppress=True)
d=0.1
for j in range(7):
    p0,R0=bp(); q=e.q(); fr=jframes(e.base(),q)
    dq=np.zeros(7); dq[j]=d; ok=e.stepq(dq,-1.0)
    p1,R1=bp(); e.stepq(-dq,-1.0)
    rv=Rot.from_matrix(R1@R0.T).as_rotvec(); ang=np.linalg.norm(rv); w=rv/ang
    A=np.eye(3)-R1@R0.T; c=np.linalg.pinv(A,rcond=1e-3)@(p1-R1@R0.T@p0)
    zf=fr[j][:3,2]; of=fr[j][:3,3]
    # distance between true axis line and FK axis line points
    cperp=c-of; cperp-=np.dot(cperp,w)*w
    print(f"j{j+1} ok={ok} ang={ang:.3f} true_w={w} fk_z={zf} dot={np.dot(w,zf):+.3f} true_pt={c} fk_org={of} off_perp={cperp}")
