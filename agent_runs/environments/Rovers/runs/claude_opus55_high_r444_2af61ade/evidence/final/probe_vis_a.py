from probe_vis_lib import *
e=E(1)
print(e.rs(0))
ok=e.path(0,[(1.0,0.0),(2.118,0.0),(2.118,1.0)]); print(ok,e.rs(0))
# test move frame: does dx move world x with theta=pi?
for k in range(3):
    rew=e.step(0,0,0,0,'cal'); print('cal',e.rs(0),rew)
rew=e.step(0,0,0,0,'img'); print('img',e.rs(0),rew,e.objs())
rew=e.step(0,0,0,0,'noop'); print(e.rs(0))
