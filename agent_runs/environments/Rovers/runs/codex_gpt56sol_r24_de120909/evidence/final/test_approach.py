import sys
from env_client import make_env
from approach import GeneratedApproach

seeds = [int(x) for x in sys.argv[1:]] or list(range(10))
for seed in seeds:
    env=make_env(); s,info=env.reset(seed=seed)
    ap=GeneratedApproach(env.action_space,env.observation_space,env.make_primitives())
    ap.reset(s,info)
    term=trunc=False
    for step in range(env.max_steps):
        s,r,term,trunc,inf=env.step(ap.get_action(s))
        if term or trunc: break
    rovers=[]
    rt=env.observation_space.get_type("rover")
    for o in s.get_objects(rt):
        rovers.append((o.name,round(s.get(o,"x"),2),round(s.get(o,"y"),2),
                       int(s.get(o,"store_full")),int(s.get(o,"at_home"))))
    ot=env.observation_space.get_type("objective")
    st=env.observation_space.get_type("sample")
    print(seed,info.get("object_count"),step+1,term,trunc,
          "img",[int(s.get(o,"received_image")) for o in s.get_objects(ot)],
          "samp",[int(s.get(o,"received_analysis")) for o in s.get_objects(st)],rovers)
    env.close()
