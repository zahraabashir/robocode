import numpy as np
from approach import geometry, _wrap
D=np.load("term_data.npy"); term=D[:,-1]>0.5
def pt(o, local):
    c,s=np.cos(o[2]),np.sin(o[2]); return o[0:2]+np.array([c*local[0]-s*local[1], s*local[0]+c*local[1]])
for name in ["ref","com","barcenter","bbox"]:
    ok=[]
    for o in D:
        rects,com,k2=geometry(o); w,L,V=o[12],o[13],o[14]
        loc={"ref":(0,0),"com":tuple(com),"barcenter":(0,-w/2),"bbox":(0,-(w+V)/2)}[name]
        p=pt(o[0:3],loc); g=pt(o[29:32],loc)
        e=np.abs(p-g); et=abs(_wrap(o[2]-o[31]))
        ok.append((e[0]<0.03)&(e[1]<0.03)&(et<np.deg2rad(8)))
    ok=np.array(ok)
    print(name, "agree", (ok==term).mean(), "pred_T_actual_F", (ok&~term).sum(), "pred_F_actual_T", (~ok&term).sum(), "nterm", term.sum())
E=np.stack([np.abs(D[:,0]-D[:,29]),np.abs(D[:,1]-D[:,30]),np.abs(_wrap(D[:,2]-D[:,31]))],1)
okref=(E[:,0]<0.03)&(E[:,1]<0.03)&(E[:,2]<np.deg2rad(8))
print("terminated errs max", E[term].max(0), "\n", np.round(E[term][:10],4))
print("ref-ok not term errs min", E[okref&~term].min(0)); print(np.round(E[okref&~term][::20],4))
