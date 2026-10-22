import time
from env_client import make_env
from approach import GeneratedApproach
env=make_env(); obs,info=env.reset(seed=0)
ap=GeneratedApproach(env.action_space, env.observation_space, {}); ap.reset(obs,info)
t=time.time(); 
for _ in range(10): a=ap.get_action(obs)
print('get_action', (time.time()-t)/10)
t=time.time()
for _ in range(10): obs2=env.step(a*0)
print('env step', (time.time()-t)/10)
