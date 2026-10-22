from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
sx,sy=0.547,-1.348
D=Driver(1); D.goto(0,sx+0.2,sy); D.act(0,'sample')
for tgt in [(0.25,-2.2),(0.25,-2.45),(0.6,-2.45),(1.0,-2.45),(1.0,0.0),(0.6,2.45),(0.25,2.45)]:
  ok,p=goto_fine(D,0,*tgt); D.act(0,'send'); print('r0 at',[round(v,3) for v in p],'recv',S(D.obs,'sample3')['received_analysis'])
# sweep west at many y
for y in [-2.45,-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,2.45]:
  ok,p=goto_fine(D,0,0.6,y); ok2,p2=goto_fine(D,0,-0.6,y); print('y',y,'reach',[round(v,3) for v in p],'west->',[round(v,3) for v in p2])
