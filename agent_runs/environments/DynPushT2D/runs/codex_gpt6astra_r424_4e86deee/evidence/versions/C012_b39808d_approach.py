"""Contact-aware closed-loop pushing with collision-free repositioning."""
import numpy as np
import math
import heapq

def rot(a):
 c,s=math.cos(a),math.sin(a)
 return np.array([[c,-s],[s,c]])
def action(d):return d/max(1.,float(np.max(np.abs(d)))/.049)
def wrap(a):return (a+math.pi)%(2*math.pi)-math.pi

class GeneratedApproach:
 def __init__(self, action_space, observation_space, primitives):self.reset(None,{})
 def reset(self,state,info):
  self.contact=None;self.phase='choose';self.age=0;self.last=None
 def geometry(self,s,pad):
  w,h,v=s[12:15];a=h/2+pad;b=w/2+pad;t=pad;m=-w-pad;bot=-w-v-pad
  return np.array([[-a,t],[a,t],[a,m],[b,m],[b,bot],[-b,bot],[-b,m],[-a,m]])
 def clear(self,a,b,s,pad=.112):
  R=rot(s[2]);a=(a-s[:2])@R;b=(b-s[:2])@R;d=b-a;w,h,v=s[12:15]
  for lo,hi in [(np.array([-h/2-pad,-w-pad]),np.array([h/2+pad,pad])),(np.array([-w/2-pad,-w-v-pad]),np.array([w/2+pad,-w+pad]))]:
   low=0.;high=1.
   for j in range(2):
    if abs(d[j])<1e-10:
     if a[j]<=lo[j] or a[j]>=hi[j]:low=2.;break
    else:
     x=(lo[j]-a[j])/d[j];y=(hi[j]-a[j])/d[j]
     low=max(low,min(x,y));high=min(high,max(x,y))
   if low<high:return False
  return True
 def path(self,start,end,s):
  if self.clear(start,end,s):return [end]
  nodes=[start,end]+list(self.geometry(s,.135)@rot(s[2]).T+s[:2])
  n=len(nodes);ds=[float('inf')]*n;ds[0]=0.;prev=[-1]*n;queue=[(0.,0)]
  while queue:
   cost,i=heapq.heappop(queue)
   if cost>ds[i]:continue
   if i==1:break
   for j in range(1,n):
    if j==i or not np.all((nodes[j]>.105)&(nodes[j]<4.895)):continue
    if not self.clear(nodes[i],nodes[j],s):continue
    val=cost+float(np.linalg.norm(nodes[j]-nodes[i]))
    if val<ds[j]:ds[j]=val;prev[j]=i;heapq.heappush(queue,(val,j))
  if prev[1]<0:
   # Exit contact region before routing around the object.
   q=(start-s[:2])@rot(s[2]);w,h,v=s[12:15]
   cen=np.array([0.,-.35*v]);delta=q-cen;delta/=max(np.linalg.norm(delta),1e-9)
   return [start+rot(s[2])@delta*.15]
  ids=[];j=1
  while j:ids.append(j);j=prev[j]
  return [nodes[i] for i in ids[::-1]]
 def candidates(self,s):
  poly=self.geometry(s,0);R=rot(s[2]);w,h,v=s[12:15]
  for i in range(8):
   a=poly[i];b=poly[(i+1)%8];t=b-a;length=np.linalg.norm(t);t/=length;n=np.array([-t[1],t[0]])
   for f in np.linspace(.12,.88,max(2,int(length/.15))):
    p=a+f*(b-a);yield p,n
 def rate(self,s,p,n):
  R=rot(s[2]);w,h,v=s[12:15]
  cy=-(h*w/2+v*(w+v/2))/(h+v);c=np.array([0.,cy]);r=p-c
  force=-n;moment=np.cross(r,force);j=(h*((h*h+w*w)/12+(-w/2-cy)**2)+v*((w*w+v*v)/12+(-w-v/2-cy)**2))/(h+v)
  omega=moment/j;vel=force-omega*np.array([-c[1],c[0]])
  ep=(s[29:31]-s[:2])@R;ea=wrap(s[31]-s[2]);weight=.5
  twist=np.r_[vel,weight*omega];error=np.r_[ep,weight*ea]
  gain=np.dot(error,twist)/(np.linalg.norm(twist)+1e-8)
  return gain,twist,error
 def choose(self,s):
  R=rot(s[2]);best=-1e9;choice=None
  for p,n in self.candidates(s):
   target=s[:2]+R@(p+n*.145)
   if not np.all((target>.11)&(target<4.89)) or not self.clear(target,target,s):continue
   gain,_,_=self.rate(s,p,n)
   dist=np.linalg.norm(target-s[16:18]);score=gain/(1+.22*dist)
   if score>best:best=score;choice=(p,n)
  if choice is None:choice=(np.zeros(2),np.array([0.,1.]))
  self.contact=choice;self.phase='move';self.age=0
 def get_action(self,state):
  s=np.asarray(state);self.age+=1
  if self.contact is None or (self.phase=='move' and self.age>130):self.choose(s)
  p,n=self.contact;R=rot(s[2]);target=s[:2]+R@(p+n*.145)
  if self.phase=='move':
   if np.linalg.norm(target-s[16:18])<.025:self.phase='push';self.age=0
   else:
    route=self.path(s[16:18],target,s)
    return action(route[0]-s[16:18])
  gain,twist,error=self.rate(s,p,n)
  best=max(self.rate(s,x,y)[0] for x,y in self.candidates(s))
  if (self.age>8 and gain<best*.6) or gain<.008 or self.age>110:
   self.contact=None
   return np.clip(R@n*.045,-.049,.049)
  scale=np.clip(np.dot(error,twist)/(np.dot(twist,twist)+1e-9),.003,.035)
  target=s[:2]+R@(p+n*(.099-scale))
  return action(target-s[16:18])
