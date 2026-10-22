import numpy as np, kin, importlib as _il
from env_client import make_env
GA = _il.import_module("approach_v2").GeneratedApproach
env = make_env()
obs, info = env.reset(seed=113, options={'object_count': 9})
ap = GA(env.action_space, env.observation_space, {}); ap.reset(obs, info)
for t in range(0): obs,*_=env.step(ap.get_action(obs))
objs=ap._parse(obs)
for n in ["obstruction0","obstruction5","obstruction7","obstruction2"]:
    c=ap._grasp_candidates(objs[n], objs)
    print(n, [ (round(x[0],3), round(np.degrees(x[1])%360), round(x[2],3), round(x[3],3), x[4], round(x[5],3)) for x in c[:4]])
