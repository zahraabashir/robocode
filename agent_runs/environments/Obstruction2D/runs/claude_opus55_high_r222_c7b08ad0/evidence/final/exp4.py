from env_client import make_env
import numpy as np
env = make_env()
for off in [0.0, 0.02, 0.03, 0.034, 0.04]:
    obs, info = env.reset(seed=0)
    R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
    def st(a):
        global obs
        obs,*_ = env.step(np.array(a,dtype=np.float32))
    st([0,0,0,0.1,0])
    top = obs.get(B,'y')+obs.get(B,'height'); tx = obs.get(B,'x') - off
    gy = top + 0.21 + 0.002
    for i in range(40):
        st([np.clip(tx-obs.get(R,'x'),-.05,.05), np.clip(gy-obs.get(R,'y'),-.05,.05),0,0,0])
    st([0,0,0,0,1]); st([0,0.05,0,0,1])
    print(off, 'block y', round(obs.get(B,'y'),3), round(obs.get(R,'y')-gy,3))
env.close()
