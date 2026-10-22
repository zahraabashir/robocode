from probe_col_lib import R
import numpy as np, sys
def approach(r,i,target,tol=1e-4):
    step=0.2
    while step>tol:
        p=r.pos(i)[:2]; d=np.array(target)-p; n=np.linalg.norm(d)
        if n<1e-6: break
        s=min(step,n); q=r.step(i,*(d/n*s))[:2]
        if np.allclose(q,p,atol=1e-9): step/=2
    return r.pos(i)
def rot(r,i,tot):
    while abs(tot)>1e-9:
        d=np.clip(tot,-0.4,0.4); r.step(i,0,0,d); tot-=d
if __name__=="__main__":
     for dth in [0,0.4,np.pi/4,np.pi/2,1.0]:
        r=R(0)
        rot(r,0,dth); rot(r,1,dth)
        out=[]
        r.goto(0,1.0,-1.5); out.append(approach(r,0,(3,-1.5))[0]); r.goto(0,1.0,-1.5)
        out.append(approach(r,0,(1.0,-3))[1]); r.goto(0,1.0,-1.5)
        out.append(approach(r,0,(-1,-1.5))[0]); r.goto(0,1.0,-1.5)
        # rover1: avoid lander; go to (-1,-1.2)
        r.goto(1,-1.0,-1.2); out.append(approach(r,1,(1,-1.2))[0]); r.goto(1,-1.0,-1.2)
        out.append(approach(r,1,(-3,-1.2))[0]); r.goto(1,-1.0,-1.2)
        print('dth %.3f th0 %.3f'%(dth,r.pos(0)[2]),'r0 maxx %.4f miny %.4f minx %.4f | r1 maxx %.4f minx %.4f'%tuple(out))
        r.env.close()
