from probe_send_lib import *
e=E(27)
orig=e.step
def st(a0=(0,0,0,0),a1=(0,0,0,0)):
    r=orig(a0,a1)
    if r[1] or r[2]: print('TERM/TRUNC at',e.t,r)
    return r
e.step=st
def samp(k,n,off):
    sx,sy=e.g(n,'x'),e.g(n,'y'); print('nav',n,nav(e,k,(sx+off[0],sy+off[1])))
    e.act(k,(0,0,0),SEL['sample']); e.act(k,(0,0,0),SEL['drop']); print(n,e.feats(n))
samp(1,'sample0',(0.15,0.1))
samp(1,'sample5',(-0.15,-0.1))
o=e.objs('objective')[0]
print('nav',nav(e,1,(-1.4,1.3))); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image']); print(o,e.feats(o))
e.turn(1,1.0)  # face away from lander
e.act(1,(0,0,0),SEL['send']); print('ONE send:',e.feats('sample0'),e.feats('sample5'),e.feats(o))
print('nav home',nav(e,1,(-1.0,-1.75)), e.pose(1), e.last)
e.turn(1,0.0); print(e.pose(1),e.feats('rover0'),e.last)
