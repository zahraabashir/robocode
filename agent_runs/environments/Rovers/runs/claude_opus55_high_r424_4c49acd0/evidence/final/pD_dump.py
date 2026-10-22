from pB_lib import *
s=Sim(0)
for n in sorted(s.obs.get_object_names()):
    o=s.obs.get_object_from_name(n)
    print(n,s.obs.vec([o]).round(3).tolist())
o=s.obs.get_object_from_name('rover0'); print(dir(o.type))
