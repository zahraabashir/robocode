from env_client import make_env
import numpy as np
env = make_env()
for gap in [0.0, 0.005, 0.01, 0.015, 0.02, 0.03, 0.05]:
    obs, info = env.reset(seed=0)
    R = obs.get_object_from_name('robot'); B = obs.get_object_from_name('target_block')
    def st(a):
        global obs
        obs,*_ = env.step(np.array(a,dtype=np.float32))
    st([0,0,0,0.1,0])
    top = obs.get(B,'y')+obs.get(B,'height'); tx = obs.get(B,'x')+obs.get(B,'width')/2
    gy = top + 0.21 + gap
    for i in range(40):
        st([np.clip(tx-obs.get(R,'x'),-.05,.05), np.clip(gy-obs.get(R,'y'),-.05,.05),0,0,0])
    y0 = obs.get(R,'y')
    st([0,0,0,0,1]); st([0,0.05,0,0,1])
    print(gap, round(y0-0.21-top,4), 'block y', round(obs.get(B,'y'),3))
env.close()
