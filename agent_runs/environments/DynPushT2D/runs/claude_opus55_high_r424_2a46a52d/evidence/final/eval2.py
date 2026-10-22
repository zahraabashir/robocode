import numpy as np, glob
import push_model as pm
from eval_model import X,A,Y,moved
for mu in [0.9,1.0,1.1]:
    P=np.array([pm.predict(x,a,mu,0.265) for x,a in zip(X,A)])
    dp=np.linalg.norm(P[:,0:2]-Y[:,0:2],axis=1); dth=np.abs((P[:,2]-Y[:,2]+np.pi)%(2*np.pi)-np.pi)
    print(mu, "pos mean",dp[moved].mean(),"th mean",dth[moved].mean())
P=np.array([pm.predict(x,a,1.0,0.265) for x,a in zip(X,A)])
dp=np.linalg.norm(P[:,0:2]-Y[:,0:2],axis=1)
s=np.linalg.norm(A,axis=1)
rel=dp/np.maximum(np.linalg.norm(Y[:,0:2]-X[:,0:2],axis=1),1e-4)
for lo,hi in [(0,0.01),(0.01,0.02),(0.02,0.035),(0.035,0.08)]:
    m=moved&(s>=lo)&(s<hi); print(f"step {lo}-{hi}: n={m.sum()} pos err mean {dp[m].mean():.2e} rel median {np.median(rel[m]):.3f}")
idx=np.argsort(-dp)[:8]
np.set_printoptions(precision=4,suppress=True,linewidth=200)
for i in idx:
    th=X[i,2]; from push_model import _R
    q=_R(th).T@(X[i,16:18]+A[i]-X[i,0:2])
    print(i, "robot_local_new",q,"a_loc",_R(th).T@A[i],"meas",Y[i,0:3]-X[i,0:3],"pred",P[i]-X[i,0:3], "wlv",X[i,12:15])
