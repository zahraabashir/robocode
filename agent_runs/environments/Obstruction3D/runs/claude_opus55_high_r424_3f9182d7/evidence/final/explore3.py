from env_client import make_env
import numpy as np, kin, sys
F = ['joint_%d'%i for i in range(1,8)]
env = make_env()
obs, info = env.reset(seed=1)
r = obs.get_object_from_name('robot'); tb=obs.get_object_from_name('target_block')
def getq(o): return np.array([o.get(r,f) for f in F])
base=(obs.get(r,'pos_base_x'),obs.get(r,'pos_base_y'),obs.get(r,'pos_base_rot'))
q=getq(obs)
def step(a):
    global obs,q
    obs,_,_,_,_=env.step(np.array(a,dtype=np.float32)); q=getq(obs)
def goto(pos, yaw):
    global obs,q
    qt,ok=kin.ik(base,q,np.array(pos),kin.down_R(yaw))
    if not ok: print("ik fail",pos); return False
    while True:
        d=qt-q
        if np.max(np.abs(d))<1e-6: return True
        d=np.clip(d,-0.19,0.19)
        a=np.zeros(11); a[3:10]=d
        q0=q.copy(); step(a)
        if np.allclose(q0,q): print("rejected at", kin.fk(base,q)[:3,3]); return False
bx,by,bz=[obs.get(tb,f) for f in ['pose_x','pose_y','pose_z']]
hx,hy=obs.get(tb,'half_extent_x'),obs.get(tb,'half_extent_y')
print("block",bx,by,bz,hx,hy)
off=float(sys.argv[1]); yaw=float(sys.argv[2])
step([0]*10+[1])
goto([bx,by,bz+0.25],yaw)
for zz in np.arange(bz+0.25,bz+off-1e-9,-0.01):
    if not goto([bx,by,zz],yaw): break
goto([bx,by,bz+off],yaw)
print("ee",kin.fk(base,q)[:3,3], "finger",obs.get(r,'finger_state'))
for i in range(3):
    step([0]*10+[-1])
    print("after close: finger",obs.get(r,'finger_state'),"grasp",obs.get(r,'grasp_active'),obs.get(tb,'grasp_active'),
      [round(obs.get(r,f),4) for f in ['grasp_tf_x','grasp_tf_y','grasp_tf_z','grasp_tf_qx','grasp_tf_qy','grasp_tf_qz','grasp_tf_qw']])
goto([bx,by,bz+0.25],yaw)
print("block now",[round(obs.get(tb,f),4) for f in ['pose_x','pose_y','pose_z','pose_qx','pose_qy','pose_qz','pose_qw']])
M=kin.fk(base,q); print("ee",M[:3,3]); 
env.close()
