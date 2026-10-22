import numpy as np, math
from scipy.optimize import least_squares
ox,oy=2.117588520050049,1.9229792356491089
data=[(-3.142,-0.08519),(-2.356,-0.14425),(-1.571,-0.16156),(-0.785,-0.12606),(0.0,-0.06022),(0.785,-0.00356),(1.571,0.01244),(2.356,-0.02067)]
def res(p):
    a,b,D=p; r=[]
    for th,y in data:
        th=-math.pi+round((th+math.pi)/(math.pi/4))*math.pi/4
        cx=2.118+a*math.cos(th)-b*math.sin(th); cy=y+a*math.sin(th)+b*math.cos(th)
        r.append(math.hypot(ox-cx,oy-cy)-D)
    return r
s=least_squares(res,[-0.08,0,2.0]); print(s.x, np.round(s.fun,5))
