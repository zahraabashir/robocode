import numpy as np
def R(t): return np.array([[np.cos(t),-np.sin(t)],[np.sin(t),np.cos(t)]])
def com_I(w,L,V):
    A1=L*w; A2=V*w; y1=-w/2; y2=-w-V/2
    yc=(A1*y1+A2*y2)/(A1+A2)
    I=A1*(L*L+w*w)/12+A1*(y1-yc)**2+A2*(V*V+w*w)/12+A2*(y2-yc)**2
    return np.array([0.0,yc]), I/(A1+A2)   # com local, k^2
