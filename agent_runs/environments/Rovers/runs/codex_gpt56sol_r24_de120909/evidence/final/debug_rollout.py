import sys
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); s,info=env.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0)
ap=GeneratedApproach(env.action_space,env.observation_space,env.make_primitives()); ap.reset(s,info)
for step in range(160):
    if step < 25 or step%10==0:
        vals=[]
        for i,n in enumerate(ap.names):
            r=s.get_object_from_name(n); p=(s.get(r,"x"),s.get(r,"y"))
            vals.append((i,tuple(round(x,2) for x in p),ap._choose_task(s,i,p),len(ap.paths[i]),ap.stalls[i]))
        ots=env.observation_space.get_type("objective")
        imgs=[(o.name,int(s.get(o,"have_image_rover0")),int(s.get(o,"have_image_rover1")),int(s.get(o,"received_image"))) for o in s.get_objects(ots)]
        print(step,vals,imgs)
    s,r,t,tr,inf=env.step(ap.get_action(s))
    if t or tr: print("END",step+1,t,tr);break
env.close()
