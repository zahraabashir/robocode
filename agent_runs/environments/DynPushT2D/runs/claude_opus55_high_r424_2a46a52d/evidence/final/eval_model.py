import numpy as np, glob, sys
import push_model as pm
D=[np.load(f) for f in sorted(glob.glob("data_*.npz"))]
X=np.concatenate([d['X'] for d in D]);A=np.concatenate([d['A'] for d in D]);Y=np.concatenate([d['Y'] for d in D])
moved=np.abs(Y[:,0:3]-X[:,0:3]).max(1)>1e-9
def ev(mu,c,verbose=False):
    P=np.array([pm.predict(x,a,mu,c) for x,a in zip(X,A)])
    dp=np.linalg.norm(P[:,0:2]-Y[:,0:2],axis=1); dth=np.abs((P[:,2]-Y[:,2]+np.pi)%(2*np.pi)-np.pi)
    mag=np.linalg.norm(Y[:,0:2]-X[:,0:2],axis=1)
    if verbose:
        pm_=np.abs(P[:,0:3]-X[:,0:3]).max(1)>1e-9
        print(f"n={len(X)} moved={moved.sum()} pred-moved={pm_.sum()} contact-mismatch={(pm_!=moved).sum()}")
        print(f"pos err: mean {dp[moved].mean():.2e} p95 {np.percentile(dp[moved],95):.2e} max {dp.max():.2e}; mean |dpos| moved {mag[moved].mean():.2e}")
        print(f"th err: mean {dth[moved].mean():.2e} p95 {np.percentile(dth[moved],95):.2e} max {dth.max():.2e}")
    return dp.mean()+dth.mean()
if len(sys.argv)>1:
    for mu in [1.0,1.3,1.6,2.0,3.0,1e9]:
        print(mu, [round(ev(mu,c)*1e4,3) for c in [0.24,0.265,0.29]])
ev(pm.MU,pm.C_GAP,True)
