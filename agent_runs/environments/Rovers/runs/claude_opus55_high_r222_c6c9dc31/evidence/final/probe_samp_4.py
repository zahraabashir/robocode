from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
for s in [1,0]:
  D=Driver(s)
  print('seed',s,'r1 east', D.goto(1,1.0,-2.3), rov(D.obs,1)['x'],rov(D.obs,1)['y'])
  D=Driver(s)
  print('seed',s,'r0 west', D.goto(0,-1.0,-1.2), rov(D.obs,0)['x'],rov(D.obs,0)['y'])
  D=Driver(s)
  print('seed',s,'r1 north', D.goto(1,-1.0,2.0), rov(D.obs,1)['x'],rov(D.obs,1)['y'])
# send from far: seed1 rover0 samples sample3 soil then drives to various points and sends
sx,sy=0.547,-1.348
for tgt in [(2.0,1.0),(1.5,-0.5),(0.9,-1.3)]:
  D=Driver(1); D.goto(0,sx+0.2,sy); D.act(0,'sample')
  ok=D.goto(0,*tgt); p=rov(D.obs,0); D.act(0,'send')
  print('send from',tgt,ok,round(p['x'],2),round(p['y'],2),'recv',S(D.obs,'sample3')['received_analysis'],'store',rov(D.obs,0)['store_full'])
