from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=1)
R = obs.get_object_from_name('robot')
def rs(o): return tuple(round(float(o.get(R,f)),3) for f in ['x','y','theta','arm_joint','vacuum'])
def run(a,n):
    global obs
    for i in range(n):
        p=rs(obs); obs,*_ = env.step(np.array(a,dtype=np.float32))
        if rs(obs)==p: break
    print(a, rs(obs))
run([0,0.05,0,0,0],20)
run([-0.05,0,0,0,0],30)
run([0,0,0,0.1,0],3)
run([0,-0.05,0,0,0],30)
run([0,-0.01,0,0,0],30)
run([0,0,0,-0.1,0],3)
run([0,-0.01,0,0,0],30)
run([0.05,0,0,0,0],60)
