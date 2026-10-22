import math
import numpy as np

class GeneratedApproach:
    def __init__(self, action_space, observation_space, primitives):
        self.action_space = action_space
        self.observation_space = observation_space
        self.rt = observation_space.get_type('crv_robot')
        self.bt = observation_space.get_type('target_block')
        self.st = observation_space.get_type('target_surface')
        self.ot = observation_space.get_type('rectangle')

    def reset(self, state, info):
        self.robot = state.get_objects(self.rt)[0]
        self.block = state.get_objects(self.bt)[0]
        self.surface = state.get_objects(self.st)[0]
        self.phase = 'select'
        self.obj = None
        self.n = 0
        self.stashed = []

    def val(self, s, o, f):
        return s.get(o, f)

    def rect(self, s, o):
        return [s.get(o,f) for f in ('x','y','width','height')]

    def action(self, s, x=None, y=None, vac=0):
        r=self.robot
        return np.array([0 if x is None else np.clip(x-s.get(r,'x'),-.05,.05),
                         0 if y is None else np.clip(y-s.get(r,'y'),-.05,.05),
                         np.clip(-math.pi/2-s.get(r,'theta'),-.19634954,.19634954),
                         np.clip(.2-s.get(r,'arm_joint'),-.1,.1),vac],dtype=np.float32)

    def get_action(self, s):
        r=self.robot; rx=s.get(r,'x'); ry=s.get(r,'y')
        for _ in range(10):
            if self.phase == 'select':
                bx,by,bw,bh=self.rect(s,self.block)
                sx,sy,sw,sh=self.rect(s,self.surface)
                self.destx=sx+(sw-bw)/2
                obs=[o for o in s.get_objects(self.ot) if o not in (self.block,self.surface)]
                blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
                self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
                self.phase='above'
            x,y,w,h=self.rect(s,self.obj)
            if self.phase == 'above':
                if ry<.72: return self.action(s,y=.75)
                if abs(rx-(x+w/2))>.001: return self.action(s,x=x+w/2,y=.75)
                self.phase='down'; self.n=0; self.last_down=None
            if self.phase == 'down':
                self.n+=1
                goal=y+h+.2+.006
                if ry>goal+.001 and (self.last_down is None or abs(ry-self.last_down)>.00001):
                    self.last_down=ry
                    return self.action(s,y=goal,vac=1)
                self.pick_y=y; self.phase='lift';self.n=0
            if self.phase == 'lift':
                self.n+=1
                if ry<.749:return self.action(s,y=.75,vac=1)
                if y < self.pick_y+.02:
                    self.phase='down'; self.last_down=None
                    return self.action(s,y=y+h+.195,vac=1)
                self.offsetx=x-rx;self.offsety=y-ry
                if self.obj==self.block:
                    self.dropx=self.destx
                else:
                    occupied=[]
                    for other in s.get_objects(self.ot):
                        if other==self.obj:continue
                        ox,oy,ow,oh=self.rect(s,other)
                        occupied.append((ox-.012,ox+ow+.012))
                    candidates=[]
                    for cx in np.linspace(.101,1.517,220):
                        left=cx-w/2
                        if left<.005 or left+w>1.613:continue
                        if any(left<b and left+w>a for a,b in occupied):continue
                        candidates.append(left)
                    self.dropx=min(candidates,key=lambda v:abs(v-x)) if candidates else .01
                    self.dropy=.101
                if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.001
                self.phase='carry'
            if self.phase == 'carry':
                goal=self.dropx-self.offsetx
                if abs(rx-goal)>.001:return self.action(s,x=goal,vac=1)
                self.phase='place'
            if self.phase == 'place':
                goal=self.dropy-self.offsety
                if abs(ry-goal)>.001:return self.action(s,y=goal,vac=1)
                self.stashed.append(self.obj);self.phase='retreat'
                return self.action(s,vac=0)
            if self.phase=='retreat':
                if ry<.749:return self.action(s,y=.75,vac=0)
                self.phase='select'
        return self.action(s)
