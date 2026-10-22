from probe_vis_util import *
def smp(r): return {o.name:feats(r.obs,o,TF['sample'][3:]) for o in objs(r.obs,'sample')}
r=R(0)
path(r,0,[(1.2,0.0),(1.2,1.6)])
for k in range(2): r.act(0,'calibrate'); r.act(0,'image')
print(r.objst())
path(r,0,[(1.2,0.0),(0.5,-1.0)])
r.act(0,'send'); print('one send rover0:',r.objst())
# rover1: sample then image then send
print(path(r,1,[(-0.271,-1.9)]), r.rv(1))
r.act(1,'sample'); print('after sample', r.rv(1)['store_full'], smp(r))
r.goto(1,-0.271,-2.04); r.act(1,'sample'); print('after sample at exact', r.rv(1)['store_full'], smp(r))
r.act(1,'send'); print('send analysis', smp(r), r.objst())
r.act(1,'send'); print('send again', smp(r), r.rv(1))
