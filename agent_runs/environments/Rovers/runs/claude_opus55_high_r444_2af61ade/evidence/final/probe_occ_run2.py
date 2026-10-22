from probe_occ_lib import *
from concurrent.futures import ThreadPoolExecutor
L=(-1.9,-2.0)
def online(P0,x):
    t=(x-P0[0])/(L[0]-P0[0]); return (x,round(P0[1]+t*(L[1]-P0[1]),4))
G=[((0.6,-0.35),-1.0),((1.2,0.0),-0.5),((0.6,-0.35),-0.3)]
jobs=[]
for P0,x in G:
  for h in (math.pi/2,math.pi,-math.pi/2):
    for dy in (1,-1):
        jobs.append((P0,online(P0,x),h,(0,dy)))
def f(j):
    P0,Q,h,d=j
    return j, sweep(44,P0,math.pi,Q,h,d,step=0.005,n=90)
with ThreadPoolExecutor(18) as ex:
    for r in ex.map(f,jobs): print(r,flush=True)
