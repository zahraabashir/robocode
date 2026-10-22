from env_client import make_env
import numpy as np, approach
env = make_env()
obs, info = env.reset(seed=7)
ap = approach.GeneratedApproach(env.action_space, env.observation_space, None)
ap.reset(obs, info)
for i in range(32):
    a = ap.get_action(obs); obs,*_ = env.step(a)
R = obs.get_object_from_name('robot')
for n in obs.get_object_names():
    o=obs.get_object_from_name(n)
    print(n, [round(float(obs.get(o,f)),3) for f in (['x','y','arm_joint','theta'] if n=='robot' else ['x','y','width','height'])])
import copy
for a in [[0,-0.026,0,0,1],[0.024,0,0,0,1],[0,-0.01,0,0,1],[0,-0.02,0,0,1],[0,0,0,0.0,0]]:
    o2,*_ = env.step(np.array(a,dtype=np.float32))
    print(a, [round(float(o2.get(R,f)),3) for f in ['x','y','arm_joint','vacuum']])
print('---')
o2,*_ = env.step(np.array([0,0,0,0,1],dtype=np.float32))
for a in [[0,0.004,0,0,1],[0.024,0,0,0,1],[0.024,0,0,0,1],[0.05,0,0,0,1],[0,0.03,0,0,1],[0.05,0,0,0,1]]:
    o2,*_ = env.step(np.array(a,dtype=np.float32))
    B=o2.get_object_from_name('obstruction0')
    print(a, [round(float(o2.get(R,f)),3) for f in ['x','y','arm_joint','vacuum']], round(float(o2.get(B,'x')),3), round(float(o2.get(B,'y')),3))
