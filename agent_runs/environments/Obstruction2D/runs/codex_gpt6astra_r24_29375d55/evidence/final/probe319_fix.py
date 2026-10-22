from env_client import make_env
from approach import GeneratedApproach
class Probe(GeneratedApproach):
 def conflicts(self,s,obj,x,y,offset,others):
  _,_,w,h=self.rect(s,obj);rx=x+offset;ry=y+h+.215
  gripper=(rx-.035,ry-.21,.07,.01);arm=(rx-.008,ry-.2,.016,.2);bad=[]
  for o in others:
   q=self.rect(s,o);dx=max(q[0]-rx,0,rx-q[0]-q[2]);dy=max(q[1]-ry,0,ry-q[1]-q[3])
   if self.overlap((x,y,w,h),q,.0002) or self.overlap(gripper,q,.014) or self.overlap(arm,q) or dx*dx+dy*dy<.103**2:bad.append(o)
  return bad
E=make_env();s,i=E.reset(seed=319);a=Probe(E.action_space,E.observation_space,{});a.reset(s,i)
for n in range(1000):
 act=a.get_action(s);s,r,t,tr,_=E.step(act)
 if t:break
print('success',t,'steps',n+1,'phase',a.phase);E.close()
