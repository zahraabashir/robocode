import sys, numpy as np
exec(open('probe_c6.py').read().split('tests=')[0])
def up(obs,dz,wb):
    x=ap._x(obs); Tt=wb_fk(x); a=np.zeros(11,dtype=np.float32)
    if wb: xn,ok=wb_ik2(x,Tt[:3,3]+np.array([0,0,dz]),down_R(yaw),k_null=0.05,bx_max=-0.09); a[0:10]=np.clip(xn-x,-0.2,0.2)
    else: q,ok=tool_ik(x[3:],Tt[:3,3]+np.array([0,0,dz]),down_R(yaw),tuple(x[:3])); a[3:10]=np.clip(q-x[3:],-0.2,0.2)
    o2,*_=env.step(a); return o2
for dz,wb in [(0.01,False),(0.007,False),(0.005,False)]:
    env.close(); env,obs,ap=replay()
    for k in range(8):
        o2=up(obs,dz,wb); mv=not np.allclose(ap._x(o2),ap._x(obs)); obs=o2
        print(dz,wb,k,mv,np.round(wb_fk(ap._x(obs))[:3,3],3))
