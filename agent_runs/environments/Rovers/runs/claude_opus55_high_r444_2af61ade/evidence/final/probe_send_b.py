from probe_send_lib import *
e=E(0)
sx,sy=e.g('sample3','x'),e.g('sample3','y'); print('s3',sx,sy)
ok=e.goto(1,sx-0.5,sy); print('reached',ok,e.pose(1),e.t)
for d in [0.40,0.35,0.30,0.28,0.26,0.255,0.25,0.245,0.24,0.22,0.2,0.1,0.0]:
    e.goto(1,sx-d,sy)
    f0=e.flags(); e.act(1,(0,0,0),SEL['sample']); f1=e.flags()
    print(d,e.pose(1),diff(f0,f1))
    if diff(f0,f1): break
