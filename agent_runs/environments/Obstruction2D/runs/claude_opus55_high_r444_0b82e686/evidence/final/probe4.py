from env_client import make_env
import numpy as np
env = make_env()
def rb(o):
    r=o.get_object_from_name('robot'); return [float(o.get(r,f)) for f in ["x","y","arm_joint","vacuum"]]
def blk(o,n='target_block'):
    b=o.get_object_from_name(n); return [round(float(o.get(b,f)),4) for f in ["x","y"]]
for mode in ["vac_during","vac_on_last","none"]:
    obs,_=env.reset(seed=0)
    def st(a):
        global obs
        obs,*_=env.step(np.array(a,dtype=np.float32))
    v = 1.0 if mode=="vac_during" else 0.0
    st([0.05,0,0,0.1,v])
    for _ in range(20): st([np.clip(0.4896-rb(obs)[0],-.05,.05),0,0,0,v])
    ty=0.17254292219877243+0.21+2e-4
    for _ in range(20):
        d=np.clip(ty-rb(obs)[1],-.05,.05); last=abs(d)<0.05
        st([0,d,0,0,1.0 if (mode=="vac_during" or (last and mode!="none")) else 0])
    print(mode, np.round(rb(obs),4), blk(obs))
    st([0.05,0.05,0,0,1.0]); print(" after move", np.round(rb(obs),4), blk(obs))
    st([-0.05,0,0,0,0.0]); print(" release+move", np.round(rb(obs),4), blk(obs))
env.close()
