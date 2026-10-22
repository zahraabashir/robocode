from pA_lib import P
import numpy as np
p=P(0)
ah=lambda i=1: p.st('rover%d'%i)['at_home']
home={0:np.array([1,-1.75,np.pi]),1:np.array([-1,-1.75,0])}
def thr_pos(i,u):
    p.reset(0); p.mv(i,u[0]*0.17,u[1]*0.17); last=None
    for k in range(100):
        if ah(i)==0: break
        last=np.linalg.norm(p.pos(i)[:2]-home[i][:2]); p.mv(i,u[0]*0.001,u[1]*0.001)
    return round(last,4),round(np.linalg.norm(p.pos(i)[:2]-home[i][:2]),4)
def thr_rot(i,s):
    p.reset(0); last=None
    for k in range(400):
        if ah(i)==0: break
        last=p.pos(i)[2]; p.mv(i,0,0,0.002*s)
    return round(last,4),round(p.pos(i)[2],4)
for i in [0,1]:
    for ang in []:
        u=np.array([np.cos(np.radians(ang)),np.sin(np.radians(ang))])
        print('rover',i,'dir',ang,thr_pos(i,u))
    print('rover',i,'rot+',thr_rot(i,1),'rot-',thr_rot(i,-1))
# combined: offset 0.2 + rot 0.4
p.reset(0); p.mv(1,0,0.2,0.4); print('off .2 rot .4',ah())
p.reset(0); p.mv(1,0,0.24,0.0); p.mv(1,0,0,0.4); print('off .24 rot .4',ah())
