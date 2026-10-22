from probe_send_lib import *
e=E(0)
sx,sy=e.g('sample3','x'),e.g('sample3','y')
nav(e,1,(sx-0.2,sy)); 
for th in [3.14159,1.57]:
    e.turn(1,th); e.act(1,(0,0,0),SEL['sample']); print('facing',th,e.feats('rover1'),e.feats('sample3')); e.act(1,(0,0,0),SEL['drop'])
