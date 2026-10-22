from probe_coll_util import *
obs,_=env.reset(seed=0)
print(rov(obs))
obs,*_=step((0.1,0,0),(0.1,0,0)); print('dx .1 both',rov(obs))
obs,*_=step((0,0.1,0),(0,0.1,0)); print('dy .1',rov(obs))
obs,*_=step((0,0,0.3),(0,0,0.3)); print('dth .3',rov(obs))
obs,*_=step((0.1,0,0),(0.1,0,0)); print('dx .1 after rot',rov(obs))
obs,*_=step((0.123456,0.0654321,0),(0,0,0)); print('frac',rov(obs))
obs,r,te,tr,info=env.step(np.array([0.5,0,1.0,0,0,0.5,0,0],dtype=np.float32)); print('clip test',rov(obs),r,te,tr,info)
obs,*_=step((0,0,0.4),(0,0,0)); 
for i in range(8): obs,*_=step((0,0,0.4),(0,0,0))
print('theta wrap',rov(obs))
