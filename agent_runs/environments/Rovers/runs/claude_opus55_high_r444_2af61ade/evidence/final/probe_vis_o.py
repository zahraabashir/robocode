from probe_vis_lib import *
import sys, json
seed=int(sys.argv[1]); ri=int(sys.argv[2]); x,y=float(sys.argv[3]),float(sys.argv[4]); path=eval(sys.argv[5]); objn=sys.argv[6]
e=E(seed); print(e.path(ri,path+[(x,y)]), e.rs(ri)['x'], e.rs(ri)['y'])
o=e.objs()[objn]; brg=math.degrees(math.atan2(o['y']-y,o['x']-x))
N=360; res=[]
for k in range(N):
    th=-math.pi+k*2*math.pi/N
    e.turn(ri,th); st=e.rs(ri)
    e.step(ri,0,0,0,'cal'); c=e.rs(ri)['calibrated']; e.step(ri,0,0,0,'img')
    res.append((st['x'],st['y'],st['theta'],int(c)))
s=''.join(str(r[3]) for r in res)
runs=[];cur=s[0];start=0
for i,ch in enumerate(s[1:]+'x',1):
    if ch!=cur: runs.append((cur,round(math.degrees(res[start][2])),round(math.degrees(res[i-1][2])))); cur=ch; start=i
print('bearing to obj %.1f'%brg, runs)
