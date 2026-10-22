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
   if not self.clear(start,start,s):
    poly=self.geometry(s,.14)@rot(s[2]).T+s[:2];candidates=[]
    for a,b in zip(poly,np.roll(poly,-1,axis=0)):
     d=b-a;q=a+np.clip(np.dot(start-a,d)/np.dot(d,d),0.,1.)*d
     if np.all((q>.105)&(q<4.895)):candidates.append(q)
    if candidates:return [min(candidates,key=lambda q:np.linalg.norm(q-start))]
   return None
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
  j=(h*((h*h+w*w)/12+(-w/2-cy)**2)+v*((w*w+v*v)/12+(-w-v/2-cy)**2))/(h+v)
  z=np.array([-r[1],r[0]])/j
  weight=.65
  M=np.array([[1+cy*z[0],cy*z[1]],[0.,1.],weight*z])
  ep=(s[29:31]-s[:2])@R;ea=wrap(s[31]-s[2]);error=np.r_[ep,weight*ea]
  F=np.linalg.solve(M.T@M+.00001*np.eye(2),M.T@error)
  t=np.array([-n[1],n[0]])
  options=[]
  if np.dot(F,-n)>0 and abs(np.dot(F,t))<.8*np.dot(F,-n):options.append(F)
  for sign in [-1,1]:
   d=-n+sign*.8*t;md=M@d
   options.append(d*max(0.,np.dot(md,error)/np.dot(md,md)))
  F=min(options,key=lambda f:np.linalg.norm(M@f-error))
  twist=M@F;omega=np.dot(z,F)
  u=F+omega*np.array([-r[1],r[0]])
  gain=np.linalg.norm(twist)
  return gain,u,error
 def choose(self,s):
  R=rot(s[2]);choices=[]
  for p,n in self.candidates(s):
   target=s[:2]+R@(p+n*.145)
   if not np.all((target>.11)&(target<4.89)) or not self.clear(target,target,s):continue
   gain,_,_=self.rate(s,p,n)
   dist=np.linalg.norm(target-s[16:18]);score=gain/(1+.22*dist)
   choices.append((score,p,n,target))
  choices.sort(key=lambda x:-x[0]);choice=None
  for score,p,n,target in choices:
   route=self.path(s[16:18],target,s)
   if route is not None:choice=(p,n);break
  if choice is None:
   choice=(choices[0][1],choices[0][2]) if choices else (np.zeros(2),np.array([0.,1.]))
  self.contact=choice;self.phase='move';self.age=0
 def get_action(self,state):
  s=np.asarray(state);self.age+=1
  if self.contact is None or (self.phase=='move' and self.age>130):self.choose(s)
  p,n=self.contact;R=rot(s[2]);target=s[:2]+R@(p+n*.145)
  if self.phase=='move':
   if np.linalg.norm(target-s[16:18])<.025:self.phase='push';self.age=0
   else:
    route=self.path(s[16:18],target,s)
    if route is None:
     self.contact=None
     return np.zeros(2)
    return action(route[0]-s[16:18])
  # Track the contact point along its current face.
  q=(s[16:18]-s[:2])@R;t=np.array([-n[1],n[0]])
  poly=self.geometry(s,0)
  for a,b in zip(poly,np.roll(poly,-1,axis=0)):
   d=b-a;L=np.linalg.norm(d);tt=d/L;nn=np.array([-tt[1],tt[0]])
   if np.dot(nn,n)>.99 and abs(np.dot(p-a,n))<1e-5 and -.001<=np.dot(p-a,tt)<=L+.001:
    along=np.dot(q-a,tt)
    if along<.035 or along>L-.035:
     self.contact=None
     return action(R@n*.05)
    p=a+np.clip(along,.035,L-.035)*tt
    self.contact=(p,n)
    break
  gain,u,error=self.rate(s,p,n)
  if self.age%5==0:
   best=max(self.rate(s,x,y)[0] for x,y in self.candidates(s))
  else:best=gain
  if (self.age>10 and gain<best*.78) or gain<.005 or self.age>150:
   self.contact=None
   return action(R@n*.05)
  u*=min(.6,.037/max(np.linalg.norm(u),1e-9))
  target=s[:2]+R@(p+n*.099+u)
  return action(target-s[16:18])
