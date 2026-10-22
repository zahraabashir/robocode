from env_client import make_env
import sys,numpy as np
E=make_env();s,i=E.reset(seed=int(sys.argv[1]),options={'object_count':int(sys.argv[2])});o=s.get_object_from_name(sys.argv[3]);pos=lambda o:np.array([s.get(o,'pose_'+f) for f in 'xyz']);p=pos(o)
for x in sorted(s.get_objects(E.observation_space.get_type('Kinematic3DCuboid')),key=lambda x:np.linalg.norm(pos(x)-p)):
 print(x,pos(x).round(4),[round(s.get(x,'half_extent_'+f),4) for f in 'xyz'])
E.close()
