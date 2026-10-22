from env_client import make_env
import numpy as np
env = make_env()
obs, info = env.reset(seed=0)
T = {t.name:t for t in env.observation_space.types}
def g(name,f): return float(obs.get(obs.get_object_from_name(name),f))
# rover1 at (-1,-1.75). sample3 soil at (-1.387,0.152). move rover1 up along x=-1 ... find path: go to x=-1.387+? check pillars
print([ (o.name, round(g(o.name,'x'),2), round(g(o.name,'y'),2)) for o in obs.get_objects(T['obstacle'])])
def step(a):
    global obs
    obs,r,te,tr,info = env.step(np.array(a,dtype=np.float32)); return te
# move rover1 to (-1.0, 0.152-0.45) area: path along x=-1 upward: pillars at (-0.808,0.192),(-1.354,0.554),(-1.808,-1.549)
for i in range(10): step([0,0,0,1/6, 0,0.2,0,1/6])
print('r1', g('rover1','x'), g('rover1','y'))
# now at y=0.25? compute
step([0,0,0,1/6, -0.2,0.15,0,-5/6])
print('r1', g('rover1','x'), g('rover1','y'), 'store', g('rover1','store_full'))
# move away while sampling? test pre: drop then move away with sample
step([0,0,0,1/6, 0,0,0,5/6])
