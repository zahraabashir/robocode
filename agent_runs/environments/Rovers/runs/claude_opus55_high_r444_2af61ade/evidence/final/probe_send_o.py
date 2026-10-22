from probe_send_lib import *
e=E(1)
orig=e.step
log=[]
def st(a0=(0,0,0,0),a1=(0,0,0,0)):
    r=orig(a0,a1)
    if r[1] or r[2]: log.append((e.t,r)); print('TERM/TRUNC at',e.t,r)
    return r
e.step=st
def sendtry(k,names):
    for th in [None,0.0,1.57,3.14,-1.57]:
        if th is not None: e.turn(k,th)
        e.act(k,(0,0,0),SEL['send'])
def samp(k,n,off):
    sx,sy=e.g(n,'x'),e.g(n,'y'); print('nav',n,nav(e,k,(sx+off[0],sy+off[1])))
    e.act(k,(0,0,0),SEL['sample']); e.act(k,(0,0,0),SEL['drop']); print(n,e.feats(n))
samp(1,'sample1',(0.15,0))
samp(1,'sample5',(0.15,0))
print('nav',nav(e,1,(-1.4,1.3))); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image']); print('obj1',e.feats('objective1'))
sendtry(1,None); print('after send r1', e.feats('sample1'),e.feats('sample5'),e.feats('objective1'))
print('nav home',nav(e,1,(-1.0,-1.75))); e.turn(1,0.0); print('r1',e.feats('rover1'),'t',e.t)
print('nav',nav(e,0,(1.5,1.4))); e.act(0,(0,0,0),SEL['cal']); e.act(0,(0,0,0),SEL['image']); print('obj0',e.feats('objective0'))
print('nav',nav(e,0,(0.5,-1.5))); sendtry(0,None); print('obj0',e.feats('objective0'))
print('nav home',nav(e,0,(1.0,-1.75))); print('r0',e.feats('rover0'),e.t,e.last)
e.turn(0,3.14159); print('r0',e.feats('rover0'),e.t,e.last)
for i in range(3): e.act(0,(0,0,0),0.0); print(e.t,e.last)
