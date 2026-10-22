import numpy as np, glob, sys
from scipy.optimize import minimize
import push_model as pm
O=[];A=[];O2=[]
for f in sorted(glob.glob('data_*.npz')):
    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2'])
O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2)
dpos=np.linalg.norm(O2[:,0:2]-O[:,0:2],axis=1); dth=np.abs(O2[:,2]-O[:,2])
print('N',len(O),'moved',(dpos>1e-7).sum())
# robot tracking
rerr=O2[:,16:18]-O[:,16:18]-A; print('robot track err max',np.abs(rerr).max(),'mean',np.abs(rerr).mean())
# block near walls? use polygon
ok=np.array([pm.t_polygon_world(o[0:3],pm.geom_from_obs(o)).min()>0.05 and pm.t_polygon_world(o2[0:3],pm.geom_from_obs(o)).max()<4.95 for o,o2 in zip(O,O2)])
print('not near wall',ok.sum())
rng=np.random.default_rng(0)
idx=np.where(ok)[0]; rng.shuffle(idx)
tr=idx[:int(sys.argv[1]) if len(sys.argv)>1 else 1500]; te=idx[3000:]
def errs(params,ids):
    E=[]
    for i in ids:
        o=O[i]; p,_=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),params)
        dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
        E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt)])
    return np.array(E)
def loss(x,nsub):
    params=dict(cx=x[0],cy=x[1],k2=abs(x[2])+1e-3,mu=abs(x[3]),nsub=nsub,r_eff=x[4])
    E=errs(params,tr); return np.mean(E[:,0]**2+(0.4*E[:,1])**2)
for nsub in [1,4]:
    x0=np.array([0,-0.35,0.12,0.3,0.1])
    r=minimize(loss,x0,args=(nsub,),method='Nelder-Mead',options=dict(maxfev=400,xatol=1e-4,fatol=1e-10))
    print(nsub,r.x,r.fun)
    params=dict(cx=r.x[0],cy=r.x[1],k2=abs(r.x[2])+1e-3,mu=abs(r.x[3]),nsub=nsub,r_eff=r.x[4])
    E=errs(params,te[:2000]); mv=np.array([dpos[i]>1e-7 for i in te[:2000]])
    print(' test pos err mean %.5f p95 %.5f  th err mean %.5f p95 %.5f; moved-only pos %.5f'%(E[:,0].mean(),np.percentile(E[:,0],95),E[:,1].mean(),np.percentile(E[:,1],95),E[mv,0].mean()))
    print(' baseline (no motion) pos %.5f th %.5f'%(dpos[te[:2000]].mean(),dth[te[:2000]].mean()),flush=True)
