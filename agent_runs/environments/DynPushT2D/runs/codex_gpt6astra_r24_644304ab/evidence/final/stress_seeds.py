from env_client import make_env
import numpy as np
import json

def clearance(s,offset):
    p=s[offset:offset+2]; angle=s[offset+2]; w,h,v=s[12:15]
    pts=np.array([[-h/2,0],[h/2,0],[-h/2,-w],[h/2,-w],[-w/2,-w-v],[w/2,-w-v]])
    co,si=np.cos(angle),np.sin(angle); world=pts@np.array([[co,si],[-si,co]])+p
    return min(world.min(),5-world.max())
e=make_env(); rows=[]
for seed in range(2000,4000):
    s,_=e.reset(seed=seed)
    co,si=np.cos(s[2]),np.sin(s[2]); r=(s[16:18]-s[:2])@np.array([[co,-si],[si,co]])
    w,h,v=s[12:15]
    collision=(abs(r[0])<h/2+.1 and -w-.1<r[1]<.1) or (abs(r[0])<w/2+.1 and -w-v-.1<r[1]<-w+.1)
    rows.append((seed,clearance(s,0),clearance(s,29),collision))
e.close()
chosen=sorted(set([r[0] for r in sorted(rows,key=lambda r:r[1])[:30]]+[r[0] for r in sorted(rows,key=lambda r:r[2])[:30]]+[r[0] for r in rows if r[3]][:20]))
with open('stress_seeds.json','w') as f:json.dump(chosen,f)
print(' '.join(map(str,chosen)))
print('minimum initial/goal clearance',min(r[1] for r in rows),min(r[2] for r in rows))
