from env_client import make_env
from approach import GeneratedApproach
import numpy as np
import time,json,argparse
P=argparse.ArgumentParser();P.add_argument('--start',type=int,default=0);P.add_argument('--n',type=int,default=100);P.add_argument('--count',type=int);P.add_argument('--out',default='stats.json');a=P.parse_args();out=[]
for seed in range(a.start,a.start+a.n):
 e=make_env();s,info=e.reset(seed=seed,options={'object_count':a.count} if a.count else None);ap=GeneratedApproach(e.action_space,e.observation_space,{});st=time.time();ap.reset(s,info);tm=time.time()-st
 bad=[0,0,0];ops=[0,0,0,0,0];success=False
 for t in range(200):
  st=time.time();act=ap.get_action(s);tm+=time.time()-st
  s2,_,done,trunc,_=e.step(act)
  for r in range(2):
   op=act[4*r+3];rob=ap.rovers[r]
   if np.linalg.norm(act[4*r:4*r+2])>.01 and np.linalg.norm(ap.xy(s,rob)-ap.xy(s2,rob))<1e-6:bad[0]+=1
   if abs(op+.5)<1e-4:
    ops[0]+=1
    if s2.get(rob,'calibrated')<.5:bad[1]+=1
   if abs(op+.166666)<1e-4:ops[1]+=1
   if abs(op-.5)<1e-4:
    ops[2]+=1
    if ap.pending(s2,r):bad[2]+=1
   if abs(op+.83333)<1e-4:ops[3]+=1
   if abs(op-.83333)<1e-4:ops[4]+=1
  s=s2
  if done or trunc:success=done;break
 rec={'seed':seed,'n':info.get('object_count'),'success':success,'steps':t+1,'time':round(tm,3),'bad':bad,'ops':ops};out.append(rec)
 if not success or seed%10==0:print(rec,flush=True)
 e.close()
open(a.out,'w').write(json.dumps(out))
print('SUMMARY',sum(r['success'] for r in out),len(out),'mean',np.mean([r['steps'] for r in out]),'max_time',max(r['time'] for r in out),flush=True)
