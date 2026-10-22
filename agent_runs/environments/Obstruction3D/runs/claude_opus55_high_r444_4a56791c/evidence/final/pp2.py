import sys
exec(open('pp1.py').read().split("b=objd(obs,'target_block'); r=")[0])
b=objd(obs,'target_block'); r=objd(obs,'target_region')
print(goto([b['pose_x'],b['pose_y'],0.25]))
for z in [0.14,0.13,0.12,0.11,0.105,0.1,0.095]:
    bl,ok=goto([b['pose_x'],b['pose_y'],z]); print(z,bl)
    if bl: break
R=robot(obs); print('fk tool z', kin.fk(base,getq(obs))[2,3])
a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); pr('closed')
print([round(obs.get(R,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
print(goto([b['pose_x'],b['pose_y'],0.25])); pr('lifted')
tx,ty=0.30,0.0
print(goto([tx,ty,0.25])); pr('moved')
for z in np.arange(0.24,0.05,-0.005):
    bl,ok=goto([tx,ty,z])
    if bl: print('blocked',z); break
pr('lowered')
a=np.zeros(11,dtype=np.float32); a[10]=1; obs,rew,term,*_=env.step(a); pr('release')
print(goto([tx,ty,0.25])); pr('up')
