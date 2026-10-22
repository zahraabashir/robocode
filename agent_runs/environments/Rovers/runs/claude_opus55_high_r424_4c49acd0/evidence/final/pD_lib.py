import numpy as np
from pB_lib import Sim, objf, gp
SEED=44
def prep(s0):
    s=Sim(SEED)
    assert gp(s,0,[(1.0,0.7)]),'r0 path'
    s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img'))
    k=[k for k in range(3) if objf(s,k,'have_image_rover0')==1]
    assert k,'noimg'
    s.k=k[0]
    assert gp(s,0,[(s0[0],s0[1])],th=s0[2]),'r0 to S'
    return s
def place1(s,p):
    # move rover1 to p: go via y=-0.3 corridor first
    pts=[(-1.0,-0.6),(p[0],-0.6),(p[0],p[1])] if p[1]>-1.4 or True else [(p[0],p[1])]
    s.goto(1,-1.0,-0.6); s.goto(1,p[0],max(p[1],-0.6) if p[1]>-0.6 else -0.6)
    ok=s.goto(1,p[0],p[1],th=p[2])
    r=s.r(1); return ok and abs(r['x']-p[0])<1e-3 and abs(r['y']-p[1])<1e-3
def send(s):
    s.act(a0=(0,0,0,'send'))
    return objf(s,s.k,'received_image')==1
def trial(args):
    s0,p=args
    s=prep(s0)
    if p is not None:
        if not place1(s,p): return None
    else: s.goto(1,-1.0,-0.3)
    return send(s)
def sensept(s0):
    x,y,th=s0; c,sn=np.cos(th),np.sin(th)
    return np.array([x+c*-0.087-sn*-0.012, y+sn*-0.087+c*-0.012])
L=np.array([-1.9,-2.0])
def pos_on_line(s0,t,off,th=0.0):
    a=sensept(s0); d=L-a; n=np.linalg.norm(d); u=d/n; perp=np.array([-u[1],u[0]])
    q=a+t*d+off*perp; return (float(q[0]),float(q[1]),th)
