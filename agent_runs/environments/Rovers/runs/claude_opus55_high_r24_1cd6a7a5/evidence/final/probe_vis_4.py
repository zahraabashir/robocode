from probe_vis_lib import *
import sys
ang=float(sys.argv[1])*np.pi/180
for thd in range(0,360,45):
    th=np.deg2rad(thd); th=(th+np.pi)%(2*np.pi)-np.pi
    a=scan(2,'objective2',ang,2.3,1.5,0.01,th=th,via=[(-0.492,-1.75)])
    b=scan(2,'objective2',ang,a[0]+0.01,a[0]-0.001,0.0005,th=th,via=[(-0.492,-1.75)]) if a and a[0]!='unreach' else None
    print('th',thd,a,b)
