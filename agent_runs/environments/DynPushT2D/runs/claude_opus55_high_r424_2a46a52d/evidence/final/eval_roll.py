import numpy as np, push_model as pm
from eval_model import X,A,Y,moved
# segments
segs=[];cur=[0]
for i in range(1,len(X)):
    if np.allclose(X[i],Y[i-1]): cur.append(i)
    else: segs.append(cur);cur=[i]
segs.append(cur)
E=[];ET=[];M=[]
for sg in segs:
    x=X[sg[0]].copy()
    for i in sg:
        x[16:18]=X[i,16:18]; x[0:3]=pm.predict(x,A[i])
    E.append(np.linalg.norm(x[0:2]-Y[sg[-1],0:2])); ET.append(abs((x[2]-Y[sg[-1],2]+np.pi)%(2*np.pi)-np.pi))
    M.append(np.linalg.norm(Y[sg[-1],0:2]-X[sg[0],0:2]))
E=np.array(E);ET=np.array(ET);M=np.array(M)
print(f"{len(segs)} open-loop rollouts (~{len(X)/len(segs):.0f} steps): block travel mean {M.mean():.3f}; final pos err mean {E.mean():.4f} median {np.median(E):.4f} p90 {np.percentile(E,90):.4f}; theta err mean {ET.mean():.4f} median {np.median(ET):.4f}")
