from env_client import make_env
import numpy as np
env=make_env()
for s in range(0,40):
    obs,info=env.reset(seed=s)
    g=lambda n,f: obs.get(obs.get_object_from_name(n),f)
    names=sorted(obs.get_object_names())
    obst=[n for n in names if n.startswith('obs')]
    print(s, info['object_count'], "reg",round(g('target_region','pose_x'),2),round(g('target_region','pose_y'),2), "blk",round(g('target_block','pose_x'),2),round(g('target_block','pose_y'),2),
      "yaw?",round(g('target_block','pose_qz'),2), "obs",[(round(g(n,'pose_x'),2),round(g(n,'pose_y'),2),round(g(n,'pose_z'),3)) for n in obst])
