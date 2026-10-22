import numpy as np
exec(open('probe_base_11.py').read().split("for seed in")[0])
for seed in [1]:
    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot"); o0=objs(obs)
    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
    TB=obs.get_object_from_name("target_block"); tb=np.array([obs.get(TB,"pose_x"),obs.get(TB,"pose_y")])
    rel=tb-base; q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,_=goto(obs,R,q)
    z=0.125
    for zr in np.arange(0.40,z,-0.01):
        q,_=ik(np.array([rel[0]-0.12,rel[1],zr]),q); obs,rj=goto(obs,R,q)
    rejs=[];grasps=[]
    for dy in np.arange(-0.1,0.101,0.025):
        for dx in np.arange(-0.12,0.121,0.01):
            q,_=ik(np.array([rel[0]+dx,rel[1]+dy,z]),q); obs,rj=goto(obs,R,q)
            if rj: rejs.append((round(dx,3),round(dy,3)))
            a=np.zeros(11,np.float32); a[10]=-1; obs,*_=env.step(a)
            if obs.get(R,"grasp_active")>0.5 or obs.get(R,"finger_state")!=0: grasps.append((round(dx,3),round(dy,3),obs.get(R,"finger_state")))
            a[10]=1; obs,*_=env.step(a)
        q,_=ik(np.array([rel[0]-0.12,rel[1]+dy+0.025,z+0.1]),q); obs,_=goto(obs,R,q)
    o=objs(obs)
    print("rejections",len(rejs),rejs[:20]); print("grasps",grasps[:10])
    print("moved:",{k:np.round(o[k]-o0[k],3) for k in o0 if np.abs(o[k]-o0[k]).max()>1e-6})
env.close()
