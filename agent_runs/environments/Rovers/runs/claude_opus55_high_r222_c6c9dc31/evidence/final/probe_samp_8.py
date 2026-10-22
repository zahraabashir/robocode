from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
sx,sy=0.547,-1.348
def trial(tgt):
  D=Driver(1); D.goto(0,sx+0.2,sy); D.act(0,'sample')
  ok,p=goto_fine(D,0,*tgt); D.act(0,'send'); return [round(v,3) for v in p], S(D.obs,'sample3')['received_analysis']
if __name__=="__main__":
 for tgt in [(0.25,-1.3),(0.25,-1.6),(0.25,-1.8),(0.25,-1.9),(0.25,-2.0),(0.25,-2.1),(0.5,-2.2),(0.8,-2.2),(1.2,-2.2),(1.6,-2.2),(0.8,-2.0),(0.8,-1.8)]:
  print(tgt, *trial(tgt))
