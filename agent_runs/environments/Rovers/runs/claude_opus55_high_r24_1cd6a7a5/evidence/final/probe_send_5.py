from probe_send_lib import *
reset(21)
def straight(tx,ty,n=40):
    for _ in range(n):
        x,y=pos(0)[:2]; dx=max(-.2,min(.2,tx-x)); dy=max(-.2,min(.2,ty-y))
        if abs(dx)+abs(dy)<1e-4: break
        step(0,dx,dy)
for y in [-2.6,-2.45,-2.3,-2.1,-1.95,-1.8,0,2.5]:
    straight(0.5,y); a=[round(v,3) for v in pos(0)[:2]]; straight(-0.5,y,10); print(y,a,[round(v,3) for v in pos(0)[:2]])
