from pm_util import *
from geom import com_I
exec(open('e6.py').read().split('e=E()')[0].split('from geom import com_I')[1])
e=E(); seed=12
o=e.reset(seed); w,L,V=o[12:15]; c,k2=com_I(w,L,V)
for ang in [60,70,80,87]:
    a=np.deg2rad(ang); d=[np.sin(a),-np.cos(a)]
    # start so that we hit top at x ~ -0.2 after approach
    mv,obs,act=run_push(e,seed,[-0.35,0.1+0.2*np.cos(a)],d,0.01,30)
    print(f"ang {ang} navmv={mv:.1e}")
    for i in range(1,31,2):
        b0=obs[i-1][0:3]; b1=obs[i][0:3]
        dl=R(b0[2]).T@(b1[0:2]-b0[0:2]); dth=b1[2]-b0[2]
        rl=R(b0[2]).T@(obs[i-1][16:18]-b0[0:2]); ul=R(b0[2]).T@act
        dist,pc=closest_pt(rl,w,L,V)
        if dist>0.13: continue
        pd,po=stick_pred(pc,ul,c,k2)
        print(f"   {i} rob_loc={rl} dist={dist:.4f} meas dl={dl} dth={dth:+.5f} | stick dl={pd} dth={po:+.5f}")
