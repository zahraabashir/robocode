from dyn_lib import *
from dyn_model import *
rng=np.random.default_rng(0)
errs1=[];errsN=[]
for trial in range(12):
    seed=int(rng.integers(0,100)); e=E(seed)
    ang=rng.uniform(0,2*np.pi); tgt_b=np.array([0,-0.4])+0.9*np.array([np.cos(ang),np.sin(ang)])
    e.goto_safe(tgt_b)
    o=e.obs; g=geom(o[12],o[13],o[14])
    pose0=o[0:3].copy(); pb0=o[16:18].copy(); poseN=pose0.copy(); pbN=pb0.copy()
    cw=to_world(o,[0,-0.4]); 
    moved=0
    for k in range(40):
        d=cw-e.obs[16:18]; d=d/np.linalg.norm(d)*0.04 + rng.normal(0,0.01,2)
        d=np.clip(d,-0.049,0.049)
        ob=e.obs.copy()
        p1,_=sim_step(g,ob[0:3],ob[16:18],d)
        poseN,pbN=sim_step(g,poseN,pbN,d)
        o2=e.step(d)
        if np.linalg.norm(o2[0:3]-ob[0:3])>1e-6: moved+=1; errs1.append(np.r_[p1[0:2]-o2[0:2],p1[2]-o2[2]])
    errN=np.r_[poseN[0:2]-e.obs[0:2],poseN[2]-e.obs[2]]
    print(f'trial {trial} seed {seed} moved_steps {moved} open-loop final err pos {np.linalg.norm(errN[:2]):.4f} th {errN[2]:.4f}  total disp {np.linalg.norm(e.obs[0:2]-pose0[0:2]):.3f} dth {e.obs[2]-pose0[2]:.3f}')
E1=np.array(errs1); print('1-step err (contact steps): pos rms',np.sqrt((E1[:,:2]**2).sum(1).mean()),'max',np.sqrt((E1[:,:2]**2).sum(1)).max(),'th rms',np.sqrt((E1[:,2]**2).mean()),'max',np.abs(E1[:,2]).max())
