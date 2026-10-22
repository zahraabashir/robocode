import numpy as np, glob, sys
from scipy.optimize import minimize
import push_model as pm
O=[];A=[];O2=[]
for f in sorted(glob.glob('data_*.npz')):
    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2'])
O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2)
rng=np.random.default_rng(0); idx=rng.permutation(len(O)); tr=idx[:700]; te=idx[3000:5000]
def errs(fn,ids):
    E=[]
    for i in ids:
        o=O[i]; g=pm.geom_from_obs(o); p,_=pm.predict_step(o[0:3],o[16:18],A[i],g,fn(g))
        dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
        E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt)])
    return np.array(E)
def mk(x,nsub,full):
    def fn(g):
        c,k2=pm.mass_props(g)
        d=dict(mu=abs(x[0]),r_eff=x[1],beta=x[2],nsub=nsub)
        if full: d.update(cx=0.0,cy=c[1]+x[3],k2=k2*abs(x[4]))
        return d
    return fn
for full in [0,1]:
  for nsub in [1,4]:
    x0=np.array([1.0,0.1,0.25]+([0,1.0] if full else []))
    loss=lambda x: np.mean((lambda E: E[:,0]**2+(0.4*E[:,1])**2)(errs(mk(x,nsub,full),tr)))
    r=minimize(loss,x0,method='Nelder-Mead',options=dict(maxfev=300 if not full else 500,xatol=1e-4,fatol=1e-11))
    E=errs(mk(r.x,nsub,full),te)
    print('full',full,'nsub',nsub,np.round(r.x,4),'test pos mean %.5f p95 %.5f th mean %.5f p95 %.5f'%(E[:,0].mean(),np.percentile(E[:,0],95),E[:,1].mean(),np.percentile(E[:,1],95)),flush=True)
