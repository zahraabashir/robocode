import numpy as np, glob, sys
import push_model as pm
O=[];A=[];O2=[];MT=[]
for f in sorted(glob.glob('data_*.npz')):
    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2']);MT.append(d['META'])
O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2);MT=np.concatenate(MT)
rng=np.random.default_rng(1); idx=rng.choice(len(O),1500,replace=False)
params=eval(sys.argv[1]) if len(sys.argv)>1 else None
E=[]
for i in idx:
    o=O[i]; p,_=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),params)
    dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
    E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt),np.linalg.norm(O2[i,:2]-o[:2]),abs(O2[i,2]-o[2])])
E=np.array(E); M=MT[idx]
print('all: pos %.5f th %.5f | motion pos %.5f th %.5f'%tuple(E.mean(0)))
for k in [0,1,2,5,13]:
    m=M[:,5]==k; print(' k=%d pos %.5f th %.5f | mot %.5f %.5f'%((k,)+tuple(E[m].mean(0))))
for e in range(8):
    m=M[:,1]==e; print(' edge=%d pos %.5f th %.5f | mot %.5f %.5f'%((e,)+tuple(E[m].mean(0))))
for lo,hi in [(0,0.3),(0.3,0.6),(0.6,0.9)]:
    m=(np.abs(M[:,3])>=lo)&(np.abs(M[:,3])<hi); print(' |ang| %.1f-%.1f pos %.5f th %.5f | mot %.5f %.5f'%((lo,hi)+tuple(E[m].mean(0))))
