from env_client import make_env
from approach import GeneratedApproach
import json
E=make_env();s,i=E.reset(seed=319);a=GeneratedApproach(E.action_space,E.observation_space,{});a.reset(s,i)
def dump(s):
 for n in sorted(s.get_object_names()):
  o=s.get_object_from_name(n)
  fs=['x','y','theta'] if n=='robot' else ['x','y','width','height']
  print(n,[round(s.get(o,f),6) for f in fs])
print('INITIAL',i);dump(s);prev=None
for step in range(1000):
 act=a.get_action(s);s,r,t,tr,_=E.step(act)
 sig=(a.phase,a.task.name,a.dest)
 if sig!=prev:print(step,sig,'robot',[round(s.get(a.robot,f),6) for f in ['x','y']],'task',[round(s.get(a.task,f),6) for f in ['x','y']]);prev=sig
 if t:print('SUCCESS',step);break
print('FINAL');dump(s);E.close()
