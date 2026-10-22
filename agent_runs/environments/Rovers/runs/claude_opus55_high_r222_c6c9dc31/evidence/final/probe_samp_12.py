from probe_samp_util import *
for i,hth in [(0,math.pi),(1,0.0)]:
 for dth in [0.38,0.39,0.395,0.399,0.4,0.401,0.405,0.41,-0.39,-0.399,-0.401]:
  D=Driver(1); D.turn(i,hth+dth); p=rov(D.obs,i)
  print(i,dth,round(p['theta'],5),p['at_home'],end=' | ')
 print()
