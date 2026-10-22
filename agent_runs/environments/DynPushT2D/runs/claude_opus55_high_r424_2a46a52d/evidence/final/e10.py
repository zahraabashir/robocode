from pm_util import *
e=E()
for d in [[-1,0],[0,-1],[1,0],[0,1]]:
    for s in [0.001,0.01,0.049]:
        o=e.reset(12)
        for i in range(150): o=e.step(np.array(d)*0.049)
        for i in range(8): o=e.step(-np.array(d)*0.02)
        p=o[16:18].copy(); hist=[]
        for i in range(int(0.3/s)):
            o=e.step(np.array(d)*s); hist.append(o[16:18].copy())
        hist=np.array(hist)
        print(d,s,"final",hist[-1],"last moves",np.round(np.diff(hist[-4:],axis=0).ravel(),5))
# sliding along wall
o=e.reset(12)
for i in range(150): o=e.step(np.array([-0.049,0]))
p=o[16:18].copy()
for i in range(10): o=e.step(np.array([-0.02,0.02]))
print("slide along left wall", p, "->", o[16:18])
