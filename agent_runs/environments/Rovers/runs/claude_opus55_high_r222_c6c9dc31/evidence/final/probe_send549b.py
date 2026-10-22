import sys, numpy as np
from env_client import make_env
from approach import GeneratedApproach, SEL
env=make_env(); obs,info=env.reset(seed=int(sys.argv[2]))
ap=GeneratedApproach(env.action_space, env.observation_space,{}); ap.reset(obs,info)
for i in range(int(sys.argv[1])):
    obs,*_=env.step(ap.get_action(obs))
r0=ap.w.rovers['rover0']; r1=ap.w.rovers['rover1']
smp=ap.w.samples
def st(): return round(float(obs.get(r0,'x')),3), round(float(obs.get(r0,'y')),3), round(float(obs.get(r1,'x')),3),round(float(obs.get(r1,'y')),3)
def recv(): return sum(float(obs.get(s,'received_analysis')) for s in smp)
print('start',st(), recv(), [(s.name,float(obs.get(s,'analyzed_rover0'))) for s in smp])
for dx,dy in [(0,0)]+[(0,-0.2)]*5+[(0.2,0)]*4:
    a=np.zeros(8,np.float32); a[0:4]=[dx,dy,0,SEL['send']]; a[7]=SEL['none']
    b=recv(); obs,*_=env.step(a); print(st(), 'send ok' if recv()>b else 'fail')
    if recv()>b: break
