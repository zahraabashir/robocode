from env_client import make_env
from approach import GeneratedApproach
import json

e=make_env(); cases=[]
for seed in range(1000,1201):
 s,_=e.reset(seed=seed)
 p=GeneratedApproach(e.action_space,e.observation_space,{})
 p.reset(s,{})
 p.get_action(s)
 bx,by,bw,bh=p.rect(s,p.block)
 cx=min(1.516,p.destx+bw/2);cy=.1+bh+.206
 for o in s.get_objects(p.ot):
  if o in (p.block,p.surface):continue
  ox,oy,ow,oh=p.rect(s,o)
  if ox<p.destx+bw+.004 and ox+ow>p.destx-.004:continue
  dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
  if dx*dx+dy*dy<.101**2:
   cases.append(seed);print('CASE',seed,'target',bw,bh,'dest',p.destx,'neighbor',o.name,[ox,oy,ow,oh],flush=True);break
print('FOUND',cases,flush=True)
for seed in cases[:5]:
 s,_=e.reset(seed=seed);p=GeneratedApproach(e.action_space,e.observation_space,{});p.reset(s,{})
 for t in range(e.max_steps):
  a=p.get_action(s);s,r,term,trunc,_=e.step(a)
  if term or trunc:break
 print('RESULT',seed,term,t+1,p.phase,flush=True)
e.close()
