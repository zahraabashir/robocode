import sys
exec(open('pp1.py').read().split("b=objd(obs,'target_block'); r=")[0])
b=objd(obs,'target_block')
R=robot(obs)
for z in np.arange(0.16,0.10,-0.005):
    goto([b['pose_x'],b['pose_y'],0.25]); bl,ok=goto([b['pose_x'],b['pose_y'],z])
    a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a)
    print(round(z,3), bl, obs.get(R,'grasp_active'), round(obs.get(R,'finger_state'),3), [round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z']])
    a[10]=1; obs,*_=env.step(a); 
    if obs.get(R,'grasp_active'): print('release failed at grasp height')
    b2=objd(obs,'target_block'); print('   block after', np.round([b2['pose_x'],b2['pose_y'],b2['pose_z']],4))
