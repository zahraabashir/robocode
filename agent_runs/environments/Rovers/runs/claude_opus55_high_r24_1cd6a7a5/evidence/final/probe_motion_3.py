from probe_motion_lib import *
obs,_=env.reset(seed=0)
L=[o for o in obs.get_objects(T['lander'])][0]
print('lander feats', {f:round(float(obs.get(L,f)),3) for f in env.observation_space.type_features[T['lander']]})
# partial move test: rover1 toward lander with big step from near contact
obs,_=env.reset(seed=0)
goto(1,-1.15,-1.75,s=0.05); obs,*_=step(1,-0.2,0); print('big step near block ->',np.round(rov(obs,1)[:2],4))
# wall: rover0 at x=1, various y, drive -x
for seed in [0]:
  for y in np.arange(-2.25,2.26,0.25):
    obs,_=env.reset(seed=seed)
    p=goto(0,1.0,y)
    if abs(p[1]-y)>1e-3: print(y,'could not reach',np.round(p,3)); continue
    p=approach(0,-1,0)
    print(f'y={y:.2f} blocked at x={p[0]:.3f} y={p[1]:.3f}')
