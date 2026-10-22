from env_client import make_env
import sys
FE = {'crv_robot':["x","y","theta","base_radius","arm_joint","arm_length","vacuum","gripper_height","gripper_width"],
 'rectangle':["x","y","theta","static","color_r","color_g","color_b","z_order","width","height"]}
FE['target_block']=FE['rectangle']; FE['target_surface']=FE['rectangle']
def dump(obs):
    for name in sorted(obs.get_object_names(), key=str):
        o = obs.get_object_from_name(name)
        print(name, {f: round(float(obs.get(o,f)),3) for f in FE[o.type.name]})
if __name__=="__main__":
    env = make_env()
    for seed in map(int, sys.argv[1:]):
        obs, info = env.reset(seed=seed); print("seed",seed,info); dump(obs)
    env.close()
