import numpy as np, pickle
from scipy.optimize import least_squares
data=pickle.load(open('dyn_fitdata.pkl','rb'))
data=[d for i,d in enumerate(data) if i!=10]
def pred(params,cp,u):
    xc,yc,c2=params
    rx,ry=cp[0]-xc,cp[1]-yc
    A=np.array([[1+ry**2/c2,-rx*ry/c2],[-rx*ry/c2,1+rx**2/c2]])
    f=np.linalg.solve(A,u)
    w=(rx*f[1]-ry*f[0])/c2
    return np.array([f[0]+w*yc, f[1]-w*xc, w])
def res(p): return np.concatenate([pred(p,cp,u)-tw for cp,u,tw in data])*1000
for fix in [None]:
    r=least_squares(res,[0,-0.3,0.2]); print('fit xc,yc,c2',r.x,'rms(1e-3)',np.sqrt(np.mean(r.fun**2)))
    for cp,u,tw in data: print(cp.round(3),u,tw,pred(r.x,cp,u).round(5))
