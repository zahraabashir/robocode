from probe_ops_lib import *
reset(1)
def push(i,dx,dy,n=200):
    for k in range(n):
        x,y=pos(i)[:2]; step(i,dx,dy)
        if math.hypot(pos(i)[0]-x,pos(i)[1]-y)<1e-6: break
    return [round(v,3) for v in pos(i)[:2]]
print('down',push(1,0,-0.05)); print('left',push(1,-0.05,0))
print('right', push(1,0.05,0))
for yy in [-1.0,-0.5,0,0.5,1.0,1.5,2.0,2.5]:
    p=pos(1); 
    push(1,-0.05,0,n=4)
    for k in range(60):
        y=pos(1)[1]
        if y>=yy: break
        step(1,0,min(0.1,yy-y)); 
    print('y',round(pos(1)[1],2),'right',push(1,0.05,0))
print('up',push(1,0,0.05))
