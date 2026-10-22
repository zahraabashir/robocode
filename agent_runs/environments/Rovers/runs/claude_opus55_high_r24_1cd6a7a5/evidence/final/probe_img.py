from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=2)
T = {t.name:t for t in env.observation_space.types}
for o in obs.get_objects(T['objective']): print(o.name, obs.get(o,'x'), obs.get(o,'y'))
for o in obs.get_objects(T['obstacle']): print(o.name, round(obs.get(o,'x'),2), round(obs.get(o,'y'),2), obs.get(o,'half_x'))
