from probe_vis_lib import *
import sys
e=E(4)
x,y=float(sys.argv[1]),float(sys.argv[2]); N=int(sys.argv[3])
print(e.path(1,[(-1.0,-1.0),(-1.0,y),(x,y)]), e.rs(1))
s=''
blocked=[]
for k in range(N):
    th=-math.pi+k*2*math.pi/N
    e.turn(1,th)
    st=e.rs(1)
    if abs((st['theta']-th+math.pi)%(2*math.pi)-math.pi)>1e-3: s+='?'; continue
    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
    s+=str(int(c))
    if not c: blocked.append(round(math.degrees(th),1))
print(s); print(blocked)
