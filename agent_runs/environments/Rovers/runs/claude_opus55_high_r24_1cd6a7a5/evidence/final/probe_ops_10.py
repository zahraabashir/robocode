from probe_ops_lib import *
reset(14)
ox,oy=get('objective0')[:2]; px,py=get('obstacle7')[:2]
dd=math.hypot(px-ox,py-oy); ux,uy=(px-ox)/dd,(py-oy)/dd; vx,vy=-uy,ux
goto(0,1.0,0.0)
for L in [1.8,1.3]:
  for s in [-0.4,-0.3,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.3,0.4]:
    tx,ty=ox+L*ux+s*vx,oy+L*uy+s*vy
    ok=goto(0,tx,ty,tol=0.005)
    step(0,op='calibrate'); c=pos(0)[4]
    if c: step(0,op='image')
    x,y=pos(0)[:2]
    # perpendicular distance of pillar center from rover-objective segment
    ax,ay=ox-x,oy-y; t=((px-x)*ax+(py-y)*ay)/(ax*ax+ay*ay); perp=math.hypot(x+t*ax-px,y+t*ay-py)
    print('L',L,'s',s,'reached',ok,'cal',c,'perp_dist_pillar_to_line',round(perp,3),'img',get('objective0')[3])
