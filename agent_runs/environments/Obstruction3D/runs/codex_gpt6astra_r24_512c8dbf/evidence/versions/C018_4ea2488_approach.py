import numpy as np
from kin import ik

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space=action_space
        self.observation_space=observation_space
    def reset(self,state,info):
        self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
        self.block=state.get_object_from_name('target_block')
        self.region=state.get_object_from_name('target_region')
        self.phase='above';self.t=0;self.stall=0
    def pos(self,state,obj):
        return np.array([state.get(obj,'pose_'+f) for f in 'xyz'])
    def get_action(self,state):
        self.t+=1;r=self.robot;b=self.block
        bp=self.pos(state,b);rp=self.pos(state,self.region)
        qnow=np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
        held=state.get(r,'grasp_active')>0
        if held and self.phase in ['above','grasp']: self.phase='lift'
        if self.phase=='above':dest=bp+[0,0,.18];grip=0
        elif self.phase=='grasp':dest=bp+[0,0,.052];grip=-1
        elif self.phase=='lift':dest=np.array([bp[0],bp[1],.30]);grip=0
        elif self.phase=='carry':dest=np.array([rp[0],rp[1],.30]);grip=0
        elif self.phase=='lower':dest=np.array([rp[0],rp[1],rp[2]+state.get(self.region,'half_extent_z')+state.get(b,'half_extent_z')+.002]);grip=0
        else:dest=bp;grip=1
        if held:
            from kin import fk
            model,_=fk(qnow)
            model+=np.array([state.get(r,'pos_base_x')+.12,state.get(r,'pos_base_y'),0])
            dest=dest+model-bp
        q=ik(dest[0]-state.get(r,'pos_base_x')-.12,dest[2])
        by=dest[1]-.001
        err=max(np.max(np.abs(q-qnow)),abs(by-state.get(r,'pos_base_y')))
        if err<.002:
            self.phase={'above':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
        a=np.zeros(11,dtype=np.float32);a[1]=by-state.get(r,'pos_base_y');a[3:10]=q-qnow;a[10]=grip
        return np.clip(a,self.action_space.low,self.action_space.high)
