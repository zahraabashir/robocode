from pF_lib import *
import sys
i=1
def push(s,ux,uy):
    for h in (0.08,0.04,0.02,0.01,0.005,0.0025,0.00125):
        for _ in range(60):
            p=pose(s,i); q=step(s,i,h*ux,h*uy)
            if np.allclose(q,p,atol=1e-7): break
    return pose(s,i)
for thr in [float(v) for v in sys.argv[1].split(',')]:
    s=Sim(28); r={}
    go(s,i,-0.6,-1.0); go(s,i,-0.6,-1.0,thr); r['theta']=round(pose(s,i)[2],4)
    r['ymin']=round(push(s,0,-1)[1],5); go(s,i,-0.6,-1.0)
    r['xmin']=round(push(s,-1,0)[0],5); go(s,i,-0.6,-1.0)
    r['xmax(wall?)']=round(push(s,1,0)[0],5); go(s,i,-0.6,-1.0)
    go(s,i,-0.6,1.2); go(s,i,-0.5,1.2)
    r['mound3 bottom y']=round(push(s,0,1)[1],5); go(s,i,-0.5,1.2); go(s,i,-1.1,1.2); ok=go(s,i,-1.1,2.0)
    r['mound3 left x']=round(push(s,1,0)[0],5) if ok else None; go(s,i,-1.1,2.0); go(s,i,-1.104,1.396)
    p=push(s,np.sqrt(.5),np.sqrt(.5)); r['corner(-0.75,1.75) dist']=round(float(np.hypot(p[0]+0.75,p[1]-1.75)),5)
    print('thr',thr,r,flush=True); s.env.close()
