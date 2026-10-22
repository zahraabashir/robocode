from env_client import make_env
from approach import GeneratedApproach
import sys
E=make_env();s,info=E.reset(seed=int(sys.argv[1]) if len(sys.argv)>1 else 0);p=GeneratedApproach(E.action_space,E.observation_space,{});p.reset(s,info)
for t in range(120):
 a=p.get_action(s);s,r,done,trunc,inf=E.step(a)
 if t%5==0 or done:print(t,[[round(s.get(ro,k),3) for k in ['x','y','store_full','calibrated','at_home']] for ro in p.rovers],[[s.get(o,k) for k in ['received_image','have_image_rover0','have_image_rover1']] for o in p.objs],a.round(2),flush=True)
 if done:break
E.close()
