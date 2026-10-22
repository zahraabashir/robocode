from probe_occ_lib import *
from concurrent.futures import ThreadPoolExecutor
import sys
L=np.array((-1.9,-2.0))
def camp(P0,th=math.pi):
    c,s=math.cos(th),math.sin(th); return np.array((P0[0]-0.087*c+0.0125*s, P0[1]-0.087*s-0.0125*c))
def point(P0,x,sd):
    C=camp(P0); d=L-C; d/=np.linalg.norm(d); n=np.array((-d[1],d[0]))  # cross(d,n)>0
    t=(x-C[0])/(L[0]-C[0]); base=C+t*(L-C)
    q=base+sd*n
    # sign convention: cross(L-C, q-C) = sd*|..| >0 -> check
    return (round(float(q[0]),4),round(float(q[1]),4))
def test(job):
    P0,x,sd,h=job; Q=point(P0,x,sd)
    e,err=setup(44,P0,math.pi,Q,h)
    if err: e.env.close(); return job,Q,err
    e.step((0,0,0,SEL['send']),(0,0,0,0)); ok=e.feats('sample5')[6]>0.5; e.env.close()
    return job,Q,int(ok)
if __name__=='__main__':
    P=(0.6,-0.35); jobs=[]
    jobs+=[(P,-0.3,round(s,3),math.pi/4) for s in np.arange(0.03,0.26,0.02)]
    jobs+=[(P,-0.6,round(-s,3),math.pi/4) for s in np.arange(0.05,0.26,0.02)]
    jobs+=[(P,-0.45,round(s,3),0.0) for s in np.arange(-0.25,0.26,0.025)]
    jobs+=[(P,-1.0,round(sg*s,3),0.0) for s in np.arange(0.15,0.26,0.02) for sg in (1,-1)]
    with ThreadPoolExecutor(12) as ex:
        for r in ex.map(test,jobs): print(r,flush=True)
