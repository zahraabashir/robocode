from pA_lib import P
import numpy as np,sys
seed=int(sys.argv[1])
p=P(seed)
print('pillars near wall:',[(n,round(p.st(n)['x'],2),round(p.st(n)['y'],2)) for n in p.obs.get_object_names() if n.startswith('obstacle') and abs(p.st(n)['x'])<0.6])
crossed=[];unreach=[]
p.goto(1,-0.24,-2.27)
for y in np.arange(-2.27,2.28,0.02):
    st=p.pos(1)
    _,ok=p.mv(1,0,y-st[1])
    if not ok or abs(p.pos(1)[0]+0.24)>1e-3:
        # detour
        p.goto(1,-0.6,st[1]); p.goto(1,-0.6,y); p.goto(1,-0.24,y)
    q=p.pos(1)
    if abs(q[1]-y)>1e-3 or abs(q[0]+0.24)>1e-3: unreach.append(round(y,2)); continue
    _,ok=p.mv(1,0.2,0)
    if ok: crossed.append(round(y,2)); p.mv(1,-0.2,0)
print('crossed at',crossed); print('unreachable',unreach)
