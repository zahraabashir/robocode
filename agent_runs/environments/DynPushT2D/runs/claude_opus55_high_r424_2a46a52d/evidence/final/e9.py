from pm_util import *
e=E()
o=e.reset(12); print("start robot",o[16:18],"block",o[0:3])
for d in [[-1,0],[0,-1],[1,0],[0,1]]:
    o=e.reset(12)
    # move away from block first: block at ~ (2.36,2.40); robot at (1.1,1.26)
    for i in range(150):
        o=e.step(np.array(d)*0.049)
    print(d,"robot",o[16:18],"block",o[0:3])
# go to corner (0,0) direction
o=e.reset(12)
for i in range(150): o=e.step(np.array([-0.049,-0.049]))
print("corner", o[16:18])
