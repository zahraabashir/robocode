import sys; sys.argv=['x','99']
src=open('obl_a.py').read().split("seed=int")[0]
exec(src)
for s in [0]:
  obs,_=env.reset(seed=s)
  for a in [48,51,54,57]: trial(s,'stem',a)
  for a in [50,55]: trial(s,'top',a)
