from env_client import make_env
from approach import GeneratedApproach
import sys
e=make_env();s,i=e.reset(seed=int(sys.argv[1]),options={'object_count':int(sys.argv[2])});p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,i)
for t in range(200):
 s,r,d,tr,i=e.step(p.get_action(s))
 if d:break
print('done',d,'step',t+1,'phase',p.phase,'obj',p.obj,flush=True)
print('robot',[s.get(p.robot,f) for f in ['x','y','arm_joint']],flush=True)
for o in s.get_objects(p.ot):print(o.name,p.rect(s,o),flush=True)
print({k:v for k,v in p.__dict__.items() if k in ['destx','target_grasp','offsetx','offsety','dropx','dropy','emptyheight','carryheight','pick_y']},flush=True)
e.close()
