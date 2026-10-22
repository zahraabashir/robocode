from dyn_lib import *
import sys
def body_twist(o0,o1):
    dpw=o1[0:2]-o0[0:2]; dth=(o1[2]-o0[2]+np.pi)%(2*np.pi)-np.pi
    return np.r_[R(o0[2]).T@dpw, dth]
def push(seed, start_b, dir_b, step, nsteps, verbose=False):
    e=E(seed); e.goto_safe(start_b); o0=e.obs.copy()
    d=np.asarray(dir_b,float); d/=np.linalg.norm(d)
    # approach slowly until contact
    for i in range(2000):
        o=e.step(R(e.obs[2])@d*0.001)
        if np.linalg.norm(o[0:3]-o0[0:3])>1e-9: break
    out=[]
    for k in range(nsteps):
        ob=e.obs.copy()
        o=e.step(R(ob[2])@d*step)   # direction fixed in body frame
        tw=body_twist(ob,o)
        cb=to_body(ob,ob[16:18])  # pusher pos in body frame before step
        out.append((cb,tw))
    return out,e
if __name__=='__main__':
    for x in [0.0,0.2,0.4,0.55]:
        out,e=push(0,[x,0.6],[0,-1],0.01,12)
        for k in [1,5,11]:
            cb,tw=out[k]
            # ICR in body frame: v = w x (p - c) => c = p_origin + (-vy/w, vx/w)
            icr = np.array([-tw[1]/tw[2], tw[0]/tw[2]]) if abs(tw[2])>1e-9 else None
            print(f'x={x} k={k} pusher_b={cb} twist={tw} icr={icr}')
