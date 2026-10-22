from probe_motion_lib import *
import math,sys
def probe(seed, i, start, ang, th=None):
    obs,_=env.reset(seed=seed)
    p=goto(i,*start)
    if th is not None:
        for _ in range(20):
            cur=rov(env.step(act(i))[0],i)[2]; d=(th-cur+math.pi)%(2*math.pi)-math.pi
            if abs(d)<1e-4: break
            step(i,0,0,np.clip(d,-.4,.4))
    ux,uy=math.cos(ang),math.sin(ang)
    p=approach(i,ux,uy,steps=(0.1,0.02,0.004,0.001,0.0002))
    return p
mode=sys.argv[1]
if mode=='pillar':
    # seed2 pillar obstacle11 at (0.735,0.444) half .05
    cx,cy=0.735,0.444
    for deg in [0,30,45,60,90,180,225,270]:
        a=math.radians(deg)
        st=(cx-0.5*math.cos(a), cy-0.5*math.sin(a))
        p=probe(2,0,st,a)
        dx,dy=p[0]-cx,p[1]-cy
        # box distance
        bx=max(abs(dx)-0.05,0); by=max(abs(dy)-0.05,0)
        print(f'pillar approach {deg}deg stop ({p[0]:.4f},{p[1]:.4f}) center-dist {math.hypot(dx,dy):.4f} box-dist {math.hypot(bx,by):.4f} gaps {abs(dx)-0.05:.4f},{abs(dy)-0.05:.4f}')
    for th in [0, math.pi/4, math.pi/2]:
        p=probe(2,0,(cx+0.5,cy),math.pi,th); print('theta',round(th,3),'from +x stop x',round(p[0],4),'gap',round(p[0]-cx-0.05,4))
elif mode=='mound':
    # mound obstacle2 (0.5,2.0) half .25 ; approach from below and from right, diag
    cx,cy=0.5,2.0
    for deg,st in [(90,(0.5,1.2)),(180,(1.3,2.0)),(135,(1.2,1.3)),(90,(0.9,1.2)),(90,(0.95,1.2)),(90,(1.0,1.2)),(180,(1.3,2.3))]:
        a=math.radians(deg); p=probe(int(sys.argv[2]),0,st,a)
        dx,dy=p[0]-cx,p[1]-cy; bx=max(abs(dx)-0.25,0); by=max(abs(dy)-0.25,0)
        print(f'mound from {st} dir {deg} stop ({p[0]:.4f},{p[1]:.4f}) box-dist {math.hypot(bx,by):.4f} center-dist {math.hypot(dx,dy):.4f}')
elif mode=='bounds':
    for deg,st in [(0,(1,0)),(90,(1,0)),(270,(1,0)),(180,(-1,0.)),(180,(1,0))]:
        i=1 if st[0]<0 else 0
        p=probe(2,i,st,math.radians(deg)); print('bound dir',deg,'rover',i,np.round(p,4))
elif mode=='lander':
    cx,cy=-1.9,-2.0
    for deg,st in [(180,(-1.0,-2.0)),(180,(-1.0,-1.75)),(270,(-1.9,-1.0)),(270,(-1.7,-1.0)),(225,(-1.2,-1.3)),(180,(-1.0,-2.2))]:
        p=probe(int(sys.argv[2]),1,st,math.radians(deg))
        print(f'lander from {st} dir {deg} stop ({p[0]:.4f},{p[1]:.4f}) center-dist {math.hypot(p[0]-cx,p[1]-cy):.4f}')
