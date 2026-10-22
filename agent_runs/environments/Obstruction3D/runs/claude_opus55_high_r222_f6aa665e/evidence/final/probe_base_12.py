import numpy as np, sys
sys.argv=['x']
exec(open('probe_base_11.py').read().split("for seed in")[0])
for seed in [1,0]:
    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot"); o0=objs(obs)
    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
    TB=obs.get_object_from_name("target_block"); tb=np.array([obs.get(TB,"pose_x"),obs.get(TB,"pose_y")])
    rel=tb-base; q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,_=goto(obs,R,q)
    for zr in np.arange(0.40,0.105,-0.01):
        q,_=ik(np.array([rel[0],rel[1],zr]),q); obs,rj=goto(obs,R,q)
    # scan xy offsets at this height for grasp
    a=np.zeros(11,np.float32); a[10]=-1
    obs,*_=env.step(a); print("seed",seed,"close at block: finger",obs.get(R,"finger_state"),"grasp",obs.get(R,"grasp_active"), "TB grasp",obs.get(TB,"grasp_active"))
    for zr in np.arange(0.11,0.3,0.02):
        q,_=ik(np.array([rel[0],rel[1],zr]),q); obs,rj=goto(obs,R,q)
    o=objs(obs); print(" after lift moved:",{k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6})
env.close()
