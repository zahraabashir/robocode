from env_client import make_env
for seed in range(6):
 env=make_env(); s,_=env.reset(seed=seed)
 print('SEED',seed)
 for name in s.get_object_names():
  o=s.get_object_from_name(name)
  fields=['x','y','theta']+(['base_radius','arm_joint','arm_length','gripper_width','gripper_height'] if o.type.name=='crv_robot' else ['width','height','static'])
  print(name,o.type.name,{f:round(float(s.get(o,f)),4) for f in fields})
 env.close()
