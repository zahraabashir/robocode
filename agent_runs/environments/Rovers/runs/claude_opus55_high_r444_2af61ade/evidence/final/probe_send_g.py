from probe_send_lib import *
import sys
k=int(sys.argv[1]); tx,ty=float(sys.argv[2]),float(sys.argv[3])
seed=1 if k==0 else 0; sn='sample3'
e=E(seed)
sx,sy=e.g(sn,'x'),e.g(sn,'y')
off=0.15 if k==0 else -0.15
nav(e,k,(sx+off,sy)); e.act(k,(0,0,0),SEL['sample']); e.act(k,(0,0,0),SEL['drop'])
assert e.g(sn,f'analyzed_rover{k}')==1
import os
if os.environ.get("MOVE"): print("moved other",nav(e,1-k,tuple(map(float,os.environ["MOVE"].split(",")))))
ok=nav(e,k,(tx,ty)); L=(-1.9,-2.0)
res=[]
for th in eval(sys.argv[4]) if len(sys.argv)>4 else [None,0.0,1.57,3.14,-1.57]:
    if th is not None: e.turn(k,th)
    e.act(k,(0,0,0),SEL['send'])
    if e.g(sn,'received_analysis')==1: res.append(('SENT',e.pose(k)[2])); break
    res.append(('no',e.pose(k)[2]))
P=e.pose(k)
print(f'rover{k} target {(tx,ty)} reached {ok} pose {P} dist {np.hypot(P[0]-L[0],P[1]-L[1]):.3f}',res)
