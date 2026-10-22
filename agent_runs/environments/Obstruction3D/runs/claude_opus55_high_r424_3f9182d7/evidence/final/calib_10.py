import numpy as np, kin
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation as Rot
D=np.concatenate([np.load(f'dbg/g{s}.npy') for s in [1,5,6]])
def T6(p): M=np.eye(4); M[:3,:3]=Rot.from_rotvec(p[3:6]).as_matrix(); M[:3,3]=p[:3]; return M
blk=[]
for d in D:  # block pose in mobile-base frame
    M=np.eye(4); M[:3,:3]=Rot.from_quat(d[13:17]).as_matrix(); M[:3,3]=d[10:13]
    Tb=np.eye(4); Tb[:3,:3]=kin._rz(d[2]); Tb[:3,3]=[d[0],d[1],0]; blk.append(np.linalg.inv(Tb)@M)
def res(p):
    r=[]
    for i,d in enumerate(D):
        P=T6(p[:6])@kin.fk((0,0,0),d[3:10]+p[12:19])@T6(p[6:12])
        r.append(P[:3,3]-blk[i][:3,3]); r.append(0.1*(P[:3,:3]-blk[i][:3,:3]).ravel())
    return np.concatenate(r)
best=None
for k in range(8):
    p0=np.random.default_rng(k).normal(0,0.3,19) if k else np.zeros(19)
    s=least_squares(res,p0)
    if best is None or s.cost<best.cost: best=s
    print(k, s.cost)
p=best.x; r=res(p).reshape(len(D),-1)
print('pos rms',np.sqrt((r[:,:3]**2).mean()),'max',np.abs(r[:,:3]).max(),'rot rms',np.sqrt((r[:,3:]**2).mean())*10)
np.set_printoptions(precision=4,suppress=True); print(p)
