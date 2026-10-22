import numpy as np, kin
from scipy.spatial.transform import Rotation as Rot
D=np.load('dbg/g1.npy')
np.set_printoptions(precision=3,suppress=True)
for i in [0,1,2,3,4,5,10,20,40]:
    d=D[i]; Rb=Rot.from_quat(d[13:17]).as_matrix(); Ra=kin.fk(d[:3],d[3:10])[:3,:3]
    print(i, np.round(d[:3],3), Rot.from_matrix(Ra.T@Rb).as_rotvec(), 'blkpos',d[10:13])
