import numpy as np
def rpy(r,p,y):
    cr,sr,cp,sp,cy,sy=np.cos(r),np.sin(r),np.cos(p),np.sin(p),np.cos(y),np.sin(y)
    return np.array([[cy*cp, cy*sp*sr-sy*cr, cy*sp*cr+sy*sr],[sy*cp, sy*sp*sr+cy*cr, sy*sp*cr-cy*sr],[-sp, cp*sr, cp*cr]])
def T(xyz, R):
    M=np.eye(4); M[:3,:3]=R; M[:3,3]=xyz; return M
def rz(q):
    c,s=np.cos(q),np.sin(q); return np.array([[c,-s,0],[s,c,0],[0,0,1]])
PI=np.pi
JOINTS=[((0,0,0.15643),(PI,0,0)),((0,0.005375,-0.12838),(PI/2,0,0)),((0,-0.21038,-0.006375),(-PI/2,0,0)),
((0,0.006375,-0.21038),(PI/2,0,0)),((0,-0.20843,-0.006375),(-PI/2,0,0)),((0,0.00017505,-0.10593),(PI/2,0,0)),((0,-0.10593,-0.00017505),(-PI/2,0,0))]
EE=((0,0,-0.061525),(PI,0,0))
def fk(base, q, base_z=0.0, tool=0.0):
    bx,by,br=base
    M=T((bx,by,base_z), rz(br))
    for (xyz,r),qi in zip(JOINTS,q):
        M=M@T(xyz,rpy(*r))@T((0,0,0),rz(qi))
    M=M@T(EE[0],rpy(*EE[1]))
    M=M@T((0,0,tool),np.eye(3))
    return M
if __name__=="__main__":
    q=[0,-0.35,-PI,-2.5,0,-0.87,PI/2]
    np.set_printoptions(precision=4,suppress=True)
    print(fk((-0.12,0,0),q))
