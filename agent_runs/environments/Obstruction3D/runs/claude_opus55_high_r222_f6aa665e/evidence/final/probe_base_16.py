import numpy as np
exec(open('probe_base_11.py').read().split("for seed in")[0])
def run(seed,dy,z):
    obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
    base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
    TB=obs.get_object_from_name("target_block"); tb0=np.array(obs.data[TB][:7],float)
    rel=tb0[:2]-base+np.array([0,dy]); q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,rj=goto(obs,R,q)
    for zr in np.arange(0.40,z,-0.01):
        q,_=ik(np.array([rel[0]-0.12,rel[1],zr]),q); obs,rj=goto(obs,R,q)
        if rj: return f"rej descending {zr:.2f}"
    for dx in np.arange(-0.12,0.121,0.01):
        q,_=ik(np.array([rel[0]+dx,rel[1],z]),q); obs,rj=goto(obs,R,q)
        tb=np.array(obs.data[TB][:7],float)
        if rj or np.abs(tb-tb0).max()>1e-6: return f"stop dx={dx:+.2f} rej={rj} tb_delta={np.round(tb-tb0,4)}"
    return "passed through all dx"
for z in [0.13,0.15,0.17,0.2]:
    for dy in [0.0,-0.12]:
        print(f"z={z} dy={dy}:",run(1,dy,z))
env.close()
