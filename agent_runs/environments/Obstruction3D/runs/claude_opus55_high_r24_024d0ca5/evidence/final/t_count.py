from env_client import make_env
env=make_env()
for opt in [{'object_count':5},{'num_obstructions':5}]:
    try:
        obs,info=env.reset(seed=0,options=opt); print(opt, info, len(obs.get_object_names()))
    except Exception as e: print(opt,'ERR',str(e)[:200])
env.close()
