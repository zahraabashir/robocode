import numpy as np
from kin import ik, fk

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space=action_space
        self.observation_space=observation_space
        self.cache={}
    def pos(self,state,obj):
        return np.array([state.get(obj,'pose_'+f) for f in 'xyz'])
    def size(self,state,obj):
        return np.array([state.get(obj,'half_extent_'+f) for f in 'xyz'])
    def reset(self,state,info):
        self.robot=state.get_objects(self.observation_space.get_type('Kinematic3DRobot'))[0]
        self.block=state.get_object_from_name('target_block')
        self.region=state.get_object_from_name('target_region')
        self.objects=state.get_objects(self.observation_space.get_type('Kinematic3DCuboid'))
        rp=self.pos(state,self.region);rs=self.size(state,self.region)
        obs=[o for o in self.objects if o not in [self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-rp[:2]) < self.size(state,o)[:2]+rs[:2]+.012)]
        obs.sort(key=lambda o:-self.pos(state,o)[2])
        self.todo=obs+[self.block];self.index=0;self.phase='above';self.t=0;self.stall=0;self.last=None
        self.lift_step=.04;self.bad_places={};self.last_released=None;self.attempts={};self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[0];self.destination=self.choose_destination(state)
    def choose_destination(self,state):
        self.failed_places=self.bad_places.setdefault(self.obj,[])
        self.placing_goal=self.obj==self.block and not any(o!=self.block for o in self.todo[self.index+1:])
        if self.placing_goal:
            p=self.pos(state,self.region).copy();p[2]+=self.size(state,self.region)[2]+self.size(state,self.obj)[2]+.001
            return p
        h=self.size(state,self.obj)
        candidates=[]
        for x in [.135,.2,.265,.33,.395,.465]:
            for y in [-.36,.36,-.29,.29,-.22,.22,-.15,.15,0]:
                p=np.array([x,y,.075+h[2]+.001]);free=True
                for other in self.objects:
                    if other==self.obj:continue
                    op=self.pos(state,other);oh=self.size(state,other)
                    if np.all(np.abs(p[:2]-op[:2]) < np.maximum(h[:2],.055)+oh[:2]+.009):free=False;break
                if free:
                    if all(np.linalg.norm(p[:2]-bad)>.025 for bad in self.failed_places):candidates.append(p)
        if candidates:
            start=self.pos(state,self.obj)
            return min(candidates,key=lambda p:np.linalg.norm(p[:2]-start[:2]))
        # Rectangle-edge candidates provide finer packing as the object count grows.
        xs=[.103+h[0],.497-h[0]];ys=[-.397+h[1],.397-h[1]]
        for other in self.objects:
            if other==self.obj:continue
            op=self.pos(state,other);oh=self.size(state,other)
            xs.extend([op[0]-oh[0]-h[0]-.005,op[0]+oh[0]+h[0]+.005])
            ys.extend([op[1]-oh[1]-h[1]-.005,op[1]+oh[1]+h[1]+.005])
        for x in xs:
            if not .1+h[0]<x<.5-h[0]:continue
            for y in ys:
                if not -.4+h[1]<y<.4-h[1]:continue
                p=np.array([x,y,.076+h[2]])
                if any(np.linalg.norm(p[:2]-bad)<.025 for bad in self.failed_places):continue
                if all(other==self.obj or np.any(np.abs(p[:2]-self.pos(state,other)[:2])>=h[:2]+self.size(state,other)[:2]+.003) for other in self.objects):return p
        return np.array([.135,-.36,.076+h[2]])
    def get_action(self,state):
        self.t+=1;r=self.robot
        qnow=np.array([state.get(r,'joint_'+str(i)) for i in range(1,8)])
        base=np.array([state.get(r,'pos_base_x'),state.get(r,'pos_base_y')])
        model,_=fk(qnow);model+=np.r_[base+[.12,0],0]
        held=state.get(r,'grasp_active')>0
        bp=self.pos(state,self.obj)
        signature=np.r_[base,qnow,held]
        if self.last is not None and np.max(abs(signature-self.last))<1e-6:self.stall+=1
        else:self.stall=0
        self.last=signature
        if not held and self.phase=='grasp' and self.stall>=3:
            self.attempt+=1;self.attempts[self.obj]=self.attempt
            if self.attempt%2==0:
                pending=[o for o in self.todo[self.index:] if o not in [self.obj,self.block]]
                if not pending:
                    pending=[o for o in self.objects if o not in [self.obj,self.block,self.region] and np.all(np.abs(self.pos(state,o)[:2]-bp[:2])<.095)]
                    pending.sort(key=lambda o:-self.pos(state,o)[2])
                if pending:
                    postponed=[] if self.obj==self.block else [self.obj]
                    self.todo=self.todo[:self.index]+pending+postponed+[self.block]
                    self.obj=self.todo[self.index];bp=self.pos(state,self.obj)
                    self.attempt=self.attempts.get(self.obj,0);self.failed_places=[]
                    self.destination=self.choose_destination(state)
            self.wrist=[np.pi/2,0,np.pi/4,-np.pi/4][self.attempt%4];self.phase='above';self.stall=0
        if held and self.phase in ['above','align','grasp']:
            grabbed=[o for o in self.objects if state.get(o,'grasp_active')>0]
            if grabbed and grabbed[0]!=self.obj:
                actual=grabbed[0]
                self.todo=[o for j,o in enumerate(self.todo) if o!=actual or j<self.index]
                self.todo.insert(self.index,actual)
                if actual==self.block and any(o!=self.block for o in self.todo[self.index+1:]):self.todo.append(self.block)
                self.obj=actual;self.destination=self.choose_destination(state);bp=self.pos(state,self.obj)
            self.phase='lift';self.lift_xy=bp[:2].copy();self.lift_step=.04
        if self.phase=='release' and not held:
            self.last_released=self.obj
            self.index+=1
            if self.index>=len(self.todo):self.index=len(self.todo)-1
            self.attempt=0;self.wrist=np.pi/2;self.failed_places=[];self.obj=self.todo[self.index];self.destination=self.choose_destination(state);self.phase='above';bp=self.pos(state,self.obj)
        if not held and self.phase=='above' and self.stall>=3 and self.last_released is not None:
            released=self.last_released
            oldpos=self.pos(state,released)
            if np.linalg.norm(oldpos[:2]-model[:2])<.04:
                self.todo.insert(self.index,released);self.obj=released
                self.failed_places=self.bad_places.setdefault(released,[])
                self.failed_places.append(oldpos[:2].copy());self.destination=self.choose_destination(state)
                self.phase='grasp';self.attempt=0;self.wrist=qnow[6];self.stall=0
                a=np.zeros(11,dtype=np.float32);a[10]=-1
                return a
        if held and self.phase=='lower' and not self.placing_goal and self.stall>=3:
            self.failed_places.append(self.destination[:2].copy());self.destination=self.choose_destination(state);self.phase='lift';self.lift_xy=bp[:2].copy();self.stall=0
        if held and self.phase=='lift' and self.stall>=2:
            self.lift_step=max(.001,self.lift_step/4)
        for _ in range(4):
            grip=0
            if self.phase=='above':dest=np.r_[model[:2],.30]
            elif self.phase=='align':dest=np.r_[bp[:2],.30]
            elif self.phase=='grasp':dest=bp+[0,0,.025];grip=-1
            elif self.phase=='lift':dest=np.r_[self.lift_xy,.24]
            elif self.phase=='carry':dest=np.r_[self.destination[:2],.24]
            elif self.phase=='lower':dest=self.destination.copy()
            else:dest=bp.copy();grip=1
            if held:dest=dest+model-bp
            if self.phase=='above':dest[2]=.30
            # Preserve a vertical wrist throughout travel and use the mobile base for XY.
            dz=np.clip(dest[2]-model[2],-.008 if self.phase=='grasp' and model[2]-bp[2]<.09 else -.04,self.lift_step if self.phase=='lift' else .04)
            z=model[2]+dz
            key=round(float(z),7)
            if key not in self.cache:self.cache[key]=ik(.50,z)
            q=self.cache[key].copy()
            q[6]=qnow[6] if self.phase=='above' else self.wrist
            targetbase=dest[:2]-[.62,.001]
            delta=np.r_[targetbase-base,q-qnow]
            scale=max(1.,np.max(np.abs(delta))/.18)
            a=np.zeros(11,dtype=np.float32);a[:2]=delta[:2]/scale;a[3:10]=delta[2:]/scale;a[10]=grip
            error=np.max(np.abs(dest-model))
            if error<.0015 and np.max(abs(q-qnow))<.006:
                next_phase={'above':'align','align':'grasp','grasp':'grasp','lift':'carry','carry':'lower','lower':'release','release':'release'}[self.phase]
                if next_phase!=self.phase:
                    self.phase=next_phase
                    continue
            return np.clip(a,self.action_space.low,self.action_space.high)
        return np.clip(a,self.action_space.low,self.action_space.high)
