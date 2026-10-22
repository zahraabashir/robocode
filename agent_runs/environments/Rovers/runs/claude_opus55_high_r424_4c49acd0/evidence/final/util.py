import numpy as np
def parse(s):
    d={}
    for n in s.get_object_names():
        o=s.get_object_from_name(n)
        d[n]={f:float(s.get(o,f)) for f in FEATS[o.type.name]} if False else o
    return d
def feats(s):
    out={}
    for n in sorted(s.get_object_names()):
        o=s.get_object_from_name(n)
        out[n]=o
    return out
def R(s,name):
    o=s.get_object_from_name(name)
    return [round(float(s.get(o,f)),3) for f in ['x','y','theta','store_full','calibrated','at_home']]
