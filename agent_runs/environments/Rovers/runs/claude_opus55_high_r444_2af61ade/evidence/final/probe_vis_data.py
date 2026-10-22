from probe_vis_lib import *
import sys, json, time
seed=int(sys.argv[1]); ri=int(sys.argv[2]); objn=sys.argv[3]
path=eval(sys.argv[4]); xs=eval(sys.argv[5]); ys=eval(sys.argv[6]); ths=eval(sys.argv[7]); outf=sys.argv[8]
e=E(seed)
print('path',e.path(ri,path))
data=[]
t0=time.time()
for y in ys:
    for i,x in enumerate(xs if ys.index(y)%2==0 else xs[::-1]):
        ok=e.goto(ri,x,y,tol=1e-7)
        if not ok: continue
        for th in ths:
            e.turn(ri,th); st=e.rs(ri)
            e.step(ri,0,0,0,'cal'); c=e.rs(ri)['calibrated']; e.step(ri,0,0,0,'img')
            data.append((st['x'],st['y'],st['theta'],int(c)))
json.dump({'seed':seed,'obj':objn,'data':data},open(outf,'w'))
print(len(data),time.time()-t0)
