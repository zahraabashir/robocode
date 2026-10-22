from probe_send_lib import *
e=E(1)
sx,sy=e.g('sample3','x'),e.g('sample3','y')
print('nav',nav(e,0,(sx+0.15,sy)),e.pose(0))
f0=e.flags(); e.act(0,(0,0,0),SEL['sample']); print(diff(f0,e.flags()))
e.act(0,(0,0,0),SEL['drop'])
L=np.array([-1.9,-2.0])
pts=[(0.24,y) for y in np.arange(-2.25,1.6,0.25)]+[(x,-2.25) for x in (0.5,1.0)]+[(x,-1.0) for x in (0.5,1.0,1.5)]
pts.sort(key=lambda p:np.hypot(p[0]-L[0],p[1]-L[1]))
for p in pts:
    ok=nav(e,0,p)
    f0=e.flags(); e.act(0,(0,0,0),SEL['send'])
    for th in (0.0,1.57,3.14,-1.57):
        e.turn(0,th); e.act(0,(0,0,0),SEL['send'])
    df=diff(f0,e.flags())
    print(p,ok,e.pose(0),round(np.hypot(e.pose(0)[0]-L[0],e.pose(0)[1]-L[1]),3),'SENT' if any(k.startswith('sample') for k in df) else '')
print(e.t)
