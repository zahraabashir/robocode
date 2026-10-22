import numpy as np, glob, sys
import push_model as pm
O=[];A=[];O2=[]
for f in sorted(glob.glob('data_*.npz')):
    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2'])
O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2)
rng=np.random.default_rng(0); idx=rng.permutation(len(O)); te=idx[3000:4500]
for ps in sys.argv[1:]:
    params=eval(ps); E=[]
    for i in te:
        o=O[i]; p,rb=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),params)
        dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
        E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt),np.linalg.norm(rb-O2[i,16:18])])
    E=np.array(E)
    print(ps,'pos %.5f p95 %.5f max %.4f th %.5f p95 %.5f max %.4f robot %.6f'%(E[:,0].mean(),np.percentile(E[:,0],95),E[:,0].max(),E[:,1].mean(),np.percentile(E[:,1],95),E[:,1].max(),E[:,2].max()),flush=True)
