from probe_vis_lib import *
import probe_vis_lib as L, sys
L.RV=sys.argv[1]; seed=int(sys.argv[2]); N=int(sys.argv[3])
rng=np.random.default_rng(seed*7+len(L.RV))
reset(seed)
objs=[objpos(o.name) for o in L.obs.get_objects(L.T['objective'])]
pills=[np.array([L.obs.get(b,'x'),L.obs.get(b,'y')]) for b in L.obs.get_objects(L.T['obstacle']) if L.obs.get(b,'half_x')<0.1]
def segdist(a,b,p):
    d=b-a; t=np.clip(np.dot(p-a,d)/np.dot(d,d),0,1); return np.linalg.norm(a+t*d-p)
def pred(b,th):
    c=b+np.array([-0.087*np.cos(th)+0.0125*np.sin(th), -0.087*np.sin(th)-0.0125*np.cos(th)])
    res=[]
    for o in objs:
        dist=np.linalg.norm(o[:2]-c)
        rel=abs((np.degrees(np.arctan2(o[1]-c[1],o[0]-c[0])-th)+180)%360-180)
        clr=min(segdist(c,o[:2],p) for p in pills)
        if dist>2.007 or (rel<=95 and clr<0.05): v=0
        elif dist<1.987 and (rel>=100 or clr>=0.09): v=1
        else: v=None
        res.append(v)
    return res
sx=1 if L.RV=='rover0' else -1
goto([(sx*1.0,-1.0)])
stats={'ok':0,'bad':0,'amb':0}
for i in range(N):
    tgt=np.array([sx*rng.uniform(0.3,2.3), rng.uniform(-0.5,1.6)])
    goto([tuple(tgt)]); turn(rng.uniform(-np.pi,np.pi)); p=pos()
    pr=pred(p[:2],p[2]); c=cal()
    if c>0.5: step(op=-1/6)
    if any(v==1 for v in pr): exp=1
    elif all(v==0 for v in pr): exp=0
    else: stats['amb']+=1; continue
    if exp==int(c): stats['ok']+=1
    else: stats['bad']+=1; print('MISMATCH',p.round(3),pr,int(c))
print(stats)
