import numpy as np, glob
import push_model as pm
O=[];A=[];O2=[];MT=[]
for f in sorted(glob.glob('data_*.npz')):
    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2']);MT.append(d['META'])
O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2);MT=np.concatenate(MT)
P=dict(mu=0.99,r_eff=0.1015,beta=0.22,nsub=4)
E=[]
for i in range(len(O)):
    o=O[i]; p,_=pm.predict_step(o[0:3],o[16:18],A[i],pm.geom_from_obs(o),P)
    dt=(p[2]-O2[i,2]+np.pi)%(2*np.pi)-np.pi
    E.append([np.linalg.norm(p[:2]-O2[i,:2]),abs(dt)])
E=np.array(E); np.save('E_all.npy',E)
print('ALL N=%d pos mean %.5f p50 %.5f p95 %.5f p99 %.5f | th mean %.5f p95 %.5f p99 %.5f'%(len(E),E[:,0].mean(),np.median(E[:,0]),*np.percentile(E[:,0],[95,99]),E[:,1].mean(),*np.percentile(E[:,1],[95,99])))
for i in np.argsort(-E[:,0])[:12]:
    o=O[i]; g=pm.geom_from_obs(o); pl=pm.to_local if hasattr(pm,'to_local') else None
    poly=pm.t_polygon_world(o[0:3],g)
    rl=(o[16:18]-o[:2])@pm._rot(o[2])
    print('i%d err %.4f th %.4f meta %s rob_local %s dpre %.4f blkminmax %.2f %.2f true move %.4f %.4f'%(i,E[i,0],E[i,1],np.round(MT[i],3),np.round(rl,3),pm.block_distance(o[0:3],g,o[16:18]),poly.min(),poly.max(),np.linalg.norm(O2[i,:2]-o[:2]),O2[i,2]-o[2]))
