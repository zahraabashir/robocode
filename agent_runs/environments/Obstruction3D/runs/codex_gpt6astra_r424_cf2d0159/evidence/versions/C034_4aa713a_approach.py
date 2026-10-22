import numpy as np
from scipy.optimize import least_squares
from kinematics_fit import fk


def ik(x,z,guess=None):
    if guess is None: guess=np.array([0,.4,-np.pi,-1.8,0,-1.,np.pi/2])
    def residual(a):
        q=guess.copy();q[[1,3,5]]=a
        p,r=fk(q)
        return [p[0]-x,p[2]-z,r[0,2]]
    sol=least_squares(residual,guess[[1,3,5]],max_nfev=35,ftol=1e-8,xtol=1e-8,gtol=1e-8)
    q=guess.copy();q[[1,3,5]]=sol.x
    return q

class GeneratedApproach:
    def __init__(self,action_space,observation_space,primitives):
        self.action_space=action_space
        self.robot_type=observation_space.get_type('Kinematic3DRobot')
        self.cube_type=observation_space.get_type('Kinematic3DCuboid')
        self.x=.55
        self.cache={}
    def config(self,z):
        z=round(float(z),6)
        if z not in self.cache:self.cache[z]=ik(self.x,z)
        return self.cache[z]
    def reset(self,state,info):
        self.phase='raise'
        self.steps=0
        cubes=list(state.get_objects(self.cube_type))
        region=next(o for o in cubes if o.name=='target_region')
        rp=self.pos(state,region)
        obstacles=[o for o in cubes if o.name not in ('target_block','target_region') and all(abs(self.pos(state,o)[i]-rp[i])<state.get(region,'half_extent_'+v)+state.get(o,'half_extent_'+v)+.06 for i,v in enumerate('xy'))]
        obstacles.sort(key=lambda o:-self.pos(state,o)[2])
        self.tasks=[o.name for o in obstacles]+['target_block']
        self.goal=self.tasks.pop(0)
        self.discarded=0
        self.height=.35
        self.queue=[]
        self.retries=0
    def pos(self,state,o):return np.array([state.get(o,'pose_'+a) for a in 'xyz'])
    def get_action(self,state):
        self.steps+=1
        robot=next(iter(state.get_objects(self.robot_type)))
        cubes=list(state.get_objects(self.cube_type))
        byname={o.name:o for o in cubes}
        q=np.array([state.get(robot,'joint_'+str(i)) for i in range(1,8)])
        b=np.array([state.get(robot,'pos_base_'+a) for a in 'xy'])
        ee,rot=fk(q)
        held=next((o for o in cubes if state.get(o,'grasp_active')>.5),None)
        region=byname['target_region']
        for _ in range(8):
            a=np.zeros(11)
            obj=byname[self.goal]
            p=self.pos(state,obj)
            if self.phase=='raise':
                a[3:10]=self.config(.35)-q
                a[10]=1
                if np.max(abs(a[3:10]))<1e-4:self.phase='align';continue
            elif self.phase=='align':
                a[:2]=p[:2]-ee[:2]-b
                a[10]=1
                if np.max(abs(a[:2]))<1e-4:
                    self.height=.33;self.phase='descend';continue
            elif self.phase=='descend':
                if held is not None:
                    self.goal=held.name;self.phase='lift';self.height=min(.35,ee[2]+.025);continue
                a[3:10]=self.config(self.height)-q
                if np.max(abs(a[3:10]))<1e-4:
                    if self.height>p[2]+.055:
                        self.height=max(p[2]+.055,self.height-.025);continue
                    self.phase='close';continue
            elif self.phase=='close':
                if held is not None:self.goal=held.name;self.phase='lift';self.height=ee[2]+.025;continue
                a[10]=-1
                self.retries+=1
                if self.retries%3==0:
                    self.height=max(p[2]+.005,self.height-.005);self.phase='descend'
            elif self.phase=='lift':
                a[3:10]=self.config(min(.35,self.height))-q
                if np.max(abs(a[3:10]))<1e-4:
                    if self.height<.35:self.height=min(.35,self.height+.025);continue
                    self.phase='transfer';continue
            elif self.phase=='transfer':
                dest=self.pos(state,region)
                if self.goal!='target_block':
                    if not hasattr(self,'drop') or self.drop_goal!=self.goal:
                        h=np.array([state.get(obj,'half_extent_'+v) for v in 'xy'])
                        best=None
                        for x in np.linspace(.105+h[0],.495-h[0],9):
                            for y in np.linspace(-.395+h[1],.395-h[1],15):
                                xy=np.array([x,y]);clear=10.
                                for other in cubes:
                                    if other==obj:continue
                                    oh=np.array([state.get(other,'half_extent_'+v) for v in 'xy'])
                                    d=abs(xy-self.pos(state,other)[:2])-oh-h
                                    clear=min(clear,float(np.max(d)))
                                score=clear-.03*np.linalg.norm(xy-p[:2])
                                if best is None or score>best[0]:best=(score,xy)
                        self.drop=np.r_[best[1],.075+state.get(obj,'half_extent_z')+.001]
                        self.drop_goal=self.goal
                    dest=self.drop.copy()
                a[:2]=dest[:2]-p[:2]
                if np.max(abs(a[:2]))<1e-4:
                    self.destination=dest.copy()
                    if self.goal=='target_block':self.destination[2]+=state.get(region,'half_extent_z')+state.get(obj,'half_extent_z')+.001
                    self.finalheight=ee[2]+self.destination[2]-p[2]
                    self.height=max(self.finalheight,ee[2]-.02);self.phase='lower';continue
            elif self.phase=='lower':
                a[3:10]=self.config(self.height)-q
                if np.max(abs(a[3:10]))<1e-4:
                    if self.height>self.finalheight+1e-5:self.height=max(self.finalheight,self.height-.02);continue
                    self.phase='release';continue
            elif self.phase=='release':
                a[10]=1
                if held is None and self.goal!='target_block':
                    self.discarded+=1
                    self.goal=self.tasks.pop(0) if self.tasks else 'target_block'
                    self.phase='raise';self.retries=0;continue
            m=np.max(abs(a[:10]))
            if m>.15:a[:10]*=.15/m
            return np.clip(a,self.action_space.low,self.action_space.high).astype(np.float32)
        return np.zeros(11,dtype=np.float32)
