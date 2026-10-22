from env_client import make_env
env=make_env()
T={t.name:t for t in env.observation_space.types}
F={'rover':['x','y','theta','store_full','calibrated','at_home'],'lander':['x','y','z'],'objective':['x','y','z','have_image_rover0','have_image_rover1','received_image'],'sample':['x','y','z','is_soil','analyzed_rover0','analyzed_rover1','received_analysis'],'obstacle':['x','y','z','half_x','half_y','half_z']}
import sys
for seed in map(int,sys.argv[1:]):
    obs,info=env.reset(seed=seed); print('seed',seed,info)
    for t in F:
        for o in obs.get_objects(T[t]): print(' ',o.name,[round(float(obs.get(o,f)),2) for f in F[t]])
