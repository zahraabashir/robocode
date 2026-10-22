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

    def storage(self, s, x, w, h):
        others=[(o,self.rect(s,o)) for o in s.get_objects(self.ot) if o!=self.obj]
        low=max(.005,.101+self.offsetx)
        high=min(1.613-w,1.517+self.offsetx)
        positions=[low,high,float(np.clip(x,low,high))]
        for o,(ox,oy,ow,oh) in others:
            positions.extend([ox+ow+.013,ox-w-.013])
        def base_clear(left,bottom):
            cx=left-self.offsetx;cy=bottom-self.offsety
            for o,(ox,oy,ow,oh) in others:
                dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
                if dx*dx+dy*dy<.101**2:return False
            return True
        floor=[]
        for left in positions:
            if left<low or left>high:continue
            if any(left<ox+ow+.012 and left+w>ox-.012 for o,(ox,oy,ow,oh) in others):continue
            if base_clear(left,.101):floor.append(left)
        if floor:return min(floor,key=lambda left:abs(left-x)),.101
        # Keep elevated storage outside both the destination and pickup columns.
        positions.extend(np.linspace(low,high,90))
        stacks=[]
        max_height=max([a[3] for o,a in others if o!=self.surface]+[h])
        ceiling=.89-.24-max_height
        for left in positions:
            if left<low or left>high:continue
            if any(o in (self.surface,self.block) and left<ox+ow+.04 and left+w>ox-.04 for o,(ox,oy,ow,oh) in others):continue
            bottom=.101
            for o,(ox,oy,ow,oh) in others:
                if left<ox+ow+.012 and left+w>ox-.012:bottom=max(bottom,oy+oh+.012)
            while bottom+h<=ceiling and not base_clear(left,bottom):bottom+=.01
            if bottom+h<=ceiling and bottom-self.offsety<=.89:stacks.append((left,bottom))
        if stacks:return min(stacks,key=lambda a:(a[1],abs(a[0]-x)))
        # Rare densely packed scenes: retain reachable coordinates for recovery.
        return float(np.clip(x,low,high)),max(.101,ceiling-h)

    def get_action(self, s):
        r=self.robot; rx=s.get(r,'x'); ry=s.get(r,'y')
        for _ in range(10):
            if self.phase == 'select':
                bx,by,bw,bh=self.rect(s,self.block)
                sx,sy,sw,sh=self.rect(s,self.surface)
                obs=[o for o in s.get_objects(self.ot) if o not in (self.block,self.surface)]
                choices=np.linspace(sx+.001,sx+sw-bw-.001,21)
                def cost(left):
                    overlap=[o for o in obs if s.get(o,'x')<left+bw+.004 and s.get(o,'x')+s.get(o,'width')>left-.004 and s.get(o,'y')<sy+sh+bh+.04]
                    return (max(0,left+bw/2-1.516),len(overlap),abs(left-(sx+(sw-bw)/2)))
                self.destx=min(choices,key=cost)
                blocking=[o for o in obs if s.get(o,'x')<self.destx+bw+.004 and s.get(o,'x')+s.get(o,'width')>self.destx-.004 and s.get(o,'y')<sy+sh+bh+.04]
                self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
                self.emptyheight=min(.75,max(s.get(o,'y')+s.get(o,'height') for o in s.get_objects(self.ot))+.225)
                self.carryheight=min(.89,self.emptyheight+s.get(self.obj,'height')+.008)
                self.phase='above'
            x,y,w,h=self.rect(s,self.obj)
            if self.phase == 'above':
                if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
                grasp_shift=min(0,1.516-(self.destx+w/2)) if self.obj==self.block else 0
                grasp_x=float(np.clip(x+w/2+grasp_shift,.101,1.517))
                if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
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
                if ry<self.carryheight-.001:return self.action(s,y=self.carryheight,vac=1)
                if y < self.pick_y+.02:
                    self.phase='down'; self.last_down=None
                    return self.action(s,y=y+h+.195,vac=1)
                self.offsetx=x-rx;self.offsety=y-ry
                if self.obj==self.block:
                    self.dropx=self.destx
                else:
                    self.dropx,self.dropy=self.storage(s,x,w,h)
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
                if ry<self.emptyheight-.001:return self.action(s,y=self.emptyheight,vac=0)
                self.phase='select'
        return self.action(s)
