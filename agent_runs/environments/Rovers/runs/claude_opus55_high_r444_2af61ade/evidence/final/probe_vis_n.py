from probe_vis_lib import *
import sys, json
e=E(4)
x,y=float(sys.argv[1]),float(sys.argv[2]); N=int(sys.argv[3])
e.path(1,[(-1.0,-1.0),(-1.0,y),(x,y)])
res=[]
for k in range(N):
    th=-math.pi+k*2*math.pi/N
    e.turn(1,th); st=e.rs(1)
    e.step(1,0,0,0,'cal'); c=e.rs(1)['calibrated']; e.step(1,0,0,0,'img')
    res.append((st['x'],st['y'],st['theta'],int(c)))
json.dump(res,open('probe_vis_n_%s_%s.json'%(sys.argv[1],sys.argv[2]),'w'))
s=''.join(str(r[3]) for r in res)
# print runs
runs=[];cur=s[0];start=0
for i,ch in enumerate(s[1:]+'x',1):
    if ch!=cur: runs.append((cur,round(math.degrees(res[start][2]),1),round(math.degrees(res[i-1][2]),1))); cur=ch; start=i
print(x,y,runs)
