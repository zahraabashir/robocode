from probe_send_lib import *
e=E(27)
orig=e.step
def st(a0=(0,0,0,0),a1=(0,0,0,0)):
    r=orig(a0,a1)
    if r[1] or r[2]: print('TERM/TRUNC at',e.t,r)
    return r
e.step=st
sx,sy=e.g('sample0','x'),e.g('sample0','y')
nav(e,1,(sx+0.4,sy+0.2))
for ang in np.linspace(-1.5,1.5,13):
    e.goto(1,sx+0.4*np.cos(ang),sy+0.4*np.sin(ang))
    for rr in (0.3,0.24,0.2,0.15,0.1):
        e.goto(1,sx+rr*np.cos(ang),sy+rr*np.sin(ang),maxit=5)
    P=e.pose(1); d=np.hypot(P[0]-sx,P[1]-sy)
    if d<0.245: print('reached',P,'d',d); break
e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop']); print(e.feats('sample0'))
print('lander-rover dist',np.hypot(P[0]+1.9,P[1]+2.0))
s5=(e.g('sample5','x'),e.g('sample5','y'))
nav(e,1,(s5[0]-0.15,s5[1]-0.1)); e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop'])
o=e.objs('objective')[0]
nav(e,1,(-1.4,1.3)); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image'])
e.turn(1,1.0); e.act(1,(0,0,0),SEL['send']); print(e.feats('sample0'),e.feats('sample5'),e.feats(o))
print('nav home',nav(e,1,(-1.0,-1.75)), e.pose(1), e.last)
for th in [0.6,0.5,0.45,0.42,0.4,0.0]:
    e.turn(1,th); print(th,e.pose(1),e.g('rover1','at_home'),e.last[1])
