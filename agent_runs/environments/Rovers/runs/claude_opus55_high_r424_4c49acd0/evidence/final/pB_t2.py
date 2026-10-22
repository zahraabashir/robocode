from pB_lib import *
import numpy as np
for th in [0,np.pi/2,-np.pi/2,np.pi]:
    s=Sim(0); s.goto(0,1.0,0.5,th); s.act(a0=(0,0,0,'cal')); c=s.r(0)
    s.act(a0=(0,0,0,'img')); o=[R2 for R2 in []]
    ob=[ [float(s.obs.get(s.obs.get_object_from_name('objective%d'%k),'have_image_rover0')) for k in range(3)]]
    print('th',round(th,2),'cal',c['calibrated'],'after img',s.r(0)['calibrated'],ob)
    s.act(a0=(0,0,0,'img'))
    print('  2nd img w/o recal', [float(s.obs.get(s.obs.get_object_from_name('objective%d'%k),'have_image_rover0')) for k in range(3)])
