from env_client import make_env
import numpy as np

e=make_env(); s,_=e.reset(seed=1)
r=s.get_object_from_name('robot'); b=s.get_object_from_name('target_block')
def out(tag):
 print(tag, 'r',*[round(s.get(r,k),5) for k in ['x','y','arm_joint','arm_length','vacuum']], 'b',*[round(s.get(b,k),5) for k in ['x','y','theta']])
def step(a,tag):
 global s
 s,w,t,tr,i=e.step(np.array(a,dtype=np.float32));out(tag)
 return t
x=s.get(b,'x')+s.get(b,'width')/2
out('init')
while abs(s.get(r,'x')-x)>1e-5: step([np.clip(x-s.get(r,'x'),-.05,.05),0,0,0,0],'align')
for k in range(45): step([0,-.01,0,0,1],'down'+str(k))
for k in range(12): step([0,.025,0,0,1],'up'+str(k))
e.close()
