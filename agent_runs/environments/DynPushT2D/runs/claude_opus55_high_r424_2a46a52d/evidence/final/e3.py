from pm_util import *
e=E()
for seed in [12,20]:
    o=e.reset(seed); w,L,V=o[12:15]; print("seed",seed,"w L V",w,L,V, "L/2",L/2)
    tests={"rightend":([1.0,-w/2],[-1,0]),"leftend":([-1.0,-w/2],[1,0]),"corner_diag":([0.9,0.3],[-1,-1])}
    for k,(p,d) in tests.items():
        mv,pv,cu,db=probe(e,seed,p,d)
        print(f"  {k:20s} navmove={mv:.1e} prev={pv} cur={cu} dblock={db}")
