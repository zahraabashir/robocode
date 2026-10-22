from env_client import make_env
import numpy as np
env = make_env()
T = {t.name: t for t in env.observation_space.types}
def rov(obs, i):
    o = [r for r in obs.get_objects(T['rover']) if r.name==f'rover{i}'][0]
    return [float(obs.get(o,f)) for f in ['x','y','theta','store_full','calibrated','at_home']]
def obstacles(obs):
    return [(o.name,[round(float(obs.get(o,f)),3) for f in ['x','y','z','half_x','half_y','half_z']]) for o in obs.get_objects(T['obstacle'])]
def act(i, dx=0, dy=0, dth=0):
    a = np.zeros(8, dtype=np.float32); a[4*i:4*i+3]=[dx,dy,dth]; return a
def step(i, dx=0, dy=0, dth=0):
    return env.step(act(i,dx,dy,dth))
def drive_until_stop(i, dx, dy, nmax=200):
    obs = None
    prev = None
    for k in range(nmax):
        obs,*_ = step(i,dx,dy)
        p = rov(obs,i)[:2]
        if prev is not None and abs(p[0]-prev[0])<1e-9 and abs(p[1]-prev[1])<1e-9: return p
        prev = p
    return prev
def goto(i, tx, ty, s=0.2, n=100):
    for k in range(n):
        obs,*_ = step(i,0,0); p=rov(obs,i)
        ex,ey = tx-p[0], ty-p[1]
        if abs(ex)<1e-6 and abs(ey)<1e-6: return p
        obs,*_ = step(i, np.clip(ex,-s,s), np.clip(ey,-s,s))
    return rov(obs,i)
def approach(i, ux, uy, steps=(0.2,0.05,0.01,0.002)):
    p=None
    for s in steps: p=drive_until_stop(i, s*ux, s*uy)
    return p
