from env_client import make_env
E=make_env(); s,info=E.reset(seed=0)
print('INFO',info,'max',E.max_steps)
for t in E.observation_space.types:
 print('TYPE',t)
 for o in s.get_objects(t):
  print(str(o),[(f,s.get(o,f)) for f in E.observation_space.type_features[t]])
E.close()
