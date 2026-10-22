from probe_send_lib import *
e=E(0)
sx,sy=e.g('sample3','x'),e.g('sample3','y')
e.goto(1,sx-0.5,sy)
e.goto(1,sx-0.4,sy)
# motion+op same step: move 0.2 into range and sample
f0=e.flags(); e.act(1,(0.2,0,0),SEL['sample']); f1=e.flags(); print('move-into-range+sample',e.pose(1),diff(f0,f1))
# sample again with store full
f0=e.flags(); e.act(1,(0,0,0),SEL['sample']); print('sample when full',diff(f0,e.flags()))
f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop',diff(f0,e.flags()))
f0=e.flags(); e.act(1,(0,0,0),SEL['sample']); print('resample same',diff(f0,e.flags()))
f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop',diff(f0,e.flags()))
# move out of range + sample in same step
f0=e.flags(); e.act(1,(-0.2,0,0),SEL['sample']); print('move-out+sample',e.pose(1),diff(f0,e.flags()))
f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop',diff(f0,e.flags()))
# drop with empty store
f0=e.flags(); e.act(1,(0,0,0),SEL['drop']); print('drop empty',diff(f0,e.flags()))
# selector band test: -0.7, -0.95
e.goto(1,sx-0.1,sy)
for v in [-1.0,-0.7,-0.67,-0.66]:
    f0=e.flags(); e.act(1,(0,0,0),v); d=diff(f0,e.flags()); print('sel',v,d!={} and 'sampled')
    e.act(1,(0,0,0),SEL['drop'])
