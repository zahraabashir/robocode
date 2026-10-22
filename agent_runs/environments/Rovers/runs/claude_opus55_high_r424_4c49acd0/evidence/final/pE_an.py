import json,numpy as np
r=json.load(open('/sandbox/pE_data.json'))
def cr(a,b): return a[0]*b[1]-a[1]*b[0]
out=[]
for x in r:
    sp=np.array(x['sp']); o=np.array(x['obj']); d=o-sp; L=np.linalg.norm(d); u=d/L
    best=None
    for p in x['P']:
        v=np.array(p)-sp; t=v@u; perp=cr(u,v)
        if -0.1<t<L+0.1 and (best is None or abs(perp)<abs(best[1])): best=(t,perp)
    out.append((x['cal'],round(best[1],3),round(best[0],2),round(L,2),round(best[0]/L,2),x['seed'],x['i']))
for o in sorted(out,key=lambda z:abs(z[1])): print(o)
