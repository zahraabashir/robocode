import numpy as np, glob
import push_model as pm
O=[];A=[];O2=[];MT=[]
for f in sorted(glob.glob('data_*.npz')):
    d=np.load(f); O.append(d['O']);A.append(d['A']);O2.append(d['O2']);MT.append(d['META'])
O=np.concatenate(O);A=np.concatenate(A);O2=np.concatenate(O2);MT=np.concatenate(MT)
g=lambda o: pm.geom_from_obs(o)
m=np.where((np.abs(MT[:,3])<0.25))[0]
shown=0; last=None
for i in m:
    key=tuple(MT[i,:5])
    if key!=last:
        if shown>=4: break
        shown+=1; last=key; print('push seed %d edge %d s %.3f ang %.2f sp %.4f'%tuple(MT[i,:5]))
    o,o2=O[i],O2[i]
    d_pre=pm.block_distance(o[0:3],g(o),o[16:18]); d_post=pm.block_distance(o2[0:3],g(o),o2[16:18]); d_mid=pm.block_distance(o[0:3],g(o),o2[16:18])
    print('  k%2d dpre %.4f dnew_oldblock %.4f dpost %.4f  blk move %.4f dth %.4f  a %.4f'%(MT[i,5],d_pre,d_mid,d_post,np.linalg.norm(o2[:2]-o[:2]),o2[2]-o[2],np.linalg.norm(A[i])))
