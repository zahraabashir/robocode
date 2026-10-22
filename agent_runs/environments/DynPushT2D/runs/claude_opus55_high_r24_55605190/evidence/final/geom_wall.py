from geom_lib import *
def corners(o):
    x,y,th=o[0:3]; w,Lh,Lv=o[12:15]; M=rot(th)
    pts=np.array([[-Lh/2,0],[Lh/2,0],[Lh/2,-w],[-Lh/2,-w],[w/2,-w-Lv],[-w/2,-w-Lv]])
    return (M@pts.T).T+[x,y]
if __name__=="__main__":
  P=Prober()
  for seed,d in [(1,(1,0)),(12,(1,0)),(12,(-1,0)),(12,(0,1)),(12,(0,-1))]:
      o=P.reset(seed); d=np.array(d,float); c=P.b0[:2]
      # go behind block (opposite side), then push through center line
      P.nav(c-d*1.55)
      ext=[]
      for k in range(200):
          P.step(d*0.0499)
          ext.append(np.max(corners(P.obs)@d))
      print('seed',seed,'dir',d,'robot',np.round(P.obs[16:18],3),'block',np.round(P.obs[0:3],3),'block extreme along dir: max %.3f final %.3f'%(max(ext),ext[-1]))
  