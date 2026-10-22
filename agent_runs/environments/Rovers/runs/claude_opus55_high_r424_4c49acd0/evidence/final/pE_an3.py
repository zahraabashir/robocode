import json,numpy as np
r=json.load(open('/sandbox/pE_data.json'))
for x in r:
    sp=np.array(x['sp']); o=np.array(x['obj']); d=o-sp; L=np.linalg.norm(d); u=d/L
    th=np.pi if x['i']==0 else 0
    lx=np.cos(th)*u[0]+np.sin(th)*u[1]; ly=-np.sin(th)*u[0]+np.cos(th)*u[1]
    m=min(((abs(u[0]*(p[1]-sp[1])-u[1]*(p[0]-sp[0]))),(np.array(p)-sp)@u) for p in x['P'] if 0<(np.array(p)-sp)@u<L)
    if m[0]<0.045: print(x['seed'],x['i'],'cal',x['cal'],'u_world',np.round(u,2),'local',round(lx,2),round(ly,2),'perp',round(m[0],3))
