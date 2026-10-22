import json,numpy as np
r=json.load(open('/sandbox/pE_data.json'))
def segd(p,a,b):
    d=b-a; t=np.clip(np.dot(p-a,d)/np.dot(d,d),0,1); return np.linalg.norm(a+t*d-p)
best=[]
for ox in np.arange(-0.3,0.31,0.025):
  for oy in np.arange(-0.3,0.31,0.025):
    ms=[]
    for x in r:
        th=np.pi if x['i']==0 else 0.0
        c=np.array([x['x'],x['y']]); org=c+np.array([ox*np.cos(th)-oy*np.sin(th), ox*np.sin(th)+oy*np.cos(th)])
        o=np.array(x['obj']); ms.append(min(segd(np.array(p),org,o) for p in x['P']))
    ms=np.array(ms); cal=np.array([x['cal'] for x in r])
    for rad in np.arange(0.03,0.09,0.005):
        err=np.sum((ms>rad)!=(cal>0.5)); best.append((err,round(ox,3),round(oy,3),round(rad,3)))
best.sort(); print(best[:15], len(r))
