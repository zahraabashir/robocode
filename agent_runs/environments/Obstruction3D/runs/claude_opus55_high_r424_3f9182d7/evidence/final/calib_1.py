from calib_u import *
e=R()
for seed in range(8):
    e.reset(seed); print(seed, 'block',np.round(e.blk(),3),'obst',[np.round(e.blk(n),3) for n in e.obs.get_object_names() if 'obst' in n][:2], 'region', np.round(e.blk('target_region')[:3],3))
e.reset(1)
for g in [1,1,1,-1,-1,-1,-1,0,1]:
    e.stepq(np.zeros(7),g); print(g, e.rob('finger_state'), e.rob('grasp_active'))
