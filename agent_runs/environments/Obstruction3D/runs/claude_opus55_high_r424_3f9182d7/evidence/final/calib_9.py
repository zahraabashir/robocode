import numpy as np, kin
D=np.load('dbg/g1.npy')
for i in range(1,len(D)):
    db=D[i,:3]-D[i-1,:3]; dq=D[i,3:10]-D[i-1,3:10]
    if np.abs(db).max()>1e-6 and np.abs(dq).max()<1e-9:
        # predicted: rotate previous block pos about previous base (x,y) by dtheta then translate
        b0=D[i-1,:3]; b1=D[i,:3]; p0=D[i-1,10:13]; p1=D[i,10:13]
        rel=kin._rz(-b0[2])@(p0-[b0[0],b0[1],0]); pred=kin._rz(b1[2])@rel+[b1[0],b1[1],0]
        print(np.round(db,3),'err',np.round(p1-pred,4))
    if i>40: break
