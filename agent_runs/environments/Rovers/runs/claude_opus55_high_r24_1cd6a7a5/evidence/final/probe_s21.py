from env_client import make_env
env = make_env()
obs, info = env.reset(seed=21)
T = {t.name:t for t in env.observation_space.types}
for t in ['sample','objective','lander']:
    for o in obs.get_objects(T[t]): print(o.name, [round(obs.get(o,f),3) for f in ['x','y']], obs.get(o,'is_soil') if t=='sample' else '')
