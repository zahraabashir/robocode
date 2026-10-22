from pm_util import *
import sys
rng=np.random.default_rng(int(sys.argv[1])); N=int(sys.argv[2])
e=E(); X=[];A=[];Y=[]
seeds=[12,13,20,23,24,38,81,96,105,113,121,137,152,162]
for ep in range(N):
    seed=int(rng.choice(seeds)); o=e.reset(seed); w,L,V=o[12:15]
    # pick random point on T boundary
    if rng.random()<0.45:
        px=rng.uniform(-L/2,L/2); side=rng.choice(['top','bot','end'])
        if side=='top': p=np.array([px,0]); n=np.array([0,1.])
        elif side=='bot':
            px=rng.choice([-1,1])*rng.uniform(w/2+0.1,L/2); p=np.array([px,-w]); n=np.array([0,-1.])
        else: s=rng.choice([-1,1]); p=np.array([s*L/2,-rng.uniform(0,w)]); n=np.array([s,0.])
    else:
        side=rng.choice(['stem','bottom'])
        if side=='stem': s=rng.choice([-1,1]); p=np.array([s*w/2,-w-rng.uniform(0.1,V)]); n=np.array([s,0.])
        else: p=np.array([rng.uniform(-w/2,w/2),-w-V]); n=np.array([0,-1.])
    ang=rng.uniform(-1.3,1.3); dl=-(R(ang)@n)
    start=p+n*0.1-dl*rng.uniform(0.05,0.15)
    if np.linalg.norm(start-p)<0.1: continue
    mv=safe_goto_local(e,start)
    if mv>0: continue
    s=rng.uniform(0.003,0.049)
    dw=R(e.obs[2])@dl*s
    for i in range(int(0.25/s)+8):
        o0=e.obs.copy(); a=dw.copy()
        if rng.random()<0.3: a=a+rng.normal(0,0.3*s,2)
        a=np.clip(a,-0.049,0.049)
        o1=e.step(a).copy()
        X.append(o0);A.append(a);Y.append(o1)
np.savez(f"data_{sys.argv[1]}.npz",X=np.array(X),A=np.array(A),Y=np.array(Y))
print(len(X))
