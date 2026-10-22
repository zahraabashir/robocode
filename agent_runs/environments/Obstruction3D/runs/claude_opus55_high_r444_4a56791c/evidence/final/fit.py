import json, glob, numpy as np, kin
from scipy.optimize import least_squares
def qmat(x,y,z,w):
    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],[2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],[2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])
D=[]
for f in glob.glob('calib_*.json'): D+=json.load(open(f))
print(len(D))
def Tof(p,q):
    T=np.eye(4); T[:3,:3]=qmat(*q); T[:3,3]=p; return T
def pred(params, d, inv):
    ox,oy,oz,tx,ty,tz = params
    b=d['base']
    Tb=np.eye(4); Tb[:3,:3]=kin.rpy_mat(0,0,b[2]); Tb[:3,3]=[b[0],b[1],0]
    M=np.eye(4); M[:3,3]=[ox,oy,oz]
    T=M.copy()
    for J,qi in zip(kin.JOINTS,d['q']): T=T@J@kin.rotz(qi)
    T=T@kin.EE; Tt=np.eye(4); Tt[:3,3]=[tx,ty,tz]; T=Tb@T@Tt
    G=Tof(d['g'][1:4],d['g'][4:8])
    if inv: G=np.linalg.inv(G)
    return T@G
for inv in [False,True]:
    def res(p):
        r=[]
        for d in D:
            P=pred(p,d,inv); O=Tof(d['obj'][:3],d['obj'][3:])
            r+=list(P[:3,3]-O[:3,3]); r+=list(0.05*(P[:3,:3]-O[:3,:3]).ravel())
        return np.array(r)
    s=least_squares(res,np.zeros(6))
    r=res(s.x).reshape(len(D),-1)
    print(inv, np.round(s.x,4), 'pos rms', np.sqrt(np.mean(r[:,:3]**2)), 'rot', np.sqrt(np.mean(r[:,3:]**2))/0.05)
