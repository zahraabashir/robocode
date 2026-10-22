from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
def run(img0=True, home0=True, drop_early=True):
  D=Driver(1); T=[]
  def chk(tag):
    if D.last[1]: T.append((tag,D.steps))
  goto_fine(D,1,-1.7,-1.0); goto_fine(D,1,-1.7,0.9)
  D.turn(1,math.atan2(2.096-0.9,-2.114+1.7)); D.act(1,'calibrate'); D.act(1,'image'); D.act(1,'send')
  goto_fine(D,1,-1.7,-1.0); D.goto(1,-1.285,-1.367); D.act(1,'sample'); D.act(1,'send'); D.act(1,'drop')
  goto_fine(D,1,-1,-1.75); D.turn(1,0); chk('r1home')
  D.goto(0,0.747,-1.348); D.act(0,'sample'); goto_fine(D,0,0.8,-2.0); D.act(0,'send'); D.act(0,'drop'); chk('r0drop')
  if img0:
    goto_fine(D,0,1.7,-1.5); goto_fine(D,0,1.7,0.3)
    p=rov(D.obs,0); D.turn(0,math.atan2(1.923-p['y'],2.118-p['x'])); D.act(0,'calibrate'); D.act(0,'image')
    goto_fine(D,0,1.7,-1.5); goto_fine(D,0,0.8,-2.0); D.act(0,'send'); chk('r0send')
  if home0:
    goto_fine(D,0,1.0,-1.75); chk('r0pos'); D.turn(0,math.pi); chk('r0theta')
  D.step(); chk('final')
  print('img0',img0,'home0',home0,'term events',T[:3],'r0',{k:round(v,2) for k,v in rov(D.obs,0).items()})
run(True,False); run(False,True)
