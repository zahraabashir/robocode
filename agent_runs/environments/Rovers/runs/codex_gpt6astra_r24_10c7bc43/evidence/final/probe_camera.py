from env_client import make_env
import numpy as np
import json

def run(seed, x, y):
 e=make_env();s,_=e.reset(seed=seed)
 rovers=[s.get_object_from_name('rover'+str(i)) for i in range(2)]
 objs=list(s.get_objects(e.observation_space.get_type('objective')))
 targets=[(abs(x),y),(-abs(x),y)]
 for axis in [0,1]:
  for k in range(25):
   a=np.zeros(8)
   done=True
   for i,r in enumerate(rovers):
    diff=targets[i][axis]-s.get(r,['x','y'][axis]);a[4*i+axis]=np.clip(diff,-.2,.2)
    if abs(diff)>.001:done=False
   if done:break
   s,*_=e.step(a)
 a=np.zeros(8);a[[3,7]]=-.5
 s,*_=e.step(a)
 cal=[s.get(r,'calibrated') for r in rovers]
 a[[3,7]]=-1/6
 s,*_=e.step(a)
 images=[[o.name for o in objs if s.get(o,'have_image_rover'+str(i))] for i in range(2)]
 result={'seed':seed,'wanted':[x,y],'xy':[[s.get(r,'x'),s.get(r,'y')] for r in rovers], 'cal':cal,'images':images,'objectives':[[o.name,s.get(o,'x'),s.get(o,'y')] for o in objs]}
 e.close();return result
if __name__=='__main__':
 out=[]
 for seed in [0,1,2]:
  for x in [.4,1.,1.6,2.1]:
   for y in [.3,.8,1.3]:
    r=run(seed,x,y);out.append(r);print(json.dumps(r),flush=True)
 with open('probe_camera_results.json','w') as f:json.dump(out,f)
