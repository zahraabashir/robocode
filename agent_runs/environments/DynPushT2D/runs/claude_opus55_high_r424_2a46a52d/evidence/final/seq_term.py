import numpy as np
from approach import Model, _wrap
D=np.load("term_data.npy"); term=D[:,-1]>0.5
E=np.stack([np.abs(D[:,0]-D[:,29]),np.abs(D[:,1]-D[:,30]),np.abs(_wrap(D[:,2]-D[:,31]))],1)
okref=(E[:,0]<0.03)&(E[:,1]<0.03)&(E[:,2]<np.deg2rad(8))
# episode boundaries: goal change
ep=np.concatenate([[0],np.cumsum(np.any(np.abs(np.diff(D[:,29:32],axis=0))>1e-9,axis=1))])
for e in range(8):
    idx=np.where(ep==e)[0]
    first=idx[okref[idx]]
    if len(first)==0: continue
    i0=first[0]
    for i in range(max(idx[0],i0-2), min(idx[-1]+1, i0+6)):
        m=Model(D[i]); d=m.world_dist(D[i][None,0:2],np.array([D[i][2]]),D[i][None,16:18])[0]
        print(e,i-idx[0],np.round(E[i],4),okref[i],term[i],"robdist %.3f"%d, "blkmove", np.round(D[i,0:3]-D[i-1,0:3],4))
    print()
print("stuck candidates")
for e in range(ep.max()+1):
    idx=np.where(ep==e)[0]
    if not term[idx].any():
        i=idx[-1]; print(e, D[i,0:3], D[i,29:32])
# raw theta check
raw=np.abs(D[:,2]-D[:,31])
prev_ok=np.concatenate([[False],okref[:-1]])
print("term & raw>8deg:", (term & (np.concatenate([[9],raw[:-1]])>np.deg2rad(8))).sum())
