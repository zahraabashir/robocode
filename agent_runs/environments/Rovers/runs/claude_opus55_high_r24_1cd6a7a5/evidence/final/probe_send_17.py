exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
def one(p, mode, r1=None):
    reset(21); goto(0,0.62,-0.82); step(0,op='sample')
    if r1: goto(1,*r1)
    goto(0,*p,tol=0.002); q=pos(0); a=math.atan2(q[1]+2,q[0]+1.9)
    turn_to(0, a if mode=='away' else a+math.pi); step(0,op='send')
    q=pos(0); print(mode,np.round(q[:3],3),'dist',round(math.hypot(q[0]+1.9,q[1]+2.0),3),'recv',dump('sample')['sample3'][-1])
for mode in ['away','toward']:
    one((1.3,-0.176),mode)          # behind obstacle5 at 0.47
    one((1.08,-0.29),mode)          # behind obstacle5 at 0.22 
    one((0.26,-0.84),mode,(-1,0.3)) # behind obstacle10
    one((1.0,-1.194),mode)          # rover1 dead centre
    one((0.4,-1.36),mode)           # rover1 dead centre closer (0.58 from r1)
    one((2.05,-1.45),mode,(-1,0.3)) # dist ~4.0
