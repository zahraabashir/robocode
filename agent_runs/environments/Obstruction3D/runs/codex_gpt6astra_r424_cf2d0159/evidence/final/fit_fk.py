import json
import numpy as np
from scipy.spatial.transform import Rotation as R
from probe_fk import fk,origins
samples=json.load(open('fk_samples.json'));A=[];y=[]
for s in samples:
 q=s['q'];rb=R.from_euler('z',s['base'][2]).as_matrix();ree=R.from_quat(s['obj'][3:]).as_matrix()@R.from_quat(s['tf'][3:]).as_matrix().T;p=rb.T@(np.array(s['obj'][:3])-ree@s['tf'][:3]-np.r_[s['base'][:2],0]);rot=np.eye(3);cols=[]
 for a,(v,r) in zip(q,origins):
  cols.append(rot);rot=rot@R.from_euler('xyz',r).as_matrix()@R.from_euler('z',a).as_matrix()
 cols.append(fk(q)[1]);A.append(np.hstack(cols));y.append(p-fk(q)[0])
A=np.vstack(A);y=np.ravel(y);v,res,rank,sv=np.linalg.lstsq(A,y,rcond=1e-7)
print('N',len(samples),'rank',rank,'residual max',np.max(abs(A@v-y)),'rms',np.sqrt(np.mean((A@v-y)**2)))
print('offsets',v.reshape(-1,3));print('sv',sv)
json.dump(v.reshape(-1,3).tolist(),open('fk_corrections.json','w'))
