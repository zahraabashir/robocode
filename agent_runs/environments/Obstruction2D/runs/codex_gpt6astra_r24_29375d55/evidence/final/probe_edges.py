from env_client import make_env
import numpy as np
ext=[]
for seed in range(60):
 e=make_env();s,i=e.reset(seed=seed)
 for typ in ['rectangle','target_block']:
  for o in s.get_objects(e.observation_space.get_type(typ)):
   x=s.get(o,'x');w=s.get(o,'width')
   if x+w/2<.1 or x+w/2>1.518:ext.append((seed,o.name,x,w,s.get(o,'y'),s.get(o,'height')))
 e.close()
print('extreme',ext[:15], 'count',len(ext))
for seed,name,x,w,y,h in ext[:8]:
 e=make_env();s,i=e.reset(seed=seed);r=s.get_object_from_name('robot');b=s.get_object_from_name(name)
 bx=np.clip(x+w/2,.1001,1.5179);by=y+h+.22
 for j in range(40):s,*_=e.step(np.array([np.clip(bx-s.get(r,'x'),-.05,.05),np.clip(by-s.get(r,'y'),-.05,.05),0,.1,1],dtype=np.float32))
 orig=s.get(b,'y');s,*_=e.step(np.array([0,.05,0,0,1],dtype=np.float32))
 print(seed,name,'objx',x,'w',w,'bx',bx,'basex',s.get(r,'x'),'delta_y',s.get(b,'y')-orig)
 e.close()
