import sys
from plib import *
seed0=int(sys.argv[1]); nseeds=int(sys.argv[2]); out=sys.argv[3]
rng=np.random.default_rng(seed0)
env=make_env()
O,A,O2,META=[],[],[],[]
def outline(w,Lh,Lv):
    return np.array([(-Lh/2,0),(-Lh/2,-w),(-w/2,-w),(-w/2,-w-Lv),(w/2,-w-Lv),(w/2,-w),(Lh/2,-w),(Lh/2,0)])
for seed in range(seed0,seed0+nseeds):
    obs,_=env.reset(seed=seed); steps=0
    for push in range(8):
        pose=obs[0:3].copy(); w,Lh,Lv=obs[12:15]
        V=outline(w,Lh,Lv); E=np.roll(V,-1,0)-V; L=np.linalg.norm(E,axis=1)
        e=rng.choice(8,p=L/L.sum()); s=rng.uniform(0.01,L[e]-0.01)
        d=E[e]/L[e]; nout=np.array([d[1],-d[0]]); p=V[e]+s*d
        ang=rng.uniform(-0.9,0.9)
        nin=-nout; c,sn=np.cos(ang),np.sin(ang); u=np.array([c*nin[0]-sn*nin[1],sn*nin[0]+c*nin[1]])
        st=to_world(pose,p+nout*(R+0.02)); uw=rot(pose[2])@u
        if st.min()<0.2 or st.max()>4.8: continue
        # skip if block near wall
        if np.min(to_world(pose,V))<0.4 or np.max(to_world(pose,V))>4.6:
            print("wall",seed,flush=True); break
        obs,ok=navigate(env,obs,to_world(pose,p+nout*(R+0.16)))
        if ok: obs=goto(env,obs,st); ok=np.abs(obs[0:3]-pose).max()<1e-7
        if not ok:
            print("navfail",seed,np.linalg.norm(obs[16:18]-st),np.abs(obs[0:3]-pose).max(),flush=True); continue
        sp=rng.uniform(0.01,0.0499)
        for k in range(14):
            a=uw*sp
            o1,*_=env.step(a)
            O.append(obs);A.append(a);O2.append(o1);META.append([seed,e,s,ang,sp,k]); obs=o1
    print(seed,len(O),flush=True)
np.savez(out,O=np.array(O),A=np.array(A),O2=np.array(O2),META=np.array(META))
env.close()
