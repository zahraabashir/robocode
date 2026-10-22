from pB_lib import *
s=Sim(2)
for t,f in s.obs.type_features.items(): print(t.name,f)
