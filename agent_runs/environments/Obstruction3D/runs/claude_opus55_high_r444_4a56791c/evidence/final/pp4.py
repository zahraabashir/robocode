import sys
exec(open('pp1.py').read().split("b=objd(obs,'target_block'); r=")[0])
b=objd(obs,'target_block')
R=robot(obs)
hz=b['half_extent_z']
goto([b['pose_x'],b['pose_y'],0.25]); goto([b['pose_x'],b['pose_y'],b['pose_z']+0.03])
a=np.zeros(11,dtype=np.float32); a[10]=-1; obs,*_=env.step(a); print('grasp',obs.get(R,'grasp_active'))
tx,ty=0.30,0.0
goto([tx,ty,0.25])
for h in [0.04,0.02,0.01,0.005,0.002,0.0,-0.002]:
    bl,ok=goto([tx,ty,0.075+hz+h+0.03]); b2=objd(obs,'target_block')
    a=np.zeros(11,dtype=np.float32); a[10]=1; obs,*_=env.step(a)
    b3=objd(obs,'target_block')
    print(h, bl, 'held at', np.round([b2['pose_x'],b2['pose_y'],b2['pose_z']],4), 'after open grasp', obs.get(R,'grasp_active'), np.round([b3['pose_x'],b3['pose_y'],b3['pose_z']],4))
    if not obs.get(R,'grasp_active'): break
