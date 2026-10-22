from pE_lib import *
for seed in range(0,30):
    s0=Sim(seed); O=objs(s0); P=pillars(s0)
    for i in (0,1):
        th=s0.r(i)['theta']; C=[]
        for x in np.arange(0.3,2.3,0.1):
            for y in np.arange(-1.0,1.8,0.1):
                X=x if i==0 else -x
                if min([np.hypot(X-p[0],y-p[1]) for p in P])<0.3: continue
                sp=np.array((X-0.087*np.cos(th), y-0.087*np.sin(th)-0.012*np.cos(th)))
                d=[np.hypot(o[0]-sp[0],o[1]-sp[1]) for o in O]
                m=[min(segd(p,sp,o[:2]) for p in P) for o in O]
                inr=[k for k in range(len(O)) if d[k]<1.9 and m[k]>0.1]
                if len(inr)>=2 and all(d[k]>2.1 or k in inr for k in range(len(O))):
                    near=min(inr,key=lambda k:d[k])
                    C.append((round(X,1),round(y,1),inr,near,round(abs(d[inr[0]]-d[inr[1]]),2)))
        C=[c for c in C if c[4]>0.15]
        if C: print(seed,i,len(C),[c for c in C if c[3]!=c[2][0]][:2],[c for c in C if c[3]==c[2][0]][:2])
