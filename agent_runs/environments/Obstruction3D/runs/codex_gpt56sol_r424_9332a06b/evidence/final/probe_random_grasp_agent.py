import numpy as np
from env_client import make_env

def v(s,n,f): return float(s.get(s.get_object_from_name(n),f))

rng=np.random.default_rng(123)
for seed in range(4):
    env=make_env(); s,info=env.reset(seed=seed)
    names=list(s.get_object_names()); movable=[n for n in names if n!="robot" and n!="target_region"]
    init={n:np.array([v(s,n,"pose_x"),v(s,n,"pose_y"),v(s,n,"pose_z")]) for n in movable}
    tb="target_block"
    best=[]
    for t in range(700):
        a=np.zeros(11,np.float32)
        # Track target y with base. Keep x fixed because forward base is blocked.
        a[1]=np.clip(v(s,tb,"pose_y")-v(s,"robot","pos_base_y"),-.2,.2)
        # Correlated random walk, emphasizing pitch joints, periodic re-randomization.
        if t%12==0:
            u=rng.choice([-1.,0.,1.],size=7,p=[.4,.2,.4])*.18
        a[3:10]=u
        a[10]=-1
        s,r,te,tr,ii=env.step(a)
        moved=max(np.linalg.norm(np.array([v(s,n,"pose_x"),v(s,n,"pose_y"),v(s,n,"pose_z")])-init[n]) for n in movable)
        if moved>.002 and (not best or moved>best[-1][0]+.005):
            best.append((moved,t,[round(v(s,"robot",f"joint_{i}"),3) for i in range(1,8)]))
        held=[n for n in movable if v(s,n,"grasp_active")>.5]
        if v(s,"robot","grasp_active")>.5 or held:
            print("GRASP seed",seed,"t",t,"held",held,"j",[round(v(s,"robot",f"joint_{i}"),5) for i in range(1,8)],"base",v(s,"robot","pos_base_x"),v(s,"robot","pos_base_y"),"tf",[v(s,"robot",f"grasp_tf_{c}") for c in "xyz"])
            break
    else: print("NONE seed",seed,"bestmove",best[-5:])
    env.close()
