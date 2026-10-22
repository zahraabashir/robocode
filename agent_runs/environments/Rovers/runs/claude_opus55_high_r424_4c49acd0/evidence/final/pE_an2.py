import json,numpy as np,sys
r=json.load(open('/sandbox/pE_data.json'))
def cr(a,b): return a[0]*b[1]-a[1]*b[0]
for x in r:
    if x['seed'] not in eval(sys.argv[1]): continue
    sp=np.array(x['sp']); o=np.array(x['obj']); d=o-sp; L=np.linalg.norm(d); u=d/L
    near=[(np.round(p,2).tolist(),round(cr(u,np.array(p)-sp),3),round((np.array(p)-sp)@u,2)) for p in x['P'] if abs(cr(u,np.array(p)-sp))<0.15 and -0.2<(np.array(p)-sp)@u<L+0.2]
    print(x['seed'],x['i'],round(x['x'],2),round(x['y'],2),'obj',np.round(o,2).tolist(),'L',round(L,3),'cal',x['cal'],near)
