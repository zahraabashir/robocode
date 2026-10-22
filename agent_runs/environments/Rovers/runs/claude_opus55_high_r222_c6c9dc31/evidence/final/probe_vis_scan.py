from probe_vis_util import *
for seed in range(0,60):
    obs,_=env.reset(seed=seed)
    O=[(o.name,float(obs.get(o,'x')),float(obs.get(o,'y'))) for o in objs(obs,'objective')]
    P=[(o.name,float(obs.get(o,'x')),float(obs.get(o,'y'))) for o in objs(obs,'obstacle') if float(obs.get(o,'half_x'))<0.1]
    for on,ox,oy in O:
        for pn,px,py in P:
            v=np.array([px-ox,py-oy]); n=np.linalg.norm(v)
            if n>1.4 or np.sign(px)!=np.sign(ox): continue
            q=np.array([ox,oy])+v/n*(n+0.3)
            if abs(q[0])<0.3 or abs(q[0])>2.3 or abs(q[1])>2.3 or np.sign(q[0])!=np.sign(ox): continue
            # not near other pillars
            if min(math.hypot(q[0]-a,q[1]-b) for _,a,b in P)<0.28: continue
            if any(abs(q[0]-mx)<0.47 and abs(q[1]-2)<0.47 for mx in (-2,-0.5,0.5,2)): continue
            print(seed,on,(round(ox,2),round(oy,2)),pn,(round(px,2),round(py,2)),'n=%.2f'%n,'q',q.round(2))
