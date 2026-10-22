from env_client import make_env
import numpy as np
env = make_env()
T=None
def run(target, nimg):
    global T
    obs, info = env.reset(seed=2)
    T = {t.name:t for t in env.observation_space.types}
    r1 = obs.get_object_from_name('rover1')
    objs = sorted(obs.get_objects(T['objective']), key=lambda o:o.name)
    def pos(): return np.array([obs.get(r1,'x'), obs.get(r1,'y')])
    # go straight up x=-1 to y=target y, then x
    for wp in [(-1.0, target[1]), target]:
        for _ in range(30):
            d = np.clip(np.array(wp)-pos(), -0.2, 0.2)
            if np.abs(d).max() < 1e-6: break
            obs,*_ = env.step(np.array([0,0,0,1/6, d[0],d[1],0,1/6],dtype=np.float32))
    print('at', pos().round(3))
    for k in range(nimg):
        for op in [-0.5, -1/6]:
            obs,*_ = env.step(np.array([0,0,0,1/6, 0,0,0,op],dtype=np.float32))
        print(' after img', k, [(int(obs.get(o,'have_image_rover1'))) for o in objs], 'cal', obs.get(r1,'calibrated'))
run((-1.1,0.5), 3)
run((-1.5,0.25), 3)
run((-1.57,0.31), 3)
