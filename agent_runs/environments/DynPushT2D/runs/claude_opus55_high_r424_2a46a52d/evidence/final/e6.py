from pm_util import *
from geom import com_I
def closest_pt(q,w,L,V):
    rects=[(-L/2,L/2,-w,0),(-w/2,w/2,-w-V,-w)]
    best=None
    for x0,x1,y0,y1 in rects:
        p=np.array([np.clip(q[0],x0,x1),np.clip(q[1],y0,y1)]); dd=np.linalg.norm(q-p)
        if best is None or dd<best[0]: best=(dd,p)
    return best
def stick_pred(pc,ul,c,k2):
    r=pc-c
    K=np.eye(2)+np.array([[r[1]**2,-r[0]*r[1]],[-r[0]*r[1],r[0]**2]])/k2
    J=np.linalg.solve(K,ul); om=(r[0]*J[1]-r[1]*J[0])/k2
    return J+om*np.array([c[1],-c[0]]), om
e=E(); seed=12
o=e.reset(seed); w,L,V=o[12:15]; c,k2=com_I(w,L,V)
for ang in [20,40,50,60]:
  for side in [1]:
    a=np.deg2rad(ang)*side
    d=[np.sin(a),-np.cos(a)]
    mv,obs,act=run_push(e,seed,[0-0.3*d[0],0.3],d,0.01,40)
    print(f"ang {ang*side:+d} navmv={mv:.1e}")
    for i in range(1,41,3):
        b0=obs[i-1][0:3]; b1=obs[i][0:3]
        dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
        rl=R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]); ul=R(b0[2]).T@act
        dist,pc=closest_pt(rl,w,L,V)
        pd,po=stick_pred(pc,ul,c,k2) if dist<0.106 else (np.zeros(2),0)
        print(f"   {i} rob_loc={rl} dist={dist:.4f} meas dl={dl} dth={dth:+.5f} | stick pred dl={pd} dth={po:+.5f}")
