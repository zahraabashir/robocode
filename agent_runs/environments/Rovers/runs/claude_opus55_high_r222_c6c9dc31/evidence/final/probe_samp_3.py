from probe_samp_util import *
def S(obs,n):
    o=obs.get_object_from_name(n); return {f:round(float(obs.get(o,f)),3) for f in obs.type_features[o.type]}
sx,sy=0.547,-1.348
D=Driver(1)
D.goto(0,sx+0.2,sy); D.act(0,'sample'); D.act(0,'drop'); D.act(0,'sample')
print('resample after drop: store',rov(D.obs,0)['store_full'],S(D.obs,'sample3'))
D.act(0,'drop')
# rover1 samples sample3 too
D.goto(0,1.5,-1.0)
print('r1 goto', D.goto(1,sx-0.2,sy), rov(D.obs,1))
D.act(1,'sample'); print('r1 sample same: store',rov(D.obs,1)['store_full'],S(D.obs,'sample3'))
D.act(1,'drop')
# rover1 samples stone sample1 (-1.485,-1.367)
print(D.goto(1,-1.485+0.2,-1.367)); D.act(1,'sample'); print('r1 stone', rov(D.obs,1)['store_full'], S(D.obs,'sample1'))
# send radius: approach lander (-1.9,-2.0) from east
lx,ly=-1.9,-2.0
for d in [2.0,1.5,1.2,1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.35,0.3,0.25]:
    ok=D.goto(1,lx+d*0.8,ly+d*0.6)
    D.act(1,'send'); p=rov(D.obs,1)
    print('d',d,'ok',ok,'dist',round(math.hypot(p['x']-lx,p['y']-ly),3),'store',p['store_full'],'s1',S(D.obs,'sample1')['received_analysis'],'s3',S(D.obs,'sample3')['received_analysis'],D.last[1:])
    if S(D.obs,'sample1')['received_analysis']: break
