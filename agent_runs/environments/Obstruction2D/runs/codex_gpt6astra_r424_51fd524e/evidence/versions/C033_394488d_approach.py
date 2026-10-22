import math
import numpy as np

class GeneratedApproach:
    """Geometric pick-and-place controller for a variable-size object set.

    All scene geometry comes from the object-centric observation. The robot
    remains upright with its arm pointing down; obstructions are moved only
    when they interfere with the complete final placement configuration.
    """
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

    def rect(self, s, o):
        return [s.get(o,f) for f in ('x','y','width','height')]

    def action(self, s, x=None, y=None, vac=0):
        r=self.robot
        return np.array([0 if x is None else np.clip(x-s.get(r,'x'),-.05,.05),
                         0 if y is None else np.clip(y-s.get(r,'y'),-.05,.05),
                         np.clip(-math.pi/2-s.get(r,'theta'),-.19634954,.19634954),
                         np.clip(.2-s.get(r,'arm_joint'),-.1,.1),vac],dtype=np.float32)

    def grasp_position(self, s, obj, preferred):
        x,y,w,h=self.rect(s,obj)
        others=[self.rect(s,o) for o in s.get_objects(self.ot) if o!=obj]
        candidates=[preferred,x+w/2,x+.005,x+w-.005,.101,1.517]
        if obj==self.block:candidates.extend([x+1.516-self.destx,x+.102-self.destx])
        for ox,oy,ow,oh in others:
            candidates.extend([ox-.041,ox+ow+.041])
        valid=[]
        for cx in candidates:
            if not .101<=cx<=1.517 or cx+.035<x+.006 or cx-.035>x+w-.006:continue
            if obj==self.block and not .101<=self.destx-x+cx<=1.517:continue
            cy=y+h+.206
            collision=False
            for ox,oy,ow,oh in others:
                dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
                if dx*dx+dy*dy<.101**2:collision=True;break
                if ox<cx+.04 and ox+ow>cx-.04 and oy<y+h+.02 and oy+oh>y+h-.005:
                    collision=True;break
            if not collision:valid.append(cx)
        return min(valid,key=lambda cx:abs(cx-preferred)) if valid else float(np.clip(preferred,.101,1.517))

    def placement_collisions(self, s, obj, left, bottom, offsetx, offsety):
        _,_,w,h=self.rect(s,obj)
        cx=left-offsetx;cy=bottom-offsety
        parts=[(left-.003,bottom,left+w+.003,bottom+h),
               (cx-.055,cy-.225,cx+.055,cy-.185),
               (cx-.008,cy-.2,cx+.008,cy)]
        blocked=[]
        for other in s.get_objects(self.ot):
            if other==obj:continue
            ox,oy,ow,oh=self.rect(s,other)
            dx=max(ox-cx,0,cx-ox-ow);dy=max(oy-cy,0,cy-oy-oh)
            collision=dx*dx+dy*dy<.101**2
            for x0,y0,x1,y1 in parts:
                if x0<ox+ow and x1>ox and y0<oy+oh and y1>oy:
                    collision=True;break
            if collision:blocked.append(other)
        return blocked

    def storage(self, s, x, w, h):
        others=[(o,self.rect(s,o)) for o in s.get_objects(self.ot) if o!=self.obj]
        bx,by,bw,bh=self.rect(s,self.block)
        goalcx=self.destx-bx+self.target_grasp
        reserve_left=min(self.destx,goalcx-.105)
        reserve_right=max(self.destx+bw,goalcx+.105)
        pickup_left=min(bx,self.target_grasp-.105)
        pickup_right=max(bx+bw,self.target_grasp+.105)
        low=max(.005,.101+self.offsetx)
        high=min(1.613-w,1.517+self.offsetx)
        positions=[low,high,float(np.clip(x,low,high))]
        for o,(ox,oy,ow,oh) in others:
            positions.extend([ox+ow+.013,ox-w-.013])
        def base_clear(left,bottom):
            return not self.placement_collisions(s,self.obj,left,bottom,self.offsetx,self.offsety)
        floor=[]
        for left in positions:
            if left<low or left>high:continue
            if left<reserve_right+.008 and left+w>reserve_left-.008:continue
            if left<pickup_right+.008 and left+w>pickup_left-.008:continue
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
            if left<reserve_right+.02 and left+w>reserve_left-.02:continue
            if left<pickup_right+.02 and left+w>pickup_left-.02:continue
            if any(o in (self.surface,self.block) and left<ox+ow+.04 and left+w>ox-.04 for o,(ox,oy,ow,oh) in others):continue
            bottom=.101
            for o,(ox,oy,ow,oh) in others:
                if left<ox+ow+.012 and left+w>ox-.012:bottom=max(bottom,oy+oh+.012)
            while bottom+h<=ceiling and not base_clear(left,bottom):bottom+=.01
            if bottom+h<=ceiling and bottom-self.offsety<=.89:stacks.append((left,bottom))
        if stacks:return min(stacks,key=lambda a:(a[1],abs(a[0]-x)))
        # If geometric candidates are exhausted, retain a legal base position.
        return float(np.clip(x,low,high)),max(.101,ceiling-h)

    def get_action(self, s):
        r=self.robot; rx=s.get(r,'x'); ry=s.get(r,'y')
        for _ in range(10):
            if self.phase == 'select':
                bx,by,bw,bh=self.rect(s,self.block)
                sx,sy,sw,sh=self.rect(s,self.surface)
                choices=np.linspace(sx+.001,sx+sw-bw-.001,21)
                plans=[]
                for left in choices:
                    self.destx=left
                    preferred=bx+bw/2+min(0,1.516-(left+bw/2))
                    gx=self.grasp_position(s,self.block,preferred)
                    blocked=[o for o in self.placement_collisions(s,self.block,left,sy+sh+.021,bx-gx,-bh-.206) if o!=self.surface]
                    reach=max(0,left-bx+gx-1.517,.101-(left-bx+gx))
                    plans.append(((reach,len(blocked),abs(left-(sx+(sw-bw)/2))),left,gx,blocked))
                _,self.destx,self.target_grasp,blocking=min(plans,key=lambda p:p[0])
                self.obj=max(blocking,key=lambda o:s.get(o,'y')+s.get(o,'height')) if blocking else self.block
                self.emptyheight=min(.75,max(s.get(o,'y')+s.get(o,'height') for o in s.get_objects(self.ot))+.225)
                self.carryheight=min(.89,self.emptyheight+s.get(self.obj,'height')+.008)
                self.phase='above'
            x,y,w,h=self.rect(s,self.obj)
            if self.phase == 'above':
                if ry<self.emptyheight-.001: return self.action(s,y=self.emptyheight)
                grasp_x=self.target_grasp if self.obj==self.block else self.grasp_position(s,self.obj,x+w/2)
                if abs(rx-grasp_x)>.001: return self.action(s,x=grasp_x,y=self.emptyheight)
                self.phase='down'; self.last_down=None
            if self.phase == 'down':
                goal=y+h+.2+.006
                if ry>goal+.001 and (self.last_down is None or abs(ry-self.last_down)>.00001):
                    self.last_down=ry
                    return self.action(s,y=goal,vac=1)
                self.pick_y=y; self.phase='lift'
            if self.phase == 'lift':
                if ry<self.carryheight-.001:return self.action(s,y=self.carryheight,vac=1)
                if y < self.pick_y+.02:
                    self.phase='down'; self.last_down=None
                    return self.action(s,y=y+h+.195,vac=1)
                self.offsetx=x-rx;self.offsety=y-ry
                if self.obj==self.block:
                    self.dropx=self.destx
                else:
                    self.dropx,self.dropy=self.storage(s,x,w,h)
                if self.obj==self.block:self.dropy=s.get(self.surface,'y')+s.get(self.surface,'height')+.021
                self.phase='carry'
            if self.phase == 'carry':
                goal=self.dropx-self.offsetx
                if abs(rx-goal)>.0001:return self.action(s,x=goal,vac=1)
                self.phase='place'
            if self.phase == 'place':
                goal=self.dropy-self.offsety
                if abs(ry-goal)>.001:return self.action(s,y=goal,vac=1)
                self.phase='retreat'
                return self.action(s,vac=0)
            if self.phase=='retreat':
                if ry<self.emptyheight-.001:return self.action(s,y=self.emptyheight,vac=0)
                self.phase='select'
        return self.action(s)
