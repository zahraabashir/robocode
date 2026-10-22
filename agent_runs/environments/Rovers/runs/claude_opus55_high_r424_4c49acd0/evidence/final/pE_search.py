from pE_lib import *
import sys
for seed in range(0,12):
    s=Sim(seed); O=objs(s); P=pillars(s)
    for i in (0,1):
        th=s.r(i)['theta']; A=[];B=[]
        for x in np.arange(0.3,2.3,0.1):
            for y in np.arange(-2.0,2.2,0.1):
                X=x if i==0 else -x
                if min([np.hypot(X-p[0],y-p[1]) for p in P])<0.3: continue
                sp=(X-0.087*np.cos(th)+0.012*np.sin(th), y-0.087*np.sin(th)-0.012*np.cos(th))
                d=[np.hypot(o[0]-sp[0],o[1]-sp[1]) for o in O]
                m=[min(segd(p,sp,o[:2]) for p in P) for o in O]
                inr=[k for k in range(len(O)) if d[k]<1.93]; outr=[k for k in range(len(O)) if d[k]>2.07]
                if len(inr)+len(outr)<len(O): continue
                if inr and all(m[k]<0.03 for k in inr): A.append((round(X,2),round(y,2),inr))
                near=int(np.argmin(d))
                if near in outr and any(m[k]>0.12 for k in inr): B.append((round(X,2),round(y,2),near,inr))
        print(seed,i,'A',A[:4],'B',B[:3])
