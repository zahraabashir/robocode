import numpy as np
for m in '012':
    L=[l.split() for l in open(f'probe_col_rays_{m}.txt').read().splitlines()[1:]]
    d=[]
    for a,x,y,_ in L:
        x,y=float(x),float(y)
        cx,cy=np.clip(x,-.05,.05),np.clip(y,-.05,.05); d.append((np.hypot(x-cx,y-cy),int(a)))
    d=np.array(d); print(m,'dbox min %.4f max %.4f'%(d[:,0].min(),d[:,0].max()), 'argmax ang',d[d[:,0].argmax(),1],'argmin',d[d[:,0].argmin(),1])
