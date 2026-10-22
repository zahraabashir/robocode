from probe_occ_lib import *
from concurrent.futures import ThreadPoolExecutor
jobs=[((0.6,-0.35),(-0.5,0.0)),((0.6,-1.9),(-0.5,0.0)),((1.2,0.0),(-0.5,0.0)),((0.6,-0.35),(-1.0,-1.75))]
def f(j): return j, sweep(44,j[0],math.pi,j[1],0.0,(0,0),n=2)
with ThreadPoolExecutor(4) as ex:
    for r in ex.map(f,jobs): print(r)
