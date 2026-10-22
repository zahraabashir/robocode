from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
# seed1 rover1 samples stone sample1 (-1.485,-1.367), then sends from various positions
for tgt in [(-0.3,-0.5),(-0.3,1.0),(-1.5,1.0),(-2.2,-0.2),(-0.3,2.3),(-1.0,-2.3),(-1.9,-1.6),(-1.1,-0.2)]:
  D=Driver(1); D.goto(1,-1.285,-1.367); D.act(1,'sample')
  ok,p=goto_fine(D,1,*tgt); D.act(1,'send')
  print('send from',tgt,ok,[round(v,2) for v in p],'dist',round(math.hypot(p[0]+1.9,p[1]+2.0),2),'recv',S(D.obs,'sample1')['received_analysis'])
