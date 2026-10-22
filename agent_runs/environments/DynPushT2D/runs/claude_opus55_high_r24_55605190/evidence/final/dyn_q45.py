from dyn_push import *
def run(seed, sb, d, step, total):
    e=E(seed); e.goto_safe(sb); dw=R(e.obs[2])@np.array(d,float)
    n=int(round(total/step))
    for i in range(n): e.step(dw*step)
    return e.obs.copy()
for sb,d in [([0.4,0.4],[0,-1]),([-0.8,-0.9],[1,0]),([-0.5,0.5],[0.5,-0.866])]:
    res=[run(0,sb,d,s,0.98) for s in [0.049,0.0245,0.01,0.005]]
    for s,o in zip([0.049,0.0245,0.01,0.005],res): print(sb,d,'step',s,'pose',o[0:3],'pusher',o[16:18])
print('determinism:')
a=run(3,[0.3,0.4],[0.2,-1],0.03,1.2); b=run(3,[0.3,0.4],[0.2,-1],0.03,1.2); print(a[0:3],b[0:3],np.abs(a-b).max())
