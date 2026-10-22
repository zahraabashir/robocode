from probe_ops_lib import *
import time
def test(pts, via=None):
    """one episode: sample sample3, visit pts in order trying send; return index of first success or None"""
    reset(21)
    goto(0,0.62,-0.82); step(0,op='sample')
    assert dump('sample')['sample3'][4]==1
    res=[]
    for p in pts:
        if via: goto(0,*via(p))
        ok=goto(0,*p)
        step(0,op='send')
        x,y=pos(0)[:2]
        r=dump('sample')['sample3'][-1]
        res.append(((round(x,2),round(y,2)),ok,r))
        if r>0: break
    return res
