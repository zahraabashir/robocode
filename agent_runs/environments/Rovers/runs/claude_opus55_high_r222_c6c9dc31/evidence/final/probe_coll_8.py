from probe_coll_util import *
# wall scan: rover0 (right side) push -x at many y; rover1 push +x
obs,_=env.reset(seed=3)
print({k:[round(x,3) for x in v] for k,v in obst(obs).items() if v[2]<0.1})
for y in [-2.27,-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,2.27]:
    obs=goto(0,1.0,rov(obs)[0][1],obs); obs=goto(0,1.0,y,obs)
    p=rov(obs)[0]
    obs=push(0,(-1,0),obs,tol=1e-5)
    print('y target',y,'start',round(p[0],3),round(p[1],3),'stop',[round(v,5) for v in rov(obs)[0]])
