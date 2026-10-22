import json, numpy as np
from scipy.optimize import least_squares
from kin import fk
def q2R(x,y,z,w):
    return np.array([[1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],[2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],[2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]])
def T(p,q): M=np.eye(4); M[:3,:3]=q2R(*q); M[:3,3]=p; return M
recs=json.load(open('grasp_recs.json'))
W=[]
for d in recs:
    To=T(d['target_block'][:3],d['target_block'][3:]); Tg=T(d['tf'][:3],d['tf'][3:])
    W.append(To@np.linalg.inv(Tg))
def pred(params,d):
    mx,my,mz,tx,ty,tz=params
    b=d['base']; c,s=np.cos(b[2]),np.sin(b[2])
    base=(b[0]+c*mx-s*my, b[1]+s*mx+c*my, b[2])
    F=fk(d['q'],base,mz); Tt=np.eye(4); Tt[:3,3]=[tx,ty,tz]
    return F@Tt
def res(params):
    r=[]
    for d,Wt in zip(recs,W):
        P=pred(params,d); r.extend(P[:3,3]-Wt[:3,3]); r.extend(0.1*(P[:3,:3]-Wt[:3,:3]).ravel())
    return np.array(r)
sol=least_squares(res,np.zeros(6))
print('params',np.round(sol.x,4),'rms',np.sqrt(np.mean(sol.fun**2)))
for d,Wt in zip(recs,W):
    P=pred(sol.x,d); print(np.round(P[:3,3]-Wt[:3,3],4), round(np.linalg.norm(P[:3,:3]-Wt[:3,:3]),4), np.round(d['base'],3))
