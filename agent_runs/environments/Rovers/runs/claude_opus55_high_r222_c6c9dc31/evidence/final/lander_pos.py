from env_client import make_env
env=make_env()
for s in range(int(__import__('sys').argv[1]),int(__import__('sys').argv[2])):
    obs,_=env.reset(seed=s); l=list(obs.get_objects(env.observation_space.get_type('lander')))[0]
    print(s, round(float(obs.get(l,'x')),2), round(float(obs.get(l,'y')),2), round(float(obs.get(l,'z')),3))
