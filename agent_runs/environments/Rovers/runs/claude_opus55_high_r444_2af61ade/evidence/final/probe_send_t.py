from probe_send_lib import *
e=E(27)
orig=e.step
def st(a0=(0,0,0,0),a1=(0,0,0,0)):
    r=orig(a0,a1)
    if r[1] or r[2]: print('TERM/TRUNC at',e.t,r)
    return r
e.step=st
s5=(e.g('sample5','x'),e.g('sample5','y'))
nav(e,1,(s5[0]-0.15,s5[1]-0.1)); e.act(1,(0,0,0),SEL['sample']); e.act(1,(0,0,0),SEL['drop'])
o=e.objs('objective')[0]
nav(e,1,(-1.4,1.3)); e.act(1,(0,0,0),SEL['cal']); e.act(1,(0,0,0),SEL['image'])
e.turn(1,1.0); e.act(1,(0,0,0),SEL['send'])
nav(e,1,(-1.0,-1.75)); e.turn(1,0.0); print('r1 home',e.feats('rover1'))
s1=(e.g('sample1','x'),e.g('sample1','y')); print('s1',s1)
print(nav(e,0,(s1[0]+0.15,s1[1]))); e.act(0,(0,0,0),SEL['sample']); print(e.feats('sample1'),e.feats('rover0'))
nav(e,0,(0.5,-1.5)); e.turn(0,0.0); e.act(0,(0,0,0),SEL['send']); print('sent',e.feats('sample1'))
nav(e,0,(1.0,-1.75)); e.turn(0,np.pi); print('home w/ full store',e.feats('rover0'),e.last)
e.act(0,(0,0,0),SEL['drop']); print('after drop',e.feats('rover0'),e.last)
