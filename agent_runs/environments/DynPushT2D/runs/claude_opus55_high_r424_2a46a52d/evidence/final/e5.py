from pm_util import *
from geom import com_I
e=E(); seed=12
o=e.reset(seed); w,L,V=o[12:15]; c,k2=com_I(w,L,V); print("com",c,"k2",k2)
rows=[]
for name,p,d in [("top x=.3",[0.3,0.25],[0,-1]),("top x=-.45",[-0.45,0.25],[0,-1]),("barbot x=.4",[0.4,-0.35],[0,1]),("stem side y=-.6",[0.25,-0.6],[-1,0]),("stem side y=-1.1",[0.25,-1.1],[-1,0]),("stem side y=-.3",[-0.25,-0.3],[1,0]),("bar end",[0.8,-0.05],[-1,0])]:
    mv,obs,a=run_push(e,seed,p,d,0.01,25)
    i=len(obs)-1; b0=obs[i-1][0:3]; b1=obs[i][0:3]
    dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
    rl=R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]); ul=R(b0[2]).T@a
    # sticking model: contact pt p (robot center projected ~) ; solve for impulse with unit mass
    for tag,pc in [("robotctr",rl),("surface",rl-0.0926*np.asarray(d,float)*-1*-1 if False else rl+0.0926*np.asarray(d,float)/np.linalg.norm(d))]:
        r=pc-c
        K=np.eye(2)+np.array([[r[1]**2,-r[0]*r[1]],[-r[0]*r[1],r[0]**2]])/k2
        J=np.linalg.solve(K,ul); vc=J; om=(r[0]*J[1]-r[1]*J[0])/k2
        vref=vc+om*np.array([c[1],-c[0]])*-1  # v_ref = v_com + om x (ref-com) ; ref-com=-c ; om x v = om*(-vy,vx)
        vref=vc+om*np.array([c[1],-c[0]])
        print(f"{name:16s} {tag:8s} meas dl={dl} dth={dth:+.5f} | pred dl={vref} dth={om:+.5f}  navmv={mv:.1e}")
