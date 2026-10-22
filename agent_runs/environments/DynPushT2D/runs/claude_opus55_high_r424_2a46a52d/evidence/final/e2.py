from pm_util import *
e=E()
for seed in [12,20,24]:
    o=e.reset(seed); w,L,V=o[12:15]; print("seed",seed,"w L V",w,L,V)
    tests={"top@x=.3":([0.3,0.5],[0,-1]),"top@x=0":([0.0,0.5],[0,-1]),
           "barbottom@x=.4":([0.4,-0.4],[0,1]),"barbottom@x=-.4":([-0.4,-0.4],[0,1]),
           "stembottom":([0,-1.6],[0,1]),"stemside+x@y=-.6":([0.5,-0.6],[-1,0]),"stemside-x@y=-.6":([-0.5,-0.6],[1,0])}
    for k,(p,d) in tests.items():
        mv,pv,cu,db=probe(e,seed,p,d)
        print(f"  {k:20s} navmove={mv:.1e} prev={pv} cur={cu} dblock={db}")
