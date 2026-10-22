from pF_lib import *
import sys, json
seed=int(sys.argv[1]); px,py=[float(v) for v in sys.argv[2].split(',')]; ths=[float(v) for v in sys.argv[3].split(',')]
i=0; th0=np.pi; R0=0.6
dirs=[(np.cos(a),np.sin(a)) for a in np.arange(8)*np.pi/4]   # side where rover sits, ccw from +x
def approach2(s,ux,uy):
    for h in (0.08,0.04,0.02,0.01,0.005,0.0025,0.00125):
        for _ in range(40):
            p=pose(s,i); q=step(s,i,-h*ux,-h*uy)
            if np.allclose(q,p,atol=1e-7): break
    p=pose(s,i); return float(np.hypot(p[0]-px,p[1]-py))
out={}
for thr in ths:
    s=Sim(seed); res=[]
    # go to first start point (below pillar = dir index 6) then rotate
    order=[6,7,0,1,2,3,4,5]
    ux,uy=dirs[6]; ok=go(s,i,px+R0*ux,py+R0*uy); ok2=go(s,i,px+R0*ux,py+R0*uy,th0+thr)
    th=pose(s,i)[2]
    for k in order:
        ux,uy=dirs[k]
        if not go(s,i,px+R0*ux,py+R0*uy): res.append(None); print('noreach',thr,k); continue
        d=approach2(s,ux,uy); res.append(round(d,5))
        go(s,i,px+R0*ux,py+R0*uy)
    out[thr]=dict(order=order,d=res,theta=float(th))
    print(thr, 'theta',round(th,4), ok,ok2, dict(zip(['-y','-y+x','+x','+x+y','+y','+y-x','-x','-x-y'],res)),flush=True)
    s.env.close()
json.dump(out,open('pF_out_%s.json'%sys.argv[4],'w'))
