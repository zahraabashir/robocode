from env_client import make_env
env=make_env()
for n in [3,4,6,8]:
    obs,info=env.reset(seed=1,options={'object_count':n}); print(n, info, sorted(obs.get_object_names()))
