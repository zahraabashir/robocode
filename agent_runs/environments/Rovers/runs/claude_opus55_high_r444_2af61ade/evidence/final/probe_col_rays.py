from probe_col_lib import R
import numpy as np, sys
c=np.array([0.654,-0.199]); RAD=0.42
def approach(r,i,target,tol=1e-4):
    step=0.2
    while step>tol:
        p=r.pos(i)[:2]; d=target-p; n=np.linalg.norm(d)
        if n<1e-6: break
        s=min(step,n); q=r.step(i,*(d/n*s))[:2]
        if np.allclose(q,p,atol=1e-9): step/=2
    return r.pos(i)
def run(dths,label):
    r=R(0)
    r.path(0,[(1.0,-1.0),(c[0]+RAD,c[1])])
    for d in dths: r.step(0,0,0,d)
    th=r.pos(0)[2]
    res=[]
    for k in range(0,72):
        a=np.deg2rad(k*5)
        S=c+RAD*np.array([np.cos(a),np.sin(a)])
        if not r.goto(0,*S): print('nav fail',k,r.pos(0)); break
        p=approach(r,0,c)
        rel=p[:2]-c
        res.append((k*5,rel[0],rel[1]))
        r.goto(0,*S)
    print(label,'theta=%.4f'%th)
    for a,x,y in res: print('%3d %.4f %.4f  r=%.4f'%(a,x,y,np.hypot(x,y)))
    r.env.close()
mode=sys.argv[1]
if mode=='0': run([],'th=pi')
if mode=='1': run([0.4],'th=pi+0.4')
if mode=='2': run([0.4,0.4,0.4,0.37079633],'th=pi/2 ish')
