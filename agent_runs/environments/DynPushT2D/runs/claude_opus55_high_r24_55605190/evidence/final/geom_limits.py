from env_client import make_env
import numpy as np
env=make_env()
obs,_=env.reset(seed=0)
for a in [[0.0499,0],[0.04999999,0],[0.05,0],[0,0.05],[-0.05,0],[0.035,0.035],[0.049,0.049],[0.0499,0.0499],[-0.0499,-0.0499]]:
    try:
        o,*_=env.step(np.array(a,dtype=float)); print(a,'ok', o[16:18]-obs[16:18]); obs=o
    except Exception as e:
        print(a,'ERR',repr(e)[:300]); env.close(); env=make_env(); obs,_=env.reset(seed=0)
try:
    o,*_=env.step(np.array([0.05,0],dtype=np.float32)); print('f32 ok')
except Exception as e: print('f32 ERR',repr(e)[:200])
