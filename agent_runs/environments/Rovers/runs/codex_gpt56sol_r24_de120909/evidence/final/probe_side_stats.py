from collections import Counter
from env_client import make_env

c=Counter(); minabs=9
for seed in range(40):
 e=make_env(); s,_=e.reset(seed=seed)
 typ=next(t for t in e.observation_space.types if getattr(t,"name",str(t))=="sample")
 nums=[]
 for soil in (0,1):
  sides=[]
  for o in s.get_objects(typ):
   if round(float(s.get(o,"is_soil")))==soil:
    x=float(s.get(o,"x")); sides.append(x>0); minabs=min(minabs,abs(x))
  nums.append(sum(sides))
 c[tuple(nums)]+=1
 e.close()
print(c, "min_abs_x", minabs)
