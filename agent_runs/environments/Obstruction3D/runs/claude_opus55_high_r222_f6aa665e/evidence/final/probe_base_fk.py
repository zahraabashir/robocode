import numpy as np
D=[(np.pi/2,-(0.1564+0.1284),0),(np.pi/2,-(0.0054+0.0064),np.pi),(np.pi/2,-(0.2104+0.2104),np.pi),
   (np.pi/2,-(0.0064+0.0064),np.pi),(np.pi/2,-(0.2084+0.1059),np.pi),(np.pi/2,0,np.pi),(np.pi,-(0.1059+0.0615),np.pi)]
def dh(al,d,th):
    ca,sa,ct,st=np.cos(al),np.sin(al),np.cos(th),np.sin(th)
    return np.array([[ct,-st*ca,st*sa,0],[st,ct*ca,-ct*sa,0],[0,sa,ca,d],[0,0,0,1]])
def fk(q,tool=0.0):
    T=dh(np.pi,0,0)
    for (al,d,off),qi in zip(D,q): T=T@dh(al,d,qi+off)
    T=T@np.array([[1,0,0,0],[0,1,0,0],[0,0,1,tool],[0,0,0,1]])
    return T
if __name__=="__main__":
    q0=[0,-0.35,-np.pi,-2.5,0,-0.87,np.pi/2]
    for j2 in [-0.35,0.0,0.35,0.7]:
        q=list(q0); q[1]=j2; T=fk(q,0.12); print(j2, np.round(T[:3,3],3), "zaxis",np.round(T[:3,2],2))
    print("home",np.round(fk([0,0.26,np.pi,-2.27,0,0.96,np.pi/2],0.12)[:3,3],3))
