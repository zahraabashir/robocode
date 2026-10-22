import numpy as np, kin
from scipy.optimize import least_squares
from scipy.spatial.transform import Rotation as Rot
S=[1,5,6]; DS=[np.load(f'dbg/g{s}.npy') for s in S]
np.set_printoptions(precision=4,suppress=True)
def prep(D):
    blk=[];arm=[]
    for d in D:
        M=np.eye(4); M[:3,:3]=Rot.from_quat(d[13:17]).as_matrix(); M[:3,3]=d[10:13]
        Tb=np.eye(4); Tb[:3,:3]=kin._rz(d[2]); Tb[:3,3]=[d[0],d[1],0]; blk.append(np.linalg.inv(Tb)@M); arm.append(kin.fk((0,0,0),d[3:10]))
    return blk,arm
P=[prep(D) for D in DS]
def res(p):
    r=[]
    for k,(blk,arm) in enumerate(P):
        t=p[3+3*k:6+3*k]
        for a,b in zip(arm,blk): r.append(a[:3,:3]@t+a[:3,3]+p[:3]-b[:3,3])
    return np.concatenate(r)
s=least_squares(res,np.zeros(3+3*len(S))); r=res(s.x).reshape(-1,3)
print('pos rms',np.sqrt((r**2).mean()),'max',np.abs(r).max())
print('base offset (arm-base frame)',s.x[:3])
for k,D in enumerate(DS):
    blk,arm=P[k]; Rt=arm[0][:3,:3].T@blk[0][:3,:3]
    print('seed',S[k],'block pos in EE frame',s.x[3+3*k:6+3*k],'Rrel quat',Rot.from_matrix(Rt).as_quat(),'| grasp_tf',D[0,17:24])
