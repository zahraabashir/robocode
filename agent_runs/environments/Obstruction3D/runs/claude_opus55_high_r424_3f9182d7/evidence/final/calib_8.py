import numpy as np, kin
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation as Rot
D=np.concatenate([np.load(f'dbg/g{s}.npy') for s in [1,5,6]])
def T6(p): M=np.eye(4); M[:3,:3]=Rot.from_rotvec(p[3:6]).as_matrix(); M[:3,3]=p[:3]; return M
def Tbase(b): M=np.eye(4); M[:3,:3]=kin._rz(b[2]); M[:3,3]=[b[0],b[1],0]; return M
blkT=[]
for d in D:
    M=np.eye(4); M[:3,:3]=Rot.from_quat(d[13:17]).as_matrix(); M[:3,3]=d[10:13]; blkT.append(M)
arm=[kin.fk((0,0,0),d[3:10]) for d in D]
def pred(p,i): return Tbase(D[i,:3])@T6(p[:6])@arm[i]@T6(p[6:12])
def res(p):
    r=[]
    for i in range(len(D)):
        P=pred(p,i); r.append(P[:3,3]-blkT[i][:3,3]); r.append(0.1*(P[:3,:3]-blkT[i][:3,:3]).ravel())
    return np.concatenate(r)
best=None
for k in range(5):
    p0=np.random.default_rng(k).normal(0,0.3,12) if k else np.zeros(12)
    s=least_squares(res,p0)
    if best is None or s.cost<best.cost: best=s
p=best.x; r=res(p).reshape(len(D),-1)
print('pos rms',np.sqrt((r[:,:3]**2).mean()), 'max',np.abs(r[:,:3]).max(), 'rot rms',np.sqrt((r[:,3:]**2).mean())*10)
B=T6(p[:6]); T=T6(p[6:12])
np.set_printoptions(precision=4,suppress=True)
print('B=\n',B,'\nB rpy',Rot.from_matrix(B[:3,:3]).as_euler('xyz'),'\nT=\n',T,'\nT rpy',Rot.from_matrix(T[:3,:3]).as_euler('xyz'))
print('grasp_tf',D[0,17:24])
np.save('dbg/fitp.npy',p)
