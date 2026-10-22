from pE_lib import *
for seed,i,x,y in [(4,1,-0.9,0.3),(4,1,-1.0,0.6),(2,1,-1.4,0.4),(6,0,1.2,0.1)]:
    s=Sim(seed); drive(s,i,x,y); sp=np.array(sense(s,i)); O=objs(s); P=pillars(s)
    for k,o in enumerate(O):
        o=np.array(o[:2]); d=o-sp; L=np.linalg.norm(d); u=d/L
        if L>2: continue
        pp=[(np.round(p,2).tolist(),round(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]),3)) for p in P if abs(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]))<0.1 and 0<(np.array(p)-sp)@u<L]
        print(seed,i,(x,y),'obj',k,np.round(o,2).tolist(),'L',round(L,2),'u',np.round(u,2).tolist(),pp)
