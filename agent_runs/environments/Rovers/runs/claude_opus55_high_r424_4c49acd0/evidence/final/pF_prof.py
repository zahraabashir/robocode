from pF_lib import *
import sys, json
seed=28; px,py=0.9779,-0.9694; i=0; th0=np.pi; R0=0.6
thr=float(sys.argv[1]); ang=float(sys.argv[2]); tag=sys.argv[3]
offs=np.round(np.arange(-0.35,0.3501,0.025),4)
ux,uy=np.cos(ang),np.sin(ang); vx,vy=-uy,ux
s=Sim(seed)
def P(a,e): return px+a*ux+e*vx, py+a*uy+e*vy
go(s,i,*P(R0,offs[0])); go(s,i,*P(R0,offs[0]),th0+thr); print('theta',pose(s,i)[2])
res=[]
for e in offs:
    if not go(s,i,*P(R0,e)): res.append(None); continue
    hit=False
    for h in (0.08,0.04,0.02,0.01,0.005,0.0025,0.00125):
        for _ in range(40):
            p=pose(s,i); along=(p[0]-px)*ux+(p[1]-py)*uy
            if along-h < -0.05 and not hit: break
            q=step(s,i,-h*ux,-h*uy)
            if np.allclose(q,p,atol=1e-7): hit=True; break
    p=pose(s,i); along=(p[0]-px)*ux+(p[1]-py)*uy
    res.append(round(along,5) if hit else None)
    go(s,i,*P(R0,e))
print(tag,'thr',thr,'ang',ang, list(zip(offs.tolist(),res)),flush=True)
json.dump(dict(thr=thr,ang=ang,offs=offs.tolist(),res=res),open('pF_prof_%s.json'%tag,'w'))
