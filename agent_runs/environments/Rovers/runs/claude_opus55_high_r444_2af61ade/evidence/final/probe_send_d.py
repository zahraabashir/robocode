from probe_send_lib import *
import sys
seed=0; start=(float(sys.argv[1]),float(sys.argv[2])); stepl=float(sys.argv[3]) if len(sys.argv)>3 else 0.02
e=E(seed)
sx,sy=e.g('sample3','x'),e.g('sample3','y')
e.goto(1,sx-0.5,sy); e.goto(1,sx-0.2,sy); e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop'])
print('analyzed',e.feats('sample3'))
for wp in [start]:
    print("nav",wp,nav(e,1,wp),e.pose(1),e.t)
L=np.array([-1.9,-2.0])
p=np.array(e.pose(1)[:2]); dirv=(L-p)/np.linalg.norm(L-p)
for i in range(400):
    p=np.array(e.pose(1)[:2]); d=np.linalg.norm(p-L)
    f0=e.flags(); e.act(1,(0,0,0),SEL['send']); df=diff(f0,e.flags())
    if df: print('SENT at',p,'dist',round(d,4),df); break
    mv=dirv*stepl; e.act(1,(mv[0],mv[1],0))
    if np.linalg.norm(np.array(e.pose(1)[:2])-p)<1e-6: print('blocked at',p,d); break
