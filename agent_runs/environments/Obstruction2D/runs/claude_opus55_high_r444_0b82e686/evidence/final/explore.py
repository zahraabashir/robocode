from env_client import make_env
env = make_env()
F={'crv_robot':["x", "y", "theta", "base_radius", "arm_joint", "arm_length", "vacuum", "gripper_height", "gripper_width"]}
R=["x", "y", "theta", "static", "color_r", "color_g", "color_b", "z_order", "width", "height"]
def dump(obs):
    for n in sorted(obs.get_object_names(), key=str):
        o = obs.get_object_from_name(n) if isinstance(n,str) else n
        fs = F.get(o.type.name if hasattr(o.type,'name') else str(o.type), R)
        print(" ", n, {f: round(float(obs.get(o,f)),3) for f in fs})
for seed in range(4):
    obs, info = env.reset(seed=seed)
    print("seed", seed); dump(obs)
env.close()
