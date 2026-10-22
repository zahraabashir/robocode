import numpy as np, math, sys
from env_client import make_env
from approach import Block, GeneratedApproach
env=make_env()
G=GeneratedApproach(None,None,None); G.reset(None,None)
def rotv(v,a):
    c,s=math.cos(a),math.sin(a); return np.array([c*v[0]-s*v[1], s*v[0]+c*v[1]])
def step(d):
    global obs
    d=np.clip(d,-0.0499,0.0499); obs,_,_,_,_=env.step(d); return obs
def goto(target_local, tol=0.003, n=300):
    global obs
    for _ in range(n):
        B=Block(obs); rp=obs[16:18]; tg=B.to_world(target_local)
        if np.linalg.norm(tg-rp)<tol: return True
        wp=G.nav_step(B,rp,tg); d=wp-rp; nd=np.linalg.norm(d)
        if nd>0.045: d=d/nd*0.045
        step(d)
    return False
def trial(seed, face, alpha_deg, track=False, nsteps=15, spd=0.03):
    global obs
    obs,info=env.reset(seed=seed)
    B=Block(obs); w,yc=B.w,B.yc
    if face=='top': cl=np.array([0,0.0]); n_loc=np.array([0,-1.0]); off=np.array([0,1.0])
    else: cl=np.array([-w/2,yc]); n_loc=np.array([1.0,0]); off=np.array([-1.0,0])
    goto(cl+off*0.16)
    # final approach to contact
    for _ in range(8):
        B=Block(obs); d=B.to_world(cl+off*0.1)-obs[16:18]; nd=np.linalg.norm(d); step(d if nd<0.03 else d/nd*0.03)
    B0=Block(obs); r0=obs[16:18].copy(); lr0=B0.to_local(r0)
    a=math.radians(alpha_deg)
    dw=B0.dir_world(rotv(n_loc,a))
    for k in range(nsteps):
        if track:
            B=Block(obs); dcur=B.dir_world(rotv(n_loc,a))  # desired dir fixed in world -> use dw
            tgt=B.to_world(cl+off*0.1)+dw*spd
            step(tgt-obs[16:18])
        else:
            step(dw*spd)
    B1=Block(obs); r1=obs[16:18]
    rd=r1-r0; bd=B1.p-B0.p
    # COM displacement
    c0=B0.to_world((0,B0.yc)); c1=B1.to_world((0,B1.yc)); cd=c1-c0
    ang=lambda v: math.degrees(math.atan2(v[1],v[0]))
    wrap=lambda x:(x+180)%360-180
    lr1=B1.to_local(r1); dth=wrap(math.degrees(B1.th-B0.th))
    print(f"{face:4s} a={alpha_deg:3d} trk={int(track)} robot|d|={np.linalg.norm(rd):.3f} dir_r-cmd={wrap(ang(rd)-ang(dw)):6.1f} "
          f"COMdisp={np.linalg.norm(cd):.3f} COMdir-cmd={wrap(ang(cd)-ang(dw)):6.1f} dth={dth:6.2f}deg rot/dist={dth/max(np.linalg.norm(rd),1e-6):6.1f}deg/u "
          f"contact_local {lr0.round(3)}->{lr1.round(3)} gap={B1.dist(r1):.3f}")
seed=int(sys.argv[1]) if len(sys.argv)>1 else 0
obs,_=env.reset(seed=seed); print('block',obs[0:3].round(2),'w,Lh,Lv',obs[12:15].round(3),'robot',obs[16:18].round(2))
for a in [0,10,20,30,45]: trial(seed,'top',a)
for a in [0,15,30,-15,-30]: trial(seed,'stem',a)
for a in [0,10,20,30,45]: trial(seed,'top',a,track=True)
