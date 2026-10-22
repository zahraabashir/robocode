from pE_lib import *
import json,random
random.seed(0); rows=[]
for seed in range(0,20):
    s0=Sim(seed); O=objs(s0); P=pillars(s0)
    for i in (0,1):
        th=s0.r(i)['theta']; cands=[]
        for x in np.arange(0.2,2.3,0.05):
            for y in np.arange(-2.0,2.2,0.05):
                X=x if i==0 else -x
                if min([np.hypot(X-p[0],y-p[1]) for p in P])<0.3: continue
                sp=(X-0.087*np.cos(th)+0.012*np.sin(th), y-0.087*np.sin(th)-0.012*np.cos(th))
                d=[np.hypot(o[0]-sp[0],o[1]-sp[1]) for o in O]
                inr=[k for k in range(len(O)) if d[k]<1.95]
                if len(inr)!=1 or sum(dd<2.05 for dd in d)!=1: continue
                k=inr[0]; m=[(segd(p,sp,O[k][:2]),p) for p in P]; mm,pp=min(m)
                if mm<0.12: cands.append((X,y,k))
        random.shuffle(cands)
        for X,y,k in cands[:6]:
            s=Sim(seed)
            if not drive(s,i,X,y): continue
            sp=sense(s,i); act1(s,i,'cal'); c=s.r(i)['calibrated']
            rows.append(dict(seed=seed,i=i,x=X,y=y,sp=sp,obj=O[k][:2],P=P,cal=c))
            print(seed,i,round(X,2),round(y,2),k,c,flush=True)
json.dump(rows,open('pE_data.json','w'))
