import numpy as np
pill={'p5':(-1.717,0.906),'p8':(-0.907,1.268)}
objs={'o1':(-2.176,1.837),'o2':(-0.4922,1.8822)}
def cam(b,th,ox=-0.087,oy=-0.0125):
    return np.array([b[0]+ox*np.cos(th)-oy*np.sin(th), b[1]+ox*np.sin(th)+oy*np.cos(th)])
def segd(a,b,p):
    a,b,p=map(np.array,(a,b,p)); d=b-a; t=np.clip(np.dot(p-a,d)/np.dot(d,d),0,1); return np.linalg.norm(a+t*d-p), np.cross(d,p-a)/np.linalg.norm(d)
import sys
if __name__=='__main__':
  b=eval(sys.argv[1])
  for thd in eval(sys.argv[2]):
    c=cam(b,np.deg2rad(thd)); s=[f"{o}:{np.linalg.norm(c-np.array(op)):.3f} "+" ".join(f"{pn}={segd(c,op,pp)[1]:+.4f}" for pn,pp in pill.items()) for o,op in objs.items()]
    print(thd,c.round(4),' | '.join(s))
