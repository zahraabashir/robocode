from env_client import make_env
env=make_env()
for s in range(40):
    obs,_=env.reset(seed=s)
    ps=[(obs.get(o,'x'),obs.get(o,'y')) for o in obs if o.type.name=='obstacle' and obs.get(o,'half_x')<0.1]
    if not any(x<-0.6 and y<-0.3 for x,y in ps): print('lander-clear seed',s)
    if not any(x>0 and x<0.8 and y>1.0 for x,y in ps) : print('r0 topclear',s)
env.close()
